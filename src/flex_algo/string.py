def length_of_longest_substring(s):
    seen = {}
    left = 0
    longest = 0

    for right in range(len(s)):
        current_char = s[right]
        prev_seen_pos = seen.get(current_char)

        if prev_seen_pos is not None and prev_seen_pos >= left:
            left = prev_seen_pos + 1

        seen[current_char] = right
        longest = max(longest, right - left + 1)

    return longest


if __name__ == '__main__':
    ss = 'abcabcbb'
    longest = length_of_longest_substring(ss)
    print(longest)


