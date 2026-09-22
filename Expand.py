a = input()
l = len(a)
ans = ""
for i in range(0,l,2):
    ans = ans + (a[i] * int(a[i+1]))
print(ans)   
