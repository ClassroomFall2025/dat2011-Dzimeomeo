##bài 1
##==========Attributes================##
class SanPham: 
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia 

##============ Getter and Setter =============##
    def get_ten_san_pham(self):
        return self.__ten_san_pham
    def set_ten_san_pham(self, __ten_san_pham):
        self.__ten_san_pham = __ten_san_pham
    
    def get_gia(self):
        return self.__gia
    def set_gia(self, gia):
        self.__gia = gia

    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia

        
#============ Methods =============##
    def nhap_san_pham(self):
        self.__ten_san_pham = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("Nhập phần trăm giảm giá (1-100): ")) / 100
    

    def __thue_nhap_khau(self):
        return self.__gia * 0.1
    def __tong_thanh_toan(self):
        giam = self.__gia * self.__giam_gia
        thue = self.__thue_nhap_khau()
        tong = self.__gia - giam + thue
        return tong
    def xuat_san_pham(self):
        print(f"Tên sản phẩm: {self.__ten_san_pham}, có giá: {self.__gia}, giảm giá: {self.__giam_gia}, thuế nhập khẩu: {self.__thue_nhap_khau()}, tổng thành toán: {self.tong_thanh_toan()}")
