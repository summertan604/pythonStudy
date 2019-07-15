from trans.tools import get_trans_id


def test_trans_tools():
    """
    测试trans包下的tools模块
    :return:
    """
    trans_id = get_trans_id()
    print(type(trans_id))
    print(trans_id)