﻿from selenium import webdriver
import random
import time


def start():
    nums = int(input("输入答题次数:"))
    for n in range(nums):
        # 自定义答案
        answer = {
            '1': 0,
            '2': random.randint(2, 3),
            '3': random.randint(4, 7),
            '4': 9,
            '5': 11,
            '6': 14,
            '7': 19,
            '8': 23,
            '9': 27,
            '10': 31,
            '11': random.randint(34, 35),
            '12': random.randint(37, 38),
            '13': 43,
            '14': 47,
            '15': 50,
            '16': 53,
            '17': random.randint(58, 59),
            '18': random.randint(61, 63),
            '19': 66,
            '20': 70,
        }
        driver = webdriver.Firefox()
        url = "https://www.wjx.cn/m/20834858.aspx?from=singlemessage#"
        driver.get(url)
        for i in answer:
            js = 'document.getElementsByClassName("jqradio")[' + str(answer[i]) + '].click();'
            driver.execute_script(js)
            time.sleep(2)  # 延时2秒
        print('第'+ str(n+1)+'次题目填写完毕!')
        driver.find_element_by_id('ctlNext').click()
        print('第'+ str(n+1)+'次提交!')
        driver.close()
        # 防止问卷星要验证码这里提交一次后休眠一段时间
        time.sleep(20)


start()
