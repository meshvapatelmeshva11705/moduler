# Multi-Utility Toolkit

A Python-based **Multi-Utility Toolkit** that provides multiple useful features through a simple menu-driven command-line interface.

The project demonstrates the use of Python's built-in modules such as `math`, `random`, `string`, `time`, `uuid`, `importlib`, and `datetime`.

## Features

### 1. Datetime and Time Operations

* Display current date and time
* Calculate difference between two dates
* Format dates into different formats
* Stopwatch
* Countdown timer

### 2. Mathematical Operations

* Calculate factorial
* Compound interest calculation
* Trigonometric calculations
* Calculate area of:

  * Circle
  * Rectangle
  * Triangle
  * Square

### 3. Random Data Generation

* Generate random numbers
* Generate random lists
* Generate random passwords
* Generate random OTPs
* Simulate random sampling

### 4. UUID Generation

* Generate UUID Version 1
* Generate UUID Version 4

### 5. File Operations

* Create a new file
* Write data to a file
* Read data from a file
* Append data to a file

### 6. Module Explorer

The project allows users to enter a Python module name and explore its available attributes using `importlib` and `dir()`.

## Technologies Used

* Python 3
* `math`
* `random`
* `string`
* `time`
* `uuid`
* `datetime`
* `importlib`

All features are implemented using Python's standard library, so no external packages are required.

## Project Structure

```text
Multi-Utility-Toolkit/
│
├── main.py
└── README.md
```

> Replace `main.py` with your actual Python filename if it is different.

## How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installation:

```bash
python --version
```

### Step 2: Run the Program

Open the project folder in Terminal or Command Prompt and run:

```bash
python main.py
```

### Step 3: Select an Option

The main menu provides the following options:

```text
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations
6. Explore Module Attributes
7. Exit
```

## Example

```text
========================================
Welcome to Multi-Utility Toolkit
========================================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
========================================
```

## Error Handling

The application includes error handling for invalid inputs, such as:

* Invalid numbers
* Invalid dates
* Invalid file operations
* Missing files
* Invalid module names
* Invalid menu choices

## Learning Objectives

This project helps demonstrate:

* Python functions
* Menu-driven programming
* Exception handling
* Built-in Python modules
* Date and time handling
* Random data generation
* File handling
* UUID generation
* Dynamic module importing
* `dir()` function
* User input and output

## Author

**Meshva Patel**

## License

This project is created for educational and learning purposes.
