# BookSeat
## **脚本**

> - 请勿用于非法用途
> - 请勿恶意使用
> - 最终解释权由**leekos**所有

**如果觉得有用请点亮你的star**
# 🈲


## 使用方法

```python
username = "xxxx"  # 学号
password = "yyyy"  # 密码
beginTime = hour2Data(9)  # 开始时间
duration = 3  # 持续时间
duration = duration * 3600
num = 1  # 人数
roomID = room["202"]  # 自习室ID
categoryId = 591  # 填写自己的categoryId
```

首先安装玩项目所需的依赖

然后将main函数中学号、密码、开始小时、持续时间、人数、自习室ID进行修改，

运行脚本即可

<img src="https://s2.loli.net/2023/07/09/eJt64qYAypvcMDj.png" alt="image-20230709134201153" style="zoom: 50%;" />



## 更新信息

- 2023-7-8 v1.1版



## 相关接口

**baseURL**

`https://jxnu.huitu.zhishulib.com/`



### 登录

`/api/1/login`

post传参`json`

```
{"login_name":"学号","password":"密码.","ui_type":"com.Raw","code":"相关code","str":"相关str","org_id":"142","_ApplicationId":"lab4","_JavaScriptKey":"lab4","_ClientVersion":"js_xxx","_InstallationId":"相关id"}
```



### 找座位

`/Seat/Index/searchSeats?LAB_JSON=1`

post

```
beginTime=开始时间戳&duration=持续秒数&num=1&space_category%5Bcategory_id%5D=【category_id】&space_category%5Bcontent_id%5D=自习室id
```



### 预约座位

`/Seat/Index/bookSeats?LAB_JSON=1`

post

```
beginTime=1688857200&duration=10800&seats%5B0%5D=座位id&is_recommend=1&seatBookers%5B0%5D=身份id
```



### 座位信息

`/Seat/Index/bookingInfo?bookingId=13584476&fromType=4&LAB_JSON=1`







