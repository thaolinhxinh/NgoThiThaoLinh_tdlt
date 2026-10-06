payment_type = int(input("Nhập loại thanh toán (1/2): "))

while payment_type != 1 and payment_type != 2:
    print("Loại thanh toán không hợp lệ! Vui lòng nhập 1 hoặc 2.")
    payment_type = int(input("Nhập lại loại thanh toán (1/2): "))

x = float(input("Nhập số kWh tháng trước: "))
y = float(input("Nhập số kWh tháng nay: "))
T = 0

if payment_type == 1:
    if (y - x) <= 50:
        T = T + 1.549 * (y - x)
    elif (y - x) <= 100:
        T = T + 77.45 + 1.6 * (y - x - 50)
    elif (y - x) <= 200:
        T = T + 157.45 + 1.858 * (y - x - 100)
    elif (y - x) <= 300:
        T = T + 343.25 + 2.340 * (y - x - 200)
    elif (y - x) <= 400:
        T = T + 577.25 + 2.615 * (y - x - 300)
    else:
        T = T + 838.75 + 2.701 * (y - x - 400)

elif payment_type == 2:
    T = T + (y - x) * 2.271

print("Tổng số tiền phải trả:", T)