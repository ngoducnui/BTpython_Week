a = int(input("Nhập số a:"))
n = int(input("Nhập số n:"))
total = 0
if a > 0 and n > 0:
    print(a, n)
else:
    a = int(input("Nhập số lại luôn a:"))
    n = int(input("Nhập số lại luôn n:"))

def tinh_luy_thua (so, luy_thua):
    count = 1
    for x in range(1, luy_thua + 1):
        count = count * so
    return count
# vòng lặp cộng tổng lũy thừa của số a mũ n
for x in range(1, n+1):
    total = total + tinh_luy_thua(a, x)
print("tổng lũy thừa là:", total)

