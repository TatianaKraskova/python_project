my_set = {"January", "February", "March"}
for element in my_set:
    print(element)

my_set.add("April") #sets are not ordered, no duplication
print(my_set)

my_set.remove("January")
print(my_set)

my_list = ["Monday", "Tuesday", "Wednesday", "Monday"]
print(my_list)
my_list.remove("Monday") # remove just the first element
print(my_list)