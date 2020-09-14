n=int(input("enter a number:"))

assert n>0,"please enter the number greater than 0"
i=0
while i<n:
    i+=1
    if i%10==0:

        continue
    print(i, end=" ")

    if i>100:
        break

print()

for i in range(1,n+1):
    if i%10==0:
        continue
    if i>100:
        break

    print(i, end=" ")


