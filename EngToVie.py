import os
# from IPython.display import clear_output

def showMenu():
    print(
"""
Mời bạn chọn chức năng :

1. Xem toan bo danh sach
2. Tra cuu
3. sua tu dien
4. ket thuc
""")
    print()
    choice = int(input('Nhap chuc nang nguoi dung : '))
    return choice

def add_word(eng, vie):
    with open('C:\\Users\\Admin\\Dict.txt', 'a', encoding='utf-8') as f:
        f.write(eng + ' ' + vie + '\n')
    print('Da them thanh cong !')

def delete_word(eng):
    result = []
    with open('C:\\Users\\Admin\\Dict.txt', 'w+', encoding='utf-8') as f:
        lst = f.readlines()

        for line in lst:
            if eng not in line:
                result.append(line)

        for line in result:
            f.write(line + '\n')

    print('Da xoa thanh cong !')

def edit_dict():
    print("""
Hay chon chuc nang :

1. Them tu moi
2. Xoa tu
3. Sua tu
    """)
    print()
    choice = int(input('Nhap chuc nang nguoi dung : '))
    if choice == 1:
        # them tu moi
        clear_screen()
        eng = input('Nhap tu tieng anh : ')
        vie = input('Nhap nghia tieng viet : ')
        add_word(eng, vie)
        return
    elif choice == 2:
        #xoa tu 
        clear_screen()
        eng = input('Nhap tu tieng anh can xoa : ')
        delete_word(eng)
        return
    elif choice == 3:
        #sua tu
        pass
    else:
        clear_screen()
        print("vui long nhap lai !")
        print()
        edit_dict()

def showDict():
    with open('C:\\Users\\Admin\\Dict.txt', 'r', encoding='utf-8') as f:
        dataset = f.readlines()
        
        for index in range(len(dataset)):
            lst = dataset[index].strip().split()
            print(lst[0] + ' : ' + ' '.join(lst[1:]))

def search_word():
    with open('C:\\Users\\Admin\\Dict.txt', 'r', encoding='utf-8') as f:
        dataset = f.readlines()

        # Process input from console
        en_sentence = input('Hãy nhập từ cần tra : ')
        print()
        is_found = False
        for index in range(len(dataset)):
            lst = dataset[index].strip().split()
            if en_sentence == lst[0]:
                print(lst[0] + ' : ' + ' '.join(lst[1:]))
                is_found = True
                return

        if not is_found:
            print('Khong tim thay ! Vui long nhap lai !')
            search_word()
            
def clear_screen():
    os.system('cls')
    # clear_output()
    

while True:
    choice = showMenu()
    clear_screen()
    if (choice == 1):
        # xem toan bo tu dien
        clear_screen()
        showDict()
        pass
    elif choice == 2:
        # tra cuu
        clear_screen()
        search_word()
        pass
    elif choice == 3:
        # sua tu dien
        clear_screen()
        edit_dict()
        pass
    elif choice == 4:
        break
#     else:
#         print('Moi ban nhap lai')
    print()
    print("ban co muon tiep tuc khong ? (co / khong) ")
    is_continue = input()
    if is_continue == 'co':
        clear_screen()
    else:
        break

print('done.')
