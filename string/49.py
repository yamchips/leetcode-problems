from collections import defaultdict

# O(n^2)
def groupAnagrams(strs:list[str]) -> list[list[str]]:
    def isAnagram(str1:str, str2:str)->bool:
        if len(str1) != len(str2): return False
        chars = defaultdict(int)
        for char in str1:
            chars[char] += 1
        for char in str2:
            if chars[char] == 0:
                return False
            else:
                chars[char] -= 1
        charsArr = sorted(chars.items(), key=lambda x : x[1], reverse=False)
        if int(charsArr[0][1]) > 0: return False
        return True
    def createDict(str1:str) -> defaultdict:
        chars = defaultdict(int)
        for char in str1:
            chars[char] += 1
        return chars
    def compareDict(dict1:defaultdict, dict2:defaultdict) -> bool:
        if len(dict1) != len(dict2): return False
        arr1 = sorted(dict1.items(), key= lambda x : x[0])
        arr2 = sorted(dict2.items(), key= lambda x : x[0])
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True
    result = []
    for i in range(len(strs)):
        d = createDict(strs[i])
        flag = False
        for item in result:
            if compareDict(item[0], d):
                item.append(strs[i])
                flag = True
                break
        if flag: continue        
        arr = [d, strs[i]]
        result.append(arr)
    for item in result:
        item.pop(0)
    return result

def groupAnagrams(strs:list[str]) -> list[list[str]]:
    def createDict(str1:str) -> defaultdict:
        chars = defaultdict(int)
        for char in str1:
            chars[char] += 1
        return chars
    def tupleDict(d: defaultdict)-> tuple:
        return tuple(sorted(d.items()))
    
    seen = {}
    for word in strs:
        d = createDict(word)
        key = tupleDict(d)
        if key in seen:
            seen[key].append(word)
        else:
            seen[key] = [word]
    return list(seen.values())
        
def groupAnagrams(strs:list[str]) -> list[list[str]]:
    result = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        result[tuple(count)].append(word)
    return list(result.values())



if __name__=='__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(groupAnagrams(['']))