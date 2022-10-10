# bt01 1. Viết một chương trình sắp xếp các phần tử trong mảng và xử lý các vấn đề sau
# a) Thứ tự tăng dần.

import numpy

arrayA = list(numpy.random.randint(100, size=10))
arrayA.sort()
print(f"\ndanh sách phần tu trong mảng tăng dần là: {arrayA} ")

# b) Thứ tự giảm dần:
newarrayA = sorted(arrayA, reverse=True)
print(f'danh sách phần tử trong mảng giảm dần là: {newarrayA}')