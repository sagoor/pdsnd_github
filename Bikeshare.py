#This section of the code will contains the packages used:
import pandas as pd
import numpy as np
import time

# Dictionaries for later use in the filtering functions:
CITY_DATA = {'chicago': 'chicago.csv', 'new york': 'new_york_city.csv', 'washington': 'washington.csv'}
days = {'M': 'Monday', 'Tu': 'Tuesday', 'W': 'Wednesday','Th': 'Thursday', 'F': 'Friday', 'Sa': 'Saturday', 'Su': 'Sunday'}
months = {'January' : 1 , 'February' : 2,  'March' : 3, 'April' : 4, 'May': 5, 'June' : 6}

#This section shows the code for the filers defined within the filters function:

#The code starts by capturing the user input of the city:
message1 = 'Hi there!.\nPlease enter the neme of the city [New York, Washington, Chicago] you would like to learn more about our business \n'
city = input(message1).lower().title()
while not (city =='New York' or city == 'Chicago' or city == 'Washington'):
    print('You entered wrong input \n')
    city = input("please enter correct input: \n").lower().title()
print('You chose {} city \n'.format(city))

#Filtering by month:
def month_filter():
    message2 = 'Please choose the month you would like to filter the date with:\nJanuary, February, March, April, May, or June.\n'
    month = input(message2).lower().title()
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    while month not in months:
        print('You entered wrong input \n')
        month = input("please enter correct input: \n").lower().title()
    print('You chose the month of {} \n'.format(month))
    return month

# Filtering by day:
def day_filter():
    message3 = 'Please choose the day to filer with:\nM, Tu, W ,Th, F, Sa, Su \n'
    day = input(message3).lower().title()
    week = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
    while day not in week:
        print('You entered wrong input \n')
        day = input("please enter correct input: \n").lower().title()
    print('You chose:\n',days.get(day))
    return day

#Loading data with city filter - all dates included:
def load_city(city):
    #Debugging step to check if city is passed to this function
    print(city , 'inside the function\n')
    df_city = pd.read_csv(CITY_DATA.get(city.lower()))
    df_city = df_city.drop("Unnamed: 0", axis=1) #Dropping the unnamed column
    print(df_city.head())

    print('-'*40)

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # display the most common month
    df_city['Start Time'] = pd.to_datetime(df_city['Start Time'])
    df_city['Month'] = df_city['Start Time'].dt.month_name()
    print('Most frequent month is: .... ',df_city['Month'].mode())

    # display the most common day of week
    df_city['day'] = df_city['Start Time'].dt.day_name()
    print('\n Most frequent day is: .... ',df_city['day'].mode())

    # display the most common start hour
    df_city['hour'] = df_city['Start Time'].dt.hour
    print('\n Most frequent hour is: .... ',df_city['hour'].mode())

    print('-'*40)

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # display most commonly used start station
    print('\n Most commonly used Start Station is: .... ',df_city['Start Station'].mode())

    # display most commonly used end station
    print('\n Most commonly used End Station is: .... ',df_city['End Station'].mode())

    # display most frequent combination of start station and end station trip
    df_city['Combination'] = df_city['Start Station'] + ' AND ' + df_city['End Station']
    print('\n Most commonly used Stations Combination is: .... \n',df_city['Combination'].mode())

    print('-'*40)

    print('\nCalculating Trip Duration...\n')

    # display total travel time
    df_city['End Time'] = pd.to_datetime(df_city['End Time'])
    df_city['Trip Duration'] = df_city['End Time'] - df_city['Start Time']
    print('Total trip duration in seconds is ... ', df_city['Trip Duration'].dt.total_seconds().sum())

    # display mean travel time
    print('Mean travel time in seconds is ... ', df_city['Trip Duration'].dt.total_seconds().mean())

    print('-'*40)

    print('\nCalculating User Stats...\n')

    # Display counts of user types

    print('Count of user types: ...\n', df_city.groupby(['User Type'])['User Type'].count())

    # Display counts of gender
    if city != 'Washington':
        print('\nCount of users by Gender: ...\n', df_city.groupby(['Gender'])['Gender'].count())

        # Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth: ...', df_city['Birth Year'].min())
        print('\nMost recent year of birth: ...', df_city['Birth Year'].max())
        print('\nMost common year of birth: ...', df_city['Birth Year'].mode())

#Loading data with city and month filter:
def load_city_month(city, month):
    #Debugging step to check if city is passed to this function
    print(city, 'inside the function')
    print(month, 'inside the function')
    df_city_month = pd.read_csv(CITY_DATA.get(city.lower()))
    df_city_month = df_city_month.drop("Unnamed: 0", axis=1) #Dropping the unnamed column
    df_city_month['Start Time'] = pd.to_datetime(df_city_month['Start Time'])
    df_city_month['Month'] = df_city_month['Start Time'].dt.month
    df_city_month['Month'] = months.get(month)
    print(df_city_month.head())

    print('-'*40)

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # display the most common month
    df_city_month['Start Time'] = pd.to_datetime(df_city_month['Start Time'])

    # display the most common day of week
    df_city_month['day'] = df_city_month['Start Time'].dt.day_name()
    print('\n Most frequent day is: .... ',df_city_month['day'].mode())

    # display the most common start hour
    df_city_month['hour'] = df_city_month['Start Time'].dt.hour
    print('\n Most frequent hour is: .... ',df_city_month['hour'].mode())

    print('-'*40)

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # display most commonly used start station
    print('\n Most commonly used Start Station is: .... ',df_city_month['Start Station'].mode())

    # display most commonly used end station
    print('\n Most commonly used End Station is: .... ',df_city_month['End Station'].mode())

    # display most frequent combination of start station and end station trip
    df_city_month['Combination'] = df_city_month['Start Station'] + ' AND ' + df_city_month['End Station']
    print('\n Most commonly used Stations Combination is: .... \n',df_city_month['Combination'].mode())

    print('-'*40)

    print('\nCalculating Trip Duration...\n')

    # display total travel time
    df_city_month['End Time'] = pd.to_datetime(df_city_month['End Time'])
    df_city_month['Trip Duration'] = df_city_month['End Time'] - df_city_month['Start Time']
    print('Total trip duration in seconds is ... ', df_city_month['Trip Duration'].dt.total_seconds().sum())

    # display mean travel time
    print('Mean travel time in seconds is ... ', df_city_month['Trip Duration'].dt.total_seconds().mean())

    print('-'*40)

    print('\nCalculating User Stats...\n')

    # Display counts of user types

    print('Count of user types: ...\n', df_city_month.groupby(['User Type'])['User Type'].count())

    # Display counts of gender
    if city != 'Washington':
        print('\nCount of users by Gender: ...\n', df_city_month.groupby(['Gender'])['Gender'].count())

        # Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth: ...', df_city_month['Birth Year'].min())
        print('\nMost recent year of birth: ...', df_city_month['Birth Year'].max())
        print('\nMost common year of birth: ...', df_city_month['Birth Year'].mode())

#Loading data with city and day filter:
def load_city_day(city, day):
    #Debugging step to check if city is passed to this function
    print(city , 'inside the function')
    print(day, 'inside the function')
    df_city_day = pd.read_csv(CITY_DATA.get(city.lower()))
    df_city_day = df_city_day.drop("Unnamed: 0", axis=1) #Dropping the unnamed column
    df_city_day['Start Time'] = pd.to_datetime(df_city_day['Start Time'])
    df_city_day['day'] = df_city_day['Start Time'].dt.day
    df_city_day['day'] = days.get(day)
    print(df_city_day.head())

    print('-'*40)

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # display the most common month
    df_city_day['Start Time'] = pd.to_datetime(df_city_day['Start Time'])
    df_city_day['Month'] = df_city_day['Start Time'].dt.month_name()
    print('Most frequent month is: .... ',df_city_day['Month'].mode())

    # display the most common day of week
    df_city_day['day'] = df_city_day['Start Time'].dt.day_name()

    # display the most common start hour
    df_city_day['hour'] = df_city_day['Start Time'].dt.hour
    print('\n Most frequent hour is: .... ',df_city_day['hour'].mode())

    print('-'*40)

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # display most commonly used start station
    print('\n Most commonly used Start Station is: .... ',df_city_day['Start Station'].mode())

    # display most commonly used end station
    print('\n Most commonly used End Station is: .... ',df_city_day['End Station'].mode())

    # display most frequent combination of start station and end station trip
    df_city_day['Combination'] = df_city_day['Start Station'] + ' AND ' + df_city_day['End Station']
    print('\n Most commonly used Stations Combination is: .... \n',df_city_day['Combination'].mode())

    print('-'*40)

    print('\nCalculating Trip Duration...\n')

    # display total travel time
    df_city_day['End Time'] = pd.to_datetime(df_city_day['End Time'])
    df_city_day['Trip Duration'] = df_city_day['End Time'] - df_city_day['Start Time']
    print('Total trip duration in seconds is ... ', df_city_day['Trip Duration'].dt.total_seconds().sum())

    # display mean travel time
    print('Mean travel time in seconds is ... ', df_city_day['Trip Duration'].dt.total_seconds().mean())

    print('-'*40)

    print('\nCalculating User Stats...\n')

    # Display counts of user types

    print('Count of user types: ...\n', df_city_day.groupby(['User Type'])['User Type'].count())

    # Display counts of gender
    if city != 'Washington':
        print('\nCount of users by Gender: ...\n', df_city_day.groupby(['Gender'])['Gender'].count())

        # Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth: ...', df_city_day['Birth Year'].min())
        print('\nMost recent year of birth: ...', df_city_day['Birth Year'].max())
        print('\nMost common year of birth: ...', df_city_day['Birth Year'].mode())

#Loading data with all filters:
def load_all(city, month, day):
    #Debugging step to check if city is passed to this function
    print(city , 'inside the function')
    print(month, 'inside the function')
    print(days.get(day), 'inside the function')
    df_all = pd.read_csv(CITY_DATA.get(city.lower()))
    df_all = df_all.drop("Unnamed: 0", axis=1) #Dropping the unnamed column
    df_all['Start Time'] = pd.to_datetime(df_all['Start Time'])
    df_all['Month'] = df_all['Start Time'].dt.month
    df_all['Month'] = months.get(month)
    df_all['day'] = df_all['Start Time'].dt.day
    df_all['day'] = days.get(day)
    print(df_all.head())

    print('-'*40)

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # display the most common month
    df_all['Start Time'] = pd.to_datetime(df_all['Start Time'])

    # display the most common day of week
    df_all['day'] = df_all['Start Time'].dt.day_name()

    # display the most common start hour
    df_all['hour'] = df_all['Start Time'].dt.hour
    print('\n Most frequent hour is: .... ',df_all['hour'].mode())

    print('-'*40)

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # display most commonly used start station
    print('\n Most commonly used Start Station is: .... ',df_all['Start Station'].mode())

    # display most commonly used end station
    print('\n Most commonly used End Station is: .... ',df_all['End Station'].mode())

    # display most frequent combination of start station and end station trip
    df_all['Combination'] = df_all['Start Station'] + ' AND ' + df_all['End Station']
    print('\n Most commonly used Stations Combination is: .... \n',df_all['Combination'].mode())

    print('-'*40)

    print('\nCalculating Trip Duration...\n')

    # display total travel time
    df_all['End Time'] = pd.to_datetime(df_all['End Time'])
    df_all['Trip Duration'] = df_all['End Time'] - df_all['Start Time']
    print('Total trip duration in seconds is ... ', df_all['Trip Duration'].dt.total_seconds().sum())

    # display mean travel time
    print('Mean travel time in seconds is ... ', df_all['Trip Duration'].dt.total_seconds().mean())

    print('-'*40)

    print('\nCalculating User Stats...\n')

    # Display counts of user types

    print('Count of user types: ...\n', df_all.groupby(['User Type'])['User Type'].count())

    # Display counts of gender
    if city != 'Washington':
        print('\nCount of users by Gender: ...\n', df_all.groupby(['Gender'])['Gender'].count())

        # Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth: ...', df_all['Birth Year'].min())
        print('\nMost recent year of birth: ...', df_all['Birth Year'].max())
        print('\nMost common year of birth: ...', df_all['Birth Year'].mode())

# Check for date filter selection:
check = 'Would you like to filter by Month, Day, or Both? If Not, enter None: \n'
option = input(check).lower().title()
filters = ['Month', 'Day', 'Both', 'None']
while option not in filters:
    print('Wrong input, please choose correct filter\n')
    option = input(check).lower().title()
print('You chose to filer with {}.\n'.format(option))

#Control which function to call based on the user input (Filter Selection):
if option == 'Month':
    load_city_month(city, month = month_filter())
elif option == 'Day':
    load_city_day(city, day = day_filter())
elif option == 'Both':
    load_all(city, month = month_filter(), day = day_filter())
else:
    print(city)
    print('\nYou chose not to filer with date')
    load_city(city)

#Ask user to see the row data after selecting the city:
next_rows = ['Yes', 'No']
row_count = 0
next = input('\n Would you like to see next 5 rows? Yes or No ...').lower().title()
while next not in next_rows:
    next = input("\n Wrong input. Please select Yes or No:  \n").lower().title()
if next == 'Yes':
    while next == 'Yes':
        df_city = pd.read_csv(CITY_DATA.get(city.lower()))
        df_city = df_city.drop("Unnamed: 0", axis=1) #Dropping the unnamed column
        a = df_city.head(row_count + 5)
        print(a.tail(5))
        next = input('Would you like to see next 5 rows? Yes or No ....\n').lower().title()
        row_count += 5
