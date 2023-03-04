from functions import Give_int
from constants import ABILITIES

choose_option = 'Выберите действие из списка:\n'


def Get_menu_item() -> int:
    """
    Menu with possible actions with the database
    
    args -> none
    returns -> int
    """
    print()
    for i, item in list(enumerate(ABILITIES, start=1)):
        print(i, item, end='\n')
    choice = Give_int(choose_option, 1, 6)
    return choice


