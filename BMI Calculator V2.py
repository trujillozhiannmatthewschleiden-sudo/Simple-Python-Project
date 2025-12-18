# BMI Calculator
# This program calculates a person's Body Mass Index (BMI)
# and tells them their weight category.

# This function calculates BMI
def calculate_bmi(weight, height):
    # BMI formula: weight divided by height squared
    return weight / (height * height)

# This function decides the BMI category
def bmi_category(bmi):
    # If BMI is less than 18.5
    if bmi < 18.5:
        return "Underweight"
    
    # If BMI is between 18.5 and 24.9
    elif bmi < 24.9:
        return "Normal weight"
    
    # If BMI is between 25 and 29.9
    elif bmi < 29.9:
        return "Overweight"
    
    # If BMI is 30 or more
    else:
        return "Obese"

# Main part of the program
def main():
    # Print the title
    print("=== BMI Calculator ===")

    try:
        # Ask the user for weight in kilograms
        weight = float(input("Enter your weight in kilograms: "))
        
        # Ask the user for height in meters
        height = float(input("Enter your height in meters: "))

        # Check that weight and height are positive numbers
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Find the BMI category
        category = bmi_category(bmi)

        # Show the BMI (rounded to 2 decimal places)
        print(f"\nYour BMI is: {bmi:.2f}")
        
        # Show the weight category
        print("Category:", category)

    # If the user enters letters instead of numbers
    except ValueError:
        print("Please enter numbers only.")

# This line starts the program
if __name__ == "__main__":
    main()
