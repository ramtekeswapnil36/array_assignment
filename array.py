array_1 = [[1, 1, 2, 3], [2, 2, 3, 4], [3, 5, 6, 7], [9, 11, 12, 13]]
array_2 = [[1, 3], [3, 4], [5, 6], [9, 10], [12, 13]]

flat_array_1 = [number for sublist in array_1 for num in sublist]
flat_array_2 = [number for sublist in array_2 for num in sublist]


unique_numbers = [num for num in set(flat_array_1) if flat_array_1.count(num) == 1 and all(num not in sublist for sublist in array_2)]

print("Numbers in array_1 which are not present in array_2 and occurs only once:")
print(unique_numbers)



