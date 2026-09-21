a = input()
count= 1 
l = len(a)
ans = ""
for i in range(l-1):
    if a[i] == a[i+1]:
        count = count+ 1
    else :
        ans = ans + a[i] + str(count)
        count=1
ans = ans + a[l-1] + str(count)     
print(ans)
