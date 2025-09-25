# Restaurant Order System
A C# console project created as part of the **CSCI 1250 course**.  
This program allows users to order menu items from a restaurant, calculates the total price including tax, and provides a final receipt.

## Features
- Displays a menu with prices for each item:
```
   Pizza: $10
   Burger: $6
   Fries: $4
   Soda: $2
   Dessert: $4
```
- Allows ordering multiple items with quantities.
- Validates input to ensure non-negative quantities.
- Keeps track of ordered quantities.
- Calculates the total price including a fixed tax rate (8.5%).
- Displays a receipt with a summary of the order and total price.

## Installation
1. Clone the main repository:
git clone https://github.com/BurakBaskir/CSCI-1250-Projects.git
2. Navigate to this project folder inside the repo:
cd CSCI-1250-Projects/RestourantOrder
3. Open and run the project in your C# environment (Visual Studio or .NET CLI).

## Usage
The program will repeatedly prompt you to order items until you type done.

Example interaction:
```csharp 
--------Welcome to the Restaurant Order System!---------
Here is our menu:
pizza - $10
burger - $6
fries - $4
soda - $2
dessert - $4

Please enter the item you would like to order:(name of the food)
burger
please enter the quantity:
2

You have ordered 2 of burgers.
Would you like to order anything else? or type 'done' to finish.
done

Here is your receipt:
Your total is $13.02
Thank you for dining with us! Have a great day!
```

## Reference / Inspiration
This project was inspired by the [CSCI 1250 class resources](https://github.com/CSCI-1250/class_resources_public) provided by Professor Ryan Haas.

## Author  
**Burak Baskir**
[GitHub Profile](https://github.com/BurakBaskir)

