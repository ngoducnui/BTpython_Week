# bt1 CHO NGƯỜI DÙNG NHẬP TÊN VÀ IN RA CHỮ ĐẦU + CHỮ GIỮA + CHỮ CUỐI
import math

name = input("BT1:\n Nhập tên:")
arr = list(name)
ln = len(arr)
center = math.ceil((ln - 1) / 2)  # //làm tròn
print("output:", arr[0] + arr[center] + arr[ln - 1])
# BÀI TẬP 2: CHO MỘT ĐOẠN CHUỖI NHƯ SAU: "&*@#ynXC26a@%t^&i5v@kVe"
strg = "&*@#ynXC26a@%t^&i5v@kVe"
print("BT2: List = ", list(strg))
chars = []
digits = []
synbols = []
for x in list(strg):
    if x.isalpha():
        chars.append(x)
    elif x.isdigit():
        digits.append(x)
    else:
        synbols.append(x)
print(chars, 'total =', len(chars))
print(digits, 'total =', len(digits))
print(synbols, 'total =', len(synbols))

# BÀI TẬP 3: CHO MỘT CHUỖI BẤT KÌ: S = &*@#ynXC2612a@512t%^&i5v@kVe
S = "&*@#ynXC2612a@%512t^&i5v@kVe"
print("\nBT3: List=", list(S))
chars1 = []
sum = 0
dem = 0
for x in list(S):
    if x.isdigit():
        dem = dem + 1
        digits.append(x)
        sum = sum + int(x)
print(f"tổng:{sum}")
print(f"Average:{sum / dem}")

# BÀI TẬP 4: CHO NGƯỜI DÙNG NHẬP CHUỖI S = APPLE XUẤT RA OUTPUT BÊN DƯỚI:
chuoi = "Apple"
dich_chuoi = dict()
for i in chuoi:
    count = chuoi.count(i)
    dich_chuoi[i] = count
print(f"\nBT4: Kết quả:{dich_chuoi}")

# BÀI TẬP 5: CHO MỘT DANH SÁCH str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#           XUẤT RA CÁC PHẦN TỬ TỒN TRONG STR_LIST (NGOẠI TRỪ RỖNG)
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("\nBT5:")
for i in str_list:
    if i:
        print(i)

# BÀI TẬP 6: CHO MỘT CHUỖI li = [ 1,3,5,"a","b"]
#           KIỂM TRA XEM a CÓ TỒN TẠI TRONG LI KHÔNG?
li = [1, 3, 5, "a", "b"]
ab = "a" in li
print("\nBT6:", ab)

