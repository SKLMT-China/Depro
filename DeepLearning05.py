import pymysql
import sys
global First_Layer_Weight
global Second_Layer_Weight
global Hidden_Data
global Input_Data
global Output_Data
global Ideal_Data
Connect = pymysql.connect(
    host='localhost',
    user='root',
    password='orchid59275',
    db='promoters',
    cursorclass=pymysql.cursors.DictCursor)
cursor = Connect.cursor()
New_Generation = sys.argv[1]
print('Please wait...')
SQL_Change = 'update status set Generation=' + \
    str(New_Generation) + ' where yingyingying=0'
cursor.execute(SQL_Change)
First_Layer_Weight = [[0 for i in range(8)] for i in range(70)]
Second_Layer_Weight = [1, 1, 1, 1, 1, 1, 1, 1]
Init_Data = [0.155012231, 0.189837164, 0.347654202, 0.111101279, 0.281070217, 0.339716307,
             0.177037828, -0.108279307, 0.318687268, -0.074291729, 0.124455909, 0.550429254, 0.08155923,
             -0.029266672, 0.35566244, 0.3372241, -0.014566028, 0.216514201, 0.30601154, 0.262687507,
             0.300525705, 0.13773529, 0.212356119, 0.220772076, 0.234109161, 0.356838642, 0.128457143,
             -0.04400946, 0.07135834, 0.120022348, -0.186003028, 0.243796119, 0.473978387, 0.049719308,
             0.337799428, 0.17194432, 0.316932765, 0.232298947, 0.194708492, -0.033310342, 0.307167024,
             -0.024808585, 0.251813669, 0.235297588, 0.01134687, 0.270247162, -0.013511443, 0.188195084,
             0.189180286, 0.233474373, -0.068706099, 0.164990651, 0.048538517, 0.147593896, 0.021520289,
             0.13701368, 0.173477991, 0.309653053, 0.264742974, -0.235064409, 0.359712277,
             -0.006336457, 0.420876988, 0.242746974]


def Data_Output_Format(x):
    s = 'First'
    if(x == 2):
        s = 'Second'
    if(x == 3):
        s = 'Third'
    if(x == 4):
        s = 'Fourth'
    if(x == 5):
        s = 'Fifth'
    if(x == 6):
        s = 'Sixth'
    return(s)


def Convert_Number_Into_ATCG(x):
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
        s = Convert_Number_Into_ATCG(n) + s
        x = m
    return (s)


Study_Speed = 0.001
cursor.execute('select NumofSets from status where yingyingying=0')
Data_From_Database = cursor.fetchall()
sets = Data_From_Database[0]['NumofSets']
Training_Set = [[0 for i in range(64)] for i in range(sets)]
cursor.execute('select * from data ')
Data_From_Database = cursor.fetchall()
for i in range(sets):
    for j in range(64):
        Training_Set[i][j] = int(Data_From_Database[i][Convert_Into_Seq(j)])
Known_Output = [0 for i in range(sets)]
for i in range(sets):
    Known_Output[i] = Data_From_Database[i]['output']


def Output_Binary_String(x):
    s = ''
    while(x != 0):
        x, mod2 = divmod(x, 2)
        s = str(mod2) + s
    while(len(s) < 6):
        s = '0' + s
    return(s)


def Init_Omega1_Calculate():  # initial data calculating
    global First_Layer_Weight
    global Init_Data
    for i in range(1, 65):
        s = Output_Binary_String(i)
        Num_1 = 0
        for j in range(len(s)):
            if(s[j] == '1'):
                Num_1 += 1
        for j in range(len(s)):
            if(s[j] == '1'):
                First_Layer_Weight[i][j + 1] = Init_Data[i - 1] / Num_1


def Data_Calculate():  # To use present Weight to calculate the data of hidden layer and return final output
    global Input_Data
    global First_Layer_Weight
    global Hidden_Data
    global Second_Layer_Weight
    Hidden_Data = [0 for i in range(8)]
    for i in range(64):
        for j in range(6):
            Hidden_Data[j + 1] = Hidden_Data[j + 1] + \
                Input_Data[i] * First_Layer_Weight[i + 1][j + 1]
    Output = 0
    for i in range(6):
        Output += Hidden_Data[j + 1] * Second_Layer_Weight[j + 1]
    return(Output)


def Weight_Change():  # To update the weights with back propagation algorithm
    global Input_Data
    global Output_Data
    global Ideal_Data
    global First_Layer_Weight
    global Second_Layer_Weight
    global Hidden_Data
    Study_Speed = 0.00045 * abs(Ideal_Data - Output_Data)
    for i in range(64):
        s = Output_Binary_String(i + 1)
        for j in range(len(s)):
            if(s[j] == '1'):
                First_Layer_Weight[i + 1][j + 1] = First_Layer_Weight[i + 1][j + 1] - Study_Speed * \
                    Second_Layer_Weight[j + 1] * Input_Data[i] * (Output_Data - Ideal_Data)
    for i in range(1, 7):
        Second_Layer_Weight[i] = Second_Layer_Weight[i] - \
            Study_Speed * Hidden_Data[i] * (Output_Data - Ideal_Data)


def Supervised_Training():  # Use the known data to train the neural network model
    global Input_Data
    global Ideal_Data
    global Output_Data
    Output_Data = Data_Calculate()
    Weight_Change()


Init_Omega1_Calculate()
generation = int(New_Generation)
for i in range(generation):  # the process of supervised training
    for j in range(sets):
        Input_Data = Training_Set[j]
        Ideal_Data = Known_Output[j]
        Supervised_Training()

for i in range(1, 65):
    for j in range(1, 7):
        SQL_Change = 'update firstlayer set ' + \
            Data_Output_Format(j) + '=' + str(First_Layer_Weight[i][j]) + ' where Number=' + str(i)
        cursor.execute(SQL_Change)
for i in range(1, 7):
    SQL_Change = 'update secondlayer set ' + \
        Data_Output_Format(i) + '=' + str(Second_Layer_Weight[i]) + ' where yingyingying=0'
    cursor.execute(SQL_Change)
print('\nDeep learning has finished! Thank you for using our software.') 
Connect.commit()
Connect.close()
