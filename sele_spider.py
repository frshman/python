##写一些使用sele的时候会用到的功能

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging

logging.basicConfig(level=logging.INFO,
format= '%(asctime)s - %(levelname)s: %(message)s')

browser = webdriver.Chrome()
wait = WebDriverWait(browser,timeout=10)


def scrape_page(url,condition,locator):
    logging.info('scraping%s',url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s',url,exc_info=True)

def scrape_index(page):
    url : any = ...
    scrape_page(url,condition=expected_conditions.visibility_of_all_elements_located,locator=(By.CSS_SELECTOR,'#index.item'))

# 总结，初始化一个wait对象，可以指定页面出现特定的数据开始爬取：
#wait.until(expected_conditions.visibility_of_all_elements_located(By.CSS_SELECTOR,'#index.item'))

##不显示chrome图形界面
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# browser = webdriver.Chrome(options=options)

