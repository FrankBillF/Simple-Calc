#!/usr/bin/env python3
"""
Enhanced Calculator Application with Data Structures

This program provides basic arithmetic operations with data storage capabilities.
It uses dictionaries and lists to organize calculation history by day of the month.
"""

import datetime
from typing import Dict, List, Tuple, Any, Optional

# Global data structures to store calculation history
calculation_history: Dict[int, List[Dict[str, Any]]] = {}  # Day -> List of calculations
daily_stats: Dict[int, Dict[str, float]] = {}  # Day -> Statistics

def get_user_inputs():
    """
    Obtain user inputs for two numbers and the arithmetic operation.
    
    Returns:
        tuple: (num1, num2, operation) where num1 and num2 are floats,
               and operation is a string representing the arithmetic operation
    """
    print("=== Enhanced Calculator with Data Storage ===")
    print("Please enter two numbers and choose an operation.")
    print()
    
    # Get first number
    while True:
        try:
            num1_input = input("Enter the first number: ")
            num1 = float(num1_input)
            break
        except ValueError:
            print("Error: Please enter a valid number (e.g., 5, 3.14, -2)")
    
    # Get second number
    while True:
        try:
            num2_input = input("Enter the second number: ")
            num2 = float(num2_input)
            break
        except ValueError:
            print("Error: Please enter a valid number (e.g., 5, 3.14, -2)")
    
    # Get arithmetic operation
    print("\nAvailable operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        operation_input = input("\nChoose an operation (1-4 or +, -, *, /): ").strip()
        
        # Map numeric choices to symbols
        operation_map = {
            '1': '+',
            '2': '-', 
            '3': '*',
            '4': '/'
        }
        
        # Use the mapped operation or the direct symbol
        operation = operation_map.get(operation_input, operation_input)
        
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Error: Please choose a valid operation (1-4 or +, -, *, /)")
    
    return num1, num2, operation

def validate_inputs(num1, num2, operation):
    """
    Validate the inputs to ensure they are usable for calculations.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Arithmetic operation symbol
    
    Returns:
        bool: True if inputs are valid, False otherwise
    """
    # Check for division by zero
    if operation == '/' and num2 == 0:
        print("Error: Division by zero is not allowed!")
        return False
    
    return True

def execute_operation(num1, num2, operation):
    """
    Execute the chosen arithmetic operation on the two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Arithmetic operation symbol
    
    Returns:
        float: Result of the calculation
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        raise ValueError(f"Unknown operation: {operation}")

def store_calculation(num1: float, num2: float, operation: str, result: float):
    """
    Store the calculation in the data structures organized by day.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Arithmetic operation symbol
        result (float): Calculated result
    """
    current_day = datetime.datetime.now().day
    
    # Create calculation record
    calculation_record = {
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'num1': num1,
        'num2': num2,
        'operation': operation,
        'result': result
    }
    
    # Initialize day in history if it doesn't exist
    if current_day not in calculation_history:
        calculation_history[current_day] = []
    
    # Add calculation to history
    calculation_history[current_day].append(calculation_record)
    
    # Update daily statistics
    update_daily_stats(current_day, result)

def update_daily_stats(day: int, result: float):
    """
    Update statistics for a specific day.
    
    Args:
        day (int): Day of the month
        result (float): Calculation result to include in statistics
    """
    if day not in daily_stats:
        daily_stats[day] = {
            'count': 0,
            'sum': 0.0,
            'min': float('inf'),
            'max': float('-inf'),
            'average': 0.0
        }
    
    stats = daily_stats[day]
    stats['count'] += 1
    stats['sum'] += result
    stats['min'] = min(stats['min'], result)
    stats['max'] = max(stats['max'], result)
    stats['average'] = stats['sum'] / stats['count']

def display_result(num1, num2, operation, result):
    """
    Display the calculated result clearly to the user.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Arithmetic operation symbol
        result (float): Calculated result
    """
    print("\n" + "="*40)
    print("CALCULATION RESULT")
    print("="*40)
    print(f"{num1} {operation} {num2} = {result}")
    print("="*40)

def display_daily_history(day: Optional[int] = None):
    """
    Display calculation history for a specific day or all days.
    
    Args:
        day (Optional[int]): Specific day to display. If None, shows all days.
    """
    if day is not None:
        if day in calculation_history:
            print(f"\n=== Calculations for Day {day} ===")
            for i, calc in enumerate(calculation_history[day], 1):
                print(f"{i}. {calc['timestamp']}: {calc['num1']} {calc['operation']} {calc['num2']} = {calc['result']}")
            
            if day in daily_stats:
                stats = daily_stats[day]
                print(f"\nDay {day} Statistics:")
                print(f"  Total calculations: {stats['count']}")
                print(f"  Sum of results: {stats['sum']:.2f}")
                print(f"  Average result: {stats['average']:.2f}")
                print(f"  Min result: {stats['min']:.2f}")
                print(f"  Max result: {stats['max']:.2f}")
        else:
            print(f"No calculations found for day {day}")
    else:
        if calculation_history:
            print("\n=== All Calculation History ===")
            for day in sorted(calculation_history.keys()):
                print(f"\nDay {day} ({len(calculation_history[day])} calculations):")
                for calc in calculation_history[day]:
                    print(f"  {calc['timestamp']}: {calc['num1']} {calc['operation']} {calc['num2']} = {calc['result']}")
        else:
            print("No calculation history available.")

def get_menu_choice():
    """
    Display menu and get user choice.
    
    Returns:
        str: User's menu choice
    """
    print("\n" + "="*50)
    print("CALCULATOR MENU")
    print("="*50)
    print("1. Perform calculation")
    print("2. View today's calculations")
    print("3. View calculations for specific day")
    print("4. View all calculation history")
    print("5. View daily statistics")
    print("6. Exit")
    print("="*50)
    
    return input("Choose an option (1-6): ").strip()

def main():
    """
    Main function that orchestrates the enhanced calculator workflow.
    """
    try:
        while True:
            choice = get_menu_choice()
            
            if choice == '1':
                # Perform calculation
                num1, num2, operation = get_user_inputs()
                
                if not validate_inputs(num1, num2, operation):
                    continue
                
                result = execute_operation(num1, num2, operation)
                display_result(num1, num2, operation, result)
                store_calculation(num1, num2, operation, result)
                
            elif choice == '2':
                # View today's calculations
                current_day = datetime.datetime.now().day
                display_daily_history(current_day)
                
            elif choice == '3':
                # View calculations for specific day
                try:
                    day = int(input("Enter day of month (1-31): "))
                    if 1 <= day <= 31:
                        display_daily_history(day)
                    else:
                        print("Error: Day must be between 1 and 31")
                except ValueError:
                    print("Error: Please enter a valid day number")
                    
            elif choice == '4':
                # View all calculation history
                display_daily_history()
                
            elif choice == '5':
                # View daily statistics
                if daily_stats:
                    print("\n=== Daily Statistics ===")
                    for day in sorted(daily_stats.keys()):
                        stats = daily_stats[day]
                        print(f"\nDay {day}:")
                        print(f"  Total calculations: {stats['count']}")
                        print(f"  Sum of results: {stats['sum']:.2f}")
                        print(f"  Average result: {stats['average']:.2f}")
                        print(f"  Min result: {stats['min']:.2f}")
                        print(f"  Max result: {stats['max']:.2f}")
                else:
                    print("No statistics available.")
                    
            elif choice == '6':
                print("Thank you for using the Enhanced Calculator!")
                break
                
            else:
                print("Invalid choice. Please select 1-6.")
                
    except KeyboardInterrupt:
        print("\n\nCalculator terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 
