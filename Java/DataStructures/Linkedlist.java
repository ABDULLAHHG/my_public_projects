class Linkedlist{
    Linkedlist(){
        head = null;
    }
    Node head;
    // Create a Node class 
    class Node{
        int val; 
        Node next;
        Node(int data){
            val = data;
            next = null;
        }
    }
    // Create an append method 
    void append(int data){
        if (head == null){
            head = new Node(data);
        }
        else {
            Node current;
            for(current = head; current.next != null;current = current.next){};
            current.next = new Node(data);
        }
    }

    // Remove Method
    void Remove(int data){

            if (head.val == data){
                head = head.next;
            }
            else{
                Node current;
                Node placeHolder;
                for(current = head; current.next.val != data;current = current.next){};
                placeHolder = current.next;
                if (placeHolder.next == null){
                    current.next = null;
                }
                else{
                    current.next = placeHolder.next;
                }
            }
    }

    // Change head 
    void appendOnHead(int data){
        Node placeHolder = head;
        this.head = new Node(data);
        head.next = placeHolder;
    }

    // Print LinkedList 
    void print(){
            Node current;
            for(current = head; current != null;current = current.next){
                System.out.println(current.val);
            };
    }
    // Main function 
    public static void main(String[] args){
        Linkedlist L1 = new Linkedlist();
        L1.append(10);
        L1.append(20);
        L1.append(30);
        L1.print();

        System.out.println();
        L1.appendOnHead(40);
        // L1.Remove(10);
        // L1.Remove(20);
        L1.append(70);
        L1.print();

    }
}