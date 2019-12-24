# coding=UTF-8
#import math

# Lecture5 (10/24) & Project 1 ,# 9

if __name__ == "__main__":
    #--------------------------------------------------------------------------
    # 取值 ,
    # --------------------------------------------------------------------------
    f = open('./Q01_input_2bitH.in', 'r')
    lines = f.readlines()
    for line in lines:
        num_list = line.split(' ')
        # Write your code here
    print(num_list)
    counter_C=len(num_list)
    print(counter_C)

    #--------------------------------------------------------------------------
    # 初始設定 ,
    # --------------------------------------------------------------------------
    history_2bit=0
    #history_2bit_temp=0
    history_2BC = ['SN','SN','SN','SN']
    history_Predict='N'
    print('row |'+' 2bitHistory |'+' 2BC[0] 2BC[1] 2BC[2] 2BC[3] |'+' Predict | '+' True |' )

    # --------------------------------------------------------------------------
    # 開始 2bits History , 預測,
    # --------------------------------------------------------------------------
    for i in range(counter_C):
        if history_2bit == 0: # predict
            if history_2BC[0] == 'SN':
                history_Predict = 'N'
            elif history_2BC[0] == 'WN':
                history_Predict = 'N'
            elif history_2BC[0] == 'WT':
                history_Predict = 'T'
            elif history_2BC[0] == 'ST':
                history_Predict = 'T'
        elif history_2bit == 1: # predict
            if history_2BC[1] == 'SN':
                history_Predict = 'N'
            elif history_2BC[1] == 'WN':
                history_Predict = 'N'
            elif history_2BC[1] == 'WT':
                history_Predict = 'T'
            elif history_2BC[1] == 'ST':
                history_Predict = 'T'
        elif history_2bit == 2: # predict
            if history_2BC[2] == 'SN':
                history_Predict = 'N'
            elif history_2BC[2] == 'WN':
                history_Predict = 'N'
            elif history_2BC[2] == 'WT':
                history_Predict = 'T'
            elif history_2BC[2] == 'ST':
                history_Predict = 'T'
        elif history_2bit == 3:  # predict
            if history_2BC[3] == 'SN':
                history_Predict = 'N'
            elif history_2BC[3] == 'WN':
                history_Predict = 'N'
            elif history_2BC[3] == 'WT':
                history_Predict = 'T'
            elif history_2BC[3] == 'ST':
                history_Predict = 'T'

        print('%.3d |' %i+' 2bitH=%d     |   ' %history_2bit+str(history_2BC[0])+'     '+str(history_2BC[1])+'     '+str(history_2BC[2])+ \
              '     ' + str(history_2BC[3])+'   | Pred='+str(history_Predict)+'  |   '+num_list[i]+'   |')

        # --------------------------------------------------------------------------
        # 2bits History , 更新,
        # --------------------------------------------------------------------------
        if num_list[i]=='N': # updata
            if history_2BC[history_2bit] =='WN':
                history_2BC[history_2bit] = 'SN'
            elif history_2BC[history_2bit] =='WT':
                history_2BC[history_2bit] = 'WN'
            elif history_2BC[history_2bit] =='ST':
                history_2BC[history_2bit] = 'WT'
        elif num_list[i]=='T':
            if history_2BC[history_2bit] =='SN':
                history_2BC[history_2bit] = 'WN'
            elif history_2BC[history_2bit] =='WN':
                history_2BC[history_2bit] = 'WT'
            elif history_2BC[history_2bit] =='WT':
                history_2BC[history_2bit] = 'ST'

        if num_list[i]=='T':
            if history_2bit == 0:
                history_2bit =1
            elif history_2bit == 1:
                history_2bit =3
            elif history_2bit == 2:
                history_2bit =1
        elif num_list[i]=='N':
            if history_2bit == 1:
                history_2bit =2
            elif history_2bit == 2:
                history_2bit =0
            elif history_2bit == 3:
                history_2bit =2

    f.close()

    #--------------------------------------------------------------------------
    # --------------------------------------------------------------------------
