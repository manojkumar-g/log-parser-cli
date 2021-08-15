from .parser.name_date_format_util import get_cookie
from .parser.binary_read_utils import move_pointer_to_date


def count_day(file_name, day):
    req_date = day.date()
    with open(file_name, "rb") as fh:
        move_pointer_to_date(fh, req_date, get_cookie)
        c = 0
        while True:
            cookie = get_cookie(fh)
            print(cookie)
            if not cookie or cookie.timestamp.date() != req_date:
                break
            c += 1
        return c
