#include <stdio.h>
#include <stdlib.h>

struct Values {
    int value;
    struct Values* next;
    struct Values* head;
};

struct Values* newValue(struct Values* values, int value) {
    struct Values* newValue = malloc(sizeof(struct Values));

    if (values) {
        values->next = newValue;
        newValue->head = values->head;
    } else {
        newValue->head = newValue;
    }

    newValue->value = value;
    newValue->next = NULL;
    return newValue;
}

struct List {
    int level;
    struct Values* values;
    struct List* next;
};
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* averageOfLevels(struct TreeNode* root, int* returnSize) {
    int depth = 0;

    struct List* list = malloc(sizeof(struct List));
    list->level = 0;
    list->values = NULL;
    list->next = NULL;

    void iter(struct TreeNode* node, struct List* list, int dep) {
        if (!node) {
            if (depth < dep) depth = dep;
            return;
        }
        list->values = newValue(list->values, node->val);
        list->level = dep;

        if (!(list->next)) {
            list->next = malloc(sizeof(struct List));
            list->next->values = NULL;
            list->next->next = NULL;
        }
        iter(node->left, list->next, dep + 1);
        iter(node->right, list->next, dep + 1);
    }
    iter(root, list, 0);

    double* res = malloc(sizeof(double) * depth);

    while (list && list->values) {
        struct Values* values = list->values->head;
        double ava = 0;
        int count = 0;
        long total = 0;
        while (values) {
            count++;
            total += values->value;
            values = values->next;
        }
        ava = (double)total / (double)count;
        res[list->level] = ava;
        list = list->next;
    }
    *returnSize = depth;
    return res;
}