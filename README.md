# GitHub_Test


2 bits History

command:  
使用 Python 3.6,pycharm 書寫,  
輸入值:    
    Q01_input_2bitH.in  
    如:T N N T N N T N N T N N  
執行主程式:  
    P01_code_2bitHistory.py  
  
  
執行結果:(執行結果-01.jpg)  
['T', 'N', 'N', 'T', 'N', 'N', 'T', 'N', 'N', 'T', 'N', 'N']  
12  
row | 2bitHistory | 2BC[0] 2BC[1] 2BC[2] 2BC[3] | Predict |  True |  
000 | 2bitH=0     |   SN     SN     SN     SN   | Pred=N  |   T   |  
001 | 2bitH=1     |   WN     SN     SN     SN   | Pred=N  |   N   |  
003 | 2bitH=0     |   WN     SN     SN     SN   | Pred=N  |   T   |  
004 | 2bitH=1     |   WT     SN     SN     SN   | Pred=N  |   N   |  
005 | 2bitH=2     |   WT     SN     SN     SN   | Pred=N  |   N   |  
006 | 2bitH=0     |   WT     SN     SN     SN   | Pred=T  |   T   |  
007 | 2bitH=1     |   ST     SN     SN     SN   | Pred=N  |   N   |  
008 | 2bitH=2     |   ST     SN     SN     SN   | Pred=N  |   N   |  
009 | 2bitH=0     |   ST     SN     SN     SN   | Pred=T  |   T   |  
010 | 2bitH=1     |   ST     SN     SN     SN   | Pred=N  |   N   |  
011 | 2bitH=2     |   ST     SN     SN     SN   | Pred=N  |   N   |  
    
    
系統流程：    
1.讀擋 ,Q01_input_2bitH.in  
2.初始陣列設定  
3.做預測  
4.根據結果,更新陣列,  
5.迴圈,重複 3. 4. ,直到結束,  
  
     
程式註解:  
在主程式P01_code_2bitHistory.py中,以  
#-----------------------------------------------------------  
#-註解  
#-----------------------------------------------------------  
表示註解,  
  
  
參考:  
Lecture5 (上課驗收日：1024) & Project 1    
09-2bit history predictor example [Computer Arch - Branch]    
  
  
