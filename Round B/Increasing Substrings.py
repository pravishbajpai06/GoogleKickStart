def sol():
    n=int(input())
    a=input()
    l=[1]
    c=1
    for i in range(len(a)-1):
        if ord(a[i])<ord(a[i+1]):
            c+=1
            l.append(c)
        else:
            c=1
            l.append(c)
    return " ".join(map(str, l))   
for case in range(1,int(input())+1):
    print (f"Case #{case}:", sol())      
