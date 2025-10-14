import sinhvienpoly as svpl

class QuanLySinhVien:
    def __init__(self):
        self.dssv = []

    def nhap_dssv(self):
        while True:
            loai = input("Nhập loại sinh viên (IT/Biz, 0 để kết thúc): ").strip().lower()
            if loai == "0":
                break
            ho_ten = input("Nhập họ tên sinh viên: ")

            if loai == "it":
                java = float(input("Điểm Java: "))
                html = float(input("Điểm HTML: "))
                css = float(input("Điểm CSS: "))
                sv = svpl.SinhVienIT(ho_ten, "IT", java, html, css)
                self.dssv.append(sv)

            elif loai == "biz":
                marketing = float(input("Điểm Marketing: "))
                sales = float(input("Điểm Sales: "))
                sv = svpl.SinhVienBiz(ho_ten, "Biz", marketing, sales)
                self.dssv.append(sv)

            else:
                print("Loại sinh viên không hợp lệ!")

    def xuat_dssv(self):
        print("\n=== DANH SÁCH SINH VIÊN ===")
        for sv in self.dssv:
            sv.xuat()

    def xuat_dssv_gioi(self):
        print("\n=== DANH SÁCH SINH VIÊN CÓ HỌC LỰC GIỎI ===")
        for sv in self.dssv:
            if sv.get_hoc_luc() == "Giỏi":
                sv.xuat()

    def xuat_dssv_diem(self):
        print("\n=== DANH SÁCH SINH VIÊN SẮP XẾP THEO ĐIỂM ===")
        self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
        for sv in self.dssv:
            sv.xuat()
