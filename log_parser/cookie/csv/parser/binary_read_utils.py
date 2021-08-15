import os


def move_pointer_to_line_start(fh, no_lines=1):
    """
    This Function moves file pointer to request number of lines backwards position
    Always points the position to starting of the line
    :param fh: File handle pointer
    :param no_lines: number of lines it needs to read
    :return: if successfully able to move pointer to requested position
    """
    p = fh.tell()
    f = 0
    while p > 0:
        fh.seek(p)
        p -= 1
        c = fh.read(1)
        if c == b'\n':
            f += 1
            if f == no_lines:
                return True
    return False


def move_pointer_to_date(fh, req_date, get_cookie):
    """
    This is the core function which will make the search faster
    This is the implementation of the binary search to identifying the starting cookie information of the given day
    among all the available days and move the file handler to the starting position to read

    Since This is using binary search time complexity of this method is O(log n) to find the position

    :param fh: file handle while reading in binary form
    :param req_date: date
    :param get_cookie: function to get cookie object to support multiple formats
    :return: None
    """
    fh.seek(0)
    fh.readline()
    start = fh.tell()
    starting_cookie = get_cookie(fh)
    if not starting_cookie:
        return
    if starting_cookie.timestamp.date() <= req_date:
        fh.seek(start)
        return
    low = start
    fh.seek(0, os.SEEK_END)
    high = fh.tell()
    while low <= high:
        if low == high:
            fh.seek(low)
            return
        mid = low+((high-low)//2)
        # print(low,high,mid)
        fh.seek(mid)
        have_two_cookies = move_pointer_to_line_start(fh, 2)
        if not have_two_cookies:
            return
        mid_cookie_prev = None
        mid_prev = 0
        if have_two_cookies:
            mid_prev = fh.tell()
            mid_cookie_prev = get_cookie(fh)
        mid = fh.tell()
        mid_cookie = get_cookie(fh)
        # print(mid_cookie_prev)
        # print(mid_cookie)
        if mid_cookie.timestamp.date() == req_date and (mid_cookie_prev.timestamp.date() != req_date):
            fh.seek(mid)
            return
        if mid_cookie.timestamp.date() <= req_date:
            high = mid_prev
        else:
            low = fh.tell()
