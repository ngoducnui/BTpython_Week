import numpy

# 1. Viết một chương trình sắp xếp các phần tử trong mảng và xử lý các vấn đề sau
# a) Thứ tự tăng dần.
arrayA = list(numpy.random.randint(100, size=10))
arrayA.sort()
print(f'Danh sách phần tử trong mảng sắp xếp tăng dần là: {arrayA}')
# b) Thứ tự giảm dần.
newarray = sorted(arrayA, reverse=True)
print(f'Danh sách phần tử trong mảng sắp xếp giảm dần là: {newarray}')


# 2. BÀI TẬP MỞ RỘNG

# a) Nhập từ bàn phím chiều cao và cân nặng của n HS của một trường.


lst = []
het = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = [int(input()), int(input())]
    lst.append(ele)
for j in range(0, n):
    height = int(lst[j][0])
    weight = int(lst[j][1])
    print(f"Hoc sinh thu {i}", height, weight)

    # def caculator_function(hit, wig):
    #     return wig / (hit * 2)



    # print("IBM : ", caculator_function(height, weight))

# b) Đưa ra màn hình chỉ số BMI của các HS được sắp xếp tăng dần theo chiều cao
# c) Giả sử các HS có mã từ 1 đến n. Đưa ra màn hình danh sách mã HS và chỉ BMI được sắp xếp tăng dần theo BMI
