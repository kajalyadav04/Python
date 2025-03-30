def removeVowels( self, s) :
        # code here
    v=0
    c=0
    result=[]
    for ch in s:
        if ch in "aeiouAEIOU":
            
            continue
        else:
            result.append(ch)
    return "".join(result)
s = 'kay'
res = removeVowels(s)
print(res)
