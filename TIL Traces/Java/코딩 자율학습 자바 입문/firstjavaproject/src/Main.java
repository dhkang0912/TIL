import java.io.IOException;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        int value;
        int i = 1;
        do {
            value = 3*i;
            System.out.println("3 x " + i + " = " + value);
            i++;
        } while (i<=9);
    }
}