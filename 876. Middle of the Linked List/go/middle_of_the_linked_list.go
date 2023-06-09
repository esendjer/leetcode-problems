/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 
 func middleNode(head *ListNode) *ListNode {
    chs := head
    chf := head
    for chf != nil && chf.Next != nil {
        chf = chf.Next.Next
        chs = chs.Next
    }
    return chs
}