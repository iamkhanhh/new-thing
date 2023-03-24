import os
import pyttsx3
from IPython.display import clear_output

def showMenu():
    print(
"""
Mời bạn chọn chức năng :

1. Xem toàn bộ danh sách
2. Tra cứu
3. Sửa từ điển
4. Kết thúc tra cứu
""")
    print()
    choice = int(input('Nhập chức năng người dùng : '))
    return choice

def speaker(eng):
    engine = pyttsx3.init()
    engine.say(eng)
    engine.runAndWait()

def add_word(eng, vie):
    with open('C:\\Users\\Admin\\Dict.txt', 'a', encoding='utf-8') as f:
        f.write(eng + ' ' + vie + '\n')
    print('Đã thêm thành công !')

def delete_word(eng):
    result = []
    with open('Dict.txt', 'r', encoding='utf-8') as f:
        lst = f.readlines()

        for line in lst:
            if eng not in line:
                result.append(line)

    with open('C:\\Users\\Admin\\Dict.txt', 'w', encoding='utf-8') as f:
        for line in result:
            f.write(line)

    print('Đã xóa thành công !')
    
def edit_word(false_word):
    delete_word(false_word)
    replace_word = input('Nhập từ mới : ')
    new_meaning =  input('Nghĩa Tiếng Việt : ')
    add_word(replace_word, new_meaning)

def edit_dict():
    print("""
Hãy chọn chức năng :

1. Thêm từ mới
2. Xóa từ
    """)
    print()
    choice = int(input('Nhập chức năng người dùng : '))
    if choice == 1:
        # them tu moi
        clear_screen()
        eng = input('Nhập từ tiếng anh : ')
        vie = input('Nhap nghia tieng viet : ')
        add_word(eng, vie)
        print()
        print(f"""
Tu {eng} : {vie} vua duoc them vao tu dien, ban co muon sua doi khong ? (co / khong)
    """)
        edit = input()
        if edit == 'co':
            edit_word(eng)
    elif choice == 2:
        #xoa tu 
        clear_screen()
        eng = input('Nhap tu tieng anh can xoa : ')
        delete_word(eng)
    else:
        clear_screen()
        print("vui long nhap lai !")
        print()
        edit_dict()

def showDict():
    with open('C:\\Users\\Admin\\Dict.txt', 'r', encoding='utf-8') as f:
        dataset = f.readlines()
        print("{:<15} {:<15}".format("Từ", "Nghĩa"))
        print()
        for index in range(len(dataset)):
            lst = dataset[index].strip().split()
            print("{:<15} {:<15}".format(lst[0], " ".join(lst[1:])))

def search_word():
    with open('C:\\Users\\Admin\\Dict.txt', 'r', encoding='utf-8') as f:
        dataset = f.readlines()

        # Process input from console
        en_sentence = input('Hãy nhập từ cần tra : ')
        print()
        is_found = False
        is_exactly = False
        num = 0
        for index in range(len(dataset)):
            lst = dataset[index].strip().split()
            if en_sentence == lst[0]:
                print("{:<10} {:<12}".format(lst[0], " ".join(lst[1:])))
                is_found = True
                is_exactly = True
                word_to_speak = en_sentence
                break
            elif en_sentence == lst[0][0]:
                print("{:<10} {:<12}".format(lst[0], " ".join(lst[1:])))
                is_found = True
                num += 1
                if num == 1:
                    word_to_speak = lst[0]

        if not is_found:
            print('Khong tim thay ! Vui long nhap lai !')
            search_word()
    if is_exactly or num == 1:
        while True:
            listen = input('Ban co muon nghe phat am khong (co / khong) : ')
            if listen == 'khong':
                break
            clear_screen()
            speaker(word_to_speak)
        
    return
            
def clear_screen():
    os.system('cls')
    clear_output()
    
    

while True:
    choice = showMenu()
    clear_screen()
    if (choice == 1):
        # xem toan bo tu dien
        clear_screen()
        showDict()
    elif choice == 2:
        # tra cuu
        clear_screen()
        search_word()
    elif choice == 3:
        # sua tu dien
        clear_screen()
        edit_dict()
    elif choice == 4:
        break
    print()
    print("ban co muon tiep tuc tra cuu khong ? (co / khong) ")
    is_continue = input()
    if is_continue == 'co':
        clear_screen()
    else:
        break

print('done.')
