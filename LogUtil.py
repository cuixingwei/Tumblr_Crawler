import logging


def getLogger(logName):
    """
    返回日志实例
    :param logName:
    :return:
    """
    logger = logging.getLogger(logName)  # 创建一个logger,默认为root logger
    logger.setLevel(logging.INFO)  # 设置全局log级别为debug。注意全局的优先级最高

    hterm = logging.StreamHandler()  # 创建一个终端输出的handler,设置级别为error
    hterm.setLevel(logging.DEBUG)

    hfile = logging.FileHandler("tumblr.log")  # 创建一个文件记录日志的handler,设置级别为info
    hfile.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 创建一个全局的日志格式

    hterm.setFormatter(formatter)  # 将日志格式应用到终端handler
    hfile.setFormatter(formatter)  # 将日志格式应用到文件handler

    logger.addHandler(hterm)  # 将终端handler添加到logger
    logger.addHandler(hfile)  # 将文件handler添加到logger
    return logger


if __name__ == '__main__':
    logger = getLogger('hi')
    # 定义日志msg,注意此时是logger,不是logging了
    logger.debug("User %s is loging" % 'jeck')
    logger.info("User %s attempted wrong password" % 'fuzj')
    logger.warning("user %s attempted wrong password more than 3 times" % 'mary')
    logger.error("select db is timeout")
    logger.critical("server is down")
