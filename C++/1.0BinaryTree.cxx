#include<iostream>

struct Node{
    int val;
    Node* right;
    Node* left;
    Node(int data){
        val = data;
        right = nullptr;
        left = nullptr;
    }

};

int main(){
//  10 5 11 4 2 
    Node* root = new Node(10);
    Node* Node5 = new Node(5);
    Node* Node11 = new Node(11);
    Node* Node4 = new Node(4);
    Node* Node2 = new Node(2);

    root->left =Node5;
    root->right =Node11;
    Node5->left = Node4;
    Node4->left = Node2; 


    }