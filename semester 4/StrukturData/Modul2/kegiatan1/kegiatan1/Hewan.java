package kegiatan1;

import java.util.ArrayList;

public class Hewan {
    public static void main(String[] args) {
//        1 dan 2
        ArrayList<String> hewan = new ArrayList<>();
        hewan.add("Angsa");
        hewan.add("Bebek");
        hewan.add("Cicak");
        hewan.add("Domba");
        hewan.add("Elang");
        hewan.add("Gajah");

        //1 penambahan
        hewan.add("Badak");
        hewan.add("Bebek");

        // 1
        ArrayList<String> kosong = new ArrayList<>();
        System.out.println("Hewan : " + hewan);

        // 2
            int jumlahBebek = 0;
            int i = 0;
            for (String s : hewan) {
                if (s.equals("Bebek")) {
                    jumlahBebek++;
                    kosong.add( i + "");
                }
                i++;
            }
        System.out.println("jumlah Bebek ada : " + jumlahBebek);
        System.out.println("Posisi Bebek : " + kosong);

        //3
        hewan.remove(1);
        System.out.println("\n"+hewan);

        //4
        System.out.println("\nindex ke-0 : "+hewan.get(0)+"\n"+"index ke-2 : "+hewan.get(2));
        hewan.remove(0);

        //5
        hewan.set(0 , "ular");
        hewan.add(2, "itik");
        System.out.println("\n"+hewan);

        //6
        hewan.subList(2,5).clear();
        System.out.println("\n"+hewan);

        //7
        String element1 = hewan.get(0);
        String element2 = hewan.get(hewan.size()-1  );
        System.out.println("\nhewan Pertama : "+element1+"\nhewan Terakhir : "+element2);

        //8
        System.out.println("\nSize : "+hewan.size());

        //9
        String Badak = "Badak";
        System.out.println("\nIndex Badak : "+hewan.indexOf(Badak));

    }


}