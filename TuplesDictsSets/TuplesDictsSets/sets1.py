
nums1 = input("Please enter a series of numbers separated by commas")
nums2 = input("Please enter a series of numbers separated by commas")

set_1 = set((num.strip()) for num in nums1.split(','))
set_2 = set((num.strip()) for num in nums2.split(','))

result = [int(num) for num in set_1.intersection(set_2)]
result.sort()

result = ', ' .join(str(x) for x  in result)
print(result) 
