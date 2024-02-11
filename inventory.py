# Importing tabulate
from tabulate import tabulate


# Creating my class called 'Shoes'
class Shoes:

    # Constructor to initialize shoe attribute / variable e.g. self.country = country
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method within class to return cost
    def get_cost(self):
        return self.cost

    # Method to return the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # Method to return object in string form
    def __str__(self):
        return f"""{self.country}, {self.code}, {self.product}, {self.product}, {self.cost}, {self.quantity}"""


# Empty shoe list to append data to later
shoe_list = []


# Function 1: read data from text file
def read_shoes_data():
    # try function which reads code
    try:
        with open('inventory.txt', 'r') as file:

            # next function to skip the first line
            next(file)

            # For loop to iterate through the file
            # Split function to obtain necessary data
            for line in file:
                data = line.split(",")

                # Storing objects Country, Code, Product, Cost, Quantity in variable called shoe
                shoe = Shoes(data[0], data[1], data[2], data[3], data[4])

                # Appending variable to empty shoe list
                shoe_list.append(shoe)

    # except block with object creation containing information about the error
    except Exception as e:
        print("An error reading file has occurred:", e)

    except FileNotFoundError:
        print("Error: File 'inventory.txt' not found.")


# Function 2: Allow user to enter data about product
def capture_shoes():
    country = input("Enter the country of origin: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")

    # Input validation for cost and quantity
    while True:
        try:
            cost = float(input("Enter the cost: "))
            quantity = int(input("Enter the quantity: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Creating shoe object
    shoe = Shoes(country, code, product, cost, quantity)

    # Appending shoe object to the shoe_list list.
    shoe_list.append(shoe)


# Function 3: View all products in table format
def view_all():
    if not shoe_list:
        print("No shoes to display!")
    else:
        data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
        table = tabulate(data, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="grid")
        print(table)


# Function 4: Locate object with lowest quantity
def restock():
    quantities = []
    for object_ in shoe_list:
        quantities.append(int(object_.quantity.strip("\n")))

    # Used to stored object with lowest quantity
    object_with_lowest_quantity = ""

    # assigning max value and updating when looping through list
    lowest = max(quantities)  # At the end of loop, lowest quantity will have been grabbed

    # for loop for grabbing object with lowest current and
    # printing it out

    object_index = 0  # for grabbing index of object with lowest indice
    for index, object_ in enumerate(shoe_list):
        looping_object = int(object_.quantity.strip("\n"))  # Grabbing quantity and casting it to integer
        if looping_object < lowest:
            lowest = looping_object
            object_with_lowest_quantity = object_
            object_index = index

    # Printing out shoe with low quantity
    print(f"\nThe shoe below has lowest quantity: \n"
          f"{object_with_lowest_quantity}")

    # asking user if they would like to update quantity
    user_option = input("Would you like to update it? - (y/n): ").lower()
    if user_option == "y":

        amount_to_add_by = int(input("How much would you like to add by?: "))

        least_quantity_object = shoe_list[object_index]  # Grabbing object with least quantity
        new_quantity = int(
            least_quantity_object.quantity) + amount_to_add_by  # Creating new quantity value for replacing old quantity
        least_quantity_object.quantity = new_quantity  # Now changing the quantity to the new one

        print("QUANTITY UPDATED!!!!!!!!!")
        for i in shoe_list:
            print(i)

    elif user_option == "n":
        pass
    else:
        print("Invalid Response")


# Function 5: Search for shoe by product code
def search_shoe():
    code = input("Please enter product code here: ")
    for shoes in shoe_list:
        if code == shoes.code:
            print(shoes.product)
            return
    print("Product not found.")


# Function 6: Calculate the total value for each item
def value_per_item(shoe_list):
    # For loop to iterate through the shoe list
    for shoe in shoe_list:
        cost = float(shoe.cost)
        quantity = int(shoe.quantity)
        value = cost * quantity
        print(f'{shoe.product}: cost = £{shoe.cost}, quantity = {shoe.quantity}, value = £{value}')


# Function 7: Determine the product with the highest quantity
def highest_qty():
    # max function to return highest quantity number
    # making lambda expression to create anonymous function which returns the highest quantity
    max_quan = max(shoe_list, key=lambda x: x.quantity)

    # Print function
    print(f"\n{max_quan.product} has the highest quantity.")
    print(f'{max_quan.product} is now for sale')


# Menu

# read shoes data function so that all the data is read and appended to the empty shoe_list
read_shoes_data()

# While loop throughout main menu
while True:

    # Requesting user input from menu
    menu = input("""
    Hi welcome to the menu: 
    
     
    1. View inventory 
    2. New product entry 
    3. Search product 
    4. Re-stock product
    5. High quantity product
    6. Calculate total value of stock items 
    7. Exit 
    
    Enter choice here: """)

    # if statement for when user selects to view all inventory with view function to display in grid format
    if menu == "1":
        view_all()

    # elif statement for when user selects to enter new product with capture_shoes() function
    elif menu == "2":
        capture_shoes()

    # elif statement for when user decides to search for product via code
    elif menu == "3":
        # requesting user input and storing data in variable called 'code'
        # search_shoe(code) function to return the shoe to user
        # code = input("\nPlease enter the product code: ")
        search_shoe()

    # elif statement for when user decides to restock product with restock function
    elif menu == "4":
        restock()

    # elif statement for when user decides to view what is the highest quantity
    elif menu == "5":
        highest_qty()

    # elif statement for when user decides to view the total value for each item
    elif menu == "6":
        value_per_item(shoe_list)

    # Exit function for when they decide to exit.
    elif menu == "7":
        print("Good bye!")
        exit()

    else:
        print("\nERROR! \nPlease enter a valid integer!")


