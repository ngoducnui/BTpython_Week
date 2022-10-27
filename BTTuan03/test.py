# viết chương trình in ra các số chia hết cho 2. trong khoảng 0 - 100
mang = [x for x in range(100) if x % 2 == 0]
print(mang, end="\n")
# Viết chương trình in ra các số lẻ
mang1 = [x for x in range(100) if x % 2 != 0]
print(mang1, end="\n")
# Viết chương trình tạo ra danh sách gồm 100 phần tử.
mang2 = [x for x in range(100)]
print(mang2, end="\n")
# Viết chương trình gồm các số nguyên chia hết cho ba.
mang3 = [x for x in range(100) if x % 3 == 0]
print(mang3)
