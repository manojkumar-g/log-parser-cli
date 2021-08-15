from .parser.name_date_format_util import get_cookie
from .parser.binary_read_utils import move_pointer_to_date


def count_day(file_name, day):
    """
    Algorithm for finding the frequency of each cookie in a given day
    Reads the data in binary form and uses binary search to find the correct position of a requested time
    since the data is sorted
    :param file_name:  file name
    :param day: requested date
    :return: frequency of the each cookie
    """
    req_date = day.date()
    with open(file_name, "rb") as fh:
        move_pointer_to_date(fh, req_date, get_cookie)
        count_frequency = {}
        while True:
            cookie = get_cookie(fh)
            if not cookie or cookie.timestamp.date() != req_date:
                break
            count_frequency[cookie.name] = count_frequency.get(cookie.name, 0) + 1
        return count_frequency
