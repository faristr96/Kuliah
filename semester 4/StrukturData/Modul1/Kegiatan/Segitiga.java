
import java.util.InputMismatchException;
import java.util.Scanner;


public class Segitiga <T extends Number>{
    public T Alas;
    public T Tinggi;

    public Segitiga(T alas, T tinggi){
        this.Alas = alas;
        this.Tinggi = tinggi;
    }
}

class rumus{
    public int getResultAsInt(Segitiga Segitiga){
        return (int) ( 0.5 * Segitiga.Alas.intValue()*Segitiga.Tinggi.intValue());
    }
    public double getResultAsDouble (Segitiga Segitiga){
        return (0.5 * Segitiga.Alas.doubleValue()*Segitiga.Tinggi.doubleValue());
    }

}

class Main {
    public static void main(String[] args) {
        rumus R = new rumus();
        Scanner input = new Scanner(System.in);
        int alas, tinggi;
        double ALAS, TINGGI;
        System.out.print("Pilihan Untuk Hasil Luas Segitiga\n");
        System.out.println("1. Hasil dalam bentuk Integer");
        System.out.println("2. Hasil dalam bentuk Double");
        System.out.print("\n");

        try {
            System.out.print("Pilihan 1 atau 2 : ");
            int pilih = input.nextInt();
            switch (pilih) {
                case 1:
                    System.out.print("Luas Segitiga dalam bentuk Integer\n");
                    System.out.print("masukan alas segitiga   : ");
                    alas = input.nextInt();
                    System.out.print("masukan tinggi segitiga : ");
                    tinggi = input.nextInt();

                    Segitiga<Integer> integerSegitiga = new Segitiga<>(alas, tinggi);
                    System.out.print("Hasil Dari Luas Segitiga : " + R.getResultAsInt(integerSegitiga));
                    break;
                case 2:
                    System.out.print("Luas Segitiga dalam bentuk Double\n");
                    System.out.print("masukan alas segitiga   : ");
                    ALAS = input.nextDouble();
                    System.out.print("masukan tinggi segitiga : ");
                    TINGGI = input.nextDouble();

                    Segitiga<Double> DoubleSegitiga = new Segitiga<>(ALAS, TINGGI);
                    System.out.print("Hasil Dari Luas Segitiga : " + R.getResultAsDouble(DoubleSegitiga));
                    break;
            }

        } catch (InputMismatchException e){
            System.err.println("masukan angka");
        }
    }
}

