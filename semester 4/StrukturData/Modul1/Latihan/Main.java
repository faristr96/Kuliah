import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        ArrayList<konsumsi> listkonsumsi = new ArrayList<>();
        konsumsi<makanan, minuman> breakfast = new konsumsi<>();
        konsumsi<makanan, minuman> lunch = new konsumsi<>();

        makanan roti = new makanan();
        roti.setNamaHidangan("Roti Tawar");
        minuman susu = new minuman();
        susu.setNamaHidangan("Susu Sapi");
        breakfast.setKonsumsi(roti, susu);
        listkonsumsi.add(breakfast);
        makanan nasi = new makanan();
        nasi.setNamaHidangan("Nasi Putih");
        minuman air = new minuman();
        air.setNamaHidangan("Air Putih");
        lunch.setKonsumsi(nasi, air);
        listkonsumsi.add(lunch);

        System.out.println("Menu konsumsi");
        for (konsumsi <makanan,minuman>konsumsi : listkonsumsi){
            makanan makanan = konsumsi.getM();
            minuman minuman = konsumsi.getI();

            System.out.println(makanan.disantap());
            System.out.println(minuman.disantap());
        }

        System.out.println(listkonsumsi);
    }
}
