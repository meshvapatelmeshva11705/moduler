import math
import random
import string
import time
import uuid
import importlib
from datetime import datetime

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def display_current_datetime():
    now = datetime.now()
    print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_date_difference():
    first_str = input("Enter the first date (YYYY-MM-DD): ")
    second_str = input("Enter the second date (YYYY-MM-DD): ")
    try:
        first_date = datetime.strptime(first_str, "%Y-%m-%d")
        second_date = datetime.strptime(second_str, "%Y-%m-%d")
        difference = abs((second_date - first_date).days)
        print(f"Difference: {difference} days")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


def format_date_custom():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        print(f"Long format: {date_obj.strftime('%A, %d %B %Y')}")
        print(f"Short format: {date_obj.strftime('%d/%m/%y')}")
        print(f"ISO format: {date_obj.isoformat()}")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    input("Press Enter to stop the stopwatch...")
    elapsed = time.time() - start_time
    print(f"Elapsed time: {elapsed:.2f} seconds")

def countdown_timer():
    try:
        seconds = int(input("Enter countdown time in seconds: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTime's up!        ")

def datetime_menu():
    while True:
        print("\n" + "=" * 40)
        print("Datetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom formats")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        print("=" * 40)
        choice = input("Enter your choice: ")

        if choice == "1":
            display_current_datetime()
        elif choice == "2":
            calculate_date_difference()
        elif choice == "3":
            format_date_custom()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def calculate_factorial():
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return
        print(f"Factorial: {math.factorial(n)}")
    except ValueError:
        print("Please enter a valid integer.")

def area_of_geometric_shapes():
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    shape_choice = input("Choose a shape: ")

    try:
        if shape_choice == "1":
            radius = float(input("Enter radius: "))
            print(f"Area: {math.pi * radius ** 2:.2f}")
        elif shape_choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            print(f"Area: {length * width:.2f}")
        elif shape_choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print(f"Area: {0.5 * base * height:.2f}")
        elif shape_choice == "4":
            side = float(input("Enter side: "))
            print(f"Area: {side ** 2:.2f}")
        else:
            print("Invalid shape choice.")
    except ValueError:
        print("Please enter valid numeric values.")

def math_menu():
    while True:
        print("\n" + "=" * 40)
        print("Mathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        print("=" * 40)
        choice = input("Enter your choice: ")

        if choice == "1":
            calculate_factorial()
        elif choice == "2":
            solve_compound_interest()
        elif choice == "3":
            trigonometric_calculations()
        elif choice == "4":
            area_of_geometric_shapes()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def generate_random_number():
    try:
        low = int(input("Enter lower bound: "))
        high = int(input("Enter upper bound: "))
        print(f"Random Number: {random.randint(low, high)}")
    except ValueError:
        print("Please enter valid integers.")

def generate_random_list():
    try:
        size = int(input("Enter list size: "))
        low = int(input("Enter lower bound: "))
        high = int(input("Enter upper bound: "))
        result = [random.randint(low, high) for _ in range(size)]
        print(f"Random List: {result}")
    except ValueError:
        print("Please enter valid integers.")

def generate_random_password():
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")


def generate_random_otp():
    try:
        length = int(input("Enter OTP length: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    otp = "".join(random.choice(string.digits) for _ in range(length))
    print(f"Generated OTP: {otp}")

def simulate_random_sampling():
    try:
        population_size = int(input("Enter population size: "))
        sample_size = int(input("Enter sample size: "))
        population = list(range(1, population_size + 1))
        sample = random.sample(population, min(sample_size, population_size))
        print(f"Random Sample: {sample}")
    except ValueError:
        print("Please enter valid integers.")

def random_menu():
    while True:
        print("\n" + "=" * 40)
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Simulate Random Sampling")
        print("6. Back to Main Menu")
        print("=" * 40)
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_random_number()
        elif choice == "2":
            generate_random_list()
        elif choice == "3":
            generate_random_password()
        elif choice == "4":
            generate_random_otp()
        elif choice == "5":
            simulate_random_sampling()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def generate_uuid1():
    print(f"Generated UUID (v1): {uuid.uuid1()}")

def generate_uuid4():
    print(f"Generated UUID (v4): {uuid.uuid4()}")


def uuid_menu():
    while True:
        print("\n" + "=" * 40)
        print("Generate Unique Identifiers (UUID):")
        print("1. Generate UUID (v1 - based on host and time)")
        print("2. Generate UUID (v4 - random)")
        print("3. Back to Main Menu")
        print("=" * 40)
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_uuid1()
        elif choice == "2":
            generate_uuid4()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def create_new_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, "x") as f:
            pass
        print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print(f"File '{filename}' already exists.")
    except OSError as e:
        print(f"Error creating file: {e}")

def write_to_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")
    try:
        with open(filename, "w") as f:
            f.write(data)
        print("Data written successfully.")
    except OSError as e:
        print(f"Error writing to file: {e}")

def read_from_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as f:
            content = f.read()
        print(f"File Content:\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except OSError as e:
        print(f"Error reading file: {e}")


def append_to_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")
    try:
        with open(filename, "a") as f:
            f.write(data)
        print("Data appended successfully.")
    except OSError as e:
        print(f"Error appending to file: {e}")


def file_ops_menu():
    while True:
        print("\n" + "=" * 40)
        print("File Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        print("=" * 40)
        choice = input("Enter your choice: ")

        if choice == "1":
            create_new_file()
        elif choice == "2":
            write_to_file()
        elif choice == "3":
            read_from_file()
        elif choice == "4":
            append_to_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def explore_module_attributes():
    module_name = input("Enter module name to explore: ")
    try:
        module = importlib.import_module(module_name)
        attributes = dir(module)
        print(f"Available Attributes in module '{module_name}':")
        print(attributes)
    except ImportError:
        print(f"Module '{module_name}' could not be found.")

def module_explorer_menu():
    print("\n" + "=" * 40)
    print("Explore Module Attributes")
    print("=" * 40)
    explore_module_attributes()

def display_main_menu():
    print("=" * 40)
    print("Welcome to Multi-Utility Toolkit")
    print("=" * 40)
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("=" * 40)


def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_ops_menu()
        elif choice == "6":
            module_explorer_menu()
        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
