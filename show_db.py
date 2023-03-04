from functions import Get_lines
from constants import ABILITIES
import log


def Show():
    """
    Shows the database
    args -> none
    returns -> none
    """
    reader = Get_lines()
    for row in reader:
        print(*row)
    log.Add_logger(f"{ABILITIES[4]}")