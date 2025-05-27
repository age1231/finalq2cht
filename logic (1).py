
import random

def generate_random_numbers():
    return [random.randint(0, 99) for _ in range(40)]

def calculate_sum(numbers):
    return sum(numbers)

def calculate_avg(numbers):
    return sum(numbers) / len(numbers)

def calculate_max(numbers):
    return max(numbers)

def sort_numbers(numbers, ascending=True):
    return sorted(numbers, reverse=not ascending)
