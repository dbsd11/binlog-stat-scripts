#_*_ coding:utf-8 _*_

import sys
import os
import io

binlogfile = sys.argv[1]
database_name = sys.argv[2]
table_name = sys.argv[3]

def format_binlog():
    os.system('mysqlbinlog --base64-output=decode-rows -v '+binlogfile+'>'+binlogfile+'.txt')

def pickupbinlog():
    f = io.open(binlogfile+'.txt','r')
    fw = io.open(binlogfile+'_'+database_name+'_'+table_name+'.txt','a')
    priv_str = ''
    priv_line = ''
    goal_flag = 0
    for row in f:
        # 处理首行
        if row[0:3] == '###' and priv_str != '###':
            if database_name in row and table_name in row:
                goal_flag = 1
                fw.write(priv_line)
                fw.write(row)
        # 处理末行
        if row[0:3] != '###' and priv_str == '###':
            goal_flag = 0
        # 处理目标操作
        if row[0:3] == '###' and priv_str == '###' and goal_flag == 1:
            fw.write(row)
        priv_str = row[0:3]
        priv_line = row
    f.close()
    fw.close()

if __name__ == '__main__':
    # python2.7 pickupbinlog.py mysql-bin.001051 dbname tablename
    # python3 pickupbinlog.py mysql-bin.001051 dbname tablename
    format_binlog()
    pickupbinlog()
