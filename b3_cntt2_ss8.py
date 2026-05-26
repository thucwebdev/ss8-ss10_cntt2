raw_data = " c; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print()
    print("\n ===== HỆ THỐNG QUẢN LÝ NHÂN SỰ ===== ")
    print(" 1. Hiển thị chuỗi dữ liệu gốc")
    print(" 2. Chuẩn hóa dữ liệu và in báo cáo ")
    print(" 3. Tìm kiếm nhân viên theo mã ID ")
    print(" 4. Thoát chương trình ")

    choose = int(input("moi ban chon chuc nang: "))

    data_result = raw_data.strip().split("|")
    # print("data_result:",data_result)

    match choose :
        case 1 :
            print(f"Hiển thị dữ liệu gốc: {raw_data}")


        case 2:
            for employee in data_result :

                employee_detail = employee.split(";")

                # print("employee_detail: ",employee_detail)
                id_employee = employee_detail[0].upper()
                full_name_employee = employee_detail[1].title()
                department_employee = employee_detail[3].upper()
                phone_employee = employee_detail[2].strip().replace("-","")

                # print("phone_employee" ,phone_employee)
                if phone_employee.isdigit():
                    phone_employee = "******" + phone_employee[-4:]
                else :
                    phone_employee = "Invalid Format"

                print(f"id_employee: {id_employee} | full_name_employee : {full_name_employee} | department_employee : {department_employee} | phone_employee : {phone_employee}")

        case 3:
                found = False
                search_id=input('Nhap id nhan vien can tim').strip().upper()
                for employee in data_result :
                    employee_detail = employee.split(";")
                    id_employee = employee_detail[0].strip().upper()
                    
                    full_name_employee = employee_detail[1].title()
                    department_employee = employee_detail[3].upper()
                    phone_employee = employee_detail[2].strip().replace("-","")
                    if phone_employee.isdigit():
                        phone_employee = "******" + phone_employee[-4:]
                    else :
                        phone_employee = "Invalid Format"
                    if search_id==id_employee:
                        print('\n===Thong tin nhan vien ===')
                        print(f'Ten nhsan vien { full_name_employee } ')
                        print(f'Chuc vu { department_employee } ')
                        print(f'so dien thoai { phone_employee } ')
                        found= True
                        break
                if found == False :
                    print ('Khong tim thay nhan vien')      
           
            
        case 4:
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")

