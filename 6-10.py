import math
# Sum square difference
# Find the difference between the sum of the squares of
# the first one hundred natural numbers and the square of the sum.
def six():
    nums = [x for x in range(101)]
    sum_square = sum([pow(x, 2) for x in nums])
    square_sum = pow(sum(nums), 2)
    print(square_sum - sum_square)
