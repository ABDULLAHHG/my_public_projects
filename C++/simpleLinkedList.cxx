#include<iostream>

using namespace std;
struct Node{
    
	char val;
	Node* next  ;
	Node(char value){
			val = value ;
			next = nullptr;
		}
	
};

void print_linked_list_values(struct Node& head){
	   Node* current = &head;
	while (current != nullptr){
		cout <<current->val<<endl;
		current = current->next;
	}
}

int main()
{
     Node* A = new Node('A');
     Node* B = new Node('B');
     Node* C = new Node('C');
    
    A->next=B;
    B->next=C;
   print_linked_list_values(*A);
   
   delete A;
   delete B;
   delete C;
    
    return 0;
}
