import pymysql
import sys
global Input_Data
global Hidden_Data
global First_Layer_Weight
global Second_Layer_Weight
def Data_Input_Format(x):
    s='First'
    if(x==2):
        s='Second'
    if(x==3):
        s='Third'
    if(x==4):
        s='Fourth'
    if(x==5):
        s='Fifth'
    if(x==6):
        s='Sixth'
    return(s)

Connect=pymysql.connect(host='localhost',user='root',password='orchid59275',db='promoters',cursorclass=pymysql.cursors.DictCursor)
cursor = Connect.cursor()
First_Layer_Weight=[[0 for i in range(9)] for i in range(65)]
Second_Layer_Weight=[0 for i in range(9)]
for i in range(1,65):
    for j in range(1,7):
        SQL_Change='select '+Data_Input_Format(j)+' from firstlayer where Number='+str(i)
        cursor.execute(SQL_Change)
        First_Layer_Weight[i][j]=cursor.fetchone()[Data_Input_Format(j)]
for i in range(1,7):
    SQL_Change='select '+Data_Input_Format(i)+' from secondlayer where yingyingying=0'
    cursor.execute(SQL_Change)
    Second_Layer_Weight[i]=cursor.fetchone()[Data_Input_Format(i)]
def ATCG_Value(y):
    if (y=='A'):
        return(0)
    elif (y=='T'):
        return(1)
    elif (y=='C'):
        return(2)
    elif (y=='G'):
        return(3)
def Convert_To_Input(x,y,z): # to convert a sequence into input data
    return(16*ATCG_Value(x)+4*ATCG_Value(y)+ATCG_Value(z))
    
def Data_Calculate(): #To use present Weight to calculate the data of hidden layer and return final output
    global Input_Data
    global First_Layer_Weight
    global Hidden_Data
    global Second_Layer_Weight
    Hidden_Data=[0 for i in range(8)]
    for i in range(64):
        for j in range(6):
            Hidden_Data[j+1]=Hidden_Data[j+1]+Input_Data[i]*First_Layer_Weight[i+1][j+1]
    Output=0
    for i in range(6):
        Output+=Hidden_Data[j+1]*Second_Layer_Weight[j+1]
    return(Output)

Seq=sys.argv[1]
Input_Data=[0 for i in range(64)]
for i in range(len(Seq)-2):
    Input_Data[Convert_To_Input(Seq[i],Seq[i+1],Seq[i+2])]+=1
Output_Data=Data_Calculate()
if(Output_Data<=11):
    print('Pretty Weak')
elif(Output_Data<=12):
    print('Weak')
elif(Output_Data<=13.5):
    print('Normal')
elif(Output_Data<=14.5):
    print('Strong')
else:
    print('Pretty Strong')

Connect.commit()
Connect.close()
