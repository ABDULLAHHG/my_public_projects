#include <iostream> 

struct Node
{
    char val;
    Node* next;
    Node(char data){
        val = data;
        next = nullptr;

    }
};

class LinkedList{


public:
Node* head;

    LinkedList(){
        head = nullptr;



    }
    void append(char data){
        if(head == nullptr){
            Node* new_node = new Node(data);
            head = new_node;

        }

        else{
        Node* current = head;
        while (current->next != nullptr){
            current = current->next;

        }
        Node* new_node = new Node(data);
        current->next = new_node;
        }}

    void print_linked_list_values(){
        Node* current = head;
        while(current != nullptr){
            std::cout<<current->val;
            current = current->next;


        }


    }


};



int main(){
LinkedList list ;
list.append('A');
list.append('B');
list.append('D');
list.append('U');
list.append('L');
list.append('L');
list.append('A');
list.append('H');

list.print_linked_list_values();
std::cout<<"\n\n\n";
return 0;
}
