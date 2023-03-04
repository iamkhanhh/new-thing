class contact:
    def __init__(self,name,number,address = '',email = ''):
        self.name = name
        self.number = number
        self.address = address
        self.email = email
    def __str__(self):
        return  f'{self.name} - {self.number} - {self.address} - {self.email}'
    def edit(self,which,temp):
        if which == 'number':
            self.number = temp
        elif which == 'address': 
            self.address = temp
        elif which == 'email':
            self.email = temp
        elif which == 'name':
            self.name = temp
    def getNumber(self):
        return self.number
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getName(self):
        return self.name
    
contacts = []
# khanh = contact('khanh','0347708169', 'tam hiep', 'khanh9102004@gmail.com')
# chi = contact('chi','1234567899', 'tu hiep', 'mailinhchi2107@gmail.com')
# contacts.extend([khanh,chi])
print('''
hay chon dich vu :
1. xem toan bo danh sach
2. tim kiem
3. them lien lac
4. xoa lien lac
5. thay doi thong tin
6. ket thuc
''')
service = int(input())

while True:
    if service == 1:
        for contact in contacts:
            print(contact)
    elif service == 2:
        search = input('ban muon tim ten, so dien thoai, dia chi hay email : ')
        if search == 'ten':
            find = input('moi ban nhap so dien thoai: ')
            for contact in contacts:
                if find == contact.getNumber():
                    print('ten can tim la :',contact.getName())
        elif search == 'so dien thoai':
            find = input('moi ban nhap ten : ')
            for contact in contacts:
                if find == contact.getName():
                    print('so dien thoai can tim la :',contact.getNumber())
        elif search == 'dia chi':
            find = input('moi ban nhap ten : ')
            for contact in contacts:
                if find == contact.getName():
                    print('dia chi can tim la :',contact.getAddress())
        elif search == 'email':
            find = input('moi ban nhap ten : ')
            for contact in contacts:
                if find == contact.getName():
                    print('email can tim la :',contact.getEmail())
    elif service == 3:
        name = input('moi ban nhap ten: ')
        sdt = input('moi ban nhap sdt: ')
        address = input('moi ban nhap dia chi: ')
        email = input('moi ban nhap email: ')
        name = contact(name,sdt,address,email) 
        contacts.append(name)
    elif service == 4:
        deleteContact = input('nhap ten nguoi muon xoa: ')
        for contact in contacts:
            if contact.getName() == deleteContact:
                contacts.remove(contact)
    elif service == 5:
        search = input('nhap ten hoac so dien thoai can sua: ')
        edit = input('ban muon sua phan nao (name, number, address, email): ')
        new = input('nhap noi dung moi: ')
        for contact in contacts:
            if search == contact.getName() or search == contact.getNumber():
                contact.edit(edit, new) 
    elif service == 6:
        break
    print('''
hay chon dich vu :
1. xem toan bo danh sach
2. tim kiem
3. them lien lac
4. xoa lien lac
5. thay doi thong tin
6. ket thuc
''')
    service = int(input())
