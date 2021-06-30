"""
We have a sliding window problem here:
With this logic we check string letter by letter, going through every letter one by one.

Logic/Pseudocode:
for every leter in main_string:
    check if letter in current_string:
        if yes:
        max_length = len(current_string) if len(current_string) > maxlength
        
        # break current string at position of pos(current letter) + 1 
        # and start it new with rest of letter
        # e.g Current_string = 'abc'
        # letter = 'b'
        # new current_string = 'c'
        
        new_start = current_string.find(letter) + 1
        current_string = current_string[new_start:]
    # appending each letter in current_string
    current_string += letter
    
    # Check for max_length one last time for last letter
max_length = len(current_string) if len(current_string) > maxlength
return max_length

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        
        if len(s) == 0 :
            return 0
        
        curr_str = ""
        max_length = 0

        for letter in s:
            if letter in curr_str:

                if len(curr_str) > max_length:
                    max_length = len(curr_str)
                new_start = curr_str.find(letter) + 1
                curr_str = curr_str[new_start:]
                # print('Inside:', curr_str)

            curr_str += letter
            # print('Outside:', curr_str)
        
        if len(curr_str) > max_length:
            max_length = len(curr_str)

        return max_length
