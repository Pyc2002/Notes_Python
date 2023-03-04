from typing import Optional
from typing import List
from constants import DATA_BASE
import csv


def Give_int(input_string: str, min_num: Optional[int] = None, max_num: Optional[int] = None) -> int:
    '''
    Takes an int number from user
    args -> string
    returns -> int number or a message about an error
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите меньше {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')


def Get_list_data(filename: str) -> List[str]:
    '''
    Retuns list from file
    Args -> filename
    Returns -> list[str]
    '''
    with open(filename) as file:
        return file.read().split('\n')


def Get_lines():
    """
    Retuns list of rows from file

    args -> none
    returns -> list
    """
    with open(DATA_BASE, "r", newline='', encoding='utf-8') as csvfile:
        result = csv.DictReader(csvfile, dialect='excel', delimiter=";")
        data = []
        for row in result:
            data.append(list(row.values()))
    return data


def Write_lines(file_name: str, data):
    """
    Writes in file
    args -> filename, data
    returns -> none
    """
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, dialect='excel', delimiter=';')
        for i in data:
            writer.writerow(i)

