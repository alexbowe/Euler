with open('nums.txt', 'r') as f:
    nums = map(int, f.readlines())

print sum(nums)
