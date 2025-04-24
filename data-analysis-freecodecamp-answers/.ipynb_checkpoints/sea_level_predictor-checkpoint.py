import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    sea_lr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(df['Year'].min(), 2050, 1)
    y = sea_lr.slope * x + sea_lr.intercept
    plt.plot(x, y)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]

    sea_lr2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = np.arange(df_2000['Year'].min(), 2050, 1)
    y_2000 = sea_lr2.slope * x_2000 + sea_lr2.intercept

    plt.plot(x_2000, y_2000)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()