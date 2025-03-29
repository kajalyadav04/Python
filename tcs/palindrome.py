n=int(input(" "))

def palindronfn(n):
    org_num=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10

    if org_num==rev:
        return True
    else:
        return False

if palindronfn(n)==True:
    print("true")
else:
    print("false")









