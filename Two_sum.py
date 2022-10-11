# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def add(num,target):

    for i in range(len(num)-1):
        print(i,end="")
        for j in range(i+1,len(num)):
            print(j,end="")
            if num[i]+num[j]==target:
                return [i,j]
    return []

num = [2,3,4,67]
target =7
print(add(num,target))#[1,2]
