from log_parser.cookie.cookie import Cookie
from dateutil.parser import parse


def get_cookie(fh):
    x = fh.readline()
    if not x:
        return
    name, t = x.decode().split(",")
    return Cookie(name, parse(t))

