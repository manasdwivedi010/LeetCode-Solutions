import java.util.HashSet;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        // HashSet to store unique characters in the current window
        HashSet<Character> set = new HashSet<>();
        
        int left = 0;   // left pointer of the sliding window
        int maxLength = 0;
        
        // Iterate with right pointer
        for (int right = 0; right < s.length(); right++) {
            // If duplicate character found, shrink window from left
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            
            // Add current character to the set
            set.add(s.charAt(right));
            
            // Update max length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}