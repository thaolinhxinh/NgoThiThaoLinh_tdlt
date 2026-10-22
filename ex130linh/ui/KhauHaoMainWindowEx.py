from PyQt6.QtWidgets import QMessageBox
from ex130linh.ui.KhauHaoMainWindow import Ui_MainWindow
from ex130linh.libs.KhauHao import original_price, annual_depreciation_rate, monthly_depreciation_rate, tinh_danh_sach_khau_hao

class KhauHaoMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.btnTinhKhauHao.clicked.connect(self.xu_ly_tinh_khau_hao_co_ban)
        self.btnXemChiTiet.clicked.connect(self.xu_ly_xem_chi_tiet)

    def xu_ly_tinh_khau_hao_co_ban(self):
        try:
            gia_mua_moi = float(self.txtGiaMua.text() or 0)
            phi_van_chuyen = float(self.txtPhiVanChuyen.text() or 0)
            phi_lap_dat = float(self.txtPhiLapDat.text() or 0)
            thoi_gian_sd = int(float(self.txtSoNam.text() or 0))

            nguyen_gia = original_price(gia_mua_moi, phi_van_chuyen, phi_lap_dat)
            khau_hao_nam = annual_depreciation_rate(nguyen_gia, thoi_gian_sd)
            khau_hao_thang = monthly_depreciation_rate(khau_hao_nam)

            self.txtNguyenGia.setText(f"{nguyen_gia:,.0f}")
            self.txtKhauHaoNam.setText(f"{khau_hao_nam:,.0f}")
            self.txtKhauHaoThang.setText(f"{khau_hao_thang:,.0f}")

        except ValueError as e:
            QMessageBox.warning(
                self.MainWindow,
                "Lỗi dữ liệu",
                f"Vui lòng kiểm tra lại giá trị nhập vào!\nChi tiết: {e}"
            )

    def xu_ly_xem_chi_tiet(self):
        try:
            gia_mua_moi = float(self.txtGiaMua.text() or 0)
            phi_van_chuyen = float(self.txtPhiVanChuyen.text() or 0)
            phi_lap_dat = float(self.txtPhiLapDat.text() or 0)
            thoi_gian_sd = int(float(self.txtSoNam.text() or 0))

            nguyen_gia = original_price(gia_mua_moi, phi_van_chuyen, phi_lap_dat)
            khau_hao_nam, khau_hao_thang, bang_khau_hao = tinh_danh_sach_khau_hao(nguyen_gia, thoi_gian_sd)

            self.txtNguyenGia.setText(f"{nguyen_gia:,.0f}")
            self.txtKhauHaoNam.setText(f"{khau_hao_nam:,.0f}")
            self.txtKhauHaoThang.setText(f"{khau_hao_thang:,.0f}")

            noi_dung_chi_tiet = ""
            for nam, muc_kh, luy_ke, con_lai in bang_khau_hao:
                noi_dung_chi_tiet += f"Năm {nam}, Sau khấu hao còn => {con_lai:,.0f}\n"

            self.txtChiTiet.setPlainText(noi_dung_chi_tiet.strip())

        except ValueError as e:
            QMessageBox.warning(
                self.MainWindow,
                "Lỗi dữ liệu",
                f"Vui lòng kiểm tra lại giá trị nhập vào!\nChi tiết: {e}"
            )