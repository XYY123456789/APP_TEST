# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2020/5/26 0026 10:00
# # @Author  : XYY
# from appium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Remote()
#
# # appium-APP测试元素定位类型方式：方式3和4是重写的方式，其它定位类型是继承selenium库的
#     # 1.通过ID定位元素：resrouce-id
#     driver.find_element_by_id()
#     # 2.通过ClassName定位：classname
#     driver.find_element_by_class_name()
#     # 3.(appium特有的定位类型)通过Accessibilityld定位content-desc
#     driver.find_element_by_accessibility_id()
#     # 4.(appium特有的定位类型)通过AndroidUiAutomator定位
#     driver.find_element_by_android_uiautomator()
#         # 使用UiAutomator中UiSelector类来处理元素定位
#         # 在python客户端appium库中通过，uiautomator来获取元素的方式为：
#         driver.find_element_by_android_uiautomator()
#         # 该方式的参数UiSelector类定位元素的表达式：
#         # new UiSelector类定位元素的表达式：
#             # new UiSelector().函数名称("定位表达式")
#         # 实例化一个UiSelector对象，然后通过实例调用接口
#         # 示例：
#             driver.find_element_by_android_uiautomator('new UiSelector().resourceId("android:id/title")')
#
#     # 5.通过xpath定位
#     driver.find_element_by_xpath()
# #等待处理：与web一致
#     from selenium.webdriver.support.wait import WebDriverWait
#     WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ID,)))
#
# #元素四大基本操作
#     # 1.点击：click()
#     # 2.输入：send_keys()
#     # 3.获取文本内容：text
#     # 4.获取属性：get_attribute()
#
# # 获取窗口大小
# # height width
#     #获取当前窗口最大值（高，宽）
#     size = driver.get_window_size()
#     高 = size["height"]
#     宽 = size["width"]
#
# # 屏幕滑动:注意两次滑动的时间间隔
#     # swipe()滑动函数，需要传入起始位置坐标与终点坐标
#     driver.swipe(start_x, start_y, end_x, end_y, duration=None)
#
# # appuim模拟触屏
# # TouchAction类：
#     from appium.webdriver.common.touch_action import TouchAction
#     # 将一系列的动作放在一个链条中，然后将该链条传递给服务器，服务器接受到该链条后，解析动作并逐条执行
#     # 短按 press
#     # 释放 release
#     # 长按 longpress
#     # 点击 tap
#     # 移动到 move_to
#     # 等待 wait
#     # 执行 perfrom
#     # 取消 cancel
#     # from appuim.webdriver.common.touch_action import TouchAction
#     # # 定位一个元素
#     # ele = driver.find_element_by_id("")
#     # # 查看元素大小
#     # size = ele.size
#     # # 均分大小
#     # step = size["width"]/6
#     # # 获取起点坐标
#     # ori = ele.location
#     # ori["x"]
#     # ori["y"]
#     # # 执行触屏操作
#     # TouchAction(driver).press(x, y).wait(200).move_to(x, y).release().perform()
# #
# # toast注意事项
# # 配置toast请注意：
# # 1.# 自动化测试引擎
# # desired_caps["automationName"] = "UiAutomator2"
# # 2.要求安装的jdk1.8 64位以上
# # 3.Android版本5.0以上
# # 4.appium server版本1.6.3以上
# # 5.可以通过xpath定位，表达式：xpath = '//*[contains（@text,'部分文本内容'）]'
# # 注意：driverWait方法中，请用presence_of_element_located不要使用visibility_of_element_located，对toast的可见处理不支持，会报错命令无法执行
#
# # H5
#     # 前提;
#         #基于UiAutomator+Chromedriver
#         #native部分则uiautomator，webview部分走chromedriver，二者结合
#         #要求：
#         #Android4.4.+
#         #webview需要是debug版本
#         #获取webview的页面元素方式工具
#         # uc-devtools
#         # 常见问题：
#             #contexts这能获取native_app，无法获取webview
#             #使用uiautomatorviewer定位元素，显示calss值为：Android.webkit：webview
#             #解决方式：
#             #1.app打包的时候需要开户webview的debug属性setWebContentDebuggingEnabled（true）(开发在app应用上加上就行)
#             #2.模拟器的contexts中webview，部分手机上没有，需要root一下
#
#     # 操作：
#         # 可用的上下文（contexts）
#             # 列出所有可用的上下文（contexts）
#             # driver.contexts
#
#         # 切换至默认的上下文（context）
#             #切换回默认的上下文（context）
#             driver.switch_to.context(None)  # driver.window_handles
#
#         # 当前上下文（contexts）：列出当前的上下文（context）
#         driver.current_context
#
#         # 当前Activity：获取当前的Acticity。仅Android支持
#             driver.current_activity
#
#         # 当前包名（package）：获取当前包名（package）。仅Android支持
#             driver.current_package
#
#     # 示例：
#         #前提：代码可以识别到webview  需要开启app的webview debug属性
#         #1.先列出所有的context
#         cons = driver.contexts  #列表
#         print(cons)
#         #2.切换至webview。要确保chromedriver的版本要与webview的版本匹配。需要放置到appium安装路径下制定的文件中
#         driver.switch_to.context(cons[-1])
#         #3.切换之后：当前的操作对象：html页面    uc-devtool工具识别html页面，来定位元素
#         WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.XPATH,"元素定位")))
#
# # 微信小程序与公众号
#     # FAuto Test（了解）  https://gitee.com/zyq5858598/FAutoTest
#         #https://www.cnblogs.com/yyoba/p/9973731.html
#
# #yaml
#     #yaml是一种间接的非标记语言
#         #yaml一数据为中心，使用空白，缩进，分行组织数据，从而使的表示更加简洁
#     #基本规则：
#         1.大小写敏感
#         2.使用缩进表示层级关系
#         3.禁止使用tab缩进，只能使用空格键
#         4.缩进长度没有限制，只要是元素对齐就表示这些元素属于一个层级
#         5.使用#表示注释
#         6.字符串可以不用引号注释
