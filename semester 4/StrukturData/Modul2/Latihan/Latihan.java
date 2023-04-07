import java.util.LinkedList;

public class Latihan {
    public static void main(String[] args) {
        // Membuat objek Hewan pada Linkedlist
        LinkedList<String> hewan = new LinkedList<>();

        // Menambahkan elemen ke Linkedlist
        hewan.add("Sapi");
        hewan.add("Kelinci");
        hewan.add("Kambing");
        hewan.add("Unta");
        hewan.add("Domba");
        hewan.add("Kucing");

        System.out.println("Nama Hewan: " + hewan);
        System.out.println("Hewan yang di hapus : Kelinci, Kambing");
        //hapus index
        LinkedList<String> deleteHewan = new LinkedList<>();
        hewan.remove("Kelinci");
        hewan.remove("Kambing");

        System.out.println("Setelah di hapus : " + hewan);
    }
}