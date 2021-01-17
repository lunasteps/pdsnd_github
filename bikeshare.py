import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']



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
    city_choice = ''
    while city_choice.lower() not in cities:
        city_choice = input("Which city do you want to explore data from: Chicago, New York, Washington?")
        if city_choice in cities:
            city = city_choice.lower()
        else:
            print('Invalid city choice, please select from: Chicago, New York, Washington')


    # TO DO: get user input for month (all, january, february, ... , june)
    month_choice = ''
    while month_choice.lower() not in months:
        month_choice = input("Which month would you like to analyse data for: January, February, March, May, June or all?")
        if month_choice.lower() in months:
            month = month_choice.lower()
        else:
            print('Invalid month choice, please choose from: January, February, March, May, June or all')
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_choice = ''
    while day_choice.lower() not in days:
        day_choice = input("Which day would you like to anayse data for: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all")
        if day_choice.lower() in days:
            day = day_choice.lower()
        else:
            print('Invaid day choise, please enter any weekday or all to analyse data for this day')


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
    
    #load data
    filename = CITY_DATA.get(city)
    df = pd.read_csv(filename)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    
    #filter data by month if applicable
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter data by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    pop_month = df['month'].mode()[0]
    
    print('The most frequent month of travel is: ', pop_month.title())


    # TO DO: display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    
    print('The most frequent day of travel is: ', pop_day.title())


    # TO DO: display the most common start hour
    pop_hour = df['hour'].mode()[0]
    
    print('The most frequent start hour of travel is: ', pop_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_st = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', pop_start_st)


    # TO DO: display most commonly used end station
    pop_end_st = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', pop_end_st)


    # TO DO: display most frequent combination of start station and end station trip
    pop_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip is : ' + str(pop_combination.split("||")))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time the selected data is: ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time the selected data is: ', mean_travel_time)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of user types for the selected data is: \n', user_types)


    # TO DO: Display counts of gender
    if city == 'washington':
        print('No gender or birth date data has been collected for Washington, select another city to analyse this data')
    else:
        gender = df['Gender'].value_counts()
        print("The count of user gender for the selected data is: \n", gender)


        # TO DO: Display earliest, most recent, and most common year of birth
        
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('Earliest birth for the selected data is: \n', earliest_year)
        print('Most recent birth for the selected data is: \n', recent_year)
        print('Most common birth for the selected data is: \n', common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
