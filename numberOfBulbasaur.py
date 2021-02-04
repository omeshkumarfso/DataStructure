a1 = input()
num1 = []
B,u,l,b,a,s,r = 0,0,0,0,0,0,0
for i in range(len(a1)):
    if 'B' == a1[i]:
        B = B+1
    elif 'u' == a1[i]:
        u = u+1
    elif 'l' == a1[i]:
        l = l+1
    elif 'b' == a1[i]:
        b = b+1
    elif 'a' == a1[i]:
        a = a+1
    elif 's' == a1[i]:
        s = s+1
    elif 'r' == a1[i]:
        r = r+1

if u%2==1:
    u = u-1
if a%2==1:
    a = a-1

if(u%2==0 and a%2==0):
    num1.append(B)
    num1.append(int(u/2))
    num1.append(l)
    num1.append(b)
    num1.append(int(a/2))
    num1.append(s)
    num1.append(r)
    num1.sort()
    print(num1[0])
else:
    print(0)