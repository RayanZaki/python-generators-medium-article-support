# import itertools
# def foo():
#     return 1
#     return 2

# def foo1():
#     yield 1
#     yield 2


# def count_to_infinity_gen():
#     count = 0
#     while True:
#         count += 1
#     return count

# def count_to_infinity_yield():
#     count = 0
#     while True:
#         count += 1
#         yield count


# def return_test():
#     nums = []
#     for i in range(1000):
#         nums.append(i)
#     return nums

# def yield_test():
#     for i in range(100):
#         yield i

# print(next(foo1()))
# foo1()
# print(next(foo1()))
# # for i in yield_test():
# #     print(i)


# # # list = [ i for i in count_to_infinity_yield()]
# # gen = ( i for i in count_to_infinity_yield())

# # [print(i) for i in gen]

# def test():
#     for i in range(10):
#         yield i

# print(test().__next__())
# print(test().__next__())
l = ( i for i in range(10))
print(type(tuple(l)))