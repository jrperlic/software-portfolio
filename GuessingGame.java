import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    public static void main(String[] args) {

        Random rand = new Random();
        Scanner scanner = new Scanner(System.in);

        int randomNumber = rand.nextInt(100) + 1;
        int tries = 0;

        while(true) {
            System.out.println("Enter your guess (1-100): ");

            int playerGuess = scanner.nextInt();
            tries++;

            if(playerGuess == randomNumber) {
                System.out.println("Correct! You win!");
                System.out.println("It took you " + tries + " tries.");
                break;
            }
            else if(randomNumber > playerGuess) {
                System.out.println("Nope! The number is higher. Guess again.");
            }
            else {
                System.out.println("Nope! The number is lower. Guess again.");
            }
        }

        scanner.close();
        
    }
}
