import re
from datetime import datetime
from  hk_dh_wuhan_data import get_hk_dh_data

def test_all(capsys):
    get_hk_dh_data('ALL')
    captured = capsys.readouterr()
    record = 0
    for i in re.split('\n', captured[0]):
        record += 1
        if len(i) > 0:
            col = re.split(',', i)
            assert re.search('^Hong Kong$', col[0])
            assert re.search('^Hong Kong$', col[1])
            assert datetime.strptime(col[2], '%Y-%m-%dT%H:%M:%S')
            assert int(col[3]) >= 0 
            assert int(col[4]) >= 0
            assert int(col[5]) >= 0
            assert float(col[6]) >= -90
            assert float(col[7]) >= -180
    with open("covid19_hk_data.csv", "w") as f:
        f.write(captured[0]) 
    assert record > 0


def test_today(capsys):
    get_hk_dh_data('')
    captured = capsys.readouterr()
    col = re.split(',', captured[0])
    assert re.search('^Hong Kong$', col[0])
    assert re.search('^Hong Kong$', col[1])
    assert datetime.strptime(col[2], '%Y-%m-%dT%H:%M:%S')
    assert int(col[3]) >= 0
    assert int(col[4]) >= 0
    assert int(col[5]) >= 0
    assert float(col[6]) >= -90
    assert float(col[7]) >= -180
