import pymysql
Connect = pymysql.connect(
    host='localhost',
    user='root',
    password='orchid59275',
    db='promoters',
    cursorclass=pymysql.cursors.DictCursor)
cursor = Connect.cursor()
cursor.execute("create table status(\
                Generation int,\
                NumofSets int,\
                yingyingying int)")
cursor.execute("insert into status values(1000,21,0)")
cursor.execute("create table data(\
               Number int,\
               AAA double,\
               AAT double,\
               AAC double,\
               AAG double,\
               ATA double,\
               ATT double,\
               ATC double,\
               ATG double,\
               ACA double,\
               ACT double,\
               ACC double,\
               ACG double,\
               AGA double,\
               AGT double,\
               AGC double,\
               AGG double,\
               TAA double,\
               TAT double,\
               TAC double,\
               TAG double,\
               TTA double,\
               TTT double,\
               TTC double,\
               TTG double,\
               TCA double,\
               TCT double,\
               TCC double,\
               TCG double,\
               TGA double,\
               TGT double,\
               TGC double,\
               TGG double,\
               CAA double,\
               CAT double,\
               CAC double,\
               CAG double,\
               CTA double,\
               CTT double,\
               CTC double,\
               CTG double,\
               CCA double,\
               CCT double,\
               CCC double,\
               CCG double,\
               CGA double,\
               CGT double,\
               CGC double,\
               CGG double,\
               GAA double,\
               GAT double,\
               GAC double,\
               GAG double,\
               GTA double,\
               GTT double,\
               GTC double,\
               GTG double,\
               GCA double,\
               GCT double,\
               GCC double,\
               GCG double,\
               GGA double,\
               GGT double,\
               GGC double,\
               GGG double,\
               output double\
               )")
cursor.execute("create table firstlayer(\
               Number int,\
               First double,\
               Second double,\
                Third double,\
               Fourth double,\
               Fifth double,\
               Sixth double\
               )")
cursor.execute("create table secondlayer(\
               yingyingying int,\
               First double,\
               Second double,\
               Third double,\
               Fourth double,\
               Fifth double,\
               Sixth double\
               )")

for i in range(21):
    st = "insert into data values (" + str(
        i + 1) + ",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0  )"
    cursor.execute(st)
for i in range(64):
    st = "insert into firstlayer values (" + str(i + 1) + ",0,0,0,0,0,0 )"
    cursor.execute(st)
cursor.execute("insert into secondlayer values(0,0,0,0,0,0,0)")
Connect.commit()
Connect.close()
