# Loops & Iterators

largest = 0
smallest = 0
llist=[]
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        llist.append(int(num))
    except:
        print('Invalid input')
 
largest=max(llist)
smallest=min(llist)
    
print("Maximum is", largest)
print("Minimum is", smallest)
