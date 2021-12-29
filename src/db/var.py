import pymysql


def pymysql_connect():
    con = pymysql.connect(host='localhost',
                          user='root',
                          passwd='123456',
                          db='webdev',
                          port=3306,
                          charset='utf8')
    return con


engine_creation = 'mysql+pymysql://root:123456@localhost:3306/webdev'
table_Name = [
    'tbUser', 'tbRequest', 'tbResponse', 'tbSuccess', 'tbProfit'
]
sql_create = [
    """ 
        (   
            u_id         VARCHAR (30) UNIQUE KEY,
            u_name       VARCHAR (30) UNIQUE KEY,
            u_pwd        VARCHAR (30) NOT NULL,
            u_type       INT NOT NULL,
            r_name       VARCHAR (30) NOT NULL,
            c_type       INT NOT NULL,
            c_num        VARCHAR (30) NOT NULL,
            p_num        VARCHAR (30) NULL,
            u_level      INT NOT NULL,
            u_idct       VARCHAR (300) NULL,
            r_city       VARCHAR (30) NOT NULL,
            r_cmty       VARCHAR (30) NOT NULL,
            r_time       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            m_time       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY(u_id)              
        );
        """,
    """
        (   
            req_cmty     VARCHAR (50) NOT NULL,
            req_id       VARCHAR (50) NOT NULL,
            req_uid      VARCHAR (50) NOT NULL,  
            req_type     INT NOT NULL,
            req_topic    VARCHAR (100) NOT NULL,
            req_idct     VARCHAR (300) NOT NULL,
            req_nop      INT NOT NULL DEFAULT 1,
            end_time     TIMESTAMP NOT NULL,
            req_photo    VARCHAR (100) NULL,
            req_time     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            m_time       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            req_status   INT NOT NULL,
            PRIMARY KEY(req_id)   
        );      
    """,
    """
        (
            rsp_id       VARCHAR (50) NOT NULL,
            req_id       VARCHAR (50) NOT NULL,
            rsp_uid      VARCHAR (50) NOT NULL,  
            rsp_idct     VARCHAR (300) NOT NULL,
            rsp_time     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            m_time       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            rsp_status   INT NOT NULL,
            PRIMARY KEY(rsp_id)
        );    
    """,
    """
        (
            req_id       VARCHAR (50) NOT NULL,
            req_uid      VARCHAR (50) NOT NULL,
            rsp_id       VARCHAR (50) NOT NULL,
            rsp_uid      VARCHAR (50) NOT NULL,  
            agc_time     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(req_id,rsp_id)
        );
    """,
    """
        (
            n_month        TIMESTAMP NOT NULL,
            region         VARCHAR(50) NOT NULL,
            cmty           VARCHAR(50) NOT NULL,
            req_type       VARCHAR (50) NOT NULL,
            num            INT NOT NULL,
            total_fee      INT NOT NULL,
            PRIMARY KEY(n_month,region,cmty)
        );
    """,
]
sql_trigger = []
sql_insert = [
    """
        insert into 
        tbUser(u_id,u_name,u_pwd,u_type,r_name,c_type,c_num,p_num,u_level,u_idct,r_city,r_cmty,r_time,m_time) 
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    """
        insert into 
        tbRequest(req_cmty,req_id,req_uid,req_type,req_topic,req_idct,req_nop,end_time,req_photo,req_time,m_time,req_status) 
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    """
        insert into 
        tbResponse(rsp_id,req_id,rsp_uid,rsp_idct,rsp_time,m_time,rsp_status)
        values(%s,%s,%s,%s,%s,%s,%s)
    """,
    """
        insert into 
        tbSuccess(req_id,req_uid,rsp_uid,agc_time,req_fee,rsp_fee,agc_fee)
        values(%s,%s,%s,%s,%s,%s,%s)
    """,
    """
        insert into tbProfit(n_month,region,cmty,req_type,num,total_fee)
        values(%s,%s,%s,%s,%s,%s)
    """
]
sql_update = [
    """
        UPDATE tbUser
        SET course_name='DB',course_grade=3.5
        WHERE course_id=2;
    """,
    """
        UPDATE tbRequest
        SET course_name='DB',course_grade=3.5
        WHERE course_id=2;
    """,
    """
        UPDATE tbResponse
        SET course_name='DB',course_grade=3.5
        WHERE course_id=2;
    """,
    """
        UPDATE tbSuccess
        SET course_name='DB',course_grade=3.5
        WHERE course_id=2;
    """,
    """
        UPDATE tbProfit
        SET course_name='DB',course_grade=3.5
        WHERE course_id=2;
    """
]