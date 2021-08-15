from log_parser.cookie.cookie import Cookie
from dateutil.parser import parse


def get_cookie(fh):
    """
    Utility for getting the cookie object for the name,date format
    :param fh: file handle pointer for binary reading
    :return: Cookie object formed after reading the line
    """
    x = fh.readline()
    if not x:
        return
    name, t = x.decode().split(",")
    return Cookie(name, parse(t))

