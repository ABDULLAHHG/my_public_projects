#include<iostream>

struct Node{
    int val ;
    Node* next;
    Node(int data){
        val = data;
        next = nullptr;
    }
};

class LinkedList{

private:
    Node* head ;

public:
int length;
LinkedList(){
        head = nullptr;
        length = 0;
    }
    void append(int data){
        if (head == nullptr){
            head = new Node(data);
            length = 1;
        }
        else{
            Node* current = head;
            while (current->next != nullptr){
                current = current->next;
            }
            current->next = new Node(data);
            length +=1;
        }


    }
    void print_linked_list_values(){
        Node* current = head;
        while (current != nullptr){
            std::cout<<current->val<<"   ";
            current = current->next;
        }
    }

    int* ToArray(){
        Node* current = head;
        int* array = new int[length];
        for (int i = 0;i<length;i++){
            array[i] = current->val;
            current = current->next;
        }
        return array;
    }
};

int main(){
    LinkedList LL;
    LL.append(5);
    LL.append(6);
    LL.print_linked_list_values();
    int* arrayptr = LL.ToArray();

    for (int i = 0; i<LL.length;i++){
        std::cout<<arrayptr[i]<<std::endl;
    }

}