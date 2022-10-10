import numpy

#1. Viết một chương trình sắp xếp các phần tử trong mảng và xử lý các vấn đề sau
#a) Thứ tự tăng dần.
arrayA = list(numpy.random.randint(100, size=10))
arrayA.sort()
print(f'Danh sách phần tử trong mảng sắp xếp tăng dần là: {arrayA}')
#b) Thứ tự giảm dần.
newarray = sorted(arrayA, reverse= True)
print(f'Danh sách phần tử trong mảng sắp xếp giảm dần là: {newarray}')
