class NhanVien:
    def __init__(self, ma, ho_ten, luong):
        self.ma = ma
        self.ho_ten = ho_ten
        self.luong = float(luong)

    def getThuNhap(self):
        return self.luong

    def getThueThuNhap(self):
        thu_nhap = self.getThuNhap()
        if thu_nhap < 9000000:
            return 0
        elif thu_nhap <= 15000000:
            return thu_nhap * 0.1
        else:
            return thu_nhap * 0.12

    def __str__(self):
        return f"{self.ma} - {self.ho_ten} | Lương: {self.luong:,.0f} | Thu nhập: {self.getThuNhap():,.0f}"


class TiepThi(NhanVien):
    def __init__(self, ma, ho_ten, luong, doanh_so, hoa_hong):
        super().__init__(ma, ho_ten, luong)
        self.doanh_so = float(doanh_so)
        self.hoa_hong = float(hoa_hong)

    def getThuNhap(self):
        return self.luong + self.doanh_so * self.hoa_hong


class TruongPhong(NhanVien):
    def __init__(self, ma, ho_ten, luong, trach_nhiem):
        super().__init__(ma, ho_ten, luong)
        self.trach_nhiem = float(trach_nhiem)

    def getThuNhap(self):
        return self.luong + self.trach_nhiem