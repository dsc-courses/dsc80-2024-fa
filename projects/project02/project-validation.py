
# Do NOT edit this file. Instead, just call it from the command line,
# using the instructions in the assignment notebook.

import sys
questions = sys.argv[1:]


valid_ids = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
break_flag = False
invalid_ids = []
for question in questions:
    if question != 'all' and question not in valid_ids:
        invalid_ids.append(question)

if len(invalid_ids) > 0:
    print(str(invalid_ids) + ' is/are not a valid question number(s). The possible question numbers are ' + str(valid_ids) + '.')
    sys.exit()

# Initialize Otter
import otter
grader = otter.Notebook("project.ipynb")

# %load_ext autoreload
# %autoreload 2

import pandas as pd
import numpy as np
from pathlib import Path

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pd.options.plotting.backend = 'plotly'

from IPython.display import display

# DSC 80 preferred styles
pio.templates["dsc80"] = go.layout.Template(
    layout=dict(
        margin=dict(l=30, r=30, t=30, b=30),
        autosize=True,
        width=600,
        height=400,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        title=dict(x=0.5, xanchor="center"),
    )
)
pio.templates.default = "simple_white+dsc80"

import plotly.figure_factory as ff
def create_kde_plotly(df, group_col, group1, group2, vals_col, title=''):
    fig = ff.create_distplot(
        hist_data=[df.loc[df[group_col] == group1, vals_col], df.loc[df[group_col] == group2, vals_col]],
        group_labels=[group1, group2],
        show_rug=False, show_hist=False
    )
    return fig.update_layout(title=title)

from project import *

loans_path = Path('data') / 'loans.csv'
loans = pd.read_csv(loans_path)
loans.head()

loans['loan_amnt'].describe()

loans.loc[loans['loan_amnt'] == 3600, ['loan_amnt', 'term', 'int_rate']]

# Note: If the plot below doesn't appear, uncomment and run the following line.
# It will make all plotly plots render in a new browser tab.
# This is more inconvenient, but should bypass any rendering issues.

# pio.renderers.default = 'browser'

sample_set = loans.sample(200, random_state=1)

fig = px.scatter(sample_set, x='dti', y='int_rate', trendline='ols',
                 labels={'dti': 'Debt-to-Income Ratio', 'int_rate': 'Interest Rate (%)'},
                 trendline_color_override='orange',
                 title='Interest Rate vs. Debt-to-Income Ratio')

# fig.show()

loans = pd.read_csv(loans_path)
loans = clean_loans(loans)
loans.head()

if 'q1' in questions or questions == [] or 'all' in questions:
    print(grader.check("q1"))

(
    loans['issue_d'].dt.year
    .value_counts()
    .sort_index()
    .plot(kind='line', 
          labels={'index': 'Year', 'value': 'Frequency'},
          title='Number of Loans Granted Per Year<br>(In Sample of Loans)')
    .update_layout(showlegend=False)
)

q2_correlations = correlations(loans, [
    ('dti', 'int_rate'),
    ('annual_inc', 'int_rate'),
    ('fico_range_low', 'int_rate'),
    ('term', 'int_rate')
])
q2_correlations

if 'q2' in questions or questions == [] or 'all' in questions:
    print(grader.check("q2"))

(
    q2_correlations
    .plot(kind='barh', 
          title='Correlation Between Interest Rate and Various Quantitative Features',
          labels={'index': 'Pair of Columns', 'value': 'Correlation'}
         )
    .update_layout(showlegend=False)
)

px.scatter(loans, x='fico_range_low', y='int_rate',
           labels={'fico_range_low': 'Credit Score', 'int_rate': 'Interest Rate (%)'},
           title='Interest Rate vs. Credit Score')

q3_fig = create_boxplot(loans)
q3_fig

if 'q3' in questions or questions == [] or 'all' in questions:
    print(grader.check("q3"))

# display(loans.assign(has_ps=loans['desc'].notna()).groupby('has_ps')['int_rate'].describe())
create_kde_plotly(
    loans.assign(has_ps=loans['desc'].notna()),
    'has_ps',
    True,
    False,
    'int_rate',
    title='Distributions of Interest Rates<br>Based on Inclusion of Personal Statement'
)

if 'q4' in questions or questions == [] or 'all' in questions:
    print(grader.check("q4"))

example_brackets = [
 (0.1, 0), 
 (0.12, 11000), 
 (0.22, 44725), 
 (0.24, 95375), 
 (0.32, 182100),
 (0.35, 231251),
 (0.37, 578125)]
example_owed = tax_owed(75000, example_brackets)
example_owed

if 'q5' in questions or questions == [] or 'all' in questions:
    print(grader.check("q5"))

state_taxes_raw_path = Path('data') / 'state_taxes_raw.csv'
state_taxes_raw = pd.read_csv(state_taxes_raw_path)
state_taxes_raw.head()

state_taxes_raw = pd.read_csv(state_taxes_raw_path)
state_taxes = clean_state_taxes(state_taxes_raw)
state_taxes.head()

if 'q6' in questions or questions == [] or 'all' in questions:
    print(grader.check("q6"))

loans = clean_loans(pd.read_csv(loans_path))
state_taxes = clean_state_taxes(pd.read_csv(state_taxes_raw_path))
loans_with_state_taxes = combine_loans_and_state_taxes(loans, state_taxes)
loans_with_state_taxes.head()

if 'q7' in questions or questions == [] or 'all' in questions:
    print(grader.check("q7"))

with_disposable_income = find_disposable_income(loans_with_state_taxes)
with_disposable_income.head()

if 'q8' in questions or questions == [] or 'all' in questions:
    print(grader.check("q8"))

effective_tax_per_state = (
    with_disposable_income
    .groupby('State')
    .apply(lambda df: df['state_tax_owed'].sum() / df['annual_inc'].sum())
)

median_income = (
    with_disposable_income
    .groupby('State')
    ['annual_inc']
    .median()
)

(
    pd.DataFrame()
    .assign(
        effective_tax_per_state=effective_tax_per_state, 
        median_income=median_income,
        count=with_disposable_income.value_counts('State')
    )
    .reset_index()
    .plot(
        kind='scatter',
        x='median_income',
        y='effective_tax_per_state',
        hover_name='State',
        size='count',
        title='Effective State Tax Rate vs. Median Income Per State',
        labels={
            'median_income': 'Median Income',
            'effective_tax_per_state': 'Effective State Tax Rate<br>sum(state tax) / sum(annual income)',
            'count': 'Number of Borrowers'
        }
    )
)

eng_nurse_loan_home = aggregate_and_combine(loans, ['engineer', 'nurse'], 'loan_amnt', 'home_ownership')
eng_nurse_loan_home

if 'q9' in questions or questions == [] or 'all' in questions:
    print(grader.check("q9"))

eng_nurse_loan_home

exists_paradox(**paradox_example(loans))

if 'q10' in questions or questions == [] or 'all' in questions:
    print(grader.check("q10"))

def loan_purpose_over_time(loans):
    loans = loans.copy()
    loan_purpose_yearly = loans.groupby([loans['issue_d'].dt.year, 'purpose']).size().unstack()
    loan_purpose_yearly = loan_purpose_yearly.reset_index().melt(id_vars='issue_d', var_name='Purpose', value_name='Frequency')
    
    fig = px.line(loan_purpose_yearly, x='issue_d', y='Frequency', color='Purpose', title='Trends in Loan Purposes Over Time')
    fig.update_xaxes(title_text='Year')
    fig.update_yaxes(title_text='Number of Loans')
    return fig

loan_purpose_over_time(loans)

