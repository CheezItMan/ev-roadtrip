# Coding Challenge: EV Roadtrip

Our coding challenges are based on the Ada Developers Academy Ada Build Curriculum.

What we’re looking for:

* Ability to self-learn and apply material quickly because as a professional engineer you will be learning every day, forever.
* Ability to grasp the fundamentals of coding so that you are ready for Day 1 of Ada.
    * All admitted students are expected to be well-versed with the conditional flows, loops, lists, dictionaries and Python fundamentals on the first day of their cohort.

These concepts are covered in our Ada Build curriculum.

## Tools

For this challenge, you will use HackerRank. If you are not sure where to get started, take a look at this lecture video that has HackerRank instructions. 

## Assignment: EV Roadtrip

Ada is planning a roadtrip from Helena Montana to Adiecon in Seattle (1000km).  You are going to create a program that will help Ada determine how expensive each potential electric vehicle is for a road trip.

**Requirements**:

* You must accept user input via the function parameters
* You must use at least one loop or iterator.
* You must use at least one Dictionary or List to store your data.

### Wave 1:  Problem Statement

- Each Vehicle has a `range` (an integer in km), a `name` (a string) and a rental price.
- The function accepts a list of `vehicle_names`, `vehicle_ranges`, and `vehicle_rental_prices`.
- A Vehicle on the route must charge before exceeding it's range.
- Charging any vehicle is $5.00
- Return the name of the least expensive vehicle to take on the trip along with the total expenses

### Wave 2:  Problem Statement

Ada has decided that she will stop to eat every 3 hours on the trip.

**Assuming:**

- Each car drives an average of 90 km/hr
- Each charging station takes 1 hour to charge up the vehicle
- Ada will spend $20 on each mealbreak

Adjust the calculations and determine the total expenses.

### Going Beyond: Handling Ties

- When multiple cars are equally least expensive, return a list including each of the least expensive car names.
- Print out the name and total expenses for each vehicle:

    ```
    Vehicle: Model 3
    Total Expenses: $875.00
    Total Number of Charging Stops: 4

    Vehicle: Mach-E
    Total Expenses: $860.00
    Total Number of Charging Stops: 5

    Vehicle: ë-C4
    Total Expenses: $855.00
    Total Number of Charging Stops: 5

    Vehicle: Ioniq 5
    Total Expenses: $885.00
    Total Number of Charging Stops: 6
    ```