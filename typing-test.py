import random
import time
from IPython.display import clear_output

easy = {
    'ex1' : "Students can evaluate their teachers nowadays. Universities allow students to make it clear while teacher is teching properly or not. A well famous term 'visiting faculty' simply means as if teacher is not delivering his concepts to students he will be no more with the university's job.",
    'ex2' : "In education system science more important than literature and history. Most students chose science instead of history since they tend to think that in future science can help more than history, I would say it has more positive development than negative.",
    'ex3' : "It is generally agree today that learners in high schools do not have much time for outdoor exercises and picnic. The reason for this issue that student spend almost their time for learning, chatting or going to bed. In this essay, we will discuss the fallout and give my opinion.",
    'ex4' : "It is undeniable that the competition in the employment market is escalating dramatically. It is often believed that these days Youth is experiencing a competition with the elderly for the similar designations. This essay will discuss the potential reason for this situation and a logical solution.",
    'ex5' : "As the digital revolution moves in education, students are used to computers more and more. As a matter of fact, pencils and books are part of the old times. Will the role of the teachers in the classroom change? Of course, their role will change because they are integral individuals in the education system.",
}

normal = {
    'ex1' : "During the pandemic, many organizations allowed work from home for their employees. Even after the re-opening of enterprises, a lot of employees prefer to stay back and continue working from home instead of going to office. Few people argue that mixing work and family may create tensions at home, however I disagree with this point of view. I believe that the flexibility of working form home brings in more balance in people's life and is more beneficial for the housefold as it allows family bonding. In this essay, I will disucss both the views, and explain with examples my support for the concept of work from home.",
    'ex2' : "There are controversial perspectives heating up a debate over the schooling system of boys and girls. While some people claim that citizens ought to over-letting boys and girls to absorb insights in a co-educational system, the opposite site makes a statement that it is better to educate them in separate schools. While the latter is valid to some extent, I consider myself as an advocate of the former.",
    'ex3' : "Moreover, training in the native place helps one to learn the language with the right pronunciation. Certain words have different ways to pronounce. For example, some words when pronounced in the wrong way can completely change the entire meaning of the word or the sentence. Therefore, it is of utmost importance to narrate in the right manner. Furthermore,  constantly being in touch with the native language people, enables us to become more efficient and effective in the way we speak. It empowers us with confidence and courage. Thus, this learning experience opens a window into a unique world filled with opportunities and advancements.",
    'ex4' : "Even though the invention of the aeroplane has made it easy to travel that people around the globe are permanently living in other countries. However, they are still making their own community wherever they start to live, it still represents their nationality. In other words, Brampton is mainly known as a Punjabi community and it still shows that person is living there are from Punjab, India. As the result, the country can represent its integrity in several ways which can not be destroyed by globalization",
    'ex5' : "During the pandemic, many organizations allowed work from home for their employees. Even after the re-opening of enterprises, a lot of employees prefer to stay back and continue working from  home instead of going to the office. Few people argue that mixing work and family may create tensions at home, ,however I disagree with this point of view. I believe that the flexibility of working from home brings  more balance in people's lives and is more beneficial for the household as it allows family bonding. In this essay, I will discuss both  views, and explain with examples my support for the concept of working from home.",
}

hard = {
    'ex1' : "It is asserted by few that international programmes such as the Olympic games are crucial and help to enhance the relationship between other countries but there is a strong counter-argument amongst sections of people that they are a waste of resources as the amount can be spent on the country's infrastructure development.This is a matter to be debated in the light of several factors which would be discussed in the following paragraphs along with my opinion.",
    'ex2' : "To commence with, the first merit of sharing an apartment is cost-effectiveness. Rent and all other expenses will be divided among two folks. Therefore, a person will have more money in his pocket that he can use to pay for tuition and books. Moreover, having a company of a friend helps with homesickness. A significant number of individuals leave their homes to pursue their careers, dreams or study thus, having a friend can reduce the feeling of loneliness. For instance, it has been observed that 60% of  student feels less isolated when they live with a friend than living by themselves.",
    'ex3' : "In 1968, the number of food was the highest, at exactly 35%, which was over 30% higher than that of fuel and power. Followed by the cost of housing, clothing and footwear, which shared an equal number, accounted for 10% each. The other spending remained at around 8%. By 2018, approximately 22% of leisure spending was the highest, almost rising by 15% compared to the number of fuel and power. The figure for transport and housing also experienced an increase throughout four decades, with nearly 15% and roughly 19% respectively.",
    'ex4' : "On the paradoxical side, there are certain groups of individuals who vehemently contend that  doing business during the break makes the child  learn essential life lessons. The most prominent is that they improve their communication skills.They get to know how to deal with the customer selling a product.For instance, when they deal with a client they learn how to convince them to buy the goods and understand consumer needs as well as which helps a pupil to learn how to deal with the consumer. Furthermore,gain  experience from experts who are working for a long time in a particular field.",
    'ex5' : "On the one hand, it is often argued that there is no point in stopping  natural phenomena because they are out of our control. It is a matter of fact that numerous disasters such as T-sunami, earthquakes and devastating storms albeit warned about in advance are unstoppable.  For example, there is nothing that can be done to fight storms in the middle part of Vietnam despite their frequent occurrence. All  we can do is predict them and try to limit the number of casualties to a minimum rate. Hence, it is easy to see why this argument is strongly supported.",
}

def check(sample, user, timing):
    clear_output()
    wrong_dict = {}
    sample_lst = sample.split()
    user_lst = user.split()
    mark = 0
    lst_check = user_lst if len(user_lst) < len(sample_lst) else sample_lst
    for i in range(len(lst_check)):
        if user_lst[i] != sample_lst[i]:
            wrong_dict[sample_lst[i]] = user_lst[i]
        else:
            mark += 1
    WPM = mark / (timing / 60)
    Accuracy = round((mark / len(user_lst)) * 100, 2)
    WPM = round(WPM, 2)
    if WPM < 60:
        quality = 'Low level'
    elif 60 <= WPM and WPM < 100:
        quality = 'Medium level'
    elif 100 <= WPM and WPM < 140:
        quality = 'High level'
    elif WPM >= 140:
        quality = 'professional level'
    print(f'Your level : {quality}')
    print(f'Accuracy : {Accuracy}%')
    if timing < 60:
        print(f'Your time : {round(timing, 2)}s')
    else:
        print(f'Your time : {round(timing/60, 2)}p')
    print(f'WPM (Word per minute) : {WPM}')
    print()
    print('Wrong word list : ')
    for word in wrong_dict:
        print('{:<10} : {:<12}'.format(word, wrong_dict[word]))
    print()
    input('Press an key board to continue !')
    

def countdown(t):
    while t != -1:
        mins, secs = divmod(t, 60)  #tách phút và giây từ biến t
        timeformat = '{:02d}:{:02d}'.format(mins, secs) #định dạng thời gian hiển thị đếm ngược
        print('bắt đầu làm trong ', timeformat, end='\r') #hiển thị thời gian đếm ngược
        time.sleep(1) # chờ 1s và update thời gian
        t -= 1 #đếm ngược từng giây cho tới 0

def random_sample():
    val = random.randint(1, 5)
    return val

def mode_easy():
    countdown(5)
    clear_output()
    sample = random_sample()
    print(f'''
Sample :
{easy['ex' + str(sample)]}
    ''')
    print('Typing section : ')
    start = time.time()
    typing = input()
    end = time.time()
    time_tying = end - start
    check(easy['ex' + str(sample)], typing, time_tying)
    
while True:
    clear_output()
    print("""
Choose difficulty :
1. easy
2. normal
3. hard
4. quit
    """)
    choice = int(input('Your choice : '))
    if choice == 1:
        clear_output()
        #mode easy
        mode_easy()
    elif choice == 2:
        clear_output()
        #mode normal
        pass
    elif choice == 3:
        clear_output()
        #mode hard
        pass
    elif choice == 4:
        break

clear_output()
print('DONE !')
