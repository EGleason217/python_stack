# for x in range (151):
#     print(x)
# for x in range (5,1001,5):
#     print(x)
# for x in range (1,101):
#     if (x%10) == 0:
#         print("Coding Dojo", x)
#     elif (x%5) == 0:
#         print("Coding", x)
#     else:
#         print(x)
# sum = 0
# for x in range (500000):
#     if (x%2) != 0:
#         sum = sum + x
# print(sum)
# for x in range (2018,0,-4):
#     print(x)
# lowNum = 1
# highNum = 100
# mult = 3
# for x in range(lowNum,highNum,1):
#     if (x%mult) == 0:
#         print(x)

# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(num_list):
    for pos_num in range (len(num_list)):
        if num_list[pos_num] > 0:
            num_list.pop(pos_num)
            num_list.insert(pos_num, "big")
        else:
            pass
    return num_list
# print (biggie_size([-1, 3, 5, -5]))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(num_list):
    count = 0
    for pos_num in range (len(num_list)):
        if (num_list[pos_num]) > 0:
            count += 1
    new_val = len(num_list)-1
    num_list.pop(new_val)
    num_list.append(count)
    #
    return num_list
# print (count_positives([-1,1,1,1]))




# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(num_list):
    sum = 0
    for num in range (len(num_list)):
        sum = sum + num_list[num]
    return sum
# print (sum_total([1,2,3,4]))


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def avg(num2_list):
    sum = 0
    for num in range (len(num2_list)):
        sum = sum + num2_list[num]
    x = sum/len(num2_list)
#
    return x
# print(avg([1,2,3,4]))


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(num_list):
    return len(num_list)
# print(length([37,2,1,9]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(num_list):
    min_num = 0
    for idx in range (len(num_list)):
        if num_list[idx] < min_num:
            min_num = num_list[idx]
    return min_num
# print(minimum([37,2,1,-9]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(num_list):
    max_num = 0
    for idx in range (len(num_list)):
        if num_list[idx] > max_num:
            max_num = num_list[idx]
    return max_num
# print(maximum([37,2,1,-9]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(num_list):
    analysis = {}
    sumTotal = 0
    for num in range (len(num_list)):
        sumTotal = sumTotal + num_list[num]
    analysis.update({"sumTotal": sumTotal})
    sumAvg = 0
    for num in range (len(num_list)):
         sumAvg = sumAvg + num_list[num]
    avg = sumAvg/len(num_list)
    analysis.update({"Average": avg})
    min_num = 0
    for idx in range (len(num_list)):
         if num_list[idx] < min_num:
             min_num = num_list[idx]
    analysis.update({"Minimum Number": min_num})
    max_num = 0
    for idx in range (len(num_list)):
         if num_list[idx] > max_num:
             max_num = num_list[idx]
    analysis.update({"Maximum Number": max_num})
    analysis.update({"Length of Dictionary": len(analysis)})
    return(analysis)
# print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(num_list):
    num_list.reverse()
    return(num_list)
print(reverse_list([37,2,1,-9]))


