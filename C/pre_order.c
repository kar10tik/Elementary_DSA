//Pre-order Traversal Complexity O(n)
#include <stdio.h>
#include <stdlib.h>

struct bin_node
{
    int data;
    struct bin_node *left;
    struct bin_node *right;
};

void preorder(struct bin_node *root)
{
    if (root)
    {
        printf("%d\n", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void insertnode(struct bin_node *root, int data)
{
    
}

int main()
{
    printf("Pre-order traversal of binary tree");

    return 0;
}
