#include <stdio.h>
#include <stdlib.h>

struct IntStack {
    int data;
    struct IntStack* next;
};

void pushInt(struct IntStack** top, int data) {
    struct IntStack* newTop = (struct IntStack*)malloc(sizeof(struct IntStack));
    newTop->data = data;
    if ((*top) == NULL) {
        newTop->next = NULL;
    } else {
        newTop->next = *top;
    }
    *top = newTop;
}

int popInt(struct IntStack** top) {
    struct IntStack* tempTop = *top;
    int data = (*top)->data;
    *top = (*top)->next;
    free(tempTop);
    return data;
}

struct DynamicStack {
    struct TreeNode* data;
    struct DynamicStack* next;
};

void push(struct DynamicStack** top, struct TreeNode* data) {
    struct DynamicStack* newTop = malloc(sizeof(struct DynamicStack));
    newTop->data = data;
    if ((*top) == NULL) {
        newTop->next = NULL;
    } else {
        newTop->next = *top;
    }
    *top = newTop;

}


struct TreeNode* pop(struct DynamicStack** top) {
    struct DynamicStack* tempTop = *top;
    struct TreeNode* data = (*top)->data;
    *top = (*top)->next;
    free(tempTop);

    return data;
}

int maxDepth(struct TreeNode* root){
    int depthT = 0;
    int *max = &depthT;
    struct DynamicStack* top = NULL;

    struct IntStack* topDepth = NULL;
    push(&top, root);
    pushInt(&topDepth, 0);

    while (top) {
        struct TreeNode* node = pop(&top);
        int depth = popInt(&topDepth);
        if (!node) {
            if (*max < depth) *max = depth;
        } else {
            push(&top, node->right);
            pushInt(&topDepth, depth + 1);
            push(&top, node->left);
            pushInt(&topDepth, depth + 1);
        }
    }

    return *max;
}

// int recur(struct TreeNode* node, int depth, int *max) {
//     if (node == NULL) {
//         if (*max < depth) {
//             *max = depth;
//         }
//         return;
//     }
//     recur(node->left, depth + 1, max);
//     recur(node->right, depth + 1, max);

//     return;
// }
