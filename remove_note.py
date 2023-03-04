from functions import Get_lines, Write_lines
from constants import DATA_BASE, NOTE_TEMPLATE
from search import Search_by
from constants import ABILITIES
import log


def Delete_note():
    """Removing note in csv-file: 1. search row; 2. remove row

    args -> None
    returns -> None
    """
    reader = Get_lines()
    choice = Search_by()
    try:
        reader.remove(choice[0])
    except IndexError:
        return print("Нет данных"), log.Add_logger(f"{ABILITIES[1]};{choice}; Нет данных")
    reader.insert(0, NOTE_TEMPLATE.keys())
    Write_lines(DATA_BASE, reader)
    print()
    return print("Заметка удалена"), log.Add_logger(f"{ABILITIES[1]};{choice}")





