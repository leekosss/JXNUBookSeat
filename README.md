# JXNUBookSeat
## **JXNU自习室抢课脚本**

> - 请勿用于非法用途
> - 请勿恶意使用
> - 最终解释权由**leekos**所有

**如果觉得有用请点亮你的star**

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







