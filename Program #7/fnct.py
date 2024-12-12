import matplotlib.pyplot as plt

# Variables to store polynomial characteristics and evaluation range
degree = None
coefficients = []
domain_range = None

# Display menu with options for setting up and plotting the polynomial
def display_menu():
    global degree, coefficients, domain_range
    while True:
        # Print menu options
        print("\nPolynomial Evaluation Menu")
        print("1. Specify the polynomial degree (Current: {})".format(degree))
        print("2. Enter coefficients (Current: {})".format(coefficients if coefficients else "Not set"))
        print("3. Set the evaluation range (Current: {})".format(domain_range))
        print("4. Show the polynomial plot")
        print("5. Quit")

        # Get user input
        selection = input("Select an option (1-5): ")

        # Execute the corresponding function based on user choice
        if selection == '1':
            input_degree()
        elif selection == '2':
            input_coefficients()
        elif selection == '3':
            set_range()
        elif selection == '4':
            # Ensure degree, coefficients, and range are set before plotting
            if domain_range and degree is not None and coefficients:
                plot_polynomial()
            else:
                print("Ensure that degree, coefficients, and range are set before plotting.")
        elif selection == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please enter a number between 1 and 5.")

# Function to set polynomial degree
def input_degree():
    global degree
    while True:
        try:
            degree = int(input("Enter the degree of the polynomial: "))
            if degree < 0:
                raise ValueError("Degree should be a non-negative integer.")
            break
        except ValueError:
            print("Invalid entry. Please provide a valid non-negative integer.")

# Function to collect polynomial coefficients
def input_coefficients():
    global coefficients
    if degree is None:
        print("Please specify the polynomial degree first.")
        return

    coefficients = []  # Reset any previous entries
    print("Enter the coefficients starting from the term with the highest degree.")
    for i in range(degree, -1, -1):
        while True:
            try:
                coef = float(input(f"Enter coefficient for x^{i}: "))
                coefficients.append(coef)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Function to set the domain range for evaluation (start, stop, step)
def set_range():
    global domain_range
    try:
        start = int(input("Enter the start of the range: "))
        stop = int(input("Enter the end of the range: "))
        step = int(input("Enter the step size (positive integer): "))
        if start >= stop or step <= 0:
            raise ValueError("Ensure start < stop and step > 0.")
        domain_range = (start, stop, step)
        print(f"Range set to range({start}, {stop}, {step})")
    except ValueError:
        print("Invalid entry. Ensure start < stop and step > 0.")

# Function to plot the polynomial across the set range
def plot_polynomial():
    if not domain_range or not coefficients:
        print("Range and coefficients must be specified before plotting.")
        return

    # Generate x-values in the defined range
    x_values = list(range(domain_range[0], domain_range[1], domain_range[2]))
    # Calculate polynomial values for each x in x_values
    y_values = [sum(coef * (x ** i) for i, coef in enumerate(reversed(coefficients))) for x in x_values]

    # Plot polynomial using matplotlib
    plt.figure("Polynomial Plot")
    plt.xlabel("x-axis")
    plt.ylabel("f(x)")
    plt.title("Polynomial Curve")
    plt.grid(True)
    plt.plot(x_values, y_values, "b-", label="f(x) = Polynomial")
    plt.legend()
    plt.show()
