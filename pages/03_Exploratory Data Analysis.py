import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
# from wordcloud import WordCloud
# from nltk.corpus import stopwords
# import nltk

st.title("Exploratory Data Analysis")

df = pd.read_csv('data/involved_data_final.csv')
# st.dataframe(df)


# SELF ACCIDENT VS NOT SELF ACCIDENT
fraud_map = {0: 'is_not_self_accident', 1: 'self_accident'}
df['Class'] = df['is_self_accident'].map(fraud_map)

# Plotting function
def plot_graph(data):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x=data['Class'],
                  order=data['Class'].value_counts().index,
                  color='#1D2371')
    plt.xlabel(' ')
    plt.ylabel(' ')
    for spine in ['right', 'top']:
        ax.spines[spine].set_visible(False)
    plt.title('Distribution of Vehicular Accidents in Metro Manila', size=15, y=1)
    st.pyplot(fig)

# Streamlit app
def main():
    st.header('Vehicular Accidents in Metro Manila')
    st.write('This app visualizes the distribution of vehicular accidents.')

    # Display the DataFrame
    st.write('Data:')
    st.write(df['Class'].value_counts())

    # Plot the graph
    st.write('Graph:')
    plot_graph(df)

if __name__ == '__main__':
    main()



# TOP CITIES WHERE ACCIDENTS OCCUR
# Function to plot bar chart
def plot_bar_chart(df):
    top_cities = df['City'].value_counts().head(8)
    df_sorted = df[df['City'].isin(top_cities.index)]

  # Create color list
    colors = ['lightgray'] * len(top_cities)  # Changed color to #1D2371
    for idx, city in enumerate(top_cities.index):
        if city in top_cities.index[:3]:
            colors[idx] = '#1D2371'

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_cities.index, top_cities.values, color=colors)
    ax.set_xlabel('Number of Accidents')
    ax.set_ylabel('City')
    ax.set_title('Top Cities Where Accidents Occur')
    ax.invert_yaxis()  # To display from highest to lowest
    for spine in ['right', 'top']:
        ax.spines[spine].set_visible(False)
    st.pyplot(fig)

# Streamlit app
def main():
    st.header('Accidents Occurrence by City')
    st.write('This app visualizes the top cities where accidents occur.')

    # Plot the bar chart
    st.write('Bar Chart:')
    plot_bar_chart(df)

if __name__ == '__main__':
    main()



# TOP LOCATIONS WHERE ACCIDENTS OCCUR
# Function to plot bar chart
def plot_bar_chart(df):
    top_cities = df['Location'].value_counts().head(10)

    colors = ['lightgray'] * len(top_cities)
    top_cities_index = top_cities.index[:3]
    for idx in range(len(colors)):
        if idx < 3:
            colors[idx] = '#1D2371'  # Change to #1D2371 for the top 3 cities

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_cities.index, top_cities.values, color=colors)
    for spine in ['right', 'top']:
        ax.spines[spine].set_visible(False)

    plt.xlabel('Number of Accidents')
    plt.ylabel('Location')
    plt.title('Top Locations Where Accidents Occur')
    plt.gca().invert_yaxis()  # To display from highest to lowest
    st.pyplot(fig)

# Streamlit app
def main():
    st.title('Top Accident Locations')
    st.write('This app visualizes the top locations where accidents occur.')

    # Plot the bar chart
    st.write('Bar Chart:')
    plot_bar_chart(df)

if __name__ == '__main__':
    main()



# ACCIDENTS PER DIRECTION
# Function to plot bar chart
def plot_bar_chart(df):
    direction_counts = df['Direction'].value_counts()

    colors = ['lightgray'] * 5  # Default color of other directions
    colors[:2] = ['#1D2371'] * 2  # Change color for NB and SB

    fig, ax = plt.subplots(figsize=(10, 6))
    direction_counts.plot(kind='bar', color=colors, ax=ax)

    # Customizing the plot
    ax.set_xlabel('Direction')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Direction')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.title('Accidents by Direction')
    st.write('This app visualizes the number of accidents by direction.')

    # Plot the bar chart
    st.write('Bar Chart:')
    plot_bar_chart(df)

if __name__ == '__main__':
    main()


#ACCIDENTS PER TIME OF DAY
# Function to plot bar chart
def plot_bar_chart(df):
    part_of_day_counts = df['part_of_day'].value_counts().sort_values(ascending=False)

    colors = ['lightgray'] * 5  # Default color for all parts of the day
    colors[:1] = ['#1D2371'] * 1  # Change color for morning

    fig, ax = plt.subplots(figsize=(10, 6))
    part_of_day_counts.plot(kind='bar', color=colors, ax=ax)

    # Customizing the plot
    ax.set_xlabel('Time of Day')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Time of Day')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.title('Accidents by Time of Day')
    st.write('This app visualizes the number of accidents by time of day.')

    # Plot the bar chart
    st.write('Bar Chart:')
    plot_bar_chart(df)

if __name__ == '__main__':
    main()


#ACCIDENTS THROUGHOUT THE DAY
# Function to plot line chart
def plot_line_chart(df):
    hour_counts = df['acc_hour'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    hour_counts.plot(kind='line', color='#1D2371', marker='o', ax=ax)  # Use #1D2371 as line color

    # Customizing the plot
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Hour of the Day')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticks(hour_counts.index)  # Set the tick positions to match the hour values
    ax.set_xticklabels(hour_counts.index)  # Set the tick labels to display the hour values
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.title('Accidents by Hour of the Day')
    st.write('This app visualizes the number of accidents by hour of the day.')

    # Plot the line chart
    st.write('Line Chart:')
    plot_line_chart(df)

if __name__ == '__main__':
    main()


# ACCIDENTS PER DAY OF THE WEEK
# Maps integer value to string value of trans_weekday
weekday_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
df['acc_weekday'] = df['acc_weekday'].map(weekday_map)

# Function to plot bar chart
def plot_bar_chart(df):
    weekday_counts = df['acc_weekday'].value_counts()

    colors_mc = ['lightgray'] * len(weekday_counts)
    colors_mc[:3] = ['#1D2371'] * 3  # Change color for top 3 weekdays

    fig, ax = plt.subplots(figsize=(10, 6))
    weekday_counts.plot(kind='bar', color=colors_mc, ax=ax)

    # Customizing the plot
    ax.set_xlabel('Day of the week')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Day of the week')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.title('Accidents by Day of the Week')
    st.write('This app visualizes the number of accidents by day of the week.')

    # Plot the bar chart
    st.write('Bar Chart:')
    plot_bar_chart(df)

if __name__ == '__main__':
    main()


# ACCIDENTS PER MONTH
# Function to plot bar chart
def plot_bar_chart(df):
    accidents_per_month = df['acc_month'].value_counts().sort_index()

    colors = ['lightgray'] * 12  # Default color for all months
    colors[8:11] = ['#1D2371'] * 3  # Change color for September, October, and November

    fig, ax = plt.subplots(figsize=(10, 6))
    accidents_per_month.plot(kind='bar', color=colors, ax=ax)

    # Customizing the plot
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Month')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.title('Accidents by Month')
    st.write('This app visualizes the number of accidents by month.')

    # Plot the bar chart
    st.write('Bar Chart:')
    plot_bar_chart(df)

if __name__ == '__main__':
    main()


# ACCIDENTS PER YEAR
# Calculate accidents per month per year
accidents_per_month_year = df.groupby(['acc_year', 'acc_month']).size().unstack(fill_value=0)

# Define colors for each year
colors = ['#1D2371', '#7ABAFF', '#4D4DFF']  # Shades of blue

# Streamlit app
def main():
    st.title('Accidents by Month for Different Years')
    st.write('This app visualizes the number of accidents by month for different years.')

    # Plotting the data
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotting the line graph for each year
    for year, color in zip(accidents_per_month_year.index, colors):
        ax.plot(accidents_per_month_year.columns, accidents_per_month_year.loc[year], marker='o', label=year, color=color)

    # Customizing the plot
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Month for Different Years')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticks(accidents_per_month_year.columns)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=0)

    plt.legend(title='Year')
    plt.grid(True)
    st.pyplot(fig)

if __name__ == '__main__':
    main()