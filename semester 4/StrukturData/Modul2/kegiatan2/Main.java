package kegiatan2;

import Semester4.StrukturData.Modul2.kegiatan2.linkedList;

public class Main {
    public static void main(String[] args) {

        linkedList List = new linkedList();

        //Add nodes to the list
        List.addNode(7);
        List.addNode(1);
        List.addNode(4);
        List.addNode(6);
        List.addNode(2);
        List.addNode(3);

        //Displays the nodes present in the list
        System.out.print("Before : ");
        List.display();

        List.sortList();

        System.out.print("After  : ");
        List.display();
    }

}
