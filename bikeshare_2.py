import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # TO DO: get user input for month (all, january, february, ... , june)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    city = ""
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Would you like to see data for Chicago New York City or Washington?   ').lower()

    month = ""
    while month not in ['All', 'January', 'February', 'March', 'April', 'May', 'June']:
        month = input('which month? All, January, February, March, April, May or June?   ').title()

    day = ""
    while day not in ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        day = input('Which day? all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday   ').title()

    print('-' * 40)
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

    row_data = pd.read_csv(CITY_DATA[city])
    data = row_data.copy()
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    if month != 'all':
        data = data[data['Start Time'].dt.month_name() == month]

    if day != 'all':
        data = data[data['Start Time'].dt.day_name() == day]
    return data


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    print(df.head())
    print('the most common month: ' + str(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    print('the most common day of week: ' + str(df['day'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: ' + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['month'] = df['Start Time'].dt.month
    print('the most commonly used start station: ' + str(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('the most commonly used end station: ' + str(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' TO ' + df['End Station']
    print('the most frequent combination of start station and end station trip: ' \
          + str(df['trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:' + str(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean travel time: ' + str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Subscriber: ' + str(df['User Type'].value_counts()['Subscriber']) + ' Customer: ' + str(
        df['User Type'].value_counts()['Customer']))

    if city != 'washington':
        # TO DO: Display counts of gender
        print('Male: ' + str(df['Gender'].value_counts()['Male']) + ' Female: ' + str(
            df['Gender'].value_counts()['Female']))

        # TO DO: Display earliest, most recent, and most common year of birth
        print("the earliest year of birth: " + str(df['Birth Year'].min()))
        print("the most recent year of birth: " + str(df['Birth Year'].max()))
        print("the most common year of birth: " + str(df['Birth Year'].mode()[0]))

    else:
        print('there is No Gender or birth year data for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def row_data(df):
    index = 0
    response = input('Do you want to see sample data? yes/y or no/n:   ').lower()
    if response == 'yes' or response == 'y':
        while index < df.shape[0] and (response == 'yes' or response == 'y'):
            if index + 5 <= df.shape[0]:
                print(df.iloc[index:index + 5, :])
                index += 5
            else:
                print(df.iloc[index:df.shape[0], :])
                print('End of data')
                break

            response = input('More 5 rows? yes/y or no/n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        row_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
