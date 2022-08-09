print("hello people, i'm joshua aka ErrorNotJoin And This Is My College Work :)");


worlds = "___Numbers In Order____\n1: "
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
def Python_Control_Statements():
    print("!\___________Python Control Statements_________/!")
    #getting the user pick there number
    user_pick_a_number_one = input("1: Pick a Number: ")
    user_pick_a_number_two = input("2: Pick a Number: ")
    user_pick_a_number_three = input("3: Pick a Number: ")
    #seeing if one is higher then two
    if(user_pick_a_number_one > user_pick_a_number_two):
        # seeing if one is higher then three
        if(user_pick_a_number_one > user_pick_a_number_three):

            print(user_pick_a_number_one + "Is Higher Then The Other")
            # seeing if two is higher then three
            if(user_pick_a_number_two >  user_pick_a_number_three ):
                print(worlds + user_pick_a_number_one + "\n2: " +  user_pick_a_number_two + "\n3: "  + user_pick_a_number_three)
                Main()

            else:
                print( worlds + user_pick_a_number_one   +"\n2: " +  user_pick_a_number_three + "\n3: "  + user_pick_a_number_two)
                Main()
        else:
            if (user_pick_a_number_two > user_pick_a_number_three):
                print(
                    worlds +  user_pick_a_number_two + "\n2: " + user_pick_a_number_one + "\n3: "  + user_pick_a_number_three)
                Main()
            else:
                print(
                    worlds +user_pick_a_number_three + "\n2: " + user_pick_a_number_one + "\n3: "  + user_pick_a_number_two)
                Main()
    else:
        # seeing if two is higher then three
          if(user_pick_a_number_two > user_pick_a_number_three):
              # seeing if three is higher then one
               if(user_pick_a_number_three > user_pick_a_number_one):
                   print(worlds + user_pick_a_number_two + "\n2: " + user_pick_a_number_three + "\n3: " + user_pick_a_number_one)
                   Main()
               else:
                   print(worlds +user_pick_a_number_two + "\n2: " + user_pick_a_number_one + "\n3: "  + user_pick_a_number_three)
                   Main()

          elif(user_pick_a_number_two < user_pick_a_number_three):
              # seeing if two is higher then one
              if (user_pick_a_number_two > user_pick_a_number_one):
                  print(worlds + user_pick_a_number_three + "\n2: " + user_pick_a_number_two + "\n3: " + user_pick_a_number_one)
                  Main()
              else:
                  print(worlds+user_pick_a_number_three + "\n2: " + user_pick_a_number_one + "\n3: "  + user_pick_a_number_two)
                  Main()


def Main():
    print("!\___________Main meun_________/!")
    #leting the user pick What function That what to go
    user = input("where do you what to go: " +"\n" + "1:Maths or maths" + "\n" +"2:Python Control Statements"+"\n" + "3:Loops \n" +"I Pick: ")
    if(user == "Maths" or user == "maths" or user ==  "1"):
        print("!\____________END______________________/!")
        Maths()

    elif(user == "Python Control Statements" or user == "2"):
        print("!\____________END______________________/!")
        Python_Control_Statements()
    elif(user == "Loops" or user == "loop" or user == "3"):
        print("!\____________END______________________/!")



Main()