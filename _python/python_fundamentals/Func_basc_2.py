# def countdown(x):
#     count = []
#     for i in range (x,-1,-1):
#         count.append(i)
#     return count
# print (countdown(10))

# def a(x):
#     print (x[0])
#     return (x[1])
# a([1,2])

# def a(x):
#     y = (len(x) + x[0])
#     return (y)
# y = (a([4,2,5,8,3,2,6]))
# print (y)

# def values_greater_than_second(nums_list):
#     new_list = []
#     second_val = nums_list[1]
#     for idx in range (len(nums_list)):
#         if nums_list[idx] > second_val:
#             new_list.append(nums_list[idx])
#     return new_list
# x = (values_greater_than_second([5,2,3,2,1,4]))
# print (x)
# print (len(x))

def length_and_value(size, value):
    new_list = []
    for num_times in range(size):
        new_list.append(value)
    return new_list
print(length_and_value(5,39))

