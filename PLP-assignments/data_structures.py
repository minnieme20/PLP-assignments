my_list = []
print("This is my empty list: ", my_list)
my_list.append(20)
my_list.append(30)
my_list.append(10)
my_list.append(40)
print("This is my populated list",my_list)

my_list.insert(1, 15)
print("I have added another element at index one of the list: ",my_list)

another_list = [50, 60, 70]
my_list.extend(another_list)
print("I have combined the 2 list into: ",my_list)

del my_list[-1]
print("I have deleted the last element from the list:",my_list)

my_list.sort()
print("This list is sorted in ascending order",my_list)

print("The number 30 on my list is in index: ", my_list.index(30))
