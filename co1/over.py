list=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    ele=int(input("values"))
    list.append(ele)
print(list)
for i in range(0,n):
     if list[i]>100:
         list[i]="over"
print(list)
