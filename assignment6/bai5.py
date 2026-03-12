def remove_odds(numbers):
    result = []
    
    for num in numbers:
        if num % 2 == 0:   
            result.append(num)
    
    return result

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = remove_odds(original_list)

print("Original list:", original_list)
print("List without odd numbers:", new_list)