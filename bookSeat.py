# -*- coding = utf-8 -*-
# @Time : 2023/7/8
# @Author : Leekos
# @File : bookSeat.py
# @Software : PyCharm
# @JXNU自习室抢课脚本

import requests
from datetime import datetime, timedelta

baseURL = "https://jxnu.huitu.zhishulib.com"
count = 1


# 将时间戳转为日期
def calcData(timestamp):
    date = datetime.fromtimestamp(timestamp)
    return date


# 将小时计算为时间戳
def hour2Data(hour):
    now = datetime.now()
    zero_hour = datetime(now.year, now.month, now.day)

    if now.hour >= 22:
        zero_hour += timedelta(days=1)

    timestamp = int(zero_hour.replace(hour=hour, minute=0, second=0, microsecond=0).timestamp())
    return timestamp


# 将秒转为小时
def calcTime(second):
    return second // 3600


room = {"201": "36", "202": "35", "301": "31", "302": "37"}


class User(object):
    def __init__(self, username, password, beginTime, duration, num, roomID, categoryId):
        self.seats = None
        self.seatBookers = None
        self.bookingId = None
        self.username = username
        self.password = password
        self.beginTime = beginTime
        self.duration = duration
        self.num = num
        self.categoryId = categoryId
        self.roomID = roomID
        self.session = requests.session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"}  # UA头

    # 登录
    def login(self):
        loginURL = baseURL + "/api/1/login"  # 登录接口
        data = {"login_name": self.username, "password": self.password, "ui_type": "com.Raw",
                "code": "b529de5e2da9d7732bcd14f8bfaf2ad4", "str": "peIX1SRwIUa9BQmH", "org_id": "142",
                "_ApplicationId": "lab4", "_JavaScriptKey": "lab4", "_ClientVersion": "js_xxx",
                "_InstallationId": "15af0ca1-0630-5ff9-2b47-3b20d32ace6c"}

        res = self.session.post(url=loginURL, json=data, headers=self.headers)  # 使用session保持会话(注意传递json字符串)
        if res.status_code == 200:
            print("[+]登陆成功！")
        else:
            print("用户名或密码错误！")
            exit(0)

    # 寻找座位
    def searchSeats(self):
        searchURL = baseURL + "/Seat/Index/searchSeats?LAB_JSON=1"
        data = {
            "beginTime": self.beginTime,
            "duration": self.duration,
            "num": self.num,
            "space_category[category_id]": self.categoryId,
            "space_category[content_id]": self.roomID
        }
        res = self.session.post(url=searchURL, data=data, headers=self.headers)

        if res.status_code == 200:
            json = res.json()
        else:
            print("没有空位")
            return
        seats = json["data"]["bestPairSeats"]["seats"][0]["id"]
        seatBookers = json["allContent"]["children"][-1]["children"]["children"][-1]["userInfo"]["id"]
        self.seatBookers = seatBookers
        self.seats = seats
        self.bookSeats()

    # 抢座位
    def bookSeats(self):
        global count
        bookSeatsURL = baseURL + "/Seat/Index/bookSeats?LAB_JSON=1"
        data = {
            "beginTime": self.beginTime,
            "duration": self.duration,
            "seats[0]": self.seats,
            "is_recommend": "1",
            "seatBookers[0]": self.seatBookers
        }
        res = self.session.post(url=bookSeatsURL, data=data, headers=self.headers).json()
        msg = res["MESSAGE"]
        if res["CODE"] == "ok":
            print("[+]预约成功！")
            self.bookingId = res["DATA"]["bookingId"]
            self.bookingInfo()
        else:
            print("预约失败！" + msg + " 正在第" + str(count) + "次尝试~")
            count = count + 1

    # 获取信息
    def bookingInfo(self):
        bookingInfoURL = baseURL + "/Seat/Index/bookingInfo?bookingId=%s&fromType=4&LAB_JSON=1" % self.bookingId

        res = self.session.get(url=bookingInfoURL, headers=self.headers).json()
        seatNum = res["content"]["children"][2]["seatNum"]
        roomName = res["content"]["children"][2]["roomName"]
        date = int(res["content"]["children"][2]["date"])
        date = calcData(date)
        time = int(res["content"]["children"][2]["time"])
        time = calcTime(time)

        print("[+]您的预约信息如下:")
        print("   自习室: " + roomName)
        print("   日期: " + str(date))
        print("   时间: " + str(time) + "小时")
        print("   座位号: " + seatNum)
        exit(0)


if __name__ == "__main__":
    username = "xxxx"  # 学号
    password = "yyyy"  # 密码
    beginTime = hour2Data(9)  # 开始时间
    duration = 3  # 持续时间
    duration = duration * 3600
    num = 1  # 人数
    roomID = room["202"]  # 自习室ID
    categoryId = 591  # 填写自己的categoryId

    user = User(username, password, beginTime, duration, num, roomID, categoryId)

    user.login()
    while True:
        user.searchSeats()
