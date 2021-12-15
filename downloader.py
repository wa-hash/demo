# 以爬取同花顺数据中心'http://data.10jqka.com.cn/'的某些股票的财务分析数据为例

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

Stock_code = ['002262', '000895', '000333']  # 预选选择好的股票代码
Series = ['main', 'debt', 'benefit', 'cash']  # 需要下载的文件类别

chrome_options = Options()
chrome_options.add_argument('--headless')  # 不可视
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 使用chrome开发者模式
chrome_options.add_argument('--disable-gpu')  # 禁用gpu
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 禁止横幅

for code in Stock_code:
    prefs = {
        'download.default_directory': r"D:\download\{}".format(code),  # 设置下载路径,路径不存在会自动创建
        'download.prompt_for_download': False,  # 是否弹窗询问
        "download.directory_upgrade": False,  # 是否采用绝对路径
        "safebrowsing.enabled": False  # 是否提示安全警告
    }
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chrome_options)
    for series in Series:
        url = 'http://basic.10jqka.com.cn/api/stock/export.php?export={}&type=report&code={}'.format(series, code)  # 生成下载地址
        driver.maximize_window()
        driver.get(url)
        time.sleep(10)  # 适当设置大一点的数,建议为10
    driver.close()

# 注意：本程序并非本人原创，特此感谢在论坛无私提供解决方案的其他人。故在此开源，仅可用于非商业用途！
# 网络爬虫可能会给被访问网站带来安全隐患，请务必遵守相应的法律规范和道德约束。
