using System;

class Program
{
    const int GridWidth = 10;
    const int GridHeight = 10;

    static void Main(string[] args)
    {
        int playerX = GridWidth / 2;
        int playerY = GridHeight / 2;
        bool running = true;
        int score = 0;

        Random rng = new Random();
        int starX = rng.Next(0, GridWidth);
        int starY = rng.Next(0, GridHeight);

        Console.WriteLine("Move with W/A/S/D. Then press Enter. Type Q to quit.");
        Console.WriteLine("Walk into the '*' to score a point!");

        while (running)
        {
            DrawGrid(playerX, playerY, starX, starY, score);

            Console.WriteLine("Move: ");
            string input = Console.ReadLine();
            input = (input ?? "").Trim().ToLower();

            switch (input)
            {
                case "w": playerY = Math.Max(0, playerY - 1); break;
                case "s": playerY = Math.Min(GridHeight - 1, playerY + 1); break;
                case "a": playerX = Math.Max(0, playerX - 1); break;
                case "d": playerX = Math.Min(GridWidth - 1, playerX + 1); break;
                case "q": running = false; break;
                default:
                    Console.WriteLine("Unknown Command. Use W/A/S/D or Q.");
                    break;
            }

            if (playerX == starX && playerY == starY)
            {
                score = score + 1;
                starX = rng.Next(0, GridWidth);
                starY = rng.Next(0, GridHeight);
            }
        }
        Console.WriteLine("Thanks for Playing! Final Score: " + score);
    }

    static void DrawGrid(int playerX, int playerY, int starX, int starY, int score)
    {
        try { Console.Clear(); } catch { }
        Console.WriteLine("Score: " + score);
        for (int y = 0; y < GridHeight; y++)
        {
            for (int x = 0; x < GridWidth; x++)
            {
                if (x == playerX && y == playerY)
                    Console.Write('@');
                else if (x == starX && y == starY)
                    Console.Write('*');
                else
                    Console.Write('.');
            }
            Console.WriteLine();
        }
    }
}
