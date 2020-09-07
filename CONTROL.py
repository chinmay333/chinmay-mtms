movie_name=["Inception","Gravity","Shawshank","Interstellar"]
multiplexes={"pvr":"a","cinepolis":"b","inox":"c","Carnivals":"d","Mukta A2":"e"}
multiplexeslist=list(multiplexes)
administerslist=[]
for i in multiplexes:
                m=multiplexes.get(i)
                administerslist.append(m)
                
import webbrowser
import datetime
import random
import datetime
def administration():
                multi_name=str(input("Enter the multiplex name"))

                try:
                                if multi_name in multiplexes:
                                                print("Hello Mr how can i help you")
                                else:
                                                print("Oh no such theatre is there")
                except:
                                print("Oh no such theatre is there")
def user():
                user_name=str(input("Enter the your name"))
                i=str(input("Press Enter to watch the list"))
                try:
                                for i in movie_name:
                                                print(i)
                                movie_1=str(input("Which movie would U like to watch"))
                               
                except:
                                print("Not There")
                return("")
def registering():
                num=int(input("how many multiplexes?"))
                for i in range(num):
                                multi=str(input("Enter the new multiplex"))
                                multiplexeslist.append(multi)
                print(multiplexeslist)
"""
def information():
                print(user)
                choice=str(input("Hello"+"Which movie are you Going to watch Mr."+user_name+"?"))
                if i in movie_name:
                                links={"Inception":" ","Gravity":" ","Shawshank":" ","Interstellar":" "}
                                if i in links:
                                                webbrowser.open()
"""
def newrelease():
                opt_1=int(input("do you want to add or remove any of the movie"))
                if opt_1==1:
                                n=int(input("how many movies do U want to remove or add?"))
                                for i in range(n):
                                                opt_2=str(input("type add or remove"))
                                                if opt_2=="add":
                                                                new=str(input("Enter the name of the new movie"))
                                                                movie_name.append(new)
                                                elif opt_2=="remove":
                                                                removed=str(input("Enter the removed movie"))
                                                                for j in range(n):
                                                                                if removed in movie_name:
                                                                                                movie_name.pop(removed)
                                print(movie_name)
                else:
                                print("Okay")
"""
def offers():
                Tuesday offer ,Festival offers
                """
def Xtracharge():
                x_1=int(input("Do you want to pay the extra charge?"))
                if x_1==1:
                                webbrowser.open()
                                #mysql connectivity
                else:
                                print("Okay")
def game():
                gm=open("Lucky Draw Game.txt","r")
                for i in gm:
                                print(i)
                draw=random.randint(1,1000)
                strdraw=str(draw)
                choicee=int(input("enter number between 0 and 9"))
                for i in range(0,(len(strdraw))):
                                choicee=int(input("enter number between 0 and 9"))
                                choicees=str(choicee)
                                if choicees[i]!=strdraw[i]:
                                                print("Ohh you are out")
                                                break
                                
                                else:
                                                pass
                print("The number is ",draw)

def menu_2():
                option=int(input("Enter the option"))
                if option==1:
                                print(registering())
                elif option==2:
                                inp=int(input("Enter 7 to play lucky draw game"))
                                print(user())
                                if inp==7:
                                                print(game())
                                else:
                                                print("ok")

                elif option==3:
                                print(offers)
                elif option==4:
                                print(newrelease())
                elif option==5:
                                print(offers())
                elif option==6:
                                print(Xtracharge())
                else:
                                print("No such option")
                
                
#MAIN
print(movie_name)
print(multiplexeslist)
q=str(input("Enter if U want to start or quit"))
while q!="quit":
                if q=="start":
                                print(menu_2())            

