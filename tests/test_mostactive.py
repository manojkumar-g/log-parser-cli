from log_parser.cookie.most_active import most_active_cookie
from dateutil.parser import parse
import pytest
import datetime
from .sample_test_results_util import get_sample_results_cookies


def test_check_for_invalid_file_name():
    with pytest.raises(Exception):
        most_active_cookie('invalid.csv',datetime.date.today())

def test_check_for_unsupported_file_format():
    with pytest.raises(Exception):
        most_active_cookie('invalid.ddd',datetime.date.today())
def test_most_active():
    all_dates = ["2019-12-30T14:19:00+00:00", "2018-12-30T14:19:00+00:00", "2018-12-29T14:19:00+00:00",
                 "2018-12-28T14:19:00+00:00", "2018-12-27T14:19:00+00:00", "2018-12-26T14:19:00+00:00",
                 "2018-12-25T14:19:00+00:00", "2018-12-24T14:19:00+00:00", "2018-12-23T14:19:00+00:00",
                 "2018-12-22T14:19:00+00:00", "2018-12-21T14:19:00+00:00", "2018-12-20T14:19:00+00:00",
                 "2018-12-19T14:19:00+00:00", "2018-12-18T14:19:00+00:00", "2018-12-17T14:19:00+00:00",
                 "2018-12-16T14:19:00+00:00", "2018-12-15T14:19:00+00:00", "2018-12-14T14:19:00+00:00",
                 "2018-12-13T14:19:00+00:00"]
    for d in all_dates:
        x = parse(d)
        result = most_active_cookie('tests/sample.csv', x)
        expected = get_sample_results_cookies(d)
        assert result == expected

