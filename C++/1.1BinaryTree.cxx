#include <iostream>

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

struct Node* root = nullptr;

void addNode(Node* startNode , Node* newNode){
    if (root == nullptr){
        root = newNode;
        return;
    }

    if(newNode->val > startNode->val){
        if(startNode->right == nullptr){
            startNode->right = newNode;
            return;
        }
        addNode(startNode->right,newNode);
    }

      if(newNode->val < startNode->val){
        if(startNode->left == nullptr){
            startNode->left = newNode;
            return;
        }
        addNode(startNode->left,newNode);
    }

}


void buildTree(int* array,int size){
    for (int i = 0;i<size;i++){
        addNode(root , new Node(array[i]));
    }
}


void printInOrder(Node* Tree){
    if (Tree == nullptr){
        return;
    }
    printInOrder(Tree->left);
    std::cout<<Tree->val<<'\t';
    printInOrder(Tree->right);
}

void printPreOrder(Node* Tree){
    if (Tree == nullptr){
        return;
    }
    std::cout<<Tree->val<<'\t';
    printPreOrder(Tree->left);
    printPreOrder(Tree->right);
}

void printPostOrder(Node* Tree){
    if (Tree == nullptr){
        return;
    }
    printPostOrder(Tree->left);
    printPostOrder(Tree->right);
    std::cout<<Tree->val<<'\t';

}

void clear(Node* Tree){
    if (Tree == nullptr){
        return;
    }
    clear(Tree->left);
    clear(Tree->right);
    std::cout<<"Node deleted "<<Tree->val<<std::endl;
    delete Tree;

}

int main(){


buildTree(new int[]{2,3,4,5,1,6,7,8,10,19},10);

printInOrder(root);
std::cout<<std::endl;
printPreOrder(root);
std::cout<<std::endl;
printPostOrder(root);
std::cout<<std::endl;
clear(root);

}