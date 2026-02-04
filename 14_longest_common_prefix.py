'''14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
	• 1 <= strs.length <= 200
	• 0 <= strs[i].length <= 200
	• strs[i] consists of only lowercase English letters if it is non-empty.
 

From <https://leetcode.com/problems/longest-common-prefix/description/> 
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        cmn=strs[0]
        for i in strs[1:]:
            while not i.startswith(cmn):
                cmn=cmn[:-1]
                if cmn=="":
                    return ""
        return cmn