from datetime import datetime


def get_trans_id(date=None):
    """
    根据传过来的时间得到一个唯一的交易流水ID
    :param date: 日期
    :return: 交易流水ID字符串
    """
    # 如果没有传入时间，date为当前系统时间
    if date is None:
        date = datetime.today()
    # 保证ID唯一性 日期+时间+毫秒+随机数(6位)
    return date.strftime('%Y%m%d%H%M%S%f')
