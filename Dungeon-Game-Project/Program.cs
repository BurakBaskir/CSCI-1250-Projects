using System;
using System.Threading; // Thread.Sleep için gerekli

class Program
{
    static Random random = new Random();

    static int PlayerDamageAndEnemyHealth(int EnemyHealth)
    {
        Console.WriteLine("Click 'Enter' to attack");
        Console.ReadKey();
        int PlayerDamage = random.Next(12, 16);
        Console.WriteLine($@"You Hit {PlayerDamage} Damage
It must Hurt!");
        EnemyHealth -= PlayerDamage;
        Console.WriteLine($"Monster Health is {EnemyHealth}");
        return EnemyHealth;
    }

    static int EnemyDamageAndPlayerHealth(int PlayerHealth)
    {
        int EnemyDamage = random.Next(6, 9);
        Console.WriteLine($"You receive {EnemyDamage} Damage");
        PlayerHealth -= EnemyDamage;
        Console.WriteLine($"Player Health is {PlayerHealth}");
        return PlayerHealth;
    }

    static void FightLoop()
    {
        int playerHealth = 30;
        int EnemyHealth = 30;
        Console.WriteLine("The Fight Starts!");

        while (true)
        {
            EnemyHealth = PlayerDamageAndEnemyHealth(EnemyHealth);
            if (EnemyHealth <= 0)
            {
                Console.WriteLine("Great Job! You killed the monster!");
                break;
            }

            Console.WriteLine("Monster Attacks!");
            Thread.Sleep(2000);
            playerHealth = EnemyDamageAndPlayerHealth(playerHealth);

            if (playerHealth <= 0)
            {
                Console.WriteLine("DEFEAT! Monster Killed you!");
                Console.WriteLine("Do you want to try again? enter (y/n)");
                string choice = Console.ReadLine();
                if (choice == "y")
                {
                    Main(null); // tekrar oyuna dön
                }
                else
                {
                    Environment.Exit(0); // oyundan çık
                }
            }
        }
    }

    static void Main(string[] args)
    {
        Console.WriteLine(@"Hey Wake Up! 
We are lucky he didnt eat us yet we have to find a way to escape from here!
Hide Hide! he is coming for us");
        Console.WriteLine("\n Click enter to hide");
        Console.ReadKey();
        Console.WriteLine("Please please not me! AAAAAAAAAAAAAA");
        Console.WriteLine("Your mate is gone and he is gonna come for you as well find a way to get out");
        Console.WriteLine("\n Click enter to walk thru dungeon");
        Console.ReadKey();
        Console.WriteLine("There is a separation left and right, select one");

        string WayChoice = Console.ReadLine().ToLower();

        while (true)
        {
            if (WayChoice == "right")
            {
                Console.WriteLine("Here is a door try to open it");
                Console.WriteLine("Click enter to try");
                Console.ReadKey();
                Console.WriteLine("It is locked, try other way");
                Console.WriteLine("Click enter to go left side");
                Console.ReadKey();
                WayChoice = "left"; // tekrar sola yönlendir
            }
            else if (WayChoice == "left")
            {
                Console.WriteLine("You encounter to the monster! you better fight for your life");
                FightLoop();
                Console.WriteLine("You found a key on monster, try it to open the door");
                break;
            }
            else
            {
                Console.WriteLine("Invalid Way Choice. Type right or left:");
                WayChoice = Console.ReadLine().ToLower();
            }
        }

        Console.WriteLine("Click enter to go to the door");
        Console.ReadKey();
        Console.WriteLine("To try open door click enter");
        Console.ReadKey();
        Console.WriteLine("It Works!! You could escape from the dungeon");

        Environment.Exit(0); // ÇIKIŞ (return yazmana gerek yok)
    }
}
