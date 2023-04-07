import java.util.Stack;
public class ExampleStack {
    public static void main(String[] args) throws Exception {


        Stack<String> st = new Stack<>();
        st.push("Aku");
        st.push("Anak");
        st.push("Indonesia");

        System.out.println("Peek 1\t: "+ st.peek());
        st.push("Raya");
        System.out.println("Pop\t: "+st.pop());
        st.push("!");

        int count = st.search("Aku");

        while (count !=-1 && count >1){
            st.pop();
            count--;
        }
        System.out.println(st.peek()+" Pada Index Ke\t: "+ count);
        System.out.println(st.empty());
    }
}

