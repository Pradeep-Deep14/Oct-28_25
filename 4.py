nums=[1,2,3,4,5]
for num in nums:
    if num==3:
        print("loop breaked")
        break
else:
        print("loop ended")

#Output:
# loop breaked  
#Explanation:
# The loop iterates through the list nums.
# When num equals 3, the break statement is executed, exiting the loop immediately.
# Since the loop is exited via break, the else block is not executed.