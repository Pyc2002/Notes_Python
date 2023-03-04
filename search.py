from constants import NOTE_TEMPLATE
from functions import Give_int, Get_lines
from constants import ABILITIES
import log


def Search_by():
    """
    Search row by elements of note
    args -> none
    returns -> list of row
    """
    print()
    num = Give_int(("""
Введите номер атрибута, по которому будет осуществляться поиск:
ID :     [1]
Заголовок    : [2]
Заметка    : [3]
Дата       :[4]
"""), min_num=1, max_num=len(NOTE_TEMPLATE))
    atr = list(NOTE_TEMPLATE.keys())[num - 1]
    print(f"Выбран столбец '{atr}'")
    search_data = input("Введите искомое значение:\n>> ")
    reader = Get_lines()
    data = []
    for row in reader:
        if search_data.capitalize() in row[num-1]:
            data.append(row)
    print(f"Найдено {len(data)} записей:")
    for i in data:
        print(*i)
    if len(data) > 1:
        print(f"\nВыберите одну из записей по номеру, от 1 до {len(data)}:")
        num = Give_int(">> ", min_num=1, max_num=len(data))
        print(f"Выбрана запись {data[num - 1]}"), log.Add_logger(f"{ABILITIES[3]};{data[num - 1]}")
        del data[:num-1:]
        return data
    else:
        log.Add_logger(f"{ABILITIES[3]};{data}")
        return data


    
