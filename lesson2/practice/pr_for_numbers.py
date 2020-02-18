from random import randint

nums = [randint(1, 100) for _ in range(10)]
print(nums)
for num in nums:
    print(num + 1, end=" ")
