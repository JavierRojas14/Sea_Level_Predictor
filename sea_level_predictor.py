import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fig, axis = plt.subplots(figsize = (12, 6))
    axis.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    regresion = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = regresion.slope
    intercept = regresion.intercept

    linea_regresion = {'Year': [i for i in range(1880, 2051)], 'Value': []}

    for i in linea_regresion['Year']:
        valor_regresion = (slope * i) + intercept
        linea_regresion['Value'].append(valor_regresion)

    regresion = pd.DataFrame(linea_regresion)
    axis.plot(regresion['Year'], regresion['Value'])


    # Create second line of best fit
    mask = df['Year'] >= 2000
    df_2000 = df[mask]

    regr_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    slope_2000 = regr_2000.slope
    intercept_2000 = regr_2000.intercept

    año2050_slope2000 = {'Year': [i for i in range(2000, 2051)], 'Value': []}

    for i in año2050_slope2000['Year']:
        valor_regresion = (slope_2000 * i) + intercept_2000
        año2050_slope2000['Value'].append(valor_regresion)

    df_2000 = pd.DataFrame(año2050_slope2000)
    axis.plot(df_2000['Year'], df_2000['Value'])


    # Add labels and title
    axis.set_xlabel('Year')
    axis.set_ylabel('Sea Level (inches)')
    axis.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()