def group_numbers(numbers, target):
    true_group = []
    false_group = []
    
    for num in numbers:
        if num % target == 0:
            true_group.append(num)
        else:
            false_group.append(num)

    result = [true_group, false_group]
    return result

print(group_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  # [[3, 6, 9], [1, 2, 4, 5, 7, 8]]
print(group_numbers([23, 15, 19, 20, 75, 30, 45], 5)) # [[15, 20, 75, 30, 45], [23, 19]]


