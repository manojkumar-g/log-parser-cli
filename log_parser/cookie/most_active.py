from os import path
from .csv.count_day_sorted import count_day as csv_count


def most_active_cookie(file_name, day):
    """
    This Function prints the most active cookie for all supported formats
    :param file_name: file name
    :param day: request day
    :return: None
    """
    if not path.exists(file_name):
        raise Exception("[Error] File doesn't exists.")
    cookie_count_by_day = {}
    if file_name.endswith('.csv'):
        cookie_count_by_day = csv_count(file_name, day)
    else:
        raise Exception("[Error] Unsupported Format.")
    if not len(cookie_count_by_day):
        return []
    most_active_cookie_count = max(cookie_count_by_day.values())
    solution = []
    for key, value in cookie_count_by_day.items():
        if value == most_active_cookie_count:
            solution.append(key)
    return solution
