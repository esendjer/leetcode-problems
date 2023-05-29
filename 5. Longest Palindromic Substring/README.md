# 5. Longest Palindromic Substring

[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

The current way that was the problem solved here is pretty stupid and needs to rethought.

## Hints/tips:
* How can we reuse a previously computed palindrome to compute a larger palindrome?
* If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
* Complexity based hint: If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.


