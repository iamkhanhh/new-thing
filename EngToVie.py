import os
# from IPython.display import clear_output

def showMenu():
    print("""
Moi ban chon chuc nang :

1. Xem toan bo danh sach
2. Tra cuu
3. sua tu dien
4. ket thuc
    """)
    print()
    choice = int(input('Nhap chuc nang nguoi dung : '))
    return choice

def showDict():
    with open('Dict.txt', 'r') as f:
        dataset = f.readlines()
        
        for index in range(len(dataset)):
            lst = dataset[index].strip().split()
            print(lst[0] + ' : ' + ' '.join(lst[1:]))

def search_word():
    with open('Dict.txt', 'r') as f:
        dataset = f.readlines()

        # Process input from console
        en_sentence = input('Please type an english sentence: ')
        print()
        is_found = False
        for index in range(len(dataset)):
            lst = dataset[index].strip().split()
            if en_sentence == lst[0]:
                print(lst[0] + ' : ' + ' '.join(lst[1:]))
                is_found = True
                break

        if not is_found:
            print('Khong tim thay!')
    

while True:
#     clear_output()
    choice = showMenu()
#     os.system('cls')
    clear_output()
    if (choice == 1):
        # xem toan bo tu dien
        clear_output()
        showDict()
        pass
    elif choice == 2:
        # tra cuu
        clear_output()
        search_word()
        pass
    elif choice == 3:
        # sua tu dien
        clear_output()
        pass
    elif choice == 4:
        break
#     else:
#         print('Moi ban nhap lai')
    print()
    print("ban co muon tiep tuc khong ? (co / khong) ")
    is_continue = input()
    if is_continue == 'co':
        clear_output()
    else:
        break

print('done.')
