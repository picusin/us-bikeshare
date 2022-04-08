import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi there! Welcome to the US bikeshare database.')
    city = input('Which city would you like to obtain data from? Chicago, New York or Washington? ')
    while city.lower() != 'chicago' and city.lower() != 'new york' and city.lower() != 'washington':
        city = input('\nUnfortunately we don\'t have data for that city, please try again:\nWhich city would you like to obtain data from? Chicago, New York or Washington? ')

    filter_type = input('\nGreat choice!\nWould you like to filter the data by month (month), day of the week (day), both (both) or not filter at all (none)? ')
    while filter_type.lower() != 'month' and filter_type.lower() != 'day' and filter_type.lower() != 'both' and filter_type.lower() != 'none':
        filter_type = input('\nSorry, I didn\'t understand your choice, please try again:\nWould you like to filter the data by month (month), day of the week (day), both (both) or not filter at all (none)? ')
    if filter_type == 'day':
        month = 'all'
        day = input('\nWhich day of the week? Mon, Tue, Wed, Thu, Fri, Sat or Sun? If you prefer not to filter by day of the week, please type All: ')
        while day.lower() != 'mon' and day.lower() != 'tue' and day.lower() != 'wed' and day.lower() != 'thu' and day.lower() != 'fri' and day.lower() != 'sat' and day.lower() != 'sun' and day.lower() != 'all':
            day = input('\nPlease try again. Which day of the week? Mon, Tue, Wed, Thu, Fri, Sat or Sun? If you prefer not to filter by day of the week, please type All: ')
    elif filter_type == 'month':
        day = 'all'
        month = input('\nWhich month? Jan, Feb, Mar, Apr, May or Jun? If you prefer not to filter by month, please type All: ')
        while month.lower() != 'jan' and month.lower() != 'feb' and month.lower() != 'mar' and month.lower() != 'apr' and month.lower() != 'may' and month.lower() != 'jun' and month.lower() != 'all':
            month = input('\nPlease try again. Which month? Jan, Feb, Mar, Apr, May or Jun? If you prefer not to filter by month, please type All: ')
    elif filter_type == 'both':
        day = input('\nWhich day of the week? Mon, Tue, Wed, Thu, Fri, Sat or Sun? If you prefer not to filter by day of the week, please type All: ')
        while day.lower() != 'mon' and day.lower() != 'tue' and day.lower() != 'wed' and day.lower() != 'thu' and day.lower() != 'fri' and day.lower() != 'sat' and day.lower() != 'sun' and day.lower() != 'all':
            day = input('\nPlease try again. Which day of the week? Mon, Tue, Wed, Thu, Fri, Sat or Sun? If you prefer not to filter by day of the week, please type All: ')
        month = input('\nWhich month? Jan, Feb, Mar, Apr, May or Jun? If you prefer not to filter by month, please type All: ')
        while month.lower() != 'jan' and month.lower() != 'feb' and month.lower() != 'mar' and month.lower() != 'apr' and month.lower() != 'may' and month.lower() != 'jun' and month.lower() != 'all':
            month = input('\nPlease try again. Which month? Jan, Feb, Mar, Apr, May or Jun? If you prefer not to filter by month, please type All: ')
    else:
        day = 'all'
        month = 'all'

    city = city.lower()
    month = month.lower()
    day = day.lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = { 'mon': 'Monday',
              'tue': 'Tuesday',
              'wed': 'Wednesday',
               'thu': 'Thursday',
               'fri': 'Friday',
               'sat': 'Saturday',
               'sun': 'Sunday'}
        day = days[day]
        df = df[df['day_of_week'] == day]
    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    month_names = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most common month for the analyzed period was {}.'.format(month_names[common_month - 1]))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week for the analyzed period was {}.'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour for the analyzed period was {}.'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print('The most commonly used start station for the analyzed period was {}.'.format(common_start_st))
    # TO DO: display most commonly used end station
    common_end_st = df['End Station'].mode()[0]
    print('The most commonly used end station for the analyzed period was {}.'.format(common_end_st))
    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print('The most frequent trip for the analyzed period was {}.'.format(common_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    m, s = divmod(total_travel_time, 60)
    h, m = divmod(m, 60)
    print('The total travel time for the analyzed period was {} hours, {} minutes and {} seconds.'.format(int(h), int(m), int(s)))
    # I used this source for divmod: https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    m, s = divmod(mean_travel_time, 60)
    print('The mean travel time for the analyzed period was {} minutes and {} seconds.'.format(int(m), int(s)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('In the analyzed period we had the following counts per user types:')
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\nIn the analyzed period we had the following counts per gender:')
        print(gender)
    else:
        print('\nThere\'s no gender data for the selected city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        youngest = df['Birth Year'].max()
        oldest = df['Birth Year'].min()
        common_year = df['Birth Year'].mode()[0]
        print('\nIn the analyzed period, the youngest user was born in {}, the oldest was born in {} and the most common year of birth was {}.'.format(int(youngest), int(oldest), int(common_year)))
    else:
        print('\nThere\'s no birth year data for the selected city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data if required by the user."""

    raw = input('Would you like to see 5 rows of raw data? Enter yes or no.\n')
    i = 0
    while raw.lower() == 'y' or raw.lower() == 'yes':
        if len(df) >= i + 5:
            print(df.iloc[i:i+5])
            i += 5
            raw = input('Would you like to see 5 more rows? Enter yes or no.\n')
        else:
            print(df.iloc[i:])
            print('No more data to display.')
            break
    # I used this source to understand how to use iloc: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
