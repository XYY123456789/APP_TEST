#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 0026 9:55
# @Author  : XYY
from appium import webdriver
import time
from Common.basepage import BasePage


class SettingPage(BasePage):

    def open_setting(self, number):
        doc = "上滑页面四次"
        size = self.get_size(doc)
        for i in range(number):
            time.sleep(2)
            self.swipe_up(size, doc)



