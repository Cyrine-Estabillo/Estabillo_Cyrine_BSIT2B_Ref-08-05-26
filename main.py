class Comparator:
    def compare(self):
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))

        if num1 > num2:
            print(f"The bigger number is: {num1}")
        elif num2 > num1:
            print(f"The bigger number is: {num2}")
        else:
            print("Both numbers are equal.")

com = Comparator()
com.compare()

======================================
name = str("Cyrine Estabillo")
print (name)

age = int(19)
print(age)

lbs = float(110.231)
print(lbs)

mode1 = True
mode2 = False

print(mode1)
print(mode2)


data1 = input("Enter your name: ")
data2 = int(input("Enter your age: "))
data3 = float(input("Enter your weight in lbs: "))
data4 = input("Enter your mood (Happy or Sad): ")
if data4 == "Happy":
    print(f"Hello, {data1}! You are {data2} years old, and weigh {data3} in lbs. You are Happy")
else:
    print(f"Hello, {data1}! You are {data2} years old, and weigh {data3} in lbs. You are Sad.")

=========================================
#include <iostream>
#include <string>

int main() {
    std::string name = "Cyrine Estabillo";
    std::cout << name << std::endl;

    int age = 19;
    std::cout << age << std::endl;

    double lbs = 110.231;
    std::cout << lbs << std::endl;

    bool mode1 = true;
    bool mode2 = false;

    std::cout << std::boolalpha;
    std::cout << mode1 << std::endl;
    std::cout << mode2 << std::endl;

    return 0;
}

======================================
using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        string name = "Cyrine Lo Estabillo";
        Console.WriteLine(name);
        
        int age = 19;
        Console.WriteLine(age);
        
        double digits = 6.9;
        Console.WriteLine(digits);
        
        bool happy = true;
        bool sad = false;
        Console.WriteLine(happy);
        Console.WriteLine(sad);
    }
}
