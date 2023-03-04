from functions import Get_lines, Write_lines
from constants import DATA_BASE, NOTE_TEMPLATE
from search import Search_by
from constants import ABILITIES
import log
from add_note import Fieldnames, Id_count, Check_text
import csv
from datetime import datetime as dt


def Edit_note():
    """Edit data in file: 1. search row; 2. remove row; 3. edit row
    
    args -> None
    returns -> None
    """
    reader = Get_lines()
    choice = Search_by()
     
    try:
        reader.remove(choice[0])
    
    except IndexError:
        return print("Нет данных"), log.Add_logger(f"{ABILITIES[2]};{choice}; Нет данных")
    
    modify_key = input("""
Введите номер где нужно внести изменения
Заголовок    : [1]
Текст заметки    : [2]
""")
    edit_note = choice[0]
    
    title = edit_note[1]
    text = edit_note[2]
   
  
    
    if modify_key == '1':
        title = Check_text(input('Введите новый заголовок заметки: \n '))
    elif modify_key == '2':
        text = Check_text(input('Введите новый текст заметки:\n '))
    else: print("Нет данных")
    
    id = Id_count()
    datetime = dt.now().strftime('%Y-%m-%d, %H:%M:%S')
    edit_contact = {'ID': id,'Заголовок': title.capitalize(), 'Заметка': text.capitalize(), 'Дата' : datetime}

    reader.insert(0, NOTE_TEMPLATE.keys())
    Write_lines(DATA_BASE, reader)

    Fieldnames()

    with open(DATA_BASE, mode='a', newline='', encoding='utf-8') as csv_file:
        field_names = ['ID', 'Заголовок', 'Заметка', 'Дата']

        writer = csv.DictWriter(csv_file, fieldnames=field_names, dialect='excel', restval='', delimiter=';')
        writer.writerow(edit_contact)
        csv_file.close()
    print()
    return print("Изменения внесены"), log.Add_logger(f"{ABILITIES[2]}: до редактирования:{choice}, новая редакция: {edit_note}")

