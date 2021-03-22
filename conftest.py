import pytest
from appium import webdriver
from middleware.handler import Handler
app_data = Handler.app


@pytest.fixture()
def open_app():
    # 创建一个容器
    desired_caps = {}
    # 平台类型
    desired_caps['platformName'] = app_data['platformName']
    # 平台版本
    desired_caps['platformVersion'] = app_data['platformVersion']
    # devices 编号
    desired_caps['deviceName'] = app_data['deviceName']
    # app的系统包名
    desired_caps['appPackage'] = app_data['appPackage']
    # app的入口acitivity
    desired_caps['appActivity'] = app_data['appActivity']
    # 连接appium server 前提：appium desktop要启动，在监听端口
    # 将desired_caps 发送给appium server 打开app
    driver = webdriver.Remote(app_data['host'], desired_caps)
    yield driver
