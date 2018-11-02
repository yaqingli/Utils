import MySQLdb
from datetime import datetime, timedelta
import sys


def delete_data(host, user, psw, db, table, start_date, end_date, port=None):
    try:
        conn = MySQLdb.connect(host, user, psw, db)
        csr = conn.cursor()
        current_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        while current_date<=end_date:
            sql = "delete from {0}.{1} where pt='{2}'".format(db,table,current_date.strftime('%Y-%m-%d'))
            print sql
            csr.execute(sql)
            conn.commit()
            current_date += timedelta(days=1)
    except Exception, e:
        print str(e)
    finally:
        conn.close()


def move_data(host, user, psw, db, target_table, source_table, start_date, end_date, port=None):
    try:
        conn = MySQLdb.connect(host, user, psw, db)
        csr = conn.cursor()
        current_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        while current_date<=end_date:
            sql = "insert into {0} select * from {1}.{2} where pt='{3}'".format(target_table, db,source_table, current_date.strftime('%Y-%m-%d'))
            print sql
            csr.execute(sql)
            conn.commit()
            current_date += timedelta(days=1)
    except Exception, e:
        print str(e)
    finally:
        conn.close()

if __name__ == '__main__':
    host = ''
    user = ''
    psw = ''
    db = ''
    if len(sys.argv) == 6:
        operation = sys.argv[1]
        if operation == 'mov':
            source_table = sys.argv[2]
            target_table = sys.argv[3]
            start_time = sys.argv[4]
            end_time = sys.argv[5]
            move_data(host, user, psw, db, target_table, source_table, start_time, end_time)
        elif operation == 'del':
            table = sys.argv[2]
            start_time = sys.argv[3]
            end_time = sys.argv[4]
            delete_data(host, user, psw, db, table, start_time, end_time)
    

