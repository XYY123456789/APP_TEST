#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 0012 15:20
# @Author  : XYY
"""1.页面基本函数--执行日志，异常处理，失败截图
    2.说有的页面公共的部分"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from Config import configs
import time
from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from middleware.handler import Handler

log = Handler.logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def save_screenshots(self, doc):
        """失败截图"""
        # doc：操作名称
        # 图片名称：模块名称-页面名称-操作名称-时间.png
        # filepath = 指定图片保存目录/model（页面功能名称)_当前时间到秒.png
        # file_name = "截图存放路径"+"{0}_{1}.png".formet(name, times)
        filepath = Handler.conf.SCREENSHOT_PATH + "/{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                                            time.localtime()))
        try:
            self.driver.save_screenshot(filepath)
            log.info("截图成功。图片路径为{}".format(filepath))
        except:
            log.error("截图失败")
            raise

    def wait_element_visible(self, locator, timeout=20, poll_frequency=0.5, doc=""):
        """等待元素可见"""
        log.info("{}等待元素{}可见".format(doc, locator))
        try:
            start_times = datetime.datetime.now()
            elem = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator))
            end_times = datetime.datetime.now()
            wait_time = (end_times - start_times).seconds
            log.info("等待结束，等待时长{}".format(wait_time))
            return elem
        except:
            log.error("等待元素可见失败！！！")
            self.save_screenshots(doc)
            raise

    def wait_element_presence(self, locator, times=10, poll=0.5, doc=""):
        """等待元素存在"""
        log.info("{}等待元素{}存在".format(doc, locator))
        try:
            start_time = datetime.datetime.now()
            elem = WebDriverWait(self.driver, timeout=times, poll_frequency=poll).until(
                EC.presence_of_element_located(locator))
            end_time = datetime.datetime.now()
            wait_time = (end_time - start_time).seconds
            log.info("等待结束，等待时长{}".format(wait_time))
            return elem
        except:
            log.error("等待元素存在失败！！！")
            self.save_screenshots(doc)
            raise

    def get_element(self, locator, doc=""):
        """查找元素"""
        log.info("{} 查找到元素：{}".format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            log.error("{} 查找元素{}失败".format(doc, locator))
            self.save_screenshots(doc)
            raise

    def click(self, locator, doc=""):
        """点击元素"""
        ele = self.get_element(locator, doc)
        log.info("{} 元素点击：{}".format(doc, locator))
        try:
            ele.click()
        except:
            log.error("{} 元素点击{}失败".format(doc, locator))
            self.save_screenshots(doc)
            raise

    def input_text(self, locator, text, doc=""):
        """键盘输入操作"""
        ele = self.get_element(locator, doc)
        log.info("{} 键盘输入：{}".format(doc, locator))
        try:
            ele.send_keys(text)
        except:
            log.error("{} 键盘输入{}失败".format(doc, locator))
            self.save_screenshots(doc)
            raise

    def get_element_text(self, locator, doc=""):
        """获取文本"""
        ele = self.get_element(locator, doc)
        log.info("{} 获取文本：{}".format(doc, locator))
        try:
            return ele.text
        except:
            log.error("{} 获取文本{}失败".format(doc, locator))
            self.save_screenshots(doc)
            raise

    def get_element_attribute(self, locator, doc=""):
        """获取元素属性"""
        ele = self.get_element(locator, doc)
        log.info("{} 获取元素属性：{}".format(doc, locator))
        try:
            return ele.get_attribute()
        except:
            log.error("{} 获取元素属性{}失败".format(doc, locator))
            self.save_screenshots(doc)
            raise

    # 上下左右滑动
    def swipe_up(self, size, doc="", duration=200):
        """上划操作"""
        log.info("{} 滑动页面元素：{}".format(doc, size))
        try:
            self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5,
                              size["height"] * 0.1, duration=duration)
        except:
            log.error("{} 滑动页面元素{}失败".format(doc, size))
            self.save_screenshots(doc)
            raise

    # 向下
    def seipe_down(self, size, doc="", duration=200):
        """下划操作"""
        log.info("{} 滑动页面元素：{}".format(doc, size))
        try:
            self.driver.swipe(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5,
                              size["height"] * 0.9, duration=duration)
        except:
            log.error("{} 滑动页面元素{}失败".format(doc, size))
            self.save_screenshots(doc)
            raise

    # 向左
    def swipe_left(self, size, doc="", duration=200):
        """左划操作"""
        log.info("{} 滑动页面元素：{}".format(doc, size))
        try:
            self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1,
                              size["height"] * 0.5, duration=duration)
        except:
            log.error("{} 滑动页面元素{}失败".format(doc, size))
            self.save_screenshots(doc)
            raise

    # 向右
    def swipe_right(self, size, doc="", duration=200):
        """右划操作"""
        log.info("{} 滑动页面元素：{}".format(doc, size))
        try:
            self.driver.swipe(size["width"] * 0.1, size["height"] * 0.5, size["width"] * 0.9,
                              size["height"] * 0.5, duration=duration)
        except:
            log.error("{} 滑动页面元素{}失败".format(doc, size))
            self.save_screenshots(doc)
            raise

    # 获取整个屏幕大小
    def get_size(self, doc=""):
        log.info("获取窗口大小")
        try:
            size = self.driver.get_window_size()
            return size
        except:
            log.error("获取窗口大小失败")
            self.save_screenshots(doc)
            raise

    def get_toast(self, text, doc=""):
        """toast获取"""
        log.info("需要获取的toast的提示信息为{}".format(text))
        # 1.xpath表达式，文本匹配，注意@text在app中时属性，在web中时函数需要加（）
        loc = '//*[contains(@text,"{}")]'.format(text)
        locator = (MobileBy.XPATH, loc)
        # 等待的时候，要用元素存在的条件，不能用元素可见的条件（原因：toast提示显示时间很短）
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located(locator))
            return self.get_element_text(locator)
        except:
            log.error("没有找到对应的toast{}提示".format(text))
            self.save_screenshots(doc)
            raise

    def get_webview(self, webview, doc=""):
        """切入H5"""
        log.info("需要切入的webview的名称：{}".format(webview))
        locator = (MobileBy.CLASS_NAME, webview)
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            contexts = self.driver.contexts
            log.info("当前所有的contexts：{}".format(contexts))
            time.sleep(2)
            # self.driver.switch_to.context("WEBVIEW_{}".format("包名"))
            self.driver.switch_to.context(contexts[-1])
        except:
            log.error("没有找到当前所有的contexts：{}".format(webview))
            self.save_screenshots(doc)
            raise

    def native_webview(self, doc=""):
        """退出H5"""
        log.info("退出当前H5页面回到原app页面")
        try:
            contexts = self.driver.contexts
            if len(contexts) > 1:
                self.driver.switch_to.context(contexts[0])
            else:
                raise contexts
        except:
            log.error(f'没有找到退出当前H5页面回到原app页面')
            self.save_screenshots(doc)
            raise

    def is_eleExist(self, locator, timeout=10, doc=""):
        log.info("在页面{}中是否存在元素：{}".format(doc, locator))
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            log.info("{}秒内页面{}中存在元素：{}".format(timeout, doc, locator))
            return True
        except:
            log.info("{}秒内页面{}中不存在元素：{}".format(timeout, doc, locator))
            self.save_screenshots(doc)
            raise






