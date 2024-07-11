import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("C:\\Users\\vssau\\fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data
# Calculate the 2.5% and 97.5% quantiles
lower_quantile = df['value'].quantile(0.025)
upper_quantile = df['value'].quantile(0.975)
df = df[(df['value'] > lower_quantile) & (df['value'] < upper_quantile)]


def draw_line_plot():
    # Draw line plot
    # Set the figure size for better readability
    fig, ax = plt.subplots(figsize=(15, 5))
    # Plot the data
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    # Set the title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Resample the data by month and year to calculate the average daily page views
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    # Create the bar plot
    fig, ax = plt.subplots(figsize=(15,10))
    df_bar.plot(kind='bar', ax=ax)
    
    # Set the title and labels
    ax.set_title('Average Daily Page Views per Month (2016-2019)')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    
    # Customize the legend
    plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

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
    # Sort month names for proper order in the plot
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Define color palettes
    year_palette = sns.color_palette("husl", len(df_box['year'].unique()))  # Unique colors for each year
    month_palette = sns.color_palette("husl", len(month_order))  # Unique colors for each month

    # Create the figure and axes for the plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
   
    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], palette=year_palette)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=axes[1], palette=month_palette)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
