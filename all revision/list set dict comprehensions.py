string="hellohh"
str2="hello1hhhhhhhhhhhhhhhh"



result=[i for i in string if i in str2]
print(result)

list1=[[1,2,3],[2,3,4],[1,23,45]]
list2=[[1,2,3],[2,3,4],[1,23,45]]
z=zip(list1,list2)
sum1=[]
sum2=[]


for i in range(3):
    sum=0
    for j in range(3):
        sum+=list1[i][j]
    print(f"sum of {i+1} row is {sum}")

