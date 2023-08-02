import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("please choose one of these city (chicago, new york city, washington) :  ").lower()#converts the user input to lower case using lower()function 
    while city not in CITY_DATA.keys():
        print("sorry, choose correct city name")
        city = input("please choose one of these city (chicago, new york city, washington) : ").lower()#converts the user input to lower case using lower()function

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june", "all"]
    while True:
        month = input("please enter one of these month (january, february, march, april, may, june or type all) ").lower()#converts the user input to lower case using lower()function
        if month in months:
            break
        else:
            print("sorry, enter a full valid month name")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
    while True:
        day=input("please choose a day(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type all) ").lower()#converts the user input to lower case using lower()function
        if day in days:
            break
        else:
            print("sorry, enter a full valid day name")

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour

    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june", "all"]
        month = months.index(month) + 1
    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
    # filter by week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month is : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('Most common day is : {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('Most common start hour is : {}'.format(df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station is : {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most common end station is : {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Station']=df['Start Station']+","+df['End Station']
    print('Most frequent combination of start station and end station : {}'.format(df['Combination Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total travel time : ', Total_Travel_Time/86400, "Days")#divide Total_Travel_Time by 86400 to convert from second to days.
    
    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Average travel time : ', Mean_Travel_Time/60 , "Minutes")#divide Total_Travel_Time by 60 to convert from second to minutes.

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame())

    # TO DO: Display counts of gender
    # washington data set has no data about gender and year of birth so if statment will avoid ther errors during runtime.
    if city != "washington":
        print(df['Gender'].value_counts().to_frame())
        
    # TO DO: Display earliest, most recent, and most common year of birth
        print('Most common year of birth is : ',int(df['Birth Year'].mode()[0]))
        print('Most recent year of birth is : ',int(df['Birth Year'].max()))
        print('Most earliest year of birth is : ',int(df['Birth Year'].min()))
    else:
        print('There is no data about gender or year of birth for this city')
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
      
def display_data(df):
    # Display subsequent rows of data based upon user input.
    print('\nRaw data is available to check... \n')
    i = 0
    user_input = input('Would you like to display the first 5 rows of data? Please type yes or no: ').lower()
    if user_input not in ['yes','no']:
        print('sorry, type yes or no')
        user_input=input('Would you like to display the first 5 rows of data? Please type yes or no: ').lower()#converts the user input to lower case using lower()function
    elif user_input != 'yes':    
        print('Thank You')
              
    else:
        while i+5 < df.shape[0]:
              print(df.iloc[i:i+5])
              i += 5
              user_input =input('Would ypu like to display more 5 rows if data? Please type yes or no: ').lower()#converts the user input to lower case using lower()function
              if user_input != 'yes':
                  print('Thank You')
                  break
                 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':#converts the user input to lower case using lower()function
            print('Thank You')
            break


if __name__ == "__main__":
	main()
