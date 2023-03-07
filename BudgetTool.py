# Import the os and sys modules
import os
import sys

# Define the Budget class
class Budget(object):
    # Define the __init__ method, which runs when a Budget object is created
    def __init__(self):
        # Clear the console window
        os.system('cls')
        # Ask the user to input their budget
        self.budget = float(input('How much is your budget?\n'))
        # Calculate the default amount to spend (50% of the budget)
        self.spending = self.budget * 0.5
        # Clear the console window
        os.system('cls')
        # Call the main method to display the menu
        self.main()
        
    # Define the main method, which displays the menu and calls other methods based on user input
    def main(self):
        # Display the 5:3:2 rule of spending
        print('This calculator uses 5:3:2 rule of spending by default.')
        # Display the user's budget
        print('\nYour budget: $', '{:.2f}'.format(self.budget))
        # Ask the user what they want to do
        main_option = int(input('\nWhat do you want to do?\n1) View Budget Plan\n2) View Spending Budget\n3) Exit\n'))
        # Call the budget_plan method if the user selects option 1
        if main_option == 1:
            self.budget_plan()
        # Call the spending_budget method if the user selects option 2
        elif main_option == 2:
            self.spending_budget()
        # Quit the program if the user selects option 3
        else:
            quit

    # Define the budget_plan method, which calculates and displays the user's budget plan
    def budget_plan(self):
        # Clear the console window
        os.system('cls')
        # Ask the user how much they want to save
        option = int(input('How much do you want to save?\n1) 20%\n2) 30%\n'))
        # Set the saving amount based on the user's input
        if option == 1:
            self.saving = 0.2
        elif option == 2:
            self.saving = 0.3
        else:
            # Display an error message if the user enters an invalid option
            print('Please select only 1 or 2')
        # Calculate the amount the user needs to save
        self.final_saving = self.budget * self.saving
        # Calculate the amount of money the user has left over after spending and saving
        self.extra = self.budget-self.spending-(self.budget*self.saving)
        # Display the user's spending, savings, and extra money
        print('\nSpending: $', '{:.2f}'.format(self.spending), '\nTo Save: $', '{:.2f}'.format(self.final_saving), '\nExtra: $', '{:.2f}'.format(self.extra))
        # Wait for the user to press a key before continuing
        os.system('pause')
        # Clear the console window
        os.system('cls')
        # Call the main method to display the menu again
        self.main()

    def spending_budget(self):
    # Clear the screen
    os.system('cls')
    # Print the user's spending budget
    print('Spending Budget: $', '{:.2f}'.format(self.spending))
    # Ask the user for their monthly rent/mortgage and store it in a variable called rent
    rent = float(input('\nHow much is your rent/mortgage?\n'))
    # Ask the user for their monthly bills and store it in a variable called bills
    bills = float(input('\nHow much are your monthly bills?\n'))
    # Calculate the remaining amount available for food and store it in a variable called food
    food = self.spending - rent - bills
    # Display the expenses, including the rent/mortgage, bills, and food
    print('\nEXPENSES:\nRent: $','{:.2f}'.format(rent),'\nBills: $','{:.2f}'.format(bills),'\nFood: $','{:.2f}'.format(food))
    # Pause the program so the user can view the expenses
    os.system('pause')
    # Clear the screen
    os.system('cls')
    # Return to the main menu
    self.main()

if __name__ == '__main__':
    # Start the program by creating a new instance of the Budget class and exiting the program when it's done running
    sys.exit(Budget())
