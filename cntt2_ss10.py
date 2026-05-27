order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print()
    print("===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    choose = int(input("Moi ban chon chuc nang: "))

    match choose:
        case 1:
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")
                for order in range(len(order_list)):
                    print(f"{order + 1}. {order_list[order]}")
        case 2:
            while True:
                print()
                print("----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
                print("1. Thêm đơn hàng mới")
                print("2. Sửa đơn hàng theo vị trí")
                print("3. Xóa đơn hàng theo vị trí")
                print("4. Quay lại menu chính")

                choose_option = int(input("Moi ban chon chuc nang: "))

                # 2.1 thêm đơn hàng 

                if choose_option == 1:
                    code_order = input("Nhap ma don hang: ").strip().upper()
                    status_order = input("Nhap trang thai don hang").strip().upper()
                    new_order = f"{code_order} - {status_order}"
                    print("new_order",new_order)
                    order_list.append(new_order)
                    print("Them don hang moi thanh cong")

                # 2.2 sửa đơn hàng
                elif choose_option == 2:
                    index_order_need_update = input("Nhập vị trí đơn hàng cần sửa :")

                    if not index_order_need_update.isdigit():
                        print("Vị trí không hợp lệ!")
                        continue

                    index_order_need_update = int(index_order_need_update)

                    if index_order_need_update < 1 or index_order_need_update > len(order_list):
                        print("Không tồn tại đơn hàng ở vị trí này!")
                        continue
                    
                    update_code_order = input("Nhap ma don hang moi: ").strip().upper()
                    update_status_order = input("Nhap trang thai don hang moi: ").strip().upper()
                    update_order = f"{update_code_order} - {update_status_order}"

                    order_list[index_order_need_update - 1] = f"{update_order}"
                        
                    # in ra để check 
                    # print("gia tri sau khi cap nhat: ")
                    # for order in range(len(order_list)):
                    #     print(f"{order + 1}. {order_list[order]}")

                elif choose_option == 3:
                    delete_order= input("Nhập vị trí đơn hàng cần xóa :")

                    if not delete_order.isdigit():
                        print("Vị trí không hợp lệ!")
                        continue

                    delete_order = int(delete_order)

                    if delete_order < 1 or delete_order > len(order_list):
                        print("Không tồn tại đơn hàng ở vị trí này")
                        continue
                    
                    remove_order = order_list.pop(delete_order)
               
                    print("gia tri sau khi cap nhat: ")
                    for order in range(len(order_list)):
                        print(f"{order + 1}. {order_list[order]}")

                    print("Hiển thị đơn hàng vừa bị xóa: ",remove_order)

                elif choose_option == 4:
                    break
                else:
                    print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        case 3:
            print("chuc nang 3")
        case 4:
            print("chuc nang 4")
        case _:
            print("Nhap sai , vui long nhap lai!2")
