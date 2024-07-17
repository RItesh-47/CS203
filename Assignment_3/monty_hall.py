import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to simulate Monty Hall problem
def monty_sim(n_doors, n_cars, num_trials):
    switch_wins = 0
    keep_wins = 0
    
    # Loop over the number of trials
    for _ in range(num_trials):
        # Initialize doors with goats and cars
        doors = ['goat'] * (n_doors - n_cars) + ['car'] * n_cars
        np.random.shuffle(doors)
        
        # Player's initial choice
        player_choice = np.random.randint(0, n_doors)
        
        # Determine available doors to open (with goats behind them)
        available_doors = [i for i in range(n_doors) if i != player_choice and doors[i] == 'goat']
        
        # If there are available doors to open
        if available_doors:
            # Monty opens a door with a goat behind it
            opened_door = np.random.choice(available_doors)
            
            # Player switches to the other unopened door
            switch_choice = next(i for i in range(n_doors) if i != player_choice and i != opened_door)
            if doors[switch_choice] == 'car':
                switch_wins += 1
                
            # Player sticks with their initial choice
            if doors[player_choice] == 'car':
                keep_wins += 1
            
    # Calculate winning probabilities
    switch_win_prob = switch_wins / num_trials
    keep_win_prob = keep_wins / num_trials
    
    return switch_win_prob, keep_win_prob

# Define ranges and parameters
num_door_values = np.arange(3, 20)
num_car_values = np.arange(1, 20)
num_trials = 10000

# User input for number of doors and cars
doors_count = int(input("Enter the number of doors: "))
cars_count = int(input("Enter the number of cars: "))

# Calculate winning probabilities for user input
switch_win_prob, keep_win_prob = monty_sim(doors_count, cars_count, num_trials)
print(f"Winning probability with switching: {switch_win_prob}")
print(f"Winning probability with sticking: {keep_win_prob}")
print(f"win ratio (probability of switch / probability of keep): {switch_win_prob/keep_win_prob}")

# Calculate ratios of winning probabilities for different door and car counts
ratios = np.zeros((len(num_door_values), len(num_car_values)))
for i, num_doors in enumerate(num_door_values):
    for j, num_cars in enumerate(num_car_values):
        switch_win_prob, keep_win_prob = monty_sim(num_doors, num_cars, num_trials)
        if keep_win_prob != 0:
            ratios[i, j] = switch_win_prob / keep_win_prob
        else:
            ratios[i, j] = np.nan  

# Create meshgrid for 3D plotting
CarCount, DoorCount = np.meshgrid(num_car_values, num_door_values)  

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(DoorCount, CarCount, ratios, cmap='viridis')

# Set labels and title
ax.set_xlabel('Number of Doors (n)')
ax.set_ylabel('Number of Doors with Cars (k)')
ax.set_zlabel('Ratio: switch_win_prob / keep_win_prob')
ax.set_title('Surface Plot of n, k versus (switch_win_prob/keep_win_prob)')

# Show plot
plt.show()
