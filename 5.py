import itertools
nums=[1,2,3,4]
pairs=itertools.permutations(nums,2)
lst=list(pairs)
print(lst[0],lst[-1])

#Output:
# (1, 2) (4, 3) 
#Explanation:
# The code generates all possible 2-element permutations of the list [1, 2, 3, 4].
# The first permutation is (1, 2) and the last one is (4, 3).
