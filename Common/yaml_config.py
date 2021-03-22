#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 0024 10:34
# @Author  : XYY
import yaml
from Config import configs
import os


# 读取yml配置文件
def read_yaml(file):
    with open(file, encoding="utf8") as f:
        conf = yaml.load(f, Loader=yaml.SafeLoader)
    return conf


# 写入yml配置数据
def write_yaml(file, data):
    with open(file, encoding="utf8") as f:
        yaml.dump(f, data)


if __name__ == '__main__':
    file = os.path.join(configs.CONFIG_PATH, "config_file.yml")
    print(read_yaml(file))
