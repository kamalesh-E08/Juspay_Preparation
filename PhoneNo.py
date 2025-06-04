def lexicographically_smallest_string(n, k, s):
    unique_letters = sorted(set(s))

    if k > n:
        return s + unique_letters[0] * (k - n)
    
    s_list = list(s)
    
    for i in range(k - 1, -1, -1):
        for letter in unique_letters:
            if letter > s_list[i]:
                s_list[i] = letter
                return "".join(s_list[:i+1]) + unique_letters[0] * (k - i - 1)
    
    return "".join(s_list)
 
n, k = map(int, input().split())
s = input().strip()
print(lexicographically_smallest_string(n, k, s))

# TC: O(n * m), where m is the number of unique letters in s