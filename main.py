import os
try:
    import pyautogui
    import time
    import keyboard
    import random
    import subprocess
    import sys
    from colorama import *
except:
    os.system('pip install pyautogui')
    os.system('pip install keyboard')
    os.system('pip install colorama')
    import pyautogui
    import time
    import keyboard
    import random
    import subprocess
    import sys
    from colorama import *
just_fix_windows_console()
init()

def open_edge(url):
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    
    if not os.path.exists(edge_path):
        print("INSTALL MS EDGE!!!")
        sys.exit(1)

    
    subprocess.run([edge_path, url])


url = "https://minecraftrating.ru/add-server/"

nahlebnik_ip, adds, server_ip, user_x, user_y, name = '', 0, '', 1680, 1050, ''

def moveCur(x, y, duration):
    global user_x, user_y
    _x = x/1680 # да, у меня такой моник (16:10) И все подгонял я тоже по нему
    _y = y/1050
    __x = _x*user_x
    __y = _y*user_y
    pyautogui.moveTo(__x, __y, duration=duration)
    

def start_pooling():
    
    global nahlebnik_ip, adds, server_ip, name



    
    time.sleep(10)
    
    x, y = 500, 300  

    
    moveCur(x, y, duration=0.5)
    # Ввод "айпи-нахлебника"
    
    
    pyautogui.click()
    random_num = str(random.randint(0,999999))

    
    pyautogui.write(f'play{random_num}.{nahlebnik_ip}')
    
    x, y = 1150, 300  

    
    moveCur(x, y, duration=0.5)  
    pyautogui.click()
    # жмякаем "добавить"


    x, y = 850, 570  


    moveCur(x, y, duration=0.5) 
    time.sleep(10)
    pyautogui.click()
    # переходим на страницу сервера

    time.sleep(10)
    x, y = 1450, 600


    


    moveCur(x, y, duration=0.5)
    time.sleep(10)
    pyautogui.click()
    # жмякаем "редактировать"
    time.sleep(10)
    
    x, y = 650, 450  

   
    moveCur(x, y, duration=0.5)  
    pyautogui.click()
    # выбираем категорию "выживание"
    x, y = 650, 800  


    moveCur(x, y, duration=0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')  
    


    pyautogui.press('backspace')
    pyautogui.write(name)
    # меняем имя
    x, y = 5000, 100
    moveCur(x, y, duration=0.5)

    pyautogui.scroll(-50000)
    #скроллим вниииииииз


    x, y = 1000, 250


    moveCur(x, y, duration=0.5)
    

    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    


    pyautogui.press('backspace')
    
    random_num = str(random.randint(50,999999))
    

    pyautogui.write(f'play{random_num}.{server_ip}') #меняем ip
    
    x, y = 350, 660


    moveCur(x, y, duration=0.5)
    

    pyautogui.click()
    # жмем "сохранить"


    time.sleep(5)

    
    pyautogui.hotkey('ctrl', 'w') #закрываем окно
def main():
    global nahlebnik_ip, adds, server_ip, name, user_x, user_y
    print(Fore.GREEN + '''

        __  ____                            ______  ____        __  _            
       /  |/  (_)___  ___  ______________ _/ __/ /_/ __ \____ _/ /_(_)___  ____ _
      / /|_/ / / __ \/ _ \/ ___/ ___/ __ `/ /_/ __/ /_/ / __ `/ __/ / __ \/ __ `/
     / /  / / / / / /  __/ /__/ /  / /_/ / __/ /_/ _, _/ /_/ / /_/ / / / / /_/ / 
    /_/  /_/_/_/_/_/\___/\___/_/   \__,_/_/  \__/_/ |_|\__,_/\__/_/_/ /_/\__, /  
              / ___/____  ____ _____ ___  ____ ___  ___  _____          /____/   
              \__ \/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/                   
             ___/ / /_/ / /_/ / / / / / / / / / / /  __/ /                       
            /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/     v1.0 | by MrRabbitson 
                /_/                                                                                                                       

    ''')
    print(Fore.RED + '''
>>>      Внимание! Вам необходимо создать аккаунт для бота, иначе спаммер не работает!      <<<

>>> Attention! You need to create an account for the bot, otherwise the spammer won't work! <<<
''')
    print(Fore.CYAN + '''

    ╔════════════════════════════╗
    ╠   Select Your Language
    ╠       (Eng or Rus? )
    ╚════════════════════════════╝

    ''')
    while True:
        _lang_prompt = input()
        if _lang_prompt.lower() == 'eng' or _lang_prompt.lower() == 'english' or _lang_prompt.lower() == 'en':
            language = 1
            break
        elif _lang_prompt.lower() == 'rus' or _lang_prompt.lower() == 'ru' or _lang_prompt.lower() == 'russian':
            language = 2
            break
    
    if language == 2:
        print('''

    ╔════════════════════════════╗
    ╠   Окей, сколько раз ты 
    ╠  хочешь добавить сервер?
    ╚════════════════════════════╝

    ''')
    else:
        print('''

    ╔════════════════════════════╗
    ╠Okay, how many times have you 
    ╠Do you want to add a server?
    ╚════════════════════════════╝
    

''')
    adds = int(input())
    if language == 2:
        print('''

    ╔════════════════════════════╗
    ╠        Окей, введи 
    ╠    айпи твоего сервера
    ╚════════════════════════════╝

    ''')
    else:
        print('''

    ╔════════════════════════════╗
    ╠    Okay, please give me 
    ╠      your server ip
    ╚════════════════════════════╝
    

''')
    server_ip = input('')
    if language == 2:
        print('''

    ╔════════════════════════════╗
    ╠        Окей, введи 
    ╠  расширение твоего экрана
    ╠   (например 1920x1080)
    ╚════════════════════════════╝

    ''')
    else:
        print('''

    ╔════════════════════════════╗
    ╠    Okay, please give me 
    ╠   your screen resolution
    ╠       ex. 1920x1080
    ╚════════════════════════════╝
    

''')
    resolution = input()
    try:
        user_x, user_y = resolution.split('x')
        user_x = int(user_x)
        user_y = int(user_y)

    except ValueError:
        print(Fore.RED + "Ошибка: Вы ввели неверное расширение. Будет использовано 1680x1050")
        user_x, user_y = 1680, 1050
        
    if language == 2:
        print(Fore.CYAN + '''

    ╔════════════════════════════╗
    ╠        Окей, введи 
    ╠    имя твоего сервера
    ╚════════════════════════════╝

    ''')
    else:
        print('''

    ╔════════════════════════════╗
    ╠    Okay, please give me 
    ╠      your server name
    ╚════════════════════════════╝
    

''')

    name = input('')

    if language == 2:
        print('''

    ╔════════════════════════════╗
    ╠        Теперь введи 
    ╠    айпи сервера, который
    ╠    поддерживает заход с
    ╠      любого поддомена
    ╚════════════════════════════╝

    ''')
    else:
        print('''

    ╔════════════════════════════╗
    ╠        Now give me 
    ╠ the IP address of the server
    ╠ that supports connects from
    ╠       any subdomain
    ╚════════════════════════════╝
    

''')
    nahlebnik_ip = input('')
    time_for_add = adds*5
    print(Fore.RED + f'''
Take your hands off the mouse and keyboard and leave the computer for about {time_for_add} minutes!

Уберите руки от мыши и клавиатуры и оставьте компьютер. Процесс займет примерно {time_for_add} минут!

''')
    for i in range(0, 5, 1):
        timer = 5 - i
        print(Fore.YELLOW + f'>>> Запуск через: {timer}')
        print(Fore.YELLOW + f'>>> Start in: {timer}\n')
        time.sleep(1)


# Запуск меню
main()

# Сами добавления ( знаю, я пишу оч плохо, но эт хотябы работает! сорри за мой говнокод)) )
# также я не добавил проверку на число и т.п..... ну можете ломать прогу, что с этого?) XD
for i in range(adds):
    open_edge(url)
    start_pooling()

