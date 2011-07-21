def load_triangle(f):
    lines = f.readlines()
    return [[int(x) for x in line.split()] for line in lines]

def slide_window(l, length):
    for i in range(len(l) - length + 1):
        yield l[i:i + length]

# each node will just be an array of all possible paths
def max_path(nums):
    nums.reverse()
    for (i, row) in enumerate(nums[:-1]):
        for (j,[a, b]) in enumerate(slide_window(row, 2)):
            m = max(a,b)
            nums[i+1][j] += m
    return nums[-1][0]


if __name__ == '__main__':
    #f_name = 'data.txt'
    f_name = 'triangle.txt'
    with open(f_name, 'r') as f:
        nums = load_triangle(f)

    ans = max_path(nums)
    print ans
