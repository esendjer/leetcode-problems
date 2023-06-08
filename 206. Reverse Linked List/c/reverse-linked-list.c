#include <limits.h>
#include <stdio.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
    };

struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* ch = head;
    struct ListNode* tmpCh = NULL;
    struct ListNode* resNode = NULL;
    while (ch) {
        tmpCh = ch->next;
        ch->next = resNode;
        resNode = ch;
        ch = tmpCh;
    }
    return resNode;
}
