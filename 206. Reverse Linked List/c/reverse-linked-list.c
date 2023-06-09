#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
    };

struct ListNode*reverseList(struct ListNode*head){
    struct ListNode *ch = head;
    struct ListNode *tmpCh = NULL;
    struct ListNode *resNode = NULL;
    while (ch) {
        tmpCh = ch->next;
        ch->next = resNode;
        resNode = ch;
        ch = tmpCh;
    }
    return resNode;
}

struct ListNode*createLl(int arr[], int arrSize) {
    struct ListNode *fl = NULL;
    struct ListNode *head = NULL;
    fl = malloc(sizeof(struct ListNode));
    head = fl;
    for (int j = 0; j < arrSize; j++) {
        fl->val = arr[j];
        if (j != (arrSize - 1)) {
            struct ListNode *next = NULL;
            next = malloc(sizeof(struct ListNode));
            fl->next = next;
            fl = fl->next;
        }
    }
    return head;
}

int main() {
    int fCase[] = {1,2,3,4,5};
    int fRes[] = {5,4,3,2,1};
    struct ListNode*FLl = createLl(fCase, 5);

    int sCase[] = {1,2,3,4,5,6};
    int sRes[] = {6,5,4,3,2,1};
    struct ListNode*SLl = createLl(sCase, 6);
    
    struct ListNode *firstRevLList = reverseList(FLl);
    struct ListNode *secondRevLList = reverseList(SLl);

    int f = 0;
    while (firstRevLList && f <= 5) {
        assert(firstRevLList->val == fRes[f]);
        firstRevLList = firstRevLList->next;
        f++;
    }
    printf("First case is OK\n");
    f = 0;
    while (secondRevLList && f <= 6) {
        assert(secondRevLList->val == sRes[f]);
        secondRevLList = secondRevLList->next;
        f++;
    }
    printf("Second case is OK\n");
    return 0;
}