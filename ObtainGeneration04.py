import pymysql
Connect=pymysql.connect(host='localhost',user='root',password='orchid59275',db='promoters',cursorclass=pymysql.cursors.DictCursor)
cursor = Connect.cursor()
cursor.execute('select generation from status where yingyingying=0')
Existed_Generation=cursor.fetchall()[0]['generation']
Connect.commit()
Connect.close()
 
