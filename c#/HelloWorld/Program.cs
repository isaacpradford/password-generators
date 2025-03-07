namespace HelloWorld;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("ur name?");
        var name = Console.ReadLine();
        var currentDate = DateTime.Now;
        Console.WriteLine($"hello, {name}, I am AI that is going to take over world on {currentDate}");
    }
}