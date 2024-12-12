import matplotlib.pyplot as plt  # For plotting the polynomial

# Creating a Class to evaluate polynomial equation and plotting
class PolyEval:
    def __init__(self):
        # Initialising degree, coefficients, and range as None
        self.degree = None
        self.coefficients = []
        self.domain_range = None

    # Show the main menu and give options to user to select
    def display_menu(self):
        while True:
            print("\nPolynomial Evaluation Menu")
            print(f"1. Specify the polynomial degree (Current: {self.degree})")
            print(f"2. Enter coefficients (Current: {self.coefficients if self.coefficients else 'Not set'})")
            print(f"3. Set the evaluation range (Current: {self.domain_range})")
            print("4. Show the polynomial plot")
            print("5. Quit")

            # Get the user's choice or selection of option
            sel= input("Select an option (1-5): ")

            if sel == '1':
                self.input_degree()
            elif sel == '2':
                self.input_coefficients()
            elif sel == '3':
                self.set_range()
            elif sel == '4':
                self.plot_polynomial()
            elif sel == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 5.")

    # Set the degree of the polynomial
    def input_degree(self):
        while True:
            try:
                # Ask the user for the degree of the polynomial and validate it to evaluate
                self.degree = int(input("Enter the degree of the polynomial: "))
                if self.degree < 0:
                    print("Degree must be a non-negative integer.")
                else:
                    break  # Exits the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid non-negative (positive or zero) integer.")

    # Get the coefficients of the polynomial from the user to eval
    def input_coefficients(self):
        if self.degree is None:
            print("Please set the polynomial degree first.")
            return

        # Clear previous coefficients and prompt for new ones
        self.coefficients = []
        print("Enter the coefficients starting from the highest degree term.")
        for i in range(self.degree, -1, -1):
            while True:
                try:
                    coef = float(input(f"Enter the coefficient for x^{i}: "))
                    self.coefficients.append(coef)
                    break  # Exits the loop once a valid coefficient is entered by the user
                except ValueError:
                    print("Invalid input. Please enter a number.")

    # Set the range of x-values for plotting
    def set_range(self):
        try:
            # Get start, stop, and step for the range of the domain
            start = int(input("Enter the start of the range for domain: "))
            stop = int(input("Enter the end of the range for domain: "))
            step = int(input("Enter the step size (positive integer only): "))
            if start >= stop or step <= 0:
                print("Invalid range. Make sure start < stop and step > 0.")
            else:
                self.domain_range = (start, stop, step)
                print(f"Range set to: range({start}, {stop}, {step})")
        except ValueError:
            print("Invalid input. Please enter valid integers for the range.")

    # Plot the polynomial evaluation using matplotlib plotting 
    def plot_polynomial(self):
        if not self.domain_range or not self.coefficients:
            print("Please set the coefficients and range for polynomial before plotting.")
            return

        # Generating x-values based on the specified range of the domain for polynomial
        x_values = list(range(self.domain_range[0], self.domain_range[1], self.domain_range[2]))
        # Computing the corresponding y-values for the polynomial based on x values
        y_values = [
            sum(coef * (x ** i) for i, coef in enumerate(reversed(self.coefficients))) for x in x_values
        ]

        # Plot the polynomial and label them with the corresponding names
        plt.figure("Polynomial Plot")
        plt.xlabel("x-axis")
        plt.ylabel("f(x)")
        plt.title("Polynomial Curve")
        plt.grid(True)
        plt.plot(x_values, y_values, "b-", label="f(x)")
        plt.legend()
        plt.show()
