# SURFS UP

Data Storage and Retrieval Module

## Objective

Retrieve temperature data for the months of June and December in Oahu in order to determine if the surf and ice cream shop business is sustainable year-round for owner W. Avy.

Deliverables:

    1. Determine the Summary Statistics for June
    2. Determine the Summary Statistics for December
    3. Provide written report for the statistical analysis

## Overview of the analysis

Used python sqlalchemy, numpy and pandas to extract weather temperatures from a sqlite database. 

## Results

- June yields a higher average temp at 74.9 degrees 
- June yields a higher maximum temperature at 85 degrees
- December has a lower minimum temp dropping to 56 degrees

### June Temperature Summary
![June Temperature Summary](https://github.com/lnharvin/surfs_up/blob/main/images/june_temps.PNG)

### December Temperature Summary
![December Temperature Summary](https://github.com/lnharvin/surfs_up/blob/main/images/dec_temps2.PNG)

## Summary

After analyzing a minimum of six years worth of monthly weather temperatures across 9 different weather stations in Oahu we can determine that both the month of June and December yield similar temperatures with a difference of only 3 degrees in the average temperature and 2 degrees difference in the maximum temperature.

I would suggest to my client that with such minor temperature difference that it appears feasible to keep the Oahu surf and ice cream shop open all year around with maybe  shorter business hours in the month of December, perhaps opening later in the morning to allow the daily temperature to rise. 

#### Average Temperature by Month
![Avg Temp by Month](https://github.com/lnharvin/surfs_up/blob/main/images/avg_temps_by_month.PNG)

## Additional Analysis

[Number of data points per weather station](https://github.com/lnharvin/surfs_up/blob/main/images/station_dataPts.PNG)

[All weather station statistics](https://github.com/lnharvin/surfs_up/blob/main/images/station_statistics.PNG)

[Average Temperature Data](https://github.com/lnharvin/surfs_up/blob/main/images/avg_temps_by_month_data.PNG)
