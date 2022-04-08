# Bikeshare system exploration

This was the second project from Udacity's Programming for Data Science Nanodegree covering the block on Python. The following information matches the project's description on Udacity's classroom.

The goal of this project is to write an interactive script that imports data from bikeshare systems in three major US cities (New York, Chicago and Washington) and answers different questions about it by computing descriptive statistics.

## Datasets

The original data is provided by Motivate, a bike share system provider for many major cities in the United States.

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core columns:

- Start Time
- End Time
- Trip Duration
- Start Station
- End Station
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

## Statistics computed

#### Popular times of travel (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day

#### Popular stations and trip

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

#### Trip duration

- total travel time
- average travel time

#### User info

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)
