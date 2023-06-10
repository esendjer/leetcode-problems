#include <stdio.h>
#include <stdlib.h>
// #include <assert.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

bool hasCycle(struct ListNode *head) {
    struct ListNode*fast = head;
    struct ListNode*slow = head;
    while (fast && fast->next) {
        if (slow == fast->next || slow->next == fast->next->next) {
            return 0;
        }
        fast = fast->next->next;
        slow = slow->next;
    }
    return 1;
}