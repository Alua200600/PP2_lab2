thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)


