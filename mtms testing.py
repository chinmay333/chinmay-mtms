"""
01234567891111111111222222222233333333334444444444555555555
                    0123456789012345678901234567890123456789012345678                      
 *                 *          * * * * * * * * *            *                 *           * * * * * * * * *   0
 *    *       *   *                    *                      *    *       *   *          *                       1
 *        *       *                     *                      *        *       *           * * * * * * * * *   2
 *                 *                    *                      *                 *                               *   3 
 *                 *                    *                      *                 *                               *   4
 *                 *                    *                      *                 *           * * * * * * * * *   5
"""

import mysql as msc
try:
                mynn=msc.connect(host="localhost",user="root",password="chinmaybhagat",database="mtms")

                if mynn.is_connected():
                                print("Connected Successfully")
except:
                print("connection error")
def MTMS(password):
                if password=="bvcbcsmtms":
                                for i in range(5):
                                                for j in range(90):
                                                                if i==0 and (j in [1,10,16 ,18,20 ,22 ,24 ,26,37,48,58,60,62,64,66,68]): 
                                                                                print("*",end=" ")
                                                                elif i==1 and(j in [1,4,8,10,23,38,42,46,48,58]):
                                                                                print("*",end=" ")
                                                                elif i==2 and(j in [1,10,6,23,38,44,48,60,62,64,66,68,70]):
                                                                                print("*",end=" ")
                                                                elif i==3 and (j in [1,10,23,38,48,73]):
                                                                                print("*",end=" ")
                                                                elif i==4 and (j in [1,10,23,38,48,60,62,64,66,68,70]):
                                                                                print("*",end=" ")
                                                                else:
                                                                                print(" ",end=" ")
                                                print()
                                print("MOVIE TICKET MANAGEMENT SYSTEM")
                                for i in range(25):
                                                print(" ",end=" ")
                return("-By Chinmay and Bhavesh")


password=str(input("Enter the password"))
print(MTMS(password))

