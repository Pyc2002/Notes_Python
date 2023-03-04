from constants import LOG_NAME
from datetime import datetime as dt


def Add_logger(data):
    """
    Writes information to the log. See the file name in constants or specify your own.
    args -> data
    returns -> none
    """
    time = dt.now().strftime("%d-%m-%Y, %H:%M")
    with open(LOG_NAME, 'a', encoding='utf-8') as log_file:
        log_file.write('{}; {}\n'.format(time,data))