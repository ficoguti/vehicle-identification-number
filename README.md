# Vehicle Identification Number Decoder

## This project takes a user-inputted Vehicle Identification Number (VIN) and makes magic!
![VIN Infographic](https://www.cerchio.com/wp-content/uploads/2017/12/Untitled.png)


Vehicle Identification Numbers (VIN) are unique code used to identity individual motor vehicles. 
This program aims to decode a VIN number. This can provide information to be used in a number of applications, both for personal and business use.

## Description Of Algorithm:

Using [CarMD's VIN API](https://www.carmd.com/api/), this program is able to decode **any valid 17 character VIN you want to throw at it!**

### This algorithm does many things.
- It prints the year, make, and model associated with the given Vehicle Identification Number (VIN).
- It plots the the number of cars per year in a scatter plot format. This is located in the carsproducedyear.html file.
- It uploads the Vehicle Identification Number data into a SQL database, but not before converting it into a pandas dataframe!
---


## Demo

```
~/workspace/vehicle-identification-number$ python3 vin.py
Enter a Vehicle Identification Number: JH4DC4451YS004711
2000 ACURA INTEGRA HONDA L4, 1.8L; DOHC; 16V LS AUTOMATIC
VIN added to database
    ID                VIN  YEAR         MAKE             MODEL
0    1  5YJYGAEE8MF136571  2021        TESLA           MODEL Y
1    2  WBA3A5C57CF256651  2012          BMW               328
2    3  SCBZU25E82CX01501  2002      BENTLEY       CONTINENTAL
3    4  WP0AA2999YS489674  2000      PORSCHE               911
4    5  1G6AF5S35E0112634  2014     CADILLAC               ATS
5    6  ZHWGU6AU2ALA09235  2010  LAMBORGHINI          GALLARDO
6    7  5YJRE1A37A1001010  2010        TESLA          ROADSTER
7    8  1FMEU1660YLC29974  2000         FORD        EXPEDITION
8    9  1J8HG58236C276108  2006         JEEP         COMMANDER
9   10  WVWAF93D258002461  2005   VOLKSWAGEN           PHAETON
10  11  1GB3CYC80FF683168  2015    CHEVROLET         SILVERADO
11  12  WAUWKAFR0AA026123  2010         AUDI                A5
12  13  ZFF77XJA0G0214475  2016      FERRARI      CALIFORNIA T
13  14  4A3AC74H63E114450  2003   MITSUBISHI           ECLIPSE
14  15  WMWSX3C58ET772911  2014         MINI      COOPER COUPE
15  16  1C4NJPBA1CD661292  2012         JEEP           PATRIOT
16  17  5J6TF2H56ALO12946  2010        HONDA  ACCORD CROSSTOUR
17  18  2T3DK4DV8CW082696  2012       TOYOTA              RAV4
18  19  1N6AD09U19C400608  2009       NISSAN          FRONTIER
19  20  WMEEJ9AA9DK715496  2013        SMART            FORTWO
20  21  JH4DC4451YS004711  2000        ACURA           INTEGRA
```
---

## Guide:

When prompted, enter your 17 character Vehicle Identification Number (VIN) into the command line.
If you wish to clear the current dataset, use **loadSQLfromFile** followed by **clearDatasetInFile** within the main function.
---

### External Information:


[Click here for CarMD's API documentation](https://api.carmd.com/member/docs#vin-decode)

To learn more about VINs visit [AutoCheck](https://www.autocheck.com/vehiclehistory/vin-basics).
---

### Contact Information:

Name | Email
---- | -----
Federico Gutierrez | fg42768n@pace.edu
Nerissa Griffiths | ngriffit@villanova.edu
