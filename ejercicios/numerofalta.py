def encuentra_numeros(nums):
    min_num = min(nums)
    max_num = max(nums)
    faltan = []
    for i in range(min_num, max_num + 1):
        if i not in nums:
            faltan.append(i)
    return faltan
nums = [0, 2, 3, 6]
faltan = encuentra_numeros(nums)
print(faltan)
