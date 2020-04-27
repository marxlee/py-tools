import pymysql, re


def connect():
    db = pymysql.connect(host="212.64.15.***", port=3306, user="hadoop",password="hadoop", database="py_tech", charset="utf8" )
    return db


def show_database(db):
    with db.cursor() as cursor:
        cursor.execute('show databases;')
        data = cursor.fetchall()
        print(data)


def create_table(db):
    sql = """CREATE TABLE user (
             `id` BIGINT(32) NOT NULL AUTO_INCREMENT COMMENT 'ID' ,
             `user_name`  VARCHAR(255) DEFAULT NULL COMMENT '用户名',
             `gender`  INT(4) NOT NULL COMMENT '性别',
             `age` INT(4) NOT NULL COMMENT '年龄',
             `is_del` INT(4) NOT NULL COMMENT '删除',
             `create_time` timestamp NOT NULL COMMENT 'CREATE_TIME',
             `update_time` timestamp NOT NULL COMMENT 'UPDATA_TIME',
             PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '用户表';
             -- 5.6版本只能有一个默认的current_timestamp
         """
    with db.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)


def select_data(db):
    sql = """
            select * from user;
        """
    with db.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            id = row[0]
            name = row[1]
            gender = row[2]
            age = row[3]
            is_del = row[4]
            ctime = row[5]
            utime = row[6]
            print('数据信息: %d, %s, %d, %d, %d, %s, %s' % (id, name, gender, age, is_del, ctime, utime))
        # print(data)


def insert_data(db):
    sql = "INSERT INTO user( \
               user_name, gender, age, is_del, create_time, update_time) \
               VALUES ('%s', '%d',  %d,  0, now(),  now())" % \
          ('Maria', 1, 26)
    with db.cursor() as cursor:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        print(data)
        db.close()

def excutor_sql(sql):
    sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
    db = pymysql.connect(host="212.64.15.224", port=3306, user="hadoop", password="hadoop", database="py_tech",
                         charset="utf8")
    cursor = db.cursor()
    # 执行SQL语句
    cursor.execute(sql)
    try:
        ret = re.search('select', sql, re.I)
        if ret != None:
            data = cursor.fetchall()
            print(data)
        else:
            # 向数据库提交 针对update , create, insert, delete 操作
            db.commit()


    except:
        cursor.close()
        # 发生错误时回滚
        db.rollback()
    db.close()

if __name__ == '__main__':
    # db = connect()
    # show_database(db)
    # create_table(db, sql)
    # select_data(db)
    # insert_data(db)


    pass

