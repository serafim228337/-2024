def longest_substring_with_unique_chars(s):
    start = 0
    max_length = 0
    seen = set()
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[i])
        max_length = max(max_length, i - start + 1)

    return max_length


s = "abcabcbb"
result = longest_substring_with_unique_chars(s)
print(result)
