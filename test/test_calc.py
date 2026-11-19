from myapp import calc_price

def test_discount():
    # 60+60=120，满100打9折 = 108
    assert calc_price([60, 60]) == 108

def test_no_discount():
    # 30+40=70，不满100，原价 = 70
    assert calc_price([30, 40]) == 70

def test_boundary():
    # 正好100，满100（含）打9折 = 90
    assert calc_price([100]) == 90
