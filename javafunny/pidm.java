import java.util.Scanner;
import java.util.Random;

public class pidm {
    public static void main(String[] args) {
        int plhth = 20;
        int slamhet = 15;
        System.out.println("You encounter slime with " + slamhet + "hp, you have " + plhth + "hp");
        while (slamhet > -1) {
            Random slatkon = new Random();
            int wilslatk = slatkon.nextInt(2);
            System.out.println("do you attack(1), heal(2), or run(3)");
            Scanner scamer = new Scanner(System.in);
            int choice = scamer.nextInt();
            if (choice == 1) {
                Random rand = new Random();
                int mison = rand.nextInt(2);
                if (mison == 1) {
                    System.out.println("You missed! The health of the slime remains at " + slamhet + "hp, and you have "
                            + plhth + "hp");
                } else {
                    Random damage = new Random();
                    int dam = damage.nextInt(3);
                    dam += 1;
                    slamhet -= dam;
                    System.out
                            .println("You dealt " + dam + " damage, the slime has " + slamhet + "hp left adn you have  "
                                    + plhth + "hp left");
                }
            } else if (choice == 2) {
                Random healamount = new Random();
                int healrat = healamount.nextInt(3);
                healrat += 1;
                int hamtot = plhth + healrat;
                if (hamtot > 20) {
                    System.out.println("You cannot heal while your health is this high");
                } else {
                    plhth += healrat;
                    System.out.println("You healed " + healrat + " health, you have " + plhth + "hp remaining");
                }
            } else {
                System.out.println("bro really ran");
                System.exit(0);
            }
            if (slamhet == 0) {
                System.out.println("the slime is die, you win!");
                System.exit(0);
            }
            if (wilslatk == 1) {
                Random aldam = new Random();
                int slamdam = aldam.nextInt(2);
                slamdam += 1;
                plhth -= slamdam;
                System.out.println("The slime has attacked you! You have " + plhth + "hp left");
            }
            if (plhth == 0) {
                System.out.println("The you is die");
                System.exit(0);
            }
        }
    }

}
