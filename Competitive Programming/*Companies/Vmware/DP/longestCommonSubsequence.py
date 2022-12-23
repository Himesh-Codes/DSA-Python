"""
Longest Common Subsequence

Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
A = 6, B = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input Sequences
“ABCDGH” and “AEDFHR” is “ADH” of
length 3.


"""
class Solution:
    def longestSubsequence(self, str1, str2):
        