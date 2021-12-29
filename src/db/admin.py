import pandas as pd
from sqlalchemy import create_engine
from src.db import var
from src.db import tb
from src.db import user
from scipy.stats import norm
from pandas.core.frame import DataFrame
from collections import defaultdict
import datetime


"""
    根据请求标识查询发起请求用户的基本信息
    参数顺序：
        req_id
    返回值：
        成功返回list[]
        失败返回False
"""
def admin_reqid_user_info(req_id):
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # sql语句
    sql1 = f'SELECT req_uid FROM tbRequest WHERE req_id=\'{req_id}\''
    try:
        cur.execute(sql1)
        print("执行MySQL查询语句成功")
        u_id = cur.fetchone()[0]
        res = user.user_info(u_id)
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql1, err))
        res = False
    finally:
        cur.close()
        conn.commit()
        conn.close()
        return res


"""
    根据响应标识查询帮忙用户的基本信息
    参数顺序：
        rsp_id
    返回值：
        成功返回list[]
        失败返回False
"""
def admin_rspid_user_info(rsp_id):
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # sql语句
    sql1 = f'SELECT rsp_uid FROM tbResponse WHERE rsp_id=\'{rsp_id}\''
    try:
        cur.execute(sql1)
        print("执行MySQL查询语句成功")
        u_id = cur.fetchone()[0]
        res = user.user_info(u_id)
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql1, err))
        res = False
    finally:
        cur.close()
        conn.commit()
        conn.close()
        return res


"""
    管理员查询已完成请求的中介费
    参数顺序：
        
    返回值：
        成功返回agency_fee
        失败返回False
"""
def admin_agency_fee():
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    sql = f'SELECT COUNT(*) FROM tbSuccess'
    try:
        cur.execute(sql)
        tup = cur.fetchone()
        num = tup[0]
        print("执行MySQL计数语句成功")
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql, err))
    finally:
        cur.close()
        conn.commit()
        conn.close()
        return num*4


if __name__ == '__main__':
    print("admin")
    # print(admin_reqid_user_info('RQ101'))
    # print(admin_rspid_user_info('RS101'))
    print(admin_agency_fee())