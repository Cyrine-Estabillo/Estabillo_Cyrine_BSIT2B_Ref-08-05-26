public class Main {
    public static void main(String[]args){
        
        int age = 20;
        double price = 40.55;
        float weight = 85.9f;
        char grade = 'A';
        Boolean isStudent = true;
        String name = "Alice";

        System.out.println("Hello, World!");
        System.out.println("Name: "+name);
        System.out.println("Age: "+age);
        System.out.println("Price: "+price);
        System.out.println("Weight: "+weight);
        System.out.println("Grade: "+grade);
        System.out.println("Is Student? "+isStudent);
    }
}

==================

import java.util.Scanner;
public class Main {
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        
        System.out.println("\nEnter your city: ");
        String userCity = scanner.next();
        System.out.println("You live in: "+userCity);

        scanner.nextLine();
        
        System.out.println("Enter a sentence about yourself");
        String fullSentence = scanner.nextLine();
        System.out.println("You said: "+fullSentence);

        scanner.close();
    }
}

======================

public class Main {
    public static void main(String[] args){
        int a = 69, b = 74;
        double x = 10, y = 3;
        
        System.out.println("a + b = "+(a + b));
        System.out.println("a - b = "+(a - b));
        System.out.println("a * b = "+(a * b));
        System.out.println("a / b = "+(a / b));
        System.out.println("a % b = "+(a % b));
        
        System.out.println("x / y = "+(x / y));

        System.out.println("\na == b: "+(a == b));
        System.out.println("\na != b: "+(a != b));
        System.out.println("\na > b: "+(a > b));
        System.out.println("\na < b: "+(a < b));

        boolean p = true, q = false;
        System.out.println("\np && q: "+(p && q));
        System.out.println("p || q: "+(p || q));
        System.out.println("!p: "+(!p));

        int score = 50;
        score += 10;
        System.out.println("\nscore after += 10: "+score);
        score *= 2;
        System.out.println("score after *= 2: "+score);

        int counter = 5;
        System.out.println("\ncounter ++ (post): " + counter++);
        System.out.println("counter now: " + counter);
        System.out.println("++counter (pre): " + ++counter);
        
    }
}

=================

import java.util.Scanner;
public class Main {
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your exam score: ");
        int score = scanner.nextInt();

        if (score >= 90) {
            System.out.println("Grade: A");
        } else if (score >= 80) {
            System.out.println("Grade: B");
        } else if (score >= 70) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Grade: F");
        }
    }
}
