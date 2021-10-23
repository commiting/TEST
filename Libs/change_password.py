#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 17:38
# @Author  : 李彬
# @File    : change_password.py
# @Software: PyCharm
from Config.config import HOST
from Tools.getexcel import get_exl
import pytest
class Change:
    def change_password(self,path,token,inData):
        host=f'{HOST}{path}'
        heards={'X-AUTH-TOKEN':f'{token}'}
        pass