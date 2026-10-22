def original_price(gia_mua, phi_van_chuyen=0, phi_lap_dat=0, chi_phi_khac=0):
    return gia_mua + phi_van_chuyen + phi_lap_dat + chi_phi_khac


def annual_depreciation_rate(nguyen_gia, so_nam):
    if so_nam <= 0:
        raise ValueError("Số năm trích khấu hao phải lớn hơn 0")
    return nguyen_gia / so_nam


def monthly_depreciation_rate(khau_hao_nam):
    return khau_hao_nam / 12


def tinh_danh_sach_khau_hao(nguyen_gia, so_nam):
    khau_hao_nam = annual_depreciation_rate(nguyen_gia, so_nam)
    hao_mon_luy_ke = 0.0
    ket_qua_list = []

    for i in range(1, so_nam + 1):
        if i == so_nam:
            muc_khau_hao_nam_nay = nguyen_gia - hao_mon_luy_ke
            hao_mon_luy_ke = nguyen_gia
            gia_tri_con_lai = 0.0
        else:
            muc_khau_hao_nam_nay = khau_hao_nam
            hao_mon_luy_ke += muc_khau_hao_nam_nay
            gia_tri_con_lai = nguyen_gia - hao_mon_luy_ke

        ket_qua_list.append((i, muc_khau_hao_nam_nay, hao_mon_luy_ke, gia_tri_con_lai))

    return khau_hao_nam, monthly_depreciation_rate(khau_hao_nam), ket_qua_list
