def lengthOfLongestSubstring(s):
    len_s = len(s)
    sub_string = {}
    
    for i in range(len_s):
        for j in range(i,len_s):
            a = s[i:j+1]
            if len(set(a)) == len(a):
                a_len = len(a)
                sub_string[a] = a_len
    max_value = max(sub_string.values())
    max_key = [k for k,v in sub_string.items() if v == max_value]
    return max_key

NO_OF_CHARS = 256

def longestUniqueSubsttr(string):
    n = len(string)
    cur_len = 1        # To store the lenght of current substring
    max_len = 1        # To store the result
    prev_index = 0    # To store the previous index
    i = 0
 
    # Initialize the visited array as -1, -1 is used to indicate
    # that character has not been visited yet.
    visited = [-1] * NO_OF_CHARS
 
    # Mark first character as visited by storing the index of
    # first character in visited array.
    visited[ord(string[0])] = 0
 
    # Start from the second character. First character is already
    # processed (cur_len and max_len are initialized as 1, and
    # visited[str[0]] is set
    for i in range(1,n):
        prev_index = visited[ord(string[i])]

        print("prev_index value is {}" .format(prev_index))
 
        # If the currentt character is not present in the already
        # processed substring or it is not part of the current NRCS,
        # then do cur_len++
        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len+=1
            print ("if cur_len is {}" .format(cur_len))
 
        # If the current character is present in currently considered
        # NRCS, then update NRCS to start from the next character of
        # previous instance.
        else:
            # Also, when we are changing the NRCS, we should also
            # check whether length of the previous NRCS was greater
            # than max_len or not.
            if cur_len > max_len:
                max_len = cur_len
 
            cur_len = i - prev_index
            print("else i value is {}" .format(i))
            print ("else cur_len is {}" .format(cur_len))
            print ("else prev_index is {}" .format(prev_index))
 
        # update the index of current character
        visited[ord(string[i])] = i
 
    # Compare the length of last NRCS with max_len and update
    # max_len if needed
    if cur_len > max_len:
        max_len = cur_len
 
    return max_len

s = longestUniqueSubsttr("abbcd")
print (s)





