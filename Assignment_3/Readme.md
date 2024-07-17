# Monty Hall Simulation

This Python script simulates an extention version to the Monty Hall problem, a famous probability puzzle. Here a contestant must choose
between n doors, behind k of which is a prize, while the other n-k doors hide goats. After the contestant makes their initial choice, the host
reveals one of the remaining doors which doesn\'t contain the prize, and then gives the contestant the option to switch their choice to the other unopened door.

## How to Run the Simulation

### Requirements

Python 3.x NumPy Matplotlib scipy

### Installation

Ensure you have Python installed on your system. If not, you can download it from the official Python website. Install the required Python libraries by running the following command in your terminal or command prompt:

    pip install matplotlib pip install scipy pip install numpy

### Running the Simulation

Download the Assignment.py file from this repository to your local machine. Open a terminal or command prompt and navigate to the directory where the monty_hall_simulation.py file is located.
Run the script by executing the following command:

    python3 Assignment.py \<n\> \<k\>

where \<n\> represents the total number of doors, \<k\> represents the number of doors behind which car resides.

### Output

After running the script, the simulation will generate a 3D surface plot showing the relationship between the number of doors, the number of cars, and the win rate ratio between the switching strategy and keeping the initial choice strategy.
