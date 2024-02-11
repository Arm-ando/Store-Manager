# Nike Warehouse Stock Management System

## Overview

This Python program serves as a stock management system for Nike warehouses, allowing store managers to efficiently manage inventory and perform various tasks related to stock-taking. The program reads data from a text file (`inventory.txt`) and provides functionalities like searching products, determining low stock, calculating total value, and more.

## Features

- **Shoe Class:**
  - Attributes: country, code, product, cost, quantity
  - Methods:
    - `get_cost`: Returns the cost of the shoes.
    - `get_quantity`: Returns the quantity of the shoes.
    - `__str__`: Returns a string representation of a shoe.

- **Functions:**
  - `read_shoes_data`: Reads data from `inventory.txt`, creates shoe objects, and appends them to the shoe list.
  - `capture_shoes`: Allows users to capture data about a shoe, create a shoe object, and append it to the shoe list.
  - `view_all`: Iterates over the shoe list and prints shoe details in a formatted table (optional: using Python's tabulate module).
  - `re_stock`: Finds the shoe with the lowest quantity, prompts the user to restock, and updates the quantity in the file.
  - `search_shoe`: Searches for a shoe using the shoe code and returns the object for display.
  - `value_per_item`: Calculates and prints the total value for each item (value = cost * quantity).
  - `highest_qty`: Determines the product with the highest quantity and prints it as available for sale.

- **Menu:**
  - The main program includes a menu within a while loop, allowing users to execute each function interactively.

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/nike-warehouse-stock-management.git
   cd nike-warehouse-stock-management
