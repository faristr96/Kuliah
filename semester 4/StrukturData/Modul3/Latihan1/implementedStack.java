public class implementedStack {
    private int totalSize;
    private String[] array;
    private int top;

    public implementedStack (int setSizeData){
        totalSize = setSizeData;
        array = new String[totalSize];
        top = -1;
    }
    public void push (String data){
        array[++top] = data ;
    }
    public String pop(){
        return array[top--];
    }
    public String peek(){
        return array[top];
    }
    public boolean isEmpty(){
        return (top ==-1);

    }
    public boolean isFull(){
        return (top == totalSize -1);
    }

    public static void main(String[] args) {
        implementedStack implementedStack = new implementedStack(10);
        implementedStack.push("Aku");
        implementedStack.push("Anak");
        implementedStack.push("Indonesia");
        System.out.println("Peek\t: "+implementedStack.peek());
        System.out.println("Poll\t: "+implementedStack.pop());
        System.out.println("List\t: ");
        int data=1;
        while (!implementedStack.isEmpty()){
            System.out.println("Data ke "+ data+"\t: "+ implementedStack.pop());
            data++;
        }

    }

}