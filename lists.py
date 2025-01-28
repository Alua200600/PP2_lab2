arr = ["apple", "banana", "cherry", "apple", "cherry"]
print(arr)
print(len(arr))

list1 = ["abc", 34, True, 40, "male"]
print(list1)#A list can contain different data types

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)





