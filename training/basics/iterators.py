nums = [1, 2, 3, 4, 5]

i_nums = nums.__iter__()


# for num in nums:
#     print(num)

# print(i_nums)
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 5)
# for num in nums:
#     print(num)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

print('--------------------------')


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current = current + 1


nums = my_range(1, 5)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
