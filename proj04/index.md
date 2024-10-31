---
layout: page
title: "Final Project: The Data Science Lifecycle 📊"
description: Description of Final Project.
nav_exclude: true
---

<script type="text/javascript" async="" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>

# Final Project: The Data Science Lifecycle 📊
{:.no_toc}
## Checkpoint 1 Due Date: Friday, May 24th at 11:59PM
{:.no_toc}
## Checkpoint 2 Due Date: Friday, May 31st at 11:59PM
{:.no_toc}
## Final Due Date: Wednesday, June 12th at 11:59PM <span style="color:red">(no extension allowed!)</span>
{:.no_toc}

---

Welcome to Final Project, the final assignment of the quarter! 👋

This project aims to be a culmination of everything you've learned this quarter. In the project, you will conduct an open-ended investigation into one of the three datasets (Recipes and Ratings 🍽, League of Legends ⌨️, or Power Outages 🔋). **Specifically, you'll draw several visualizations to help understand the distributions of key variables, assess the missingness mechanisms of columns with missing values, test a hypotheses about the data, and finally, build and improve a predictive model.** This project will be entirely manually graded by us – that's right, no autograders!

Final Project worth 10% in your overall grade, which means it's worth double what previous projects were worth. Its checkpoint is also worth double a regular checkpoint, at 2%. 

As your final deliverables, you'll submit two things to us: a **public-facing website** as well as a **PDF of your Jupyter Notebook**. We encourage you to build something you are proud of as this will give you something concrete to put on your resume and show to potential employers!

{: .green }
> **Final Project is due on Wednesday, June 12th at 11:59PM. This is a hard deadline; you may NOT use the extension on this project.** This is because we need to start grading projects right when you turn them in, so that there is enough time for you to make regrade requests before we submit grades to campus. Note that we will not be able to hold many office hours during Finals Week, so make sure to start early.<br><br>
> The Final Project does also have two checkpoints, which is due on **Friday, May 24th** and **Friday, May 31st**. The Final Project Checkpoints are structured differently than other project checkpoints; rather than having you submit any code, you'll answer a few questions about your progress on the project. More details are in the [Checkpoint Submission](#checkpoint-submission) towards the bottom of this page. You can submit the [checkpoint 1](https://www.gradescope.com/courses/759147/assignments/4503144/) and [checkpoint 2](https://www.gradescope.com/courses/759147/assignments/4509099/) on Gradescope; make sure to tag your partner if you have one.

The project is broken into two parts:

- Part 1: An **analysis**, submitted as a Jupyter Notebook. This will contain the details of your work. **Focus on completing your analysis before moving to Part 2, as the analysis is the bulk of the project.**
- Part 2: A **report**, submitted as a website. This will contain a narrative "story" with visuals. **Focus on this after finishing _most_ of your analysis.**

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Choosing a Dataset

In this project, you will perform an open-ended investigation into a **single dataset**. You must choose **one** of the following three datasets.

[Recipes and Ratings 🍽](recipes-and-ratings){: .btn } &nbsp;&nbsp; [League of Legends ⌨️](league-of-legends){: .btn } &nbsp;&nbsp; [Power Outages 🔋](power-outages){: .btn }

The dataset description pages linked above each have three sections:
- **Getting the Data**: Describes how to access the data and, in some cases, what various features mean. (In general, you're going to have to understand what your data means on your own!)
- **Example Questions and Prediction Problems**: Example questions to explore in Part 1: Steps 1-4, and example prediction problems to build models for in Part 1: Steps 5-8. Use these as inspiration, but feel free to come up with your own questions and prediction problems!
- **Special Considerations**: Things to be aware of when working with the given dataset, e.g. some additional requirements.

When selecting which dataset you are going to use for your project, try choosing the one whose topic appeals to you the most as that will make finishing the project a lot more enjoyable.

To help contextualize the kinds of analysis you can do in this project, it might help to look at these examples from Spring 2023. These examples offer insights into crafting effective research questions, but bear in mind that they have their unique strengths and weaknesses. Treat them as a foundation for inspiration, but **don't** just repeat or copy their work – be original!

1. [League of Legends First Blood Statistical Analysis](https://krystalqjx.github.io/LOL-analysis/): This project excelled in clarifying their research aims, making the study understandable to a broader audience. In your own project, ensure that you provide a lucid and detailed explanation of your research focus.
2. [Analyzing Power Outages](https://nghosh24.github.io/power-outages/): This project presents a noval way to do the data visualization. In your project, please think about what is the best way to present your data.
3. [Investigation on the Relationship Between Amount of Sugar and Rating of Recipes](https://cecilia-lin.github.io/RecipeProject/): In this project, the students have effectively highlighted the improvement they made based on the baseline model. In your own project, also ensure that you explain what you have done to improve your baseline model.


{: .green }
Before choosing a dataset, read the rest of this page to see what's required of you!

---

## Part 1: Analysis

Before beginning your analysis, you'll need to set up a few things.

1. Pull the latest version of the [`dsc80-2024-sp`](https://github.com/dsc-courses/dsc80-2024-sp/) repo. Within the `projects/proj04` folder, there is a `template.ipynb` notebook that you will use as a template for the project. If you delete the file or want another copy of the template, you can re-download it from [here](https://github.com/dsc-courses/dsc80-2024-sp/blob/main/projects/04-The%20Data%20Science%20Lifecycle/template.ipynb). **This is where your analysis will live; you will submit this entire notebook to us.**
1. Select **one** of the three [datasets mentioned above](#choosing-a-dataset), download it, and load it into your template notebook.

Once you have your dataset loaded in your notebook, it's time for you to find meaning in the real-world data you've collected! Follow the steps below.

{: .green }
For each step, we specify what must be done in your notebook and what must go on your website, which we expand on in [Part 2](#part-2-report). We recommend you write everything in your notebook first, and then move things over to your website once you've completed your analysis.

<br>

In Steps 1-4, you'll develop a deeper understanding of your dataset while trying to answer a single question.

### Step 1: Introduction

| Step  | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **Introduction and Question Identification** | Understand the data you have access to. Brainstorm a few questions that interest you about the dataset. Pick **one** question you plan to investigate further. (As the [data science lifecycle](https://dsc80.com/resources/lectures/lec01/lec01.html#The-data-science-lifecycle) tells us, this question may change as you work on your project.) | Provide an introduction to your dataset, and clearly state the one question your project is centered around. Why should readers of your website care about the dataset and your question specifically? Report the number of rows in the dataset, the names of the columns that are relevant to your question, and descriptions of those relevant columns. |

### Step 2: Data Cleaning and Exploratory Data Analysis

| Step  | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **Data Cleaning** | Clean the data appropriately. For instance, you may need to replace data that should be missing with `NaN` or create new columns out of given ones (e.g. compute distances, scale data, or get time information from time stamps). | Describe, in detail, the data cleaning steps you took and how they affected your analyses. The steps should be explained in reference to the data generating process. Show the `head` of your cleaned DataFrame (see [Part 2: Report](#part-2-report) for instructions).|
| **Univariate Analysis** | Look at the distributions of relevant columns separately by using DataFrame operations and drawing at least two relevant plots. | Embed **at least one** `plotly` plot you created in your notebook that displays the distribution of a single column (see [Part 2: Report](#part-2-report) for instructions). Include a 1-2 sentence explanation about your plot, making sure to describe and interpret any trends present. (Your notebook will likely have more visualizations than your website, and that's fine. Feel free to embed more than one univariate visualization in your website if you'd like, but make sure that each embedded plot is accompanied by a description.) |
| **Bivariate Analysis** | Look at the statistics of pairs of columns to identify possible associations. For instance, you may create scatter plots and plot conditional distributions, or box-plots. You must plot at least two such plots in your notebook. The results of your bivariate analyses will be helpful in identifying interesting hypothesis tests! | Embed **at least one** `plotly` plot that displays the relationship between two columns. Include a 1-2 sentence explanation about your plot, making sure to describe and interpret any trends present. (Your notebook will likely have more visualizations than your website, and that's fine. Feel free to embed more than one bivariate visualization in your website if you'd like, but make sure that each embedded plot is accompanied by a description.) |
| **Interesting Aggregates** | Choose columns to group and pivot by and examine aggregate statistics. | Embed at least one grouped table or pivot table in your website and explain its significance. |

### Step 3: Assessment of Missingness

| Step  | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **NMAR Analysis** | Recall, to determine whether data are likely NMAR, you must reason about the data generating process; you cannot conclude that data are likely NMAR solely by looking at your data. As such, there's no code to write here (and hence, nothing to put in your notebook). | State whether you believe there is a column in your dataset that is NMAR. Explain your reasoning and any additional data you might want to obtain that could explain the missingness (thereby making it MAR). Make sure to explicitly use the term "NMAR." |
| **Missingness Dependency** | Pick a column in the dataset with non-trivial missingness to analyze, and perform permutation tests to analyze the dependency of the missingness of this column on other columns.<br><br>Specifically, find at least one other column that the missingness of your selected column **does** depend on, and at least one other column that the missingness of your selected column **does not** depend on.<br><br>**_Tip_**: Make sure you know the difference between the different types of missingness before approaching that section. Many students in the past have lost credit for mistaking one type of missingness for another.<br><br>Note that some datasets may have special requirements for this section; look at the "Special Considerations" section of your chosen dataset for more details. | Present and interpret the results of your missingness permutation tests with respect to your data and question. Embed a `plotly` plot related to your missingness exploration; ideas include:<br>• The distribution of column $$Y$$ when column $$X$$ is missing and the distribution of column $$Y$$ when column $$X$$ is not missing, as was done in [Lecture 8](https://dsc80.com/resources/lectures/lec08/lec08.html).<br>• The empirical distribution of the test statistic used in one of your permutation tests, along with the observed statistic. |

### Step 4: Hypothesis Testing

| Step  | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **Hypothesis Testing** | Clearly state a pair of hypotheses and perform a **hypothesis test or permutation test** that is not related to missingness. Feel free to use one of the example questions stated in the "Example Questions and Prediction Problems" section of your dataset's description page or pose a hypothesis test of your own. | Clearly state your null and alternative hypotheses, your choice of test statistic and significance level, the resulting $$p$$-value, and your conclusion. Justify why these choices are good choices for answering the question you are trying to answer.<br><br>**_Optional_**: Embed a visualization related to your hypothesis test in your website.<br><br>**_Tip_**: When making writing your conclusions to the statistical tests in this project, **never** use language that implies an absolute conclusion; since we are performing statistical tests and not randomized controlled trials, we cannot prove that either hypothesis is 100% true or false. |

<br>

In Steps 5-8, you will build a predictive model, based on the knowledge of your dataset you developed in Steps 1-4.

### Step 5: Framing a Prediction Problem

| Step  | Analysis in Notebook | Report on Website |
| --- | --- | --- |
|**Problem Identification**|Identify a prediction problem. Feel free to use one of the example prediction problems stated in the "Example Questions and Prediction Problems" section of your dataset's description page or pose a hypothesis test of your own. The prediction problem you come up with doesn't have to be related to the question you were answering in Steps 1-4, but ideally, your entire project has some sort of coherent theme.|Clearly state your prediction problem and type (classification or regression). If you are building a classifier, make sure to state whether you are performing binary classification or multiclass classification. Report the response variable (i.e. the variable you are predicting) and why you chose it, the metric you are using to evaluate your model and why you chose it over other suitable metrics (e.g. accuracy vs. F1-score).<br><br>***Note***: Make sure to justify what information you would know at the "time of prediction" and to only train your model using those features. For instance, if we wanted to predict your final exam grade, we couldn’t use your Final Project grade, because the project is only due after the final exam! Feel free to ask questions if you're not sure.|

### Step 6: Baseline Model

| Step  | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **Baseline Model** | Train a "baseline model" for your prediction task that uses at least two features. (For this requirement, two features means selecting at least two columns from your original dataset that you should transform). You can leave numerical features as-is, but you'll need to take care of categorical columns using an appropriate encoding. Implement all steps (feature transforms and model training) in a single `sklearn` `Pipeline`. <br><br>**_Note_**: **Both now and in Step 7: Final Model, make sure to evaluate your model's ability to generalize to unseen data!** <br><br>There is no "required" performance metric that your baseline model needs to achieve. | Describe your model and state the features in your model, including how many are quantitative, ordinal, and nominal, and how you performed any necessary encodings. Report the performance of your model and whether or not you believe your current model is "good" and why.<br><br>**_Tip_**: Make sure to hit all of the points above: many projects in the past have lost points for not doing so. |

### Step 7: Final Model

| Step  | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **Final Model** | Create a "final" model that improves upon the "baseline" model you created in Step 2. Do so by engineering at least two new features from the data, on top of any categorical encodings you performed in Baseline Model Step. (For instance, you may use a `StandardScaler` on a quantitative column and a `QuantileTransformer` transformer on a different column to get two new features.) Again, implement all steps in a single `sklearn` `Pipeline`. While deciding what features to use, you **must** perform a search for the best hyperparameters (e.g. tree depth) to use amongst a list(s) of options, either by using `GridSearchCV` or through some manual iterative method. In your notebook, state which hyperparameters you plan to tune and why before actually tuning them.<br><br>**_Optional_**: You are encouraged to try many different modeling algorithms for your final model (i.e. `LinearRegression`, `RandomForestClassifier`, `Lasso`, `SVC`, etc.) If you do this, make sure to clearly indicate in your notebook which model is your actual final model as that will be used to grade the above requirements.<br><br>**_Note 1_**: When training your model, make sure you use the same unseen and seen datasets from your baseline model. This way, the evaluation metric you get on your final model can be compared to your baseline's on the basis of the model itself and not the dataset it was trained on. Based on which method you use for hyperparameter tuning, this may mean that you will need to use some of your training data as your validation data. If this is the case, make sure to train your final model on the whole dataset prior to evaluation.<br><br>**_Note 2_**: You will not be graded on "how much" your model improved from Step 6: Baseline Model to Step 7: Final Model. What you will be graded on is on whether or not your model improved, as well as your thoughtfulness and effort in creating features, along with the other points above.<br><br>**_Note 3_**: Don't try to improve your model's performance just by blindly transforming existing features into new ones. Think critically about what each transformation you're doing actually does. For example, there's no use in using a `StandardScaler` transformer if your goal is to reduce the RMSE of a linear model: as we learned in DSC 40A, and in Lecture 15, standardizing features in a regression model does not change the model's predictions, only its coefficients! | State the features you added and **why** they are good for the data and prediction task. Note that you can't simply state "these features improved my accuracy", since you'd need to choose these features and fit a model before noticing that – instead, talk about _why_ you believe these features improved your model's performance from the perspective of the data generating process. <br><br>Describe the modeling algorithm you chose, the hyperparameters that ended up performing the best, and the method you used to select hyperparameters and your overall model. Describe how your Final Model's performance is an improvement over your Baseline Model's performance.<br><br>**_Optional_**: Include a visualization that describes your model's performance, e.g. a confusion matrix, if applicable. |

### Step 8: Fairness Analysis

| Step  | Analysis in Notebook | Report on Website |
| --- | --- | --- |
| **Fairness Analysis** | Perform a "fairness analysis" of your Final Model from the previous step. That is, try and answer the question "does my model perform worse for individuals in Group X than it does for individuals in Group Y?", for an interesting choice of X and Y.<br><br>As always, when comparing some quantitative attribute (in this case, something like precision or RMSE) across two groups, we use a **permutation test**. Let's illustrate how this works with an example. Let's suppose we have a sample voter dataset with columns `'Name'`, `'Age'`, and `'Voted'`, among others. We build a classifier that predicts whether someone voted (`1`) or didn't (`0`).<br><br>Here, we'll say our two groups are <br>• "young people", people younger than 40<br>• "old people", people older than 40<br><br>Note that in this example, we manually created these groups by **binarizing** the `'Age'` column in our dataset, and that's fine. (Remember, the `Binarizer` transformer with a threshold of 40 can do this for us.)<br><br>For our evaluation metric, we'll choose precision. (In Week 10's lectures, we'll look at other evaluation metrics and related parity measures for classifiers; choose the one that is most appropriate to your prediction task. If you built a regression model, you cannot use classification metrics like precision or recall; instead, you must use RMSE or $$R^2$$.)<br><br>Now, we must perform a permutation test. Before doing so, we must clearly state a null and an alternative hypothesis.<br>• **Null Hypothesis**: Our model is fair. Its precision for young people and old people are roughly the same, and any differences are due to random chance.<br>• **Alternative Hypothesis**: Our model is unfair. Its precision for young people is lower than its precision for old people.<br><br>From here, you should be able to implement the necessary permutation test. The only other guidance we will provide you with is that you should **not** be modifying your model to produce different results when computing test statistics; use only your final fitted model from Final Model Step. | Clearly state your choice of Group X and Group Y, your evaluation metric, your null and alternative hypotheses, your choice of test statistic and significance level, the resulting $$p$$-value, and your conclusion.<br><br>**_Optional_**: Embed a visualization related to your permutation test in your website. |

### Style

While your website will neatly organized and tailored for public consumption, it is important to keep your analysis notebook organized as well. Follow these guidelines:

- Your work for each of the eight project steps described above (Introduction, Data Cleaning and Exploratory Data Analysis, ..., Fairness Analysis) should be completed in code cells underneath the Markdown header of that section's name.
- You should **only include work that is relevant** to posing, explaining, and answering the question(s) you state in your website. You should include data quality, cleaning, and missingness assessments, and intermediate models and features you tried, though these should broadly be relevant to the tasks at hand.
- Make sure to clearly explain what each component of your notebook **means**. Specifically:
  - All plots should have titles, labels, and a legend (if applicable), even if they don't make it into your website. Plots should be self-contained – readers should be able to understand what they describe without having to read anything else.
  - All code cells should contain a comment describing how the code works (unless the code is self-explanatory – use your best judgement).

---

## Part 2: Report

The purpose of your website is to provide the general public – your classmates, friends, family, recruiters, and random internet strangers – with an overview of your project and its findings, without forcing them to understand every last detail. We don't expect the website creation process to take very much time, but it will certainly be rewarding. Once you've completed your analysis and know _what_ you will put in your website, start reading this section.

Your website must clearly contain the following eight headings, corresponding to the eight steps mentioned in [Part 1](#part-1-analysis):

- Introduction
- Data Cleaning and Exploratory Data Analysis
- Assessment of Missingness
- Hypothesis Testing
- Framing a Prediction Problem
- Baseline Model
- Final Model
- Fairness Analysis

**Don't** include "Step 1", "Step 2", etc. in your headings – the headings should be exactly as they are above.

The specific content your website needs to contain is described in the "Report on Website" columns above. Make sure to also give your website a creative title that relates to the question you're trying to answer, and clearly state your name(s).

Your report will be in the form of a _static_ website, hosted for free on GitHub Pages. More specifically, you'll use [Jekyll](https://jekyllrb.com), a framework built into GitHub Pages that allows you to create professional-looking websites just by writing Markdown ([dsc80.com](https://dsc80.com) is built using Jekyll!). GitHub Pages does the "hard" part of converting your Markdown to HTML.

If you'd like to follow the official [GitHub Pages & Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll) tutorial, you're welcome to, though we will provide you with a perhaps simpler set of instructions here. A very basic site with the required headings and one embedded visualization can be found at [rampure.org/dsc80-proj3-test1/](http://rampure.org/dsc80-proj3-test1/); the source code for the site is [here](https://github.com/surajrampure/dsc80-proj3-test1).

### Step 1: Initializing a Jekyll GitHub Pages Site

1. Create a GitHub account, if you don't already have one.
1. Create a new GitHub repository for your project.
   - GitHub Pages sites live at `<username>.github.io/<reponame>` (for instance, the site for [github.com/dsc-courses/dsc80-2024-sp](https://github.com/dsc-courses/dsc80-2024-sp) is [dsc-courses.github.io/dsc80-2024-sp](https://dsc-courses.github.io/dsc80-2024-sp)).
   - As such, **don't** include "DSC 80" or "Final Project" in your repo's name – this looks unprofessional to future employers, and gives you a generic-sounding URL. Instead, mention that this is a project for DSC 80 at UCSD in the repository description.
   - **Make sure to make your repository public.**
   - Select "ADD a README file." This ensures that your repository starts off non-empty, which is necessary to continue.
1. Click "Settings" in the repository toolbar (next to "Insights"), then click "Pages" in the left menu.
1. Under "Branch", click the "None" dropdown, change the branch to "main", and then click "Save." You should soon see "GitHub Pages source saved." in a blue banner at the top of the page. This initiates GitHub Pages in your repository.
1. After 30 seconds, reload the page again. You should see "**Your site is live at http://username.github.io/reponame/**". Click that link – you now have a site!
1. Click "Code" in the repo toolbar to return to the source code for your repo.

Note that the source code for your site lives in `README.md`. **As you push changes to `README.md`, they will update on your site automatically within a few minutes!** Before moving forward, make sure that you can make basic edits:

1. Clone your repo locally.
1. Make some edits to `README.md`.
1. Push those changes back to GitHub, using the following steps:
   - Add your changes to "staging" using `git add README.md` (repeat this for any other files you add).
   - Commit your changes using `git commit -m '<some message here>'`, e.g. `git commit -m 'changed title of website'`.
   - Push your changes using `git push`.

Moving forward, we recommend making edits to your website source code locally, rather than directly on GitHub. This is in part due to the fact that you'll be creating folders and adding files to your source code.

### Step 2: Choosing a Theme

The default "theme" of a Jekyll site is not all that interesting.

To change the theme of your site:

1. Create a file in your repository called `_config.yml`.
1. Go [here](https://pages.github.com/themes/), and click the links of various themes until you find one you like.
1. Open the linked repository for the theme you'd like to use and scroll down to the "Usage" section of the README. Copy the necessary information from the README to your `_config.yml` and push it to your site.

For instance, if I wanted to use the Merlot theme, I'd put the following in my `_config.yml`:

```yml
remote_theme: pages-themes/merlot@v0.2.0
plugins:
  - jekyll-remote-theme # add this line to the plugins list if you already have one
```

Note that you're free to use any Jekyll theme, not just the ones that appear [here](https://pages.github.com/themes/). You are required to choose _some_ theme other than the default, though. See more details about themes [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll).

### Step 3: Embedding Content

Now comes the interesting part – actually including content in your site. The [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/) contains tips on how to format text and other page components in Markdown (and if you'd benefit by seeing an example, you could always look at the Markdown source of [this very page](https://raw.githubusercontent.com/dsc-courses/dsc80-2024-sp/gh-pages/project4/index.md) – meta!).

What will be a bit trickier is embedding `plotly` plots in your site so that they are interactive. Note that you are **required** to do this, you cannot simply take screenshots of plots from your notebooks and embed them in your site. Here's how to embed a `plotly` plot directly in your site.

1. First, you'll need to convert your plot to HTML. If `fig` is a `plotly` `Figure` object (for instance, the result of calling `px.express`, `go.Figure`, or `.plot` when `pd.options.plotting.backend = "plotly"` has been run), then the method `fig.write_html` saves the plot as HTML to a file. Call it using `fig.write_html('file-name.html', include_plotlyjs='cdn')`.
   - Change `'file-name.html'` to the path where you'd like to initially save your plot.
   - `include_plotlyjs='cdn'` tells `write_html` to load the source code for the `plotly` library from a server, rather than including the entire source code in your HTML file. This drastically reduces the size of the resulting HTML file, keeping your repo size down.
1. Move the `.html` file(s) you've created into a folder in your website repo called `assets` (or something similar).
   - Depending on where your template notebook is saved, you could combine this step with the step above by calling `fig.write_html` with the correct path (e.g. `fig.write_html('../league-match-analysis/assets/matches-per-year.html')).
1. In `README.md`, embed your plot using the following syntax:

```html
<iframe
  src="assets/file-name.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>
```

- `iframe` stands for "inline frame"; it allows us to embed HTML files within other HTML files.
- You can change the `width` and `height` arguments, but don't change the `frameBorder` argument.

Refer [here](https://github.com/surajrampure/dsc80-proj3-test1) for a working example.

{: .note }
Try your best to make your plots look professional and unique to your group – add axis labels, change the font and colors, add annotations, etc. Remember, potential employers will see this – you don't want your plots to look like everyone else's! If you'd like to match the styles of the `plotly` plots used in lecture (e.g. with the white backgrounds), you can import and use the `dsc80_utils.py` that's in the `proj04` folder of our public repo, alongside `template.ipynb`.

To convert a DataFrame in your notebook to Markdown source code (which you need to do for both the **Data Cleaning** and **Interesting Aggregates** sections of Step 2: Data Cleaning and Exploratory Data Analysis in Part 1), use the `.to_markdown()` method on the DataFrame. For instance,

```py
print(counts[['Quarter', 'Count']].head().to_markdown(index=False))
```

displays a string, containing the Markdown representation of the first 5 rows of `counts`, including only the `'Quarter'` and `'Count'` columns (and not including the index). You can see how this appears [here](http://rampure.org/dsc80-proj3-test1/#assessment-of-missingness); remember, no screenshots. You may need to play with this a little bit so that you don't show DataFrames that are super, super wide and look ugly.

### Local Setup

The above instructions give you all you need to create and make updates to your site. However, you _may_ want to set up Jekyll locally, so that you can look at how changes to your site would look without having to push and wait for GitHub to re-build your site. To do so, follow the steps [here](https://jekyllrb.com/docs/installation/) and then [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll).

---

## Submission and Rubric

### Checkpoint 1 Submission

As mentioned at the top of this page, this project **does** have two checkpoints, which is worth 1% of your overall grade. The first checkpoint is due on **Friday, May 24th**. You can submit the checkpoint [here](https://www.gradescope.com/courses/759147/assignments/4503144/) on Gradescope.

The checkpoint 1 assignment is worth 20 points, and asks you to answer the following questions:

1. (2 points) Which of the three datasets did you choose? Why?
1. (6 points) Upload a screenshot of a `plotly` visualization you've created while completing Part 1, Step 2: Data Cleaning and Exploratory Data Analysis.
1. (6 points) What is the pair of hypotheses you plan on testing in Part 1, Step 4? What is the test statistic you plan on using?
1. (6 points) What is the column you plan on trying to predict in Part 1, Steps 5-8? Is it a classification or regression problem?

### Checkpoint 2 Submission

As mentioned at the top of this page, this project **does** have two checkpoints, which is worth 1% of your overall grade. The second one is due on **Friday, May 31st**. You can submit the checkpoint [here](https://www.gradescope.com/courses/759147/assignments/4509099/) on Gradescope.

The checkpoint 2 assignment is worth 20 points, and asks you to answer the following questions:

1. (7.5 points) For step 4, what are two hypotheses you have tested, and what were the result?
1. (7.5 points) Briefly explain your baseline model and your plans for improving the model.
1. (5 points) Submit a working GitHub page webpage URL for the project. On the webpage, you need to at least include a project title.


### Final Submission

You will ultimately submit your project in two ways:

1. By uploading a **PDF version** of your notebook to the specific "Final Project Notebook PDF (Dataset)" assignment on Gradescope **for your dataset**.
   - To export your notebook as a PDF, first, restart your kernel and run all cells. Then, go to "File > Print Preview". Then, save a print preview of the webpage as a PDF. There are other ways to save a notebook as a PDF but they may require that you have additional packages installed on your computer, so this is likely the most straightforward.
   - It's fine if your `plotly` graphs don't render in the PDF output of your notebook. However, **make sure none of the code is cut off in your notebook's PDF**. **You will lose 5% of the points available on this project if your code is cut off.**
   - This notebook asks you to include a link to your website; make sure to do so.
2. By submitting a **link to your website** to the "Final Project Website Link (All Datasets)" assignment on Gradescope.

To both submissions, make sure to tag your partner. You don't need to submit your actual `.ipynb` file anywhere. **While your website must be public and you should share it with others, you should _not_ make your code for this project available publicly.**

Since there are two assignments you need to submit on Gradescope, we will treat your submission time as being the **latter** of your two submissions. So, if you submit to the "Final Project Notebook PDF" assignment before the deadline but to the "Final Project Website Link (All Datasets)" website one day late, overall, that counts as late submission.

{: .warning }
There are a lot of moving parts to this assignment – don't wait until the last minute to try and submit!

### Rubric

Your project will be graded out of 200 points. The rough rubric is shown below. If you satisfy these requirements as described above, you will receive full credit.

Note that the rubric is intentionally vague when it comes to Steps 5-8. This is because an exact rubric would specify exactly what you need to do to build a model, but figuring out what to do is a large part of Steps 5-8.

| Component                                                      | Weight         |
| -------------------------------------------------------------- | -------------- |
| **Step 1: Introduction**       | 8 points       |
| **Step 2: Data Cleaning and Exploratory Data Analysis** <br>• Cleaned data (8 points)<br>• Performed univariate analyses (8 points)<br>• Performed bivariate analyses and aggregations (8 points) | 24 points       |
| **Step 3: Assessment of Missingness** <br>• Addressed NMAR question (4 points) <br> • Performed permutation tests for missingness (8 points) <br> • Interpreted missingness test results (8 points)                                       | 20 points |
| **Step 4: Hypothesis Testing**<br>• Selected relevant columns for a hypothesis or permutation test (4 points)<br>• Explicitly stated a null hypothesis (4 points)<br>• Explicitly stated an alternative hypothesis (4 points)<br>• Performed a hypothesis or permutation test (8 points)<br>• Used a valid test statistic (4 points)<br>• Computed a $$p$$-value and made a decision (4 points)  | 28 points | 
| **Step 5: Framing a Prediction Problem** | 15 points |
| **Step 6: Baseline Model** | 35 points |
| **Step 7: Final Model** | 35 points |
| **Step 8: Fairness Analysis** | 15 points |
| **Overall: Included all necessary components on the website** | 20 points      |
| **Total**                                                      | **200 points** |