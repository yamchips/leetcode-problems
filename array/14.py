def longestCommonPrefix(strs: list[str]) -> str:
    sorted_strs = sorted(strs)
    first = sorted_strs[0]
    last = sorted_strs[-1]
    len1 = len(first)
    len2 = len(last)
    result = []
    for i in range(min(len1, len2)):
        if first[i] == last[i]:
            result.append(first[i])
        else:
            break
    return "".join(result)

if __name__=="__main__":
    print(longestCommonPrefix(["flower", "flow", "flight"])) # "fl"
    print(longestCommonPrefix(["flower", "flow", "fxight"])) # "f"
    print(longestCommonPrefix(["flower", "flow", "tight"])) # ""

