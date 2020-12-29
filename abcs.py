data = input()
nums = [int(i) for i in data.split(" ")]

nums.sort()
a = nums[0]
b = nums[1]
c = nums[-1] - a - b

print(a, b, c)