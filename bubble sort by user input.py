#Bubble Sort
def bubble_sort(alist):
    for j in range(len(alist)):
        for i in range (0,len(list)-1):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                
                i=i+1
list=[]
size=int(input("No. of element in list:"));
for k in range (0,size):
    n=int(input("Enter an element:"));
    list.append(n)
print("List=",list)
bubble_sort(list)
print("\nsorted",list)

