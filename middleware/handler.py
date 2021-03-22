#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 0027 14:52
# @Author  : XYY
from Config import configs
from Common import yaml_config, logger_handler
import os


class Handler:
    """
    初始化所有的数据
    在其它模块当中重复使用
    是从commmon当中实例化对象
    """
    # 加载python配置项
    conf = configs

    # 加载yaml数据
    yaml = yaml_config.read_yaml(os.path.join(conf.CONFIG_PATH, "config_file.yml"))

    # logger
    logger_data = yaml["logger"]
    logger = logger_handler.get_logger(name=logger_data["name"],
                                       file=logger_data["file"],
                                       logger_level=logger_data["logger_level"],
                                       stream_level=logger_data["stream_level"],
                                       file_level=logger_data["file_level"])

    # APP
    app = yaml["app"]

if __name__ == '__main__':
        data_path = Handler.conf.DATA_PATH
        print(Handler.yaml)
        print(Handler.app_data)
        print(Handler.logger.debug("#######"))
        print(Handler.logger.info("#######"))
        # print(Handler.sql().query("select * from futureloan.member LIMIT 10"))
        # print(login())


