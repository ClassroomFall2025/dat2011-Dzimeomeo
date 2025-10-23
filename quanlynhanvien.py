<<<<<<< HEAD
# ==========================
# File: quanlynhanvien.py
# ==========================
from nhanvien import NhanVien, TiepThi, TruongPhong

# Danh sách nhân viên (toàn cục)
ds_nv = []
file_path = "nhanvien.csv"

# -------------------------------------
def nhap_nhan_vien():
    print("==> Nhập danh sách nhân viên (Hành chính / Tiếp thị / Trưởng phòng)")
    while True:
        loai = input("Nhập loại (1-HC, 2-TT, 3-TP, 0-Thoát): ")
        if loai == '0':
            break

        ma = input("Mã NV: ")
        ho_ten = input("Họ tên: ")
        luong = float(input("Lương cơ bản: "))

        if loai == '1':
            nv = NhanVien(ma, ho_ten, luong)
        elif loai == '2':
            doanh_so = float(input("Doanh số: "))
            hoa_hong = float(input("Tỷ lệ hoa hồng (vd: 0.05): "))
            nv = TiepThi(ma, ho_ten, luong, doanh_so, hoa_hong)
        elif loai == '3':
            trach_nhiem = float(input("Lương trách nhiệm: "))
            nv = TruongPhong(ma, ho_ten, luong, trach_nhiem)
        else:
            print("==> Loại không hợp lệ!")
            continue

        ds_nv.append(nv)
    print("==> Nhập danh sách hoàn tất!")


# -------------------------------------
def xuat_danh_sach():
    if not ds_nv:
        print("==> Danh sách rỗng!")
    else:
        print("==> Danh sách nhân viên:")
        for nv in ds_nv:
            print(nv)


# -------------------------------------
def tim_theo_ma():
    ma = input("Nhập mã cần tìm: ")
    for nv in ds_nv:
        if nv.ma == ma:
            print("==> Tìm thấy:", nv)
            return
    print("==> Không tìm thấy nhân viên!")


# -------------------------------------
def xoa_theo_ma():
    ma = input("Nhập mã cần xóa: ")
    for nv in ds_nv:
        if nv.ma == ma:
            ds_nv.remove(nv)
            print("==> Đã xóa nhân viên!")
            return
    print("==> Không tìm thấy nhân viên!")


# -------------------------------------
def cap_nhat_theo_ma():
    ma = input("Nhập mã cần cập nhật: ")
    for nv in ds_nv:
        if nv.ma == ma:
            nv.ho_ten = input(f"Họ tên mới ({nv.ho_ten}): ") or nv.ho_ten
            nv.luong = float(input(f"Lương mới ({nv.luong}): ") or nv.luong)
            print("==> Cập nhật thành công!")
            return
    print("==> Không tìm thấy nhân viên!")


# -------------------------------------
def tim_theo_khoang_luong():
    min_l = float(input("Nhập lương tối thiểu: "))
    max_l = float(input("Nhập lương tối đa: "))
    kq = [nv for nv in ds_nv if min_l <= nv.luong <= max_l]
    if not kq:
        print("==> Không có nhân viên trong khoảng này.")
    else:
        for nv in kq:
            print(nv)


# -------------------------------------
def sap_xep_theo_ten():
    ds_nv.sort(key=lambda nv: nv.ho_ten)
    print("==> Đã sắp xếp theo họ tên!")


# -------------------------------------
def sap_xep_theo_thu_nhap():
    ds_nv.sort(key=lambda nv: nv.getThuNhap(), reverse=True)
    print("==> Đã sắp xếp theo thu nhập!")


# -------------------------------------
def top5_thu_nhap():
    ds_top = sorted(ds_nv, key=lambda nv: nv.getThuNhap(), reverse=True)[:5]
    print("==> Top 5 nhân viên có thu nhập cao nhất:")
    for nv in ds_top:
        print(nv)


import os
def luu_file():
    file_path = "nhanvien.csv"
    # Nếu file chưa có, tạo và ghi tiêu đề
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Loai,Ma,HoTen,Luong,DoanhSo,HoaHong,TrachNhiem\n")

    # Mở file để thêm dữ liệu (append)
    with open(file_path, "a", encoding="utf-8") as f:
        for nv in ds_nv:
            if isinstance(nv, TiepThi):
                f.write(f"TT,{nv.ma},{nv.ho_ten},{nv.luong},{nv.doanh_so},{nv.hoa_hong},\n")
            elif isinstance(nv, TruongPhong):
                f.write(f"TP,{nv.ma},{nv.ho_ten},{nv.luong},,,{nv.trach_nhiem}\n")
            else:
                f.write(f"HC,{nv.ma},{nv.ho_ten},{nv.luong},,,\n")
    print("==> Đã thêm nhân viên mới vào file CSV thành công!")


def doc_file():
    ds_nv.clear()
    try:
        with open("nhanvien.csv", "r", encoding="utf-8") as f:
            next(f)  # bỏ tiêu đề
            for line in f:
                if not line.strip():
                    continue
                loai, ma, ho_ten, luong, ds, hh, tn = line.strip().split(",")
                luong = float(luong or 0)
                if loai == "TT":
                    nv = TiepThi(ma, ho_ten, luong, float(ds or 0), float(hh or 0))
                elif loai == "TP":
                    nv = TruongPhong(ma, ho_ten, luong, float(tn or 0))
                else:
                    nv = NhanVien(ma, ho_ten, luong)
                ds_nv.append(nv)
        print(f"==> Đã đọc {len(ds_nv)} nhân viên từ file CSV thành công!")
    except FileNotFoundError:
        print("==> File CSV chưa tồn tại, hãy lưu dữ liệu trước.")
=======
# ==========================
# File: quanlynhanvien.py
# ==========================
from nhanvien import NhanVien, TiepThi, TruongPhong

# Danh sách nhân viên (toàn cục)
ds_nv = []
file_path = "nhanvien.csv"

# -------------------------------------
def nhap_nhan_vien():
    print("==> Nhập danh sách nhân viên (Hành chính / Tiếp thị / Trưởng phòng)")
    while True:
        loai = input("Nhập loại (1-HC, 2-TT, 3-TP, 0-Thoát): ")
        if loai == '0':
            break

        ma = input("Mã NV: ")
        ho_ten = input("Họ tên: ")
        luong = float(input("Lương cơ bản: "))

        if loai == '1':
            nv = NhanVien(ma, ho_ten, luong)
        elif loai == '2':
            doanh_so = float(input("Doanh số: "))
            hoa_hong = float(input("Tỷ lệ hoa hồng (vd: 0.05): "))
            nv = TiepThi(ma, ho_ten, luong, doanh_so, hoa_hong)
        elif loai == '3':
            trach_nhiem = float(input("Lương trách nhiệm: "))
            nv = TruongPhong(ma, ho_ten, luong, trach_nhiem)
        else:
            print("==> Loại không hợp lệ!")
            continue

        ds_nv.append(nv)
    print("==> Nhập danh sách hoàn tất!")


# -------------------------------------
def xuat_danh_sach():
    if not ds_nv:
        print("==> Danh sách rỗng!")
    else:
        print("==> Danh sách nhân viên:")
        for nv in ds_nv:
            print(nv)


# -------------------------------------
def tim_theo_ma():
    ma = input("Nhập mã cần tìm: ")
    for nv in ds_nv:
        if nv.ma == ma:
            print("==> Tìm thấy:", nv)
            return
    print("==> Không tìm thấy nhân viên!")


# -------------------------------------
def xoa_theo_ma():
    ma = input("Nhập mã cần xóa: ")
    for nv in ds_nv:
        if nv.ma == ma:
            ds_nv.remove(nv)
            print("==> Đã xóa nhân viên!")
            return
    print("==> Không tìm thấy nhân viên!")


# -------------------------------------
def cap_nhat_theo_ma():
    ma = input("Nhập mã cần cập nhật: ")
    for nv in ds_nv:
        if nv.ma == ma:
            nv.ho_ten = input(f"Họ tên mới ({nv.ho_ten}): ") or nv.ho_ten
            nv.luong = float(input(f"Lương mới ({nv.luong}): ") or nv.luong)
            print("==> Cập nhật thành công!")
            return
    print("==> Không tìm thấy nhân viên!")


# -------------------------------------
def tim_theo_khoang_luong():
    min_l = float(input("Nhập lương tối thiểu: "))
    max_l = float(input("Nhập lương tối đa: "))
    kq = [nv for nv in ds_nv if min_l <= nv.luong <= max_l]
    if not kq:
        print("==> Không có nhân viên trong khoảng này.")
    else:
        for nv in kq:
            print(nv)


# -------------------------------------
def sap_xep_theo_ten():
    ds_nv.sort(key=lambda nv: nv.ho_ten)
    print("==> Đã sắp xếp theo họ tên!")


# -------------------------------------
def sap_xep_theo_thu_nhap():
    ds_nv.sort(key=lambda nv: nv.getThuNhap(), reverse=True)
    print("==> Đã sắp xếp theo thu nhập!")


# -------------------------------------
def top5_thu_nhap():
    ds_top = sorted(ds_nv, key=lambda nv: nv.getThuNhap(), reverse=True)[:5]
    print("==> Top 5 nhân viên có thu nhập cao nhất:")
    for nv in ds_top:
        print(nv)


import os
def luu_file():
    file_path = "nhanvien.csv"
    # Nếu file chưa có, tạo và ghi tiêu đề
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Loai,Ma,HoTen,Luong,DoanhSo,HoaHong,TrachNhiem\n")

    # Mở file để thêm dữ liệu (append)
    with open(file_path, "a", encoding="utf-8") as f:
        for nv in ds_nv:
            if isinstance(nv, TiepThi):
                f.write(f"TT,{nv.ma},{nv.ho_ten},{nv.luong},{nv.doanh_so},{nv.hoa_hong},\n")
            elif isinstance(nv, TruongPhong):
                f.write(f"TP,{nv.ma},{nv.ho_ten},{nv.luong},,,{nv.trach_nhiem}\n")
            else:
                f.write(f"HC,{nv.ma},{nv.ho_ten},{nv.luong},,,\n")
    print("==> Đã thêm nhân viên mới vào file CSV thành công!")


def doc_file():
    ds_nv.clear()
    try:
        with open("nhanvien.csv", "r", encoding="utf-8") as f:
            next(f)  # bỏ tiêu đề
            for line in f:
                if not line.strip():
                    continue
                loai, ma, ho_ten, luong, ds, hh, tn = line.strip().split(",")
                luong = float(luong or 0)
                if loai == "TT":
                    nv = TiepThi(ma, ho_ten, luong, float(ds or 0), float(hh or 0))
                elif loai == "TP":
                    nv = TruongPhong(ma, ho_ten, luong, float(tn or 0))
                else:
                    nv = NhanVien(ma, ho_ten, luong)
                ds_nv.append(nv)
        print(f"==> Đã đọc {len(ds_nv)} nhân viên từ file CSV thành công!")
    except FileNotFoundError:
        print("==> File CSV chưa tồn tại, hãy lưu dữ liệu trước.")
>>>>>>> cec3f145c6e1de1877bccfe3238d9f567e4816d2
