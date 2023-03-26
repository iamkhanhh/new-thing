import os
from IPython.display import clear_output

import pyttsx3
from pynput import keyboard
from googletrans import Translator
import speech_recognition as sr


def showMenu():
    print(
"""
Mời bạn chọn chức năng :

1. Xem toàn bộ danh sách
2. Tra cứu
3. Sửa từ điển (không khuyến khích dùng)
4. Dịch văn bản
5. Kết thúc tra cứu
""")
    print()
    choice = int(input('Nhập chức năng người dùng : '))
    return choice

def speaker(eng):
    engine = pyttsx3.init()
    engine.say(eng)
    engine.runAndWait()
    rate = engine.getProperty('rate') 
    engine.setProperty('rate', 150)

def add_word(eng, vie):
    with open('Dict.txt', 'a', encoding='utf-8') as f:
        f.write(eng + ' ' + vie + '\n')
    print('Đã thêm thành công !')

def delete_word(eng):
    result = []
    with open('Dict.txt', 'r', encoding='utf-8') as f:
        lst = f.readlines()

        for line in lst:
            if eng not in line:
                result.append(line)

    with open('Dict.txt', 'w', encoding='utf-8') as f:
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
3. Quay về
    """)
    print()
    choice = int(input('Nhập chức năng người dùng hoặc -1 để quay lại: '))
    if choice == -1:
        return
    if choice == 1:
        # them tu moi
        clear_screen()
        eng = input('Nhập từ tiếng anh : ')
        vie = input('Nhap nghia tieng viet : ')
        add_word(eng, vie)
        clear_screen()
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
        # search_word()
        delete_word(eng)
    elif choice == 3:
        clear_screen()
        mainMenu()
        return
    else:
        clear_screen()
        print("vui long nhap lai !")
        print()
        edit_dict()

def print_dict(dataset):
    print("{:<10}  {:<12}".format("Từ", "Nghĩa"))
    for index in dataset:
        lst = index.strip().split()
        print("{:<10} : {:<12}".format(lst[0], " ".join(lst[1:])))


def showDict():
    with open('Dict.txt', 'r', encoding='utf-8') as f:
        dataset = f.readlines()
    size_ = len(dataset)//5
    lastPage = len(dataset)%5
    pages = size_ if lastPage == 0 else size_ + 1
    page_num = 1
    start = 0
    end = 5
    subdataset = dataset[0:5]
    # print(subdataset)
    clear_screen()
    print(f'Trang {page_num}/{pages}: ')
    print_dict(subdataset)
    print("\n"+"Nhấn phím trái phải để sang trang, esc để thoát")
    def on_press(key):
        nonlocal start, end, page_num, pages, subdataset
        try:
            if key == keyboard.Key.right:
                if end + 5 > len(dataset) and start + 5 < len(dataset):
                    subdataset = dataset[start + 5:end + lastPage]
                    page_num += 1
                    start = len(dataset) - lastPage
                    end = start + 5
                    clear_screen()
                    print(f'Trang {page_num}/{pages}: ')
                    print_dict(subdataset)
                    print("\n"+"Nhấn phím trái phải để sang trang, esc để thoát")
                elif end < len(dataset) and start < len(dataset):
                    start += 5
                    end += 5
                    subdataset = dataset[start:end]
                    page_num += 1
                    clear_screen()
                    print(f'Trang {page_num}/{pages}: ')
                    print_dict(subdataset)
                    print("\n"+"Nhấn phím trái phải để sang trang, esc để thoát")
                    
            elif key == keyboard.Key.left:
                if start != 0:
                    start -= 5
                    end -= 5
                    page_num -= 1
                    subdataset = dataset[start:end]
                    clear_screen()
                    print(f'Trang {page_num}/{pages}: ')
                    print_dict(subdataset)
                    print("\n"+"Nhấn phím trái phải để sang trang, esc để thoát")
                    
            elif key == keyboard.Key.esc:
                clear_screen()
                return False
            
        except Exception as e:
            print(f'Error: {e}')
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def search_word():
    with open('Dict.txt', 'r', encoding='utf-8') as f:
        dataset = f.readlines()
        # Process input from console
        # print_dict(dataset)
        while True:
            
            en_sentence = input('Hãy nhập từ cần tra hoặc -1 để thoát: ')
            clear_screen()
            if en_sentence == "-1":
                return
            print()
            is_found = False
            is_exactly = False
            num = 0
            for index in range(len(dataset)):
                lst = dataset[index].strip().split()
                if en_sentence.lower() == lst[0].lower():
                    print("{:<10} {:<12}".format(lst[0], " ".join(lst[1:])))
                    is_found = True
                    is_exactly = True
                    word_to_speak = en_sentence
                    break
                    
                elif en_sentence.lower() in lst[0].lower():
                    print("{:<10} {:<12}".format(lst[0], " ".join(lst[1:])))
                    is_found = True
                    num += 1
                    if num == 1:
                        word_to_speak = lst[0]

            if not is_found:
                print('Khong tim thay ! Vui long nhap lai !')
                search_word()
                return False
            
            if is_exactly or num == 1:
                while True:
                    
                    listen = input('Ban co muon nghe phat am khong (co / khong) : ')
                    if listen == 'khong':
                        clear_screen()
                        search_word()
                        return
                    clear_screen()
                    print("{:<10} {:<12}".format(lst[0], " ".join(lst[1:])))
                    speaker(word_to_speak)
                
          
def transalte_essay():
    while True:
        clear_screen()
        print('''
Hãy chọn chức năng :
1. eng -> vie
2. vie -> eng
3. trở về menu
        ''')
        print()
        mode = int(input('Nhập chức năng để tiếp tục  : '))
        if mode == 3:
            break
#         while mode != 3:
        elif mode == 1:
            choice = isRecog()
            if choice:
                text = voice_recog("en-US")
                engTrans(text)
                input('Nhấn phím bất kỳ để quay lại : ')
                continue
            elif choice == -1:
                break
            else:
                clear_screen()
#                     while True:
                eng = input('Hãy nhập văn bản tiếng anh hoặc -1 để quay lại: ')
                engTrans(eng)
                input('Nhấn phím bất kỳ để quay lại : ')
                continue
        elif mode == 2:
            choice = isRecog()
            if choice:
                text = voice_recog("vi-Vn")
                vieTrans(text)
                input('Nhấn phím bất kỳ để quay lại : ')
                continue
            elif choice == -1:
                break
            else:
                clear_screen()
#                     while True:
                vie = input('Hãy nhập văn bản tiếng anh hoặc -1 để quay lại: ')
                vieTrans(vie)
                input('Nhấn phím bất kỳ để quay lại : ')
                continue
#             clear_screen()
#             break
    clear_screen()
    return 

def engTrans(eng):
    clear_screen()
#     while True:
#         eng = input('Hãy nhập văn bản tiếng anh hoặc -1 để quay lại: ')
    clear_screen()
#     if eng == "-1": break
    translate = Translator()
    result = translate.translate(eng, src='en', dest='vi')
    print("Văn bản gốc: ", eng)
    print("Văn bản đã dịch: ",result.text)

def vieTrans(vie):
    clear_screen()
#         vie = input('Hãy nhập văn bản tiếng việt hoặc -1 để quay lại: ')
    clear_screen()
#     if vie == "-1": break
    translate = Translator()
    result = translate.translate(vie, src='vi', dest='en')
    print("Văn bản gốc: ", vie)
    print("Văn bản đã dịch: ",result.text)
        
        
def isRecog():
    while True:
        clear_screen()
        print("""Chọn phương thức nhập:
1. Gõ văn bản
2. Nhận diện giọng nói
3. Quay lại""")
        transMode = int(input("Lựa chọn phương thức: "))
        if transMode == 1:
            return False
        elif transMode == 2:
            return True
        elif transMode == 3:
            return -1
    

def voice_recog(lang):
#     lang: "vi-Vn" or "en-US"
    # Create a recognizer object
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language= lang)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        
    return text
      
            
def clear_screen():
    os.system('cls')
    clear_output()
    
    
def mainMenu():
    clear_screen()
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
            # dich van ban
            clear_screen()
            transalte_essay()
        elif choice == 5:
            break

    print('Chuong trinh da dung')
mainMenu()
