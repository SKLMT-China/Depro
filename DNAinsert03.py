import pymysql
import sys

num = [0 for i in range(64)]


def ATCG_Into_Number(x):
    n = 0
    if(x == 'T'):
        n = 1
    elif(x == 'C'):
        n = 2
    elif(x == 'G'):
        n = 3
    return(n)


def Three_Seq(x, y, z):
    n = ATCG_Into_Number(x) * 16 + ATCG_Into_Number(y) * \
        4 + ATCG_Into_Number(z)
    return(n)


def Number_Into_ATCG(x):
    ATCG = 'A'
    if(x == 1):
        ATCG = 'T'
    if(x == 2):
        ATCG = 'C'
    if(x == 3):
        ATCG = 'G'
    return (ATCG)


def Convert_Into_Seq(x):
    s = ''
    for i in range(3):
        (m, n) = divmod(x, 4)
        s = Number_Into_ATCG(n) + s
        x = m
    return (s)


Connect = pymysql.connect(
    host='localhost',
    user='root',
    password='orchid59275',
    db='promoters',
    cursorclass=pymysql.cursors.DictCursor)
cursor = Connect.cursor()
Sequence = sys.argv[1]
Strength = sys.argv[2]
for i in range(68):
    num[Three_Seq(Sequence[i], Sequence[i + 1], Sequence[i + 2])] += 1
cursor.execute("select NumofSets from status where yingyingying=0")
sets = int(cursor.fetchone()['NumofSets'])
SQL_Change = "insert into data values (" + str(
    sets + 1) + ",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0  )"
cursor.execute(SQL_Change)
for i in range(64):
    SQL_Change = "update data set " + \
        Convert_Into_Seq(i) + "=" + str(num[i]) + " where Number=" + str(sets + 1)
    cursor.execute(SQL_Change)
SQL_Change = "update status set NumofSets=" + \
    str(sets + 1) + " where yingyingying=0"
cursor.execute(SQL_Change)
SQL_Change = "update data set output=" + \
    str(Strength) + " where Number=" + str(sets + 1)
cursor.execute(SQL_Change)
print("Congratulations! Imported successfully!")
Connect.commit()
Connect.close()
