def possibleStringCount(word: str) -> int:
    ans = 1
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            ans += 1

    return ans



res = possibleStringCount("abcd")
print(res)