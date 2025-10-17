##bài 1
##==========Attributes================##
class SanPham: 
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.giam_gia = giam_gia 

##============ Getter and Setter =============##
    def get_ten_san_pham(self):
        return self.ten_san_pham
    def set_ten_san_pham(self, ten_san_pham):
        self.ten_san_pham = ten_san_pham
    
    def get_gia(self):
        return self.gia
    def set_gia(self, gia):
        self.gia = gia

    def get_giam_gia(self):
        return self.giam_gia
    def set_giam_gia(self, giam_gia):
        self.giam_gia = giam_gia

        
#============ Methods =============##
    def nhap_san_pham(self):
        self.ten_san_pham = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập giá sản phẩm: "))
        self.giam_gia = float(input("Nhập phần trăm giảm giá (1-100): ")) / 100
    

    def thue_nhap_khau(self):
        return self.gia * 0.1
    def tong_thanh_toan(self):
        giam = self.gia * self.giam_gia
        thue = self.thue_nhap_khau()
        tong = self.gia - giam + thue
        return tong
    def xuat_san_pham(self):
        print(f"Tên sản phẩm: {self.ten_san_pham}, có giá: {self.gia}, giảm giá: {self.giam_gia}, thuế nhập khẩu: {self.thue_nhap_khau()}, tổng thành toán: {self.tong_thanh_toan()}")
