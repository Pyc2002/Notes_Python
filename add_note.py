from constants import DATA_BASE
import csv
import os.path
from datetime import datetime as dt
import re
from constants import ABILITIES 
import log

def Fieldnames():
    """Create file.csv if it not exists, to avoid duplicate headers
    
    args -> None
    returns -> None
    """
    if not os.path.exists(DATA_BASE): #  проверка существует ли файл (если да, то последующий код  функции не запускается)
        with open(DATA_BASE, 'a', newline = '', encoding='utf-8') as file:
            writer = csv.writer(file,delimiter=';')
            writer.writerow(['ID', 'Заголовок', 'Заметка', 'Дата'])
            file.close()

def Check_text(text): 
    """ Testing input data of first_name and last_name 

    args -> str (input text)
    retuns -> str
    """
    while text == '': 
        text = input('Ошибка! Обязательное поле, повторите ввод: \n') 
    return text.capitalize()
        


def Id_count():
    """ counts the number of rows with testing for number duplication 

    args -> None
    returns -> str
    """
    id = len(re.findall(r"[\n']+", open(DATA_BASE).read()))
    with open(DATA_BASE, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for item in reader:
            while str(id) in item['ID']:
                id += 1 
    return id
    

def Add_note():
    """ Adding data of new note in csv-file. User inputs data (str), def create dict and add it in file.

    args -> None
    returns -> None
    """
    Fieldnames()
    id = Id_count()
    title = Check_text(input('Введите заголовок заметки: \n '))
    text = Check_text(input('Введите текст заметки:\n '))
    datetime = dt.now().strftime('%Y-%m-%d, %H:%M:%S')
    new_contact = {'ID': id,'Заголовок': title, 'Заметка': text, 'Дата' : datetime}

   

    with open (DATA_BASE, mode = 'a', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['ID', 'Заголовок', 'Заметка', 'Дата']
        
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect='excel', restval='', delimiter=';')
        writer.writerow (new_contact)
        csv_file.close()
    print()
    return print("Заметка добавлена"),  log.Add_logger(f"{ABILITIES[0]};{new_contact}")

