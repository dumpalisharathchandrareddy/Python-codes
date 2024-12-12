/*
University of New Haven
CSCI 6617 02 Spring 2024
Java Programming
Dumpali Sharath Chandra Reddy - 00864049
%sdump1@unh.newhaven.edu%
Instructor: Dr. Donyina
NAME OF THE CLASS: FallingObjectDistanceCalculator
DESCRIPTION: It is the class which calculates distance covered by a falling object using initial velocity and time of the fall in seconds
*/

package sdump1_A1;
import java.util.Scanner;

public class FallingObjectDistanceCalculator {
    // Gravitational force constant
    private static final double GRAVITATIONAL_FORCE = 32.17405;

    public static void main(String[] args) {
        // Display header information
        System.out.println("Falling Object Distance Calculator");
        System.out.println("Author: Dumpali Sharath Chandra Reddy");
        System.out.println("Student ID: 00864049");
        System.out.println("Email: sdump1@unh.newhaven.edu");
        System.out.println("----------------------------------");

        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt user for initial velocity input
        System.out.print("Please enter the initial velocity of the falling object (in feet/second): ");
        double initialVelocity = scanner.nextDouble();
        if(initialVelocity>=0) {

        // Prompt user for time input
        System.out.print("Please enter the time of the fall (in seconds): ");
        double time = scanner.nextDouble();
        


        // Calculate the distance using the formula
        double distance = initialVelocity * time + 0.5 * GRAVITATIONAL_FORCE * Math.pow(time, 2);

        // Convert distance to two decimal places
        distance = (int) (distance * 100) / 100.0;

        // Display the result
        System.out.println("The distance traveled by an object falling at an initial velocity of "
                + initialVelocity + " feet/second over a time of " + time + " seconds is " + distance + " feet.");
        }
        else {
        	System.out.println("initialVelocity must be >=0");
        }

        // Close the Scanner
        scanner.close();
    }

}

