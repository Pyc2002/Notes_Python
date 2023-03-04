from user_interface import Get_menu_item
from remove_note import Delete_note
from add_note import Add_note
from edit_note import Edit_note
from search import Search_by
from show_db import Show



def Procedure():
    while True:
        choice = Get_menu_item()
        if choice == 1:
            Add_note()
        elif choice == 2:
            Delete_note()
        elif choice == 3:
            Edit_note()
        elif choice == 4:
            Search_by()
        elif choice == 5:
            Show()
        elif choice == 6:
            exit()