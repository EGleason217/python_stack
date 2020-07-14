def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x
new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print(sum1)
print(sum2)
print(sum3)