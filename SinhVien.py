listsv=[]
class SinhVien():
    __id=''
    __name=''
    def findsv(seft,id):
        for i in range(0,len(listsv)):
            if listsv[i].__id==id:
                return i
        else: return -1
    def addsv(seft):
        print("***THEM SINH VIEN***")
        print("Return <--- (0)")
        id=input("Nhap ID sinh vien: ")
        if id!='0':
            while True:
                if seft.findsv(id)!=-1:
                    id=input("ID nay da ton tai, vui long nhap ID khac")
                    if id=='0': break
                else: 
                    seft.__id=id
                    break
            name=input('Nhap ten sinh vien: ')
            seft.__name=name
            listsv.append(seft)
    def delsv(seft):
        print("***XOA SINH VIEN***")
        print("Return <--- (0)")
        id=input("Nhap ID sinh vien: ")
        if int(id)!=0:
            while True:
                if seft.findsv(id)!=-1:
                    listsv.pop(seft.findsv(id))
                    break
                else: 
                    id=input("Khong tim thay ID, vui long nhap lai: ")
                    if id=='0': break
    def editsv(seft):
        print("***SUA SINH VIEN***")
        print("Return <--- (0)")
        id=input("Nhap ID sinh vien: ")
        if int(id)!=0:
            while True:
                if seft.findsv(id)!=-1:
                    name=input('Nhap ten moi:')
                    listsv[seft.findsv(id)].__name=name
                    break
                else: 
                    id=input("Không tìm thấy ID, vui lòng nhập lại: ")
                    if id=='0': break                
    def showsv(seft):
        print("***DANH SACH SINH VIEN***")
        for x in listsv:
            print(x.__id," ",x.__name)





