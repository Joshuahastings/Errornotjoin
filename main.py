print("hello people, i'm joshua aka ErrorNotJoin And This Is My College Work :)");



def Maths():

 a = -5 + 8* 6
 b = (55 + 9) % 9
 c = 20 + -3 * 5 / 8
 d = 5 + 15 /3*2 - 8 % 3
 #saving the pythone awser
 print("!\___________Pythom Basics Maths_________/!" )
 print("a: " + str(a) + "\n" + "b: " + str(b) +"\n" + "c: " + str(c) + "\n" + "d: "  + str(d) + "\n" + "!\_____________END_______________________/!"   )
 #showing the aw and number them
 print(" " + "\n")
 print("!\___________User Input Maths________/!")
 user_number_one  = (input("What is Your Number: "))
 #Getting the first Number From the User
 user_number_two  = (input("What is Your Number: "))
 #Getting a sec Number  From the User
 e = int(user_number_one) / int(user_number_two)
 #Pytohn is Div the number
 print(user_number_one +" / "+ user_number_two +  " = " + str(e) )
 #Showing The User Number And What That = To
 print("!\____________END______________________/!")

 Main()



def Main():
    #leting the user pick What function That what to go
    user = input("where do you what to go: " +"\n" + "1:Maths or maths" + "\n" +"2:Games"+"\n" +"I Pick: ")
    if(user == "Maths" or user == "maths" or user == "1"):
       Maths()
    if(user == "Where Can i go" or "2"):
        print("This dose Work")


Main()