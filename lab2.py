import math

# Thông tin sinh viên
# Họ tên: Vũ Thanh Tùng
# MSSV: [Nhập MSSV của bạn]

def bai1_tinh_dien_tich_chu_vi_tron():
    print("\n--- BÀI 1: HÌNH TRÒN ---")
    r = float(input("Nhập bán kính hình tròn: "))
    chu_vi = 2 * math.pi * r
    dien_tich = math.pi * pow(r, 2)
    print(f"Chu vi: {chu_vi:.2 f}")
    print(f"Diện tích: {dien_tich:.2 f}")

def bai2_tinh_diem_trung_binh():
    print("\n--- BÀI 2: ĐIỂM TRUNG BÌNH ---")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    dtb = (toan + ly + hoa) / 3
    print(f"Điểm trung bình 3 môn: {dtb:.1 f}")

def bai3_tinh_luong():
    print("\n--- BÀI 3: TÍNH LƯƠNG NHÂN VIÊN ---")
    luong_ngay = float(input("Nhập lương mỗi ngày: "))
    so_ngay = int(input("Nhập số ngày công: "))
    tong_luong = luong_ngay * so_ngay
    print(f"Tổng lương nhận được: {tong_luong:,.0 f} VNĐ")

if __name__ == "__main__":
    print("CHƯƠNG TRÌNH LAB 2 - NHẬP MÔN LẬP TRÌNH")
    bai1_tinh_dien_tich_chu_vi_tron()
    bai2_tinh_diem_trung_binh()
    bai3_tinh_luong()
    print("\n" + "="*30)
    print("HOÀN THÀNH LAB 2 - VŨ THANH TÙNG")