def tinh_chi_tiet_khau_hao(gia_goc, so_nam_khau_hao, phi_van_chuyen=0, phi_lap_dat=0):
    if so_nam_khau_hao <= 0:
        raise ValueError("Số năm khấu hao phải lớn hơn 0")

    nguyen_gia = gia_goc + phi_van_chuyen + phi_lap_dat
    muc_khau_hao_nam = nguyen_gia / so_nam_khau_hao
    muc_khau_hao_thang = muc_khau_hao_nam / 12

    hao_mon_luy_ke = 0.0
    lich_khau_hao = []

    for nam in range(1, so_nam_khau_hao + 1):
        if nam == so_nam_khau_hao:
            so_tien_khau_hao = nguyen_gia - hao_mon_luy_ke
            hao_mon_luy_ke = nguyen_gia
            gia_tri_con_lai = 0.0
        else:
            so_tien_khau_hao = muc_khau_hao_nam
            hao_mon_luy_ke += so_tien_khau_hao
            gia_tri_con_lai = nguyen_gia - hao_mon_luy_ke

        lich_khau_hao.append({
            "nam": nam,
            "khau_hao": so_tien_khau_hao,
            "luy_ke": hao_mon_luy_ke,
            "con_lai": gia_tri_con_lai
        })

    return nguyen_gia, muc_khau_hao_nam, muc_khau_hao_thang, lich_khau_hao


gia_goc = float(input("Nhập giá gốc tài sản: "))
phi_van_chuyen = float(input("Nhập chi phí vận chuyển (để trống nếu = 0): ") or 0)
phi_lap_dat = float(input("Nhập chi phí lắp đặt (để trống nếu = 0): ") or 0)
so_nam_khau_hao = int(input("Nhập số năm khấu hao: "))

nguyen_gia, khau_hao_nam, khau_hao_thang, lich_khau_hao = tinh_chi_tiet_khau_hao(
    gia_goc, so_nam_khau_hao, phi_van_chuyen, phi_lap_dat
)


print("\nBẢNG TRÍCH KHẤU HAO CHI TIẾT:")
print(f"{'Năm':<5} | {'Mức khấu hao':<18} | {'Hao mòn lũy kế':<18} | {'Giá trị còn lại':<18}")
print("-" * 65)

for row in lich_khau_hao:
    print(f"{row['nam']:<5} | {row['khau_hao']:>15,.2f} | {row['luy_ke']:>16,.2f} | {row['con_lai']:>17,.2f}")