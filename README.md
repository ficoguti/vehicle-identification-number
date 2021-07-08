# Vehicle Identification Number Decoder

## This project takes a user-inputted Vehicle Identification Number (VIN) and makes magic!
![VIN Infographic](https://www.cerchio.com/wp-content/uploads/2017/12/Untitled.png)

Vitalik Buterin:
> Whereas most technologies tend to automate workers on the periphery doing menial tasks, blockchains automate away the center. Instead of putting the taxi driver out of a job, blockchain puts Uber out of a job and lets the taxi drivers work with the customer directly.

Vehicle Identification Numbers (VIN) are unique code used to identity individual motor vehicles. 
This program aims to decode a VIN number. This can provide information to be used in a number of applications, both for personal and business use.

## Descripton Of Algorithm:

This algorithm does many things.
- It prints the year, make, and model associated with the given Vehicle Identification Number (VIN).
- It plots the the number of cars per year in a scatter plot format. This is located in the carsproducdedyear.html file.
- It uploads the Vehicle Identification Number data into a SQL database, but not before converting it into a pandas dataframe!
---
## Guide:

When prompted, enter your 17 character Vehicle Identification Number (VIN) into the command line.
If you wish to clear the current dataset, use **loadSQLfromFile** followed by **clearDatasetInFile** within the main function**.

### External Information:

To learn more about Vehicle Identification Numbers visit [AutoCheck](https://www.autocheck.com/vehiclehistory/vin-basics).

[Click here for API information](https://api.carmd.com/member/docs#vin-decode)

### Contact Information:

Name | Email
---- | -----
Federico Gutierrez | fedeguti2001@gmail.com
Nerissa Griffiths | ngriffit@villanova.edu
