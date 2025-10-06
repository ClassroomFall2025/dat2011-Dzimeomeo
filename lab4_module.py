# Bài 1: Tính tiền nước sinh hoạt
def tinh_tien_nuoc(so_nuoc): 
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc <= 10:
       tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
       tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
       tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
       tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc


# Bài 2: Tính nguyên liệu làm bánh trung thu
def tinh_nguyen_lieu(sl_bdx,sl_btc,sl_bd):
   banh_dau_xanh = {"đường": 0.04, "đậu": 0.07}
   banh_thap_cam = {"đường": 0.06, "đậu": 0}
   banh_deo = {"đường": 0.05, "đậu": 0.02}

   nguyen_lieu = {}
   đường = sl_bdx * banh_dau_xanh["đường"] + sl_btc * banh_thap_cam["đường"] + sl_bd * banh_deo["đường"]
   đậu = sl_bdx * banh_dau_xanh["đậu"] + sl_btc * banh_thap_cam["đậu"] + sl_bd * banh_deo["đậu"]
   
   nguyen_lieu["đường"] = đường
   nguyen_lieu["đậu"] = đậu
   return tinh_nguyen_lieu

# Bài 3: Lọc các số chẵn trong dãy số nguyên bằng hàm filter và lambda

def loc_so_chan():
    chuoi = input("Nhập dãy số nguyên (cách nhau bằng dấu cách): ")

    try:
        # Tách chuỗi thành danh sách số nguyên
        my_list = list(map(int, chuoi.split()))

        # Dùng filter + lambda để lọc số chẵn
        new_list = list(filter(lambda x: x % 2 == 0, my_list))

        # Xuất kết quả
        print("Danh sách ban đầu:", my_list)
        print("Các số chẵn là:", new_list)

    except ValueError:
        print("❌ Lỗi: Vui lòng chỉ nhập số nguyên, cách nhau bằng dấu cách!")

# Gọi hàm
loc_so_chan()
