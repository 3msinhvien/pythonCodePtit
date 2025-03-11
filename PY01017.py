def encode_string(s):
    result = ""
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result += str(count) + current_char
            count = 1
            current_char = s[i]
    
    # Handle the last group of characters
    result += str(count) + current_char
    return result

# Read number of test cases
t = int(input())
for _ in range(t):
    s = input()
    print(encode_string(s))