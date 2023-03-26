# !python -m pip uninstall pyttsx3 --yes 
# !python -m pip uninstall pynput --yes 
# !python -m pip uninstall googletrans --yes 
# !python -m pip uninstall speech_recognition --yes 

import os
import sys
import time
import random
from IPython.display import clear_output
def clear_screen():
    os.system('cls')
    clear_output()
print("Đang kiểm tra yêu cầu phần mềm, vui lòng đợi ...")
# try:
#     import pyttsx3
# except:
#     print("Lỗi: thiếu thư viện pyttsx3")
#     time.sleep(2)
#     print('Đang tải thư viện pyttsx3')
#     !{sys.executable} -m pip install pyttsx3
#     time.sleep(1)
#     clear_screen()
#     print("Đã tải xong thư viện, tiếp tục trong giây lát...")
#     time.sleep(2)

# try:
#     from pynput import keyboard
# except:
#     print("Lỗi: thiếu thư viện pynput")
#     time.sleep(2)
#     print('Đang tải thư viện pynput')
#     !{sys.executable} -m pip install pynput
#     time.sleep(1)
#     clear_screen()
#     print("Đã tải xong thư viện, tiếp tục trong giây lát...")
#     time.sleep(2)
    
# try:
#     from googletrans import Translator
# except:
#     print("Lỗi: thiếu thư viện googletrans")
#     time.sleep(2)
#     print('Đang tải thư viện googletrans')
#     !{sys.executable} -m pip install googletrans
#     time.sleep(1)
#     clear_screen()
#     print("Đã tải xong thư viện, tiếp tục trong giây lát...")
#     time.sleep(2)
    
# try:
#     import speech_recognition as sr
# except:
#     print("Lỗi: thiếu thư viện speech_recognition")
#     time.sleep(2)
#     print('Đang tải thư viện speech_recognition')
#     !{sys.executable} -m pip install speech_recognition
#     time.sleep(1)
#     clear_screen()
#     print("Đã tải xong thư viện, tiếp tục trong giây lát...")
#     time.sleep(2)

def pip_install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Lỗi: thiếu thư viện {package}")
        time.sleep(2)
        print(f"Đang tải thư viện {package}")
        !{sys.executable} -m pip install {package}
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Đã tải xong thư viện {package}, tiếp tục trong giây lát...")
        time.sleep(2)

pip_install("pyttsx3")
pip_install("pynput")
pip_install("googletrans")
pip_install("speech_recognition")

def showMenu():
    print(
"""
Mời bạn chọn chức năng :

1. Xem toàn bộ danh sách
2. Tra cứu
3. Sửa từ điển
4. Dịch văn bản
5. Danh sách từ đã lưu
6. Kiểm tra từ mới
7. Kết thúc tra cứu
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
        f.write(eng.capitalize() + ' ' + vie + '\n')
    print('Đã thêm thành công !')

def delete_word(eng, file = 'Dict.txt'):
    result = []
    with open(file, 'r', encoding='utf-8') as f:
        lst = f.readlines()

        for line in lst:
            if eng.lower() not in line.lower():
                result.append(line)
    
    with open(file, 'w', encoding='utf-8') as f:
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


def showDict(file = 'Dict.txt'):
    with open(file, 'r', encoding='utf-8') as f:
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


def search_word(file = 'Dict.txt'):
    with open(file, 'r', encoding='utf-8') as f:
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
                    meaning_word = " ".join(lst[1:])
                    break
                    
                elif en_sentence.lower() in lst[0].lower():
                    print("{:<10} {:<12}".format(lst[0], " ".join(lst[1:])))
                    is_found = True
                    num += 1
                    if num == 1:
                        word_to_speak = lst[0]
                        meaning_word = " ".join(lst[1:])

            if not is_found:
                print('Khong tim thay ! Vui long nhap lai !')
                search_word()
                return False
            
            if is_exactly or num == 1:
                while True:
                    choice = int(input("Bấm 1 để lưu từ, bấm 2 để phát âm từ, bấm nút 0 để quay lại: "))
                    if choice == 1:
                        saveWord(word_to_speak, meaning_word)
                        clear_screen()
                        
                    elif choice == 2:
                        while True:
                            clear_screen()
                            speaker(word_to_speak)
                            listen = input('Bạn có muốn nghe lại không (co / khong) : ')
                            if listen == 'khong':
                                clear_screen()
                                search_word()
                                return
                    else: break

def saveWord(word, vie):
    with open('savedWord.txt', 'a', encoding='utf-8') as f:
        f.write(word + ' ' + vie + '\n')
        
    print("Đã lưu từ")
    time.sleep(2)
    
def lst_saved_word():
    print("""
1. Xem danh sách
2. Tra cứu và phát âm
3. Xóa từ
    """)
    choice = int(input('Hãy nhập phương thức : '))
    if choice == 1:
        # xem danh sach
        try:
            showDict('savedWord.txt')
        except:
            clear_screen()
            input('Danh sách rỗng, nhấn phím bất kì để tiếp tục')
    elif choice == 2:
        #tra cuu
        search_word('savedWord.txt')
    elif choice  == 3:
        #xoa tu
        delete_word('savedWord.txt')
          
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

def eng_to_vie_wordRevision():
    clear_screen()
    print("""
    1. Kho từ điển
    2. Kho từ đã lưu
    3. Quay về
    """)
    group = int(input("Lựa chọn phương thức: "))
    if group == 1:
        with open("Dict.txt", "r", encoding="utf-8") as f:
            dataset = f.readlines()
    elif group == 2:
        with open("SavedDict.txt", "r", encoding="utf-8") as f:
            dataset = f.readlines()
            if dataset < 4:
                print("Số lượng từ dưới 4, hãy chọn thêm từ để bắt đầu")
                print("Đang về menu ...")
                time.sleep(3)
                return
    elif group == 3:
        return
    #datadet = []
    clear_screen()
    Qnum = int(input("Nhập số câu bạn muốn luyện: "))
    ABCD_to_int = {"A": 0, "B": 1, "C": 2, "D": 3}
    random.shuffle(dataset)
    question_data = [i.split(" ")[0] for i in dataset]
    random.shuffle(question_data[1:])
    count_correct = 0
    wrongAns = {}
    for i in range(Qnum):
        Question = dataset[i].split(" ")[0]
        CorrectAn= " ".join(dataset[i].split(" ")[1:]).replace("\n","")
        FAsnwer1 = " ".join(dataset[i+1].split(" ")[1:]).replace("\n","")
        FAsnwer2 = " ".join(dataset[i+2].split(" ")[1:]).replace("\n","")
        FAsnwer3 = " ".join(dataset[i+3].split(" ")[1:]).replace("\n","")
        ABCD = [CorrectAn, FAsnwer1, FAsnwer2, FAsnwer3]
        random.shuffle(ABCD)
        print(f"Câu hỏi {i+1}: {Question}")
        print("A.{:<10} B.{:<10} C.{:<10} D.{:<10} ".format(*ABCD))
        choice = input("Chọn đáp án đúng: ").capitalize()
        choice = ABCD_to_int[choice]
        if choice == ABCD.index(CorrectAn):
            count_correct += 1
        else: wrongAns[i+1]= [Question, ABCD[choice], CorrectAn]
    if count_correct - Qnum != 0:
        clear_screen()
        print(f"Bạn đã trả lời đúng {count_correct}/{Qnum} câu hỏi")
        print("Bạn đã chọn sai các câu hỏi sau")
        for i in wrongAns:
            print(f"Câu {i} từ '{wrongAns[i][0]}' bạn đã chọn '{wrongAns[i][1]}'")
            print(f"Đáp án đúng: {wrongAns[i][2]}")
    else: print(f"Bạn đã trả lời đúng {count_correct}/{Qnum} câu hỏi\nXin chúc mừng")
    input("Nhấn phím bất kỳ để tiếp tục")

def wordRevisionMenu():
    while True:
        clear_screen()
        print("""Chọn chức năng:
1. Câu hỏi tiếng Anh
2. Câu hỏi tiếng Việt
3. Quay về""")
        choice = int(input("Nhập lựa chọn: "))
        if choice == 1:
            eng_to_vie_wordRevision()
            break
        elif choice == 2: 
            print("Chức năng này hiện chưa có, xin lỗi vì sự bất tiện này")
            time.sleep(2)
            continue
        elif choice == 3:
            break

def mainMenu():
    clear_screen()
    while True:
        
        result = []
        with open('Dict.txt', 'r', encoding='utf-8') as f:
            lst = f.readlines()

            for line in lst:
                result.append(line)
                
        result.sort()
        
        with open('Dict.txt', 'w', encoding='utf-8') as f:
            for line in result:
                f.write(line)
                
        clear_screen()
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
            #xem tu da luu
            lst_saved_word()
        elif choice == 6:
            #luyen trac nhiem
            wordRevisionMenu()
        elif choice == 7:
            break
    print('Chuong trinh da dung')
# time.sleep(3)
print("Xin chào, chương trình đã hoàn tất thiết lập, khởi động sau giây lát ...")
# time.sleep(2)
mainMenu()
