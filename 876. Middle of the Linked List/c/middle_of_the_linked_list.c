#include <stdio.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* middleNode(struct ListNode* head){
    struct ListNode*chf = head;
    struct ListNode*chs = head;
    while (chf && chf->next) {
        chf = chf->next->next;
        chs = chs->next;
    }
    return chs;
}

