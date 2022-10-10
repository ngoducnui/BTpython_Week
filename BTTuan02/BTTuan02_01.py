choose = input('Nhập lựa chọn:')
if int(choose) == 1:  # điều kiện để chuyển đổi từ C => F
    print("C => F".center(20, '-'))
    C = float(input("nhập nhiệt dộ C"))
    F = C * 1.8 + 32  # công thức C => F
    print("chuyển đổi C => F", F)
else:
    print("F => C".center(20, '-'))
    F = float(input("Nhập nhiệt độ F:"))  # điều kiện để chuyển đổi từ F => C
    C = (F - 32) / 1.8  # công thức F => C
    print("chuyển đổi F => C:", C)
