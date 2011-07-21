nums = range(1, 101)

sum_acc = lambda x,y: x+y
square = lambda x: x*x

sumofsquares = reduce(sum_acc, map(square, nums))
squareofsums = square(reduce(sum_acc, nums))

def sum_squares(n):
    return n * (n+1) * (2*n+1) / 6
    
def square_sum(n):
    return n**2 * (n+1)**2 / 4

print square_sum(100) - sum_squares(100)
print squareofsums - sumofsquares
