#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 0012 15:21
# @Author  : XYY
# 主要封装各文件目录
import os


# 项目框架顶层目录
ROOT_PATH = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 测试数据目录
DATA_PATH = os.path.join(ROOT_PATH, "TestData")
# 测试用例目录
CASE_PATH = os.path.join(ROOT_PATH, "TestCase")
# 测试报过输出目录
REPORT_PATH = os.path.join(ROOT_PATH, "Outputs/Reports")
# 测试日志输入目录
LOG_PATH = os.path.join(ROOT_PATH, "Outputs/Logs")
# 失败截图输出目录
SCREENSHOT_PATH = os.path.join(ROOT_PATH, "Outputs/Screenshots")
# 配置文件读取目录
CONFIG_PATH = os.path.join(ROOT_PATH, "Config")


if __name__ == '__main__':
    print(ROOT_PATH)
