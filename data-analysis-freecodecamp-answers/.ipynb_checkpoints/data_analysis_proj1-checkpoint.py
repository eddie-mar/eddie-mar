#mean-std
import numpy as np

def calculate(working_list):
    if len(working_list) != 9:
        raise ValueError('List must contain nine numbers.')
    working_array = np.array(working_list)

    calculations = dict()
    axes = [0, 1, None]

    calculations['mean'] = [working_array.mean(axis=i) for i in axes]
    calculations['variance'] = [working_array.var(axis=i) for i in axes]
    calculations['standard deviation'] = [working_array.std(axis=i) for i in axes]
    calculations['max'] = [working_array.max(axis=i) for i in axes]
    calculations['min'] = [working_array.min(axis=i) for i in axes]
    calculations['sum'] = [working_array.sum(axis=i) for i in axes]

    for key in calculations.keys():
        for index in range(len(calculations[key]) - 1):
            calculations[key][index] = list(calculations[key][index])

    return calculations


import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_total = df['education'].value_counts()['Bachelors']
    index_total = df['education'].count()
    percentage_bachelors = (bachelors_total / index_total) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    hi_educ_degree = ['Bachelors', 'Masters', 'Doctorate']
    hi_df = df[df['education'].isin(hi_educ_degree)]
    hi_df_50k = hi_df[hi_df['salary'] == '>50K'].count()['salary']

    low_df = df[~df['education'].isin(hi_educ_degree)]
    low_df_50k = low_df[low_df['salary'] == '>50K'].count()['salary']

    # percentage with salary >50K
    higher_education_rich = (hi_df_50k / hi_df.count()['salary']) * 100
    lower_education_rich = (low_df_50k / low_df.count()['salary']) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hrs_df = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_hrs_df[min_hrs_df['salary'] == '>50K'].count()['salary']
    rich_percentage = (num_min_workers / min_hrs_df.count()['salary']) * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = 0

    for country in df['native-country'].unique():
        country_df = df[df['native-country'] == country]
        over_50k = country_df[country_df['salary'] == '>50K'].count()['salary']
        country_percentage = (over_50k / country_df.count()['salary']) * 100
        if country_percentage > highest_earning_country_percentage:
            highest_earning_country_percentage = country_percentage
            highest_earning_country = country

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df[df['native-country'] == 'India']
    india_50k = india_df[india_df['salary'] == '>50K']
    top_IN_occupation = india_50k['occupation'].value_counts().keys()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


x = calculate_demographic_data()



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
# 2
df['BMI'] = (df['weight'] / (df['height'] / 100) ** 2)
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

# 4
def draw_cat_plot(df=df):
    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc',
                    'smoke', 'alco', 'active', 'overweight'],
                     var_name='variable', value_name='value')

    # 6
    df_cat = df_cat.groupby('cardio').value_counts(sort=False)
    df_cat = df_cat.reset_index()
    df_cat.rename(columns={0: 'total'}, inplace=True)

    # 7
    cat_plot = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar', errorbar=None)

    # 8
    fig = cat_plot

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map(df=df):
    # 11
    height_filter = (df['height'] > df['height'].quantile(0.025)) & (df['height'] < df['height'].quantile(0.975))
    weight_filter = (df['weight'] > df['weight'].quantile(0.025)) & (df['weight'] < df['weight'].quantile(0.975))
    dias_sys = df['ap_hi'] >= df['ap_lo']
    df_heat = df[height_filter & weight_filter & dias_sys]

    # 12
    df_heat = df_heat.drop(columns=['BMI'])
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12,10))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cbar_kws={'shrink': 0.5}, center=0)

    # 16
    fig.savefig('heatmap.png')
    return fig


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col=[0])

# Clean data
df = df[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]


def draw_line_plot(df=df):
    # Draw line plot
    df_line = df.copy()
    fig, axes = plt.subplots(figsize=(15,6))

    axes.plot(df_line.index, df_line.value)
    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month_name()
    df_bar['Month'] = pd.Categorical(df_bar['Month'], categories=[
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'], ordered=True)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(data=df_bar, x='Years', y='value', hue='Month', errorbar=None, palette='bright', ax=ax)
    ax.legend(title='Months')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,8))

    sns.boxplot(data=df_box, x='year', y='value', ax=ax1, palette='tab10', flierprops={'marker': '.', 'ms': 3, 'fillstyle': 'full'}, linewidth = 0.5)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_yticks(range(0, 220000, 20000))
    ax1.set_title('Year-wise Box Plot (Trend)')

    order = (df_box.month.unique().tolist()) * 2
    order = order[8: 20]
    sns.boxplot(data=df_box, x='month', y='value', ax=ax2, palette='muted', order=order, flierprops={'marker': '.', 'ms': 3, 'fillstyle': 'full'}, linewidth = 0.5)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_yticks(range(0, 220000, 20000))
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    sea_lr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = range(df['Year'][0], 2051)
    ax.plot(x, sea_lr.slope * x + sea_lr.intercept)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    sea_lr2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x = range(df_2000['Year'][0], 2051)
    ax.plot(x, sea_lr2.slope * x + sea_lr2.intercept)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


