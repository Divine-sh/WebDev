import pandas as pd
from sqlalchemy import create_engine
from src.db import var
from src.db import tb
from scipy.stats import norm
from pandas.core.frame import DataFrame
from collections import defaultdict
import datetime


"""
    用户发布响应信息，返回发布结果
    参数顺序：arg_list(list)
    req_id,rsp_uid,rsp_idct
    返回值：
    成功返回rsp_id
    失败返回'RS0'
"""
def user_response_release(arg_list):
    # tbUser表
    table = 2
    # 表名
    table_name = var.table_Name[table]
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # sql语句
    sql_ins = var.sql_insert[table]
    # 将参数转化为元组
    # 生成req_id
    sql1 = f'SELECT nextid FROM tbsequence WHERE tablename=\'{table_name}\''
    sql2 = f'UPDATE tbsequence SET nextid=nextid+1 WHERE tablename=\'{table_name}\''
    cur.execute(sql1)
    rsp_id = f'RS{cur.fetchone()[0]}'
    print(rsp_id)
    arg_list.insert(0, rsp_id)
    cur.execute(sql2)
    # 生成r_time和m_time
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    arg_list.append(now)
    arg_list.append(now)
    arg_list.append(0)
    # 生成元组
    tp = tuple(arg_list)
    # 插入数据库
    try:
        cur.execute(sql_ins, tp)
        print("执行MySQL插入语句成功")
        res = rsp_id
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql_ins, err))
        res = 'RS0'
    finally:
        cur.close()
        conn.commit()
        conn.close()
        return res


"""
    用户查询自己发布的所有响应信息，返回查询结果
    参数顺序：
    rsp_uid
    返回值：
    成功返回[True, tup_list]
    tup_list = list[list[rsp_id,req_id,rsp_uid,rsp_idct,rsp_time,m_time,rsp_status]]
    失败返回[False, None]
"""
def user_response_info(rsp_uid):
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    sql = f'SELECT * ' \
          f'FROM tbResponse WHERE rsp_uid=\'{rsp_uid}\''
    res = cur.execute(sql)
    if res == 0:
        print("用户未发布响应信息！")
        return [False, None]
    else:
        tup_list = []
        for tup in cur.fetchall():
            tup_list.append(list(tup))
        return [True, tup_list]


"""
    用户删除还未被接受的响应信息
    参数顺序：
    rsp_id
    返回值：
    成功返回True
    失败返回False
"""
def user_response_delete(rsp_id):
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # 判断响应信息是否存在
    sql_exist = f'SELECT * FROM tbResponse ' \
                f'WHERE rsp_id=\'{rsp_id}\''
    num = cur.execute(sql_exist)
    if num == 0:
        return False

    sql = f'UPDATE tbResponse ' \
          f'SET rsp_status=3 ' \
          f'WHERE rsp_id=\'{rsp_id}\''
    try:
        cur.execute(sql)
        print(f"更改响应{rsp_id}状态为取消响应状态！")
        res = True
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql, err))
        res = False
    finally:
        cur.close()
        conn.commit()
        conn.close()
        return res


"""
    用户修改还未被接受的响应信息
    参数顺序：arg_list(list)
    rsp_id,rsp_idct
    返回值：
    成功返回True
    失败返回False
"""
def user_response_modify(arg_list):
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # 判断响应信息是否存在
    sql_exist = f'SELECT * FROM tbResponse ' \
                f'WHERE rsp_id=\'{arg_list[0]}\''
    num = cur.execute(sql_exist)
    if num == 0:
        return False

    sql = f'UPDATE tbResponse ' \
          f'SET rsp_idct=\'{arg_list[1]}\' ' \
          f'WHERE rsp_id=\'{arg_list[0]}\''
    try:
        cur.execute(sql)
        print("执行MySQL更新语句成功")
        res = True
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql, err))
        res = False
    finally:
        cur.close()
        conn.commit()
        conn.close()
        return res


"""
    用户查看某一请求信息的所有帮忙信息，返回查询结果
    参数顺序：
    req_id
    返回值：
    成功返回[True, list[list[]]]
    失败返回[false, None]
"""
def user_request_response_info(req_id):
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    sql = f'SELECT * ' \
          f'FROM tbResponse WHERE req_id=\'{req_id}\''
    res = cur.execute(sql)
    if res == 0:
        print(f"请求信息{req_id}不存在！")
        return [False, None]
    else:
        tup_list = []
        for tup in cur.fetchall():
            tup_list.append(list(tup))
        return [True, tup_list]


"""
    用户查询自己所有已经被接受的请求响应信息，返回查询结果
    参数顺序：
    rsp_uid
    返回值：
    成功返回[True, tup_list]
    tup_list = lsit[list[rsp_id,req_id,rsp_uid,rsp_idct,rsp_time]]
    失败返回[False, None]
"""
def user_response_accepted(rsp_uid):
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    sql = f'SELECT rsp_id,req_id,rsp_uid,rsp_idct,rsp_time ' \
          f'FROM tbResponse WHERE rsp_uid=\'{rsp_uid}\' AND rsp_status=1'
    res = cur.execute(sql)
    if res == 0:
        print(f"用户{rsp_uid}不存在被接受的响应信息！")
        return [False, None]
    else:
        tup_list = []
        for tup in cur.fetchall():
            tup_list.append(list(tup))
        return [True, tup_list]


"""
    用户处理响应信息，返回处理结果
    注意，处理响应信息的情况：
        1.拒绝，被拒绝的响应信息状态修改
        2.同意，帮忙请求信息和相应信息对应状态修改，修改帮忙成功明细表
    参数顺序：arg_list(list)
    req_id,req_uid,rsp_id,rsp_uid,option
    返回值：
    成功返回True
    失败返回False
"""
def user_opt_response(arg_list):
    # 提取参数
    req_id = arg_list[0]
    req_uid = arg_list[1]
    rsp_id = arg_list[2]
    rsp_uid = arg_list[3]
    option = arg_list[4]
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # 获取当前时间
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    # 判断请求id和响应id是否对应
    sql = f'SELECT * FROM tbResponse ' \
          f'WHERE req_id=\'{req_id}\' AND rsp_id=\'{rsp_id}\''
    num = cur.execute(sql)
    print("num: ", num)
    if num == 0:
        return False
    # 判断option
    if option:  # 接收响应
        sql1 = f'UPDATE tbResponse SET rsp_status=1 WHERE rsp_id=\'{rsp_id}\''
        sql2 = f'INSERT INTO tbSuccess(req_id,req_uid,rsp_id,rsp_uid,agc_time) ' \
               f'VALUES (%s,%s,%s,%s,%s)'
        try:
            cur.execute(sql1)
            print(f"被接受的响应信息{rsp_id}状态修改")
            cur.execute(sql2, (req_id, req_uid, rsp_id, rsp_uid, now))
            print(f"帮忙成功表中添加记录")
            res = True
        except Exception as err:
            print("执行MySQL语句时出错: \n%s" % err)
            res = False
    else:  # 拒绝响应
        sql = f'UPDATE tbResponse SET rsp_status=2 WHERE rsp_id=\'{rsp_id}\''
        try:
            cur.execute(sql)
            print(f"被拒绝的响应信息{rsp_id}状态修改")
            res = True
        except Exception as err:
            print("执行MySQL: %s 时出错: \n%s" % (sql, err))
            res = False
    cur.close()
    conn.commit()
    conn.close()
    return res


if __name__ == '__main__':
    print("response")
    # user_response_release(['RQ103', 'UR100', '会舞蹈才艺'])
    # user_response_release(['RQ101', 'UR100', '上班路线相同'])
    # user_response_release(['RQ101', 'UR102', '上班路线相同'])
    # print(user_response_info('UR100'))
    # user_response_delete('RS100')
    # user_response_modify(['RS101', '上班路线相同,有搭车意向'])
    # print(user_request_response_info('RQ101'))
    # print(user_response_accepted('UR100'))
    # user_opt_response(['RQ101', 'UR101', 'RS102', 'UR102', False])
    # user_opt_response(['RQ101', 'UR101', 'RS102', 'UR102', True])
    # user_opt_response(['RQ101', 'UR101', 'RS101', 'UR100', True])
    # print(user_response_accepted('UR100'))
