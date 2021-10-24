import logging
import datetime


def logger(name=__name__):  # ��һ��ģ��ִ�о���һ��ģ��
    # 1-��־�����ƣ� ·��+���֣�����/���ڣ�+��׺��
    logname = f"../Log/{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log"
    # 2- ������־����
    loggerObject = logging.getLogger(name)
    # 3-  ��־����
    loggerObject.setLevel(logging.INFO)  # ��Ϣ���� �����Ǿ��漶��
    # 4- �ļ���������� ��־�ļ�������
    rHander = logging.FileHandler(logname, mode="w", encoding="utf-8")
    # 5 -��־���ݵĸ�ʽ
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s[%(Lineno)d] : %(message)s:  ")  # ����jmeter��ʽģ��������
    rHander.setFormatter(formatter)  # �������ļ������¸�ʽ
    loggerObject.addHandler(rHander)  # ��������
    return loggerObject  # ����һ����־����
