import random

def birthday_paradox_probability(num_people):
    """Calculate the probability of at least two people sharing a birthday in a group."""
    num_simulations = 100000   # Number of simulations to run
    success_count = 0

    for _ in range(num_simulations):
        birthdays = set(random.randint(1, 365) for _ in range(num_people))
        if len(birthdays) != num_people:
            success_count += 1

    probability = success_count / num_simulations
    return probability

def find_number_of_students(p):
    """Use binary search to find the number of students required such that the probability
    of at least two people sharing a birthday in a group exceeds the given threshold 'p'."""
    low = 1
    high = 365
    while low < high:
        mid = (low + high) // 2
        probability = birthday_paradox_probability(mid)
        if probability < p:
            low = mid + 1
        else:
            high = mid

    return low


p = float(input("Enter the required probability (between 0 and 1): "))
if p <= 0 or p > 1:
    print("Invalid probability value. Please enter a value between 0 and 1.")
    exit()
num_students = find_number_of_students(p)
print(f"The number of students required for probability >= {p} is approximately {num_students}")

