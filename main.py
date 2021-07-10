import SinhVien
action=0
while action>=0:
    sv=SinhVien.SinhVien()
    if action == 1:
        sv.addsv()
    elif action == 2:
        sv.delsv()
    elif action == 3:
        sv.editsv()
    elif action == 4:
        sv.showsv()
    print("Chọn chức năng muốn thực hiện:")
    print("Nhập 1: Thêm sinh viên")
    print("Nhập 2: Xóa sinh viên") 
    print("Nhập 3: Sửa sinh viên")
    print("Nhập 4: Xem danh sách sinh viên")
    print("Nhập 0: Thoát khỏi chương trình")    
    action=int(input())
    if action==0: break  
