# lab.py


import pandas as pd
import numpy as np
import sys
import os
from dsc80_utils import *



# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def amina_function():
    visits = pd.read_csv('data/visits.csv', parse_dates=['entry'])
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def least_function():
    ...


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def never_function():
    parks = pd.read_csv('data/parks.csv')
    visits = pd.read_csv('data/visits.csv', parse_dates=['entry'])
    df1 = parks.merge(visits, on='park_id', how='inner')
    df2 = parks.merge(visits, on='park_id', how='left')
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def prop_missing_function():
    df = pd.read_csv('data/visits_missing_a.csv')
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


np.random.seed(42)
df = pd.read_csv('data/visits_missing_a.csv')
with_2020 = df.assign(is_2020=df['entry_year'] == 2020)
stats, obs = permutation_test(with_2020, 'entry_hour', 'is_2020', tvd)

def p_val_function():
    np.random.seed(42)
    with_2020 = df.assign(is_2020=df['entry_year'] == 2020)
    stats, obs = permutation_test(with_2020, 'entry_hour', 'is_2020', tvd)
    ...

def reject_function():
    ...



# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def hour_pval_function():
    df = pd.read_csv('data/visits_missing_a.csv')
    ...

def hour_mar_function():
    ...


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


np.random.seed(42)
def pvals_functions():
    ...
    
def mar_cols_function():
    ...
    
