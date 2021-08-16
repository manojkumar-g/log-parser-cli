from log_parser.cookie.cookie import Cookie
from dateutil.parser import parse
all_dates = ["2019-12-30T14:19:00+00:00","2018-12-30T14:19:00+00:00","2018-12-29T14:19:00+00:00","2018-12-28T14:19:00+00:00","2018-12-27T14:19:00+00:00","2018-12-26T14:19:00+00:00","2018-12-25T14:19:00+00:00","2018-12-24T14:19:00+00:00","2018-12-23T14:19:00+00:00","2018-12-22T14:19:00+00:00","2018-12-21T14:19:00+00:00","2018-12-20T14:19:00+00:00","2018-12-19T14:19:00+00:00","2018-12-18T14:19:00+00:00","2018-12-17T14:19:00+00:00","2018-12-16T14:19:00+00:00","2018-12-15T14:19:00+00:00","2018-12-14T14:19:00+00:00","2018-12-13T14:19:00+00:00"]


def get_sample_results():
    results = {}
    r = []
    with open("tests/sample.csv", 'r') as fh:
        fh.readline()
        for line in fh:
            x = line.strip()
            r.append(x)
        for x in r:
            name, t = x.split(",")
            c = Cookie(name,parse(t))
            k = str(c.timestamp.date())
            if k in results:
                results[k] += 1
            else:
                results[k] = 1
    return results


def get_sample_results_cookies(date):
    with open("tests/sample.csv", 'r') as fh:
        fh.readline()
        r = []
        for line in fh:
            x = line.strip()
            if date in x:
                r.append(x.split(',')[0])
        result = {}
        for i in r:
            result[i] = result.get(i, 0) + 1
        if not result:
            return []
        most_active_cookie_count = max(result.values())
        solution = []
        for key, value in result.items():
            if value == most_active_cookie_count:
                solution.append(key)
        return solution


