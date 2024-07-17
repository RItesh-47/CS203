## Birthday Paradox Probability Calculator:
- This Python program calculates the probability of at least two people sharing a birthday in a group, also known as the birthday paradox. 
- It provides a flexible method to find the number of students required to achieve a specific probability of shared birthdays, using binary search.

## Features:
- Birthday Paradox Probability Calculation: The program utilizes simulations to estimate the probability of at least two people sharing a birthday in a group of a given size.
- Binary Search for Required Probability: It employs binary search to find the number of students needed to achieve a desired probability of shared birthdays. The hi variable is set to 365 following from pigeon hole principle.
- Customizable: Users can input the desired probability ('p') and obtain the corresponding number of students required.

## Usage:
- Run the script in your preferred Python environment.
- Follow the instructions to input the required probability ('p').
- The program will output the number of students required to achieve the specified probability.

## Requirements:
- Python 3.x

## How It Works:
- The program works by simulating multiple scenarios of random birthdays for a given number of people. It then checks if there is at least one shared birthday among them. By repeating this process numerous times, it calculates the probability of at least two people sharing a birthday.
- For finding the number of students required to achieve a desired probability, the program uses binary search. It iteratively adjusts the number of students until the calculated probability matches or exceeds the desired probability. 