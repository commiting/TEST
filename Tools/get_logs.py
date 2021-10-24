import logging
import datetime


def logger(name=__name__):  # 哪一个模块执行就哪一个模块
    # 1-日志的名称： 路径+名字（进程/日期）+后缀名
    logname = f"../Log/{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log"
    # 2- 创建日志对象
    loggerObject = logging.getLogger(name)
    # 3-  日志级别
    loggerObject.setLevel(logging.INFO)  # 信息级别 或者是警告级别
    # 4- 文件本身的设置 日志文件的属性
    rHander = logging.FileHandler(logname, mode="w", encoding="utf-8")
    # 5 -日志内容的格式
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s[%(Lineno)d] : %(message)s:  ")  # 按照jmeter格式模板来套用
    rHander.setFormatter(formatter)  # 给整个文件设置下格式
    loggerObject.addHandler(rHander)  # 加载配置
    return loggerObject  # 返回一个日志对象
