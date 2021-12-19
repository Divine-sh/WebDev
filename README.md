# 《好社区》原型系统
## 一、数据库部分

#### （1）用户类

| 用户标识 | 用户名 | 登录密码              | 用户类型 | 用户姓名 | 证件类型 | 证件号码 | 手机号码 | 用户级别   | 用户简介 | 注册城市 | 注册社区 | 注册时间 | 修改时间 |
| -------- | ------ | --------------------- | -------- | -------- | -------- | -------- | -------- | ---------- | -------- | -------- | -------- | -------- | -------- |
| u_id     | u_name | u_pwd                 | u_type   | r_name   | c_type   | c_num    | p_num    | u_level    | u_idct   | r_city   | r_cmty   | r_time   | m_time   |
|          |        | 系统管理员 / 普通用户 |          |          |          |          | 11位数字 | 一般 / VIP |          |          |          |          |          |

注：在后台数据库至少要建立一个管理员用户,用户名：admin,密码 admin。 

#### （2）“劳您驾”请求信息类

| 请求标识 | 发布用户标识 | 请求类型                                      | 请求主题名称 | 请求描述 | 请求人数 | 请求结束日期 | 请求介绍照片 | 创建时间 | 修改时间 | 状态                                  |
| -------- | ------------ | --------------------------------------------- | ------------ | -------- | -------- | ------------ | ------------ | -------- | -------- | ------------------------------------- |
| req_id   | req_uid      | req_type                                      | req_theme    | req_idct | req_nop  | end_time     | req_photo    | req_time | m_time   | req_status                            |
|          |              | 小时工 / 搬重物 / 上下班搭车 / 社区服务自愿者 |              |          |          |              | 可空         |          |          | 已完成 / 待响应 / 已取消 / 到期未达成 |

#### （3）响应类

| 响应标识 | 请求标识 | 响应用户标识 | 响应描述 | 创建时间 | 修改时间 | 状态                                    |
| -------- | -------- | ------------ | -------- | -------- | -------- | --------------------------------------- |
| rsp_id   | req_id   | rsp_uid      | rsp_idct | rsp_time | m_time   | rsp_status                              |
|          |          |              |          |          |          | 0：待接受 / 1：同意 / 2：拒绝 / 3：取消 |

#### （4）“劳您驾”帮忙成功明细表

| 请求标识 | 发布用户标识 | 响应用户标识 | 达成日期  | 发布者支付中介费 | 响应者支付中介费 | 单笔请求中介费 |
| -------- | ------------ | ------------ | --------- | ---------------- | ---------------- | -------------- |
| req_id   | req_uid      | rsp_uid      | comp_time | req_fee          | rsp_fee          | comp_fee       |
|          |              |              |           |                  |                  |                |

#### （5）中介收益汇总表

| 月份   | 地域  | 社区 | 请求帮忙类型 | 达成笔数 | 中介费收入金额 |
| ------ | ----- | ---- | ------------ | -------- | -------------- |
| YYYYMM | 省-市 |      |              |          |                |
|        |       |      |              |          |                |

注：开始可以直接在数据库中插入些符合业务逻辑的测试数据。数据库表可以涵盖上述要求基础上扩展其它内容
