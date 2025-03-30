def checkString(s):
    # write your code here
    v, c=0, 0
    s=s.lower()
    for ch in s:
        if ch.isalpha():
            if ch in "aeiou":
                v+=1
            else:
                c+=1
                
    if v>c:
        print("Yes")
        
    elif v<c:
        print("No")
    else:
        print("Same")