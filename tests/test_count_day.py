import pytest
from log_parser.cookie.csv.count_day_sorted import count_day
from dateutil.parser import parse
from .sample_test_results_util import get_sample_results

def test_total_day_count():
    all_dates = ["2019-12-30T14:19:00+00:00", "2018-12-30T14:19:00+00:00", "2018-12-29T14:19:00+00:00",
                 "2018-12-28T14:19:00+00:00", "2018-12-27T14:19:00+00:00", "2018-12-26T14:19:00+00:00",
                 "2018-12-25T14:19:00+00:00", "2018-12-24T14:19:00+00:00", "2018-12-23T14:19:00+00:00",
                 "2018-12-22T14:19:00+00:00", "2018-12-21T14:19:00+00:00", "2018-12-20T14:19:00+00:00",
                 "2018-12-19T14:19:00+00:00", "2018-12-18T14:19:00+00:00", "2018-12-17T14:19:00+00:00",
                 "2018-12-16T14:19:00+00:00", "2018-12-15T14:19:00+00:00", "2018-12-14T14:19:00+00:00",
                 "2018-12-13T14:19:00+00:00"]
    test_sample = get_sample_results()

    for d in all_dates:
        x = parse(d)
        result = count_day('tests/sample.csv', x)
        assert test_sample.get(str(x.date()), 0) == sum(result.values())
