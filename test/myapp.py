def calc_price(items):
    """计算订单总价：满 100 元打 9 折。"""
    total = sum(items)
    if total > 100:
        return total * 0.9
    return total