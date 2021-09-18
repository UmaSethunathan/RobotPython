# creating an empty list
lst = []
# number of elemetns as input
n = input("Enter number of elements : ").lower().strip()
items = n.split(",")
# iterating till the range
for i in items:
    ele = i
    lst.append(ele)  # adding the element
print(lst)
# using join() +  split() to
# perform removal
test_list = "".join(lst).split()
# Printing modified list
print("Modified list is : " + ",".join(sorted(list(set(test_list)))))
test_list.sort()
test_list.reverse()
print("Reversed list is: " + str(test_list))