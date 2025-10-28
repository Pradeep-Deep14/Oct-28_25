def my_dict():
    d={"name":"Bob","age":30}
    return len(set(d))

print(my_dict())

#Output:2
#Explanation:
# The dictionary d has two unique keys: "name" and "age".
# Therefore, the length of the set of keys is 2.
# The output of the code is 2.
