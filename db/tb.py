import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
import time
from db import var
import os


def change_database_sqlmode():
    # 初始化数据库连接，使用pymysql模块
    # MySQL的用户：root, 密码:123456, 端口：3306,数据库：ltedb
    engine = create_engine(var.engine_creation)
    sql = "select @@global.sql_mode;"
    dfData = pd.read_sql_query(sql, engine)
    sql_mode = str(dfData.iloc[0][0])
    sql_mode = sql_mode.replace('ONLY_FULL_GROUP_BY,', '')
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    sql = "set @@global.sql_mode ='" + sql_mode + "';"
    cur.execute(sql)


'''
    建表函数:table_create
    table:int   数据表，取值1-5分别表示 tbUser、tbRequest、tbResponse、tbSuccess、tbProfit;
'''


def table_create(table):
    # 索引为table
    table = table - 1
    # 表名
    tb_Name = var.table_Name[table]
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # 如果表已经存在，使用execute() 删除表
    cur.execute("drop table if EXISTS " + tb_Name)
    # sql语句
    sql1 = "create table " + tb_Name + var.sql_create[table]
    try:
        # 执行sql语句并commit
        cur.execute(sql1)
        conn.commit()
        print("建表" + tb_Name + "成功")
    except Exception as err:
        # 出错时回滚（Rollback in case there is any error）
        print("建表" + tb_Name + "时出错 {}".format(str(err)))
        conn.rollback()
    # 断开连接
    conn.close()


def table_insert(table, df):
    # 索引为table
    table = table - 1
    # 表名
    tb_Name = var.table_Name[table]
    # 将导入的nan转换为None,nan不能在MySQL中使用
    df = df.where(df.notnull(), None)

    # # 特判转换为标准datetime格式
    # if table == 1 or table == 2:
    #     df['起始时间'] = pd.to_datetime(df['起始时间'])

    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()

    # sql语句
    sql_ins = var.sql_insert[table]

    # 导入数据
    # args是一个包含多个元组的列表
    args = df.values.tolist()
    for i in range(len(args)):
        args[i] = tuple(args[i])
    # print(args)
    try:
        cur.executemany(sql_ins, args)
        print("执行MySQL插入语句成功")
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql_ins, err))
    finally:
        cur.close()
        conn.commit()
        conn.close()
        # # 若向tbPRB插入数据，则需要同时生成tbPRBNEW中的数据
        # if table == 2:
        #     print("若向tbPRB插入数据，则需要同时生成tbPRBNEW中的数据")
        #     data_bulkinsert_prbnew()


def table_update(table, arg_list):
    # 索引为table
    table = table - 1
    # 表名
    tb_Name = var.table_Name[table]

    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()

    # sql语句
    sql_upt = f'UPDATE {tb_Name} '
    if tb_Name == 'tbUser':
        arg = f'SET u_pwd={arg_list[1]},p_num={arg_list[2]}' \
              f'WHERE u_id={arg_list[0]}'
    elif tb_Name == 'tbRequest':
        arg = f'SET req_type={arg_list[1]},req_topic={arg_list[2]},req_idct={arg_list[3]},req_nop={arg_list[4]},end_time={arg_list[5]},m_time=NULL' \
              f'WHERE req_id={arg_list[0]}'
    elif tb_Name == 'tbResponse':
        arg = f'SET rsp_idct={arg_list[1]},m_time=NULL' \
              f'WHERE rsp_id={arg_list[0]}'
    elif tb_Name == 'tbSuccess':
        return
    elif tb_Name == 'tbProfit':
        return

    sql_upt += arg
    try:
        cur.execute(sql_upt)
        print("执行MySQL插入语句成功")
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql_upt, err))
    finally:
        cur.close()
        conn.commit()
        conn.close()
        # # 若向tbPRB插入数据，则需要同时生成tbPRBNEW中的数据
        # if table == 2:
        #     print("若向tbPRB插入数据，则需要同时生成tbPRBNEW中的数据")
        #     data_bulkinsert_prbnew()


if __name__ == '__main__':
    for i in range(1, 6):
        table_create(i)

    # filePath = '12. tbCellKPI-优化区17日-19日KPI指标统计表-0717至0719.xlsx'
    # df = pd.read_excel(filePath, sheet_name=0)
    # filePath = '9. tbMROData.csv'
    # df = pd.read_csv(filePath)
    # data_bulkinsert(4, df)
    # data_bulkinsert_prbnew()
    # table_create(9)
    # trigger_create(9)
    # filePath = '1.tbCell.xlsx'
    # df = pd.read_excel(filePath, sheet_name=0)
    # data_bulkinsert(1, df)
    # add_index(1, "SECTOR_ID,SECTOR_NAME,ENODEBID", "tbcell_index")
    #add_index(1, "SECTOR_NAME", "SECTOR_NAME")
    # print(select_index(1))
