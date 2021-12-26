# 一、普通用户


## （1）普通用户注册

接口 URL：```/api/ordin/register```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|u_name|是|string|用户名|
|r_name|是|string|用户姓名|
|c_type|是|string|证件类型（中华人民共和国居民身份证，台湾居民往来大陆通行证，港澳居民来往内地通行证，军人证件，护照，香港身份证，澳门身份证）|
|c_num|是|string|证件号码|
|u_pwd|是|string|用户密码|
|p_num|否|string|电话号码（11位）|
|u_idct|否|string|用户简介|
|r_city|是|string|注册城市（要和证件匹配）|
|r_cmty|是|string|注册社区|
|r_time|是|timestamp|注册时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|r_result|boolean|成功为``True``，失败为``False``|
|u_id|string|注册用户标识|

## （2）用户登录

接口 URL：```/api/ordin/login```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型   | 说明   |
| -------- | ---- | ------ | ------ |
| username | 是   | string | 用户名 |
| password | 是   | string | 密码   |

### 返回JSON

| 属性    | 类型    | 说明                                  |
| ------- | ------- | ------------------------------------- |
| isAdmin | boolean | 普通用户为``False``，管理员为``True`` |

## （3）普通用户修改信息

接口 URL：```/api/ordin/modify```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|p_num|否|string|联系电话（11位）|
|u_pwd|否|string|密码|
|u_idct|否|string|用户简介|
|m_time|是|timestamp|修改时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|m_result|Boolean|成功为``True``，失败为``False``|

## （4）普通用户发布请求信息

接口 URL：```/api/ordin/request/release```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|req_cmty|是|string|发布社区|
|req_uid|是|string|发布用户标识|
|req_type|是|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|
|req_topic|是|string|请求主题|
|req_idct|是|string|请求描述|
|end_time|是|yyyy-MM-dd|请求结束日期|
|req_nop|是|int|请求人数|
|req_time|是|timestamp|发起请求时间|
|req_photo|否||请求介绍照片|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|req_result|boolean|发布结果，成功为``True``，失败为``False``|
|req_id|string|请求标识|

## （5）普通用户查询自己发布的所有请求信息

接口 URL：```/api/ordin/request/info```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型   | 说明     |
| -------- | ---- | ------ | -------- |
| u_id     | 是   | string | 用户标识 |

### 返回JSON

|属性|类型|说明|
|---|---|---|
|req_cmty|string|发布社区|
|req_id|string|请求标识|
|req_uid|string|发布用户标识|
|req_type|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|
|req_topic|string|请求主题|
|req_idct|string|请求描述|
|req_nop|int|请求人数|
|end_time|yyyy-MM-dd|请求结束日期|
|req_photo||请求介绍照片(可空)|
|req_time|timestamp|创建时间|
|m_time|string|修改时间|
|req_status|int|状态|

## （6）普通用户删除（已发布还没有响应者）的请求信息

接口 URL：```/api/ordin/request/delete```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型   | 说明     |
| -------- | ---- | ------ | -------- |
| req_id   | 是   | string | 请求标识 |

### 返回JSON

| 属性       | 类型    | 说明                                      |
| ---------- | ------- | ----------------------------------------- |
| del_result | boolean | 删除结果，成功为``True``，失败为``False`` |

## （7）普通用户修改（已发布还没响应者）的请求信息

接口 URL：```/api/ordin/request/modify```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称  | 必选 | 类型       | 说明                                                         |
| --------- | ---- | ---------- | ------------------------------------------------------------ |
| req_id    | 是   | string     | 请求标识                                                     |
| req_type  | 否   | string     | 请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者） |
| req_topic | 否   | string     | 请求主题                                                     |
| req_idct  | 否   | string     | 请求描述                                                     |
| req_nop   | 否   | int        | 请求人数                                                     |
| end_time  | 否   | yyyy-MM-dd | 请求结束日期                                                 |
| req_photo | 否   |            | 请求介绍照片                                                 |
| m_time    | 是   | timestamp  | 请求修改时间                                                 |

### 返回JSON

| 属性     | 类型    | 说明                                      |
| -------- | ------- | ----------------------------------------- |
| m_result | boolean | 修改结果，成功为``True``，失败为``False`` |

## （8）普通用户查看响应信息

接口 URL：```/api/ordin/request/response_info```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型   | 说明     |
| -------- | ---- | ------ | -------- |
| req_id   | 是   | string | 请求标识 |

### 返回JSON

|属性|类型|说明|
|---|---|---|
|rsp_id|string|响应标识|
|req_id|string|请求标识|
|rsp_uid|string|响应用户标识|
|rsp_idct|string|响应描述|
|rsp_time|timestamp|响应时间|
|rsp_status|int|状态（0：待接受 / 1：同意 / 2：拒绝 / 3：取消）|

## （9）普通用户处理响应信息

接口 URL：```/api/ordin/request/opt_response```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|req_id|是|string|响应标识|
|option|是|boolean|是否接受响应，接受为``True``，拒绝为``False``|

### 返回JSON

| 属性       | 类型    | 说明                                      |
| ---------- | ------- | ----------------------------------------- |
| opt_result | boolean | 处理结果，成功为``True``，失败为``False`` |

## （10）用户查看所属社区所有帮忙请求信息

接口 URL：```/api/ordin/response/request_info```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|community|是|string|用户所属社区|

### 返回JSON

|属性|类型|说明|
|---|---|---|
| req_id     |string|请求标识|
| req_uid    |string|发布用户标识|
|req_type|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|
|req_topic|string|请求主题|
|req_idct|string|请求描述|
|req_nop|int|请求人数|
|end_time|timestamp|请求结束日期|
|req_time|timestamp|请求创建时间|
|req_status|string|状态|


## （11）用户提交相应信息

接口 URL：```/api/ordin/response/respond```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|rsp_uid|是|string|响应用户名|
|rsp_idct|是|string|响应描述|
|rsp_time|是|timestamp|创建响应时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|rsp_id|string|响应标识|
|rsp_result|boolean|发布响应信息结果，成功为``True``，失败为``False``|

## （12）用户查看自己发布的响应信息

接口 URL：```/api/ordin/response/response_info```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型   | 说明         |
| -------- | ---- | ------ | ------------ |
| rsp_uid  | 是   | string | 响应用户标识 |

### 返回JSON

|属性|类型|说明|
|---|---|---|
|rsp_uid|string|响应用户标识|
|req_id|string|请求标识|
|rsp_id|string|响应标识|
|rsp_idct|string|响应描述|
|rsp_time|timestamp|响应创建时间|
|m_time|timestamp|响应修改时间|
|rsp_status|int|状态|

## （13）普通用户修改还未被接受的响应信息

接口 URL：```/api/user/response/modify```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|rsp_id|是|string|响应标识|
|rsp_idct|否|string|响应描述|
|m_time|是|timestamp|修改时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|m_result|boolean|修改响应信息结果，成功为``True``，失败为``False``|

## （13）普通用户删除还未被接受的响应信息

接口 URL：```/api/user/response/delete```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|rsp_id|是|string|响应标识|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|del_result|boolean|删除响应信息结果，成功为``True``，失败为``False``|

## （14）普通用户查询已经被接受的响应

接口 URL：```/api/user/response/accepted```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型   | 说明         |
| -------- | ---- | ------ | ------------ |
| rsp_uid  | 是   | string | 响应用户标识 |

### 返回JSON

|属性|类型|说明|
|---|---|---|
|rsp_uid|string|响应用户标识|
|req_id|string|请求标识|
|rsp_id|string|响应标识|
|rsp_idct|string|响应描述|
|rsp_time|timestamp|响应创建时间|



# 二、管理员

## （1）根据请求标识查询某个用户的基本信息

接口 URL：```/api/admin/request/user_info```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型   | 说明     |
| -------- | ---- | ------ | -------- |
| req_id   | 是   | string | 请求标识 |

### 返回JSON

| 属性    | 类型   | 说明     |
| ------- | ------ | -------- |
| u_name  | string | 用户名   |
| u_type  | string | 用户类型 |
| r_name  | string | 用户姓名 |
| p_num   | string | 手机号码 |
| u_level | string | 用户级别 |
| u_idct  | string | 用户简介 |
| r_city  | string | 注册城市 |
| r_cmty  | string | 注册社区 |
| r_time  | string | 注册时间 |

## （2）根据响应标识查询某个用户的基本信息

接口 URL：```/api/admin/response/user_info```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型   | 说明     |
| -------- | ---- | ------ | -------- |
| rsp_id   | 是   | string | 响应标识 |

### 返回JSON

| 属性    | 类型   | 说明     |
| ------- | ------ | -------- |
| u_name  | string | 用户名   |
| u_type  | string | 用户类型 |
| r_name  | string | 用户姓名 |
| p_num   | string | 手机号码 |
| u_level | string | 用户级别 |
| u_idct  | string | 用户简介 |
| r_city  | string | 注册城市 |
| r_cmty  | string | 注册社区 |
| r_time  | string | 注册时间 |

## （3）管理员查询一定条件的请求帮忙信息的状态

接口 URL：```/api/admin/requset_info```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称   | 必选 | 类型      | 说明             |
| ---------- | ---- | --------- | ---------------- |
| req_cmty   | 否   | string    | 更多操作发布社区 |
| req_id     | 否   | string    | 请求标识         |
| req_uid    | 否   | string    | 发布用户标识     |
| req_type   | 否   | string    | 请求类型         |
| req_time   | 否   | timestamp | 创建时间         |
| req_status | 否   | int       | 状态             |

### 返回JSON

|属性|类型|说明|
|---|---|---|
|req_id|string|请求标识|
|req_status|int|状态|

## （4）管理员查询一定条件的接受请求信息

接口 URL：```/api/admin/response_info```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型   | 说明         |
| -------- | ---- | ------ | ------------ |
| req_id   | 否   | string | 请求标识     |
| req_uid  | 否   | string | 发布用户标识 |
| rsp_uid  | 否   | string | 响应用户标识 |
| agc_time | 否   | string | 达成日期     |

### 返回JSON

|属性|类型|说明|
|---|---|---|
|req_id|string|接受请求的请求标识|
|req_uid|string|发布用户标识|
|rsp_uid|string|响应用户标识|
|agc_time|timestamp|达成日期|
|req_fee|int|发布者支付中介费|
|rsp_fee|int|响应者支付中介费|
|agc_fee|int|单笔请求中介费|

## （5）管理员查询已完成请求的中介费

接口 URL：```/api/admin/fee```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

| 参数名称 | 必选 | 类型      | 说明         |
| -------- | ---- | --------- | ------------ |
| req_id   | 否   | string    | 请求标识     |
| req_uid  | 否   | string    | 发布用户标识 |
| rsp_uid  | 否   | string    | 响应用户标识 |
| agc_time | 否   | timestamp | 达成日期     |

### 返回JSON

|属性|类型|说明|
|---|---|---|
|agency_fee|int|累计中介费用|



# 三、统计模块（待定）

接口 URL：```/api/statistics```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|start|是|date|起始时间|
|end|是|date|终止时间|
|city|是|string|地区|
|community|是|string|社区|
|type|是|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|time|string("xx-xx-xx")|时间（按月）|
|money|int|每月中介费|