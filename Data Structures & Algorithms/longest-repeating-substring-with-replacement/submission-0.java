

class Solution {
    public int characterReplacement(String s, int k) {
        // Create a HashMap to store character frequencies
        HashMap<Character, Integer> charCount = new HashMap<>();
        int maxLength = 0;  // To store the maximum length of the valid substring
        int maxFreq = 0;    // To track the most frequent character count in the current window
        int left = 0;       // Left boundary of the window

        // Sliding window approach
        for (int right = 0; right < s.length(); right++) {
            // Get the current character and update its frequency in the map
            char currentChar = s.charAt(right);
            charCount.put(currentChar, charCount.getOrDefault(currentChar, 0) + 1);
            
            // Update the max frequency of any character in the current window
            maxFreq = Math.max(maxFreq, charCount.get(currentChar));

            // If the number of characters to change (window size - maxFreq) exceeds k, shrink the window
            if ((right - left + 1) - maxFreq > k) {
                // Remove the leftmost character from the window and reduce its frequency
                char leftChar = s.charAt(left);
                charCount.put(leftChar, charCount.get(leftChar) - 1);
                left++;  // Move the left boundary of the window to the right
            }

            // Update the maximum length of the valid substring
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}

