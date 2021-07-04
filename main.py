import math
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def one():
    nums = [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]
    print(sum(nums))


# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

def two():
    nums = [x for x in range(1, 4000000)]
    fibs = [nums[0], nums[1]]
    for x in nums[2:]:
        if x == (fibs[-1] + fibs[- 2]):
            fibs.append(x)
    even_fibs = [x for x in fibs if x % 2 == 0]
    print(sum(even_fibs))


# find prime numbers in specified range
def primes(n):
    nums = [x for x in range(n)]
    primes = [2, 3]
    for x in nums:
        for y in range(2, (x - 1)):
            if x % y == 0 and len(primes) > 10001:
                break
            elif x not in primes:
                primes.append(x)
    return primes


# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def three():
    num = 600851475143
    n = 0
    c = 0
    x = primes(7000)

    for i in x:
        if num % i == 0:
            num = num / i
            print(i)
            print(num)
            if num in x and i in x:
                n = num
                print("yes")
    print(n)


# Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def four():
    one = [x for x in range(1000)]
    two = [x for x in range(1000)]
    palin = []
    for x in one:
        for y in two:
            w = x * y
            if w != 0:
                mult = list(str(w))
                c = list(str(w))
                mult.reverse()
                if c == mult:
                    palin.append(int(''.join(c)))
    print(max(palin))


# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def five():
    check_list = [11, 13, 14, 16, 17, 18, 19, 20]
    divis = [x for x in range(20, 999999999, 20) for y in range(1, 20) if all(x % n == 0 for n in check_list)]
    final = [x for x in divis if divis.count(x) == 19 and x != 0]
    print(min(final))



# Sum square difference
# Find the difference between the sum of the squares of
# the first one hundred natural numbers and the square of the sum.
def six():
    nums = [x for x in range(101)]
    sum_square = sum([pow(x, 2) for x in nums])
    square_sum = pow(sum(nums), 2)
    print(square_sum - sum_square)

# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def seven():
    x = (primes(9999999))
    print(x[10001])

seven()