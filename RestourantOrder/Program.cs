using System;


class Program
{

    static void Main(string[] args)
    {    Console.WriteLine("\n--------Welcome to the Restaurant Order System!---------");
        string order = "";
        int BurgerQuantity = 0;
        int PizzaQuantity = 0;
        int FriesQuantity = 0;
        int SodaQuantity = 0;
        int DessertQuantity = 0;
        double Tax = 1.085;
        while (order != "done")
        {
            Console.WriteLine(@"
            Here is our menu:
            pizza - $10
            burger - $6
            fries - $4
            soda - $2
            dessert - $4 ");

            Console.WriteLine("Please enter the item you would like to order:(name of the food)");
            string food = Console.ReadLine().ToLower().Trim();

            if (food.Equals("burger"))

            {
                Console.WriteLine("please enter the quantity:");
                int Quantity_of_Burger = int.Parse(Console.ReadLine());
                if (Quantity_of_Burger < 0)
                {
                    Console.WriteLine("Invalid quantity. Please enter a non-negative number.");
                    continue;
                }
                BurgerQuantity = Quantity_of_Burger + BurgerQuantity;
            }
            else if (food.Equals("pizza"))
            {
                Console.WriteLine("please enter the quantity:");
                int Quantity_of_Pizza = int.Parse(Console.ReadLine());
                if (Quantity_of_Pizza < 0)
                {
                    Console.WriteLine("Invalid quantity. Please enter a non-negative number.");
                    continue;
                }
                PizzaQuantity = Quantity_of_Pizza + PizzaQuantity;
            }
            else if (food.Equals("fries"))
            {
                Console.WriteLine("please enter the quantity:");
                int Quantity_of_Fries = int.Parse(Console.ReadLine());
                if (Quantity_of_Fries < 0)
                {
                    Console.WriteLine("Invalid quantity. Please enter a non-negative number.");
                    continue;
                }
                FriesQuantity = Quantity_of_Fries + FriesQuantity;
            }
            else if (food.Equals("soda"))
            {
                Console.WriteLine("please enter the quantity:");
                int Quantity_of_Soda = int.Parse(Console.ReadLine());
                if (Quantity_of_Soda < 0)
                {
                    Console.WriteLine("Invalid quantity. Please enter a non-negative number.");
                    continue;
                }
                SodaQuantity = Quantity_of_Soda + SodaQuantity;
            }
            else if (food.Equals("dessert"))
            {
                Console.WriteLine("please enter the quantity:");
                int Quantity_of_Dessert = int.Parse(Console.ReadLine());
                if (Quantity_of_Dessert < 0)
                {
                    Console.WriteLine("Invalid quantity. Please enter a non-negative number.");
                    continue;
                }
                DessertQuantity = Quantity_of_Dessert + DessertQuantity;
            }
            else
            {
                Console.WriteLine("Invalid item. Please try again.");
            }
            
            Console.WriteLine($"You have ordered {BurgerQuantity} of burgers.");
            Console.WriteLine($"You have ordered {PizzaQuantity} of pizzas.");
            Console.WriteLine($"You have ordered {FriesQuantity} of fries.");
            Console.WriteLine($"You have ordered {SodaQuantity} of sodas.");
            Console.WriteLine($"You have ordered {DessertQuantity} of desserts.");
            Console.WriteLine("Would you like to order anything else? or type 'done' to finish.");

            order = Console.ReadLine();
        }
           
        
    Console.WriteLine(" Here is your receipt:");
    double total = (BurgerQuantity * 6 + PizzaQuantity * 10 + FriesQuantity * 4 + SodaQuantity * 2 + DessertQuantity * 4) * Tax;
    Console.WriteLine($"Your total is ${total}");
    Console.WriteLine("Thank you for dining with us! Have a great day!");
             
     }
}