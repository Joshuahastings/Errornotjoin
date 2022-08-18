import math

print("hello people, i'm joshua aka ErrorNotJoin And This Is My College Work :)");
one_time_table = ["\n1 x 1 = 1" , "\n1 x 2 = 2 ","\n1 x 3 = 3" , "\n1 x 4 = 4 ","\n1 x 5 = 5" ,  "\n1 x 6 = 6 ","\n1 x 7 = 7" , "\n1 x 8 = 8 ","\n1 x 9 = 9" , "\n1 x 10 = 10 ", "\n 1 x 11 + 11", "\n 1 x 12 = 12"]
two_time_table = ["\n2 x 1 = 2", "\n2 x 2 = 4", "\n2 x 3 = 6", "\n2 x 4 = 8", "\n2 x 5 = 10", "\n2 x 6 = 12", "\n2 x 7 = 14", "\n2 x 8 = 16","\n2 x 9 = 18"," \n2 x 10 = 20"," \n2 x 11 = 22", "\n2 x 12 = 24"]
six_time_table = ["\n6 x 1 = 6 ", "\n6 x 2 = 12", "\n6 x 3 = 18","\n6 x 4 = 24", "\n6 x 5 = 30", "\n6 x 6 = 36" ,"\n6 x 7 = 42","\n6 x 8 = 48","\n6 x 9 = 54","\n6 x 10 = 60"]
number_list_two = [20, 30, 25, 35, -16, 60, -100]
number_list_three = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

worlds = "___Numbers In Order____\n1: "
def Maths():

 a = -5 + 8* 6
 b = (55 + 9) % 9
 c = 20 + -3 * 5 / 8
 d = 5 + 15 /3*2 - 8 % 3
 #saving the python awser
 print("\n!\_________python Basics Maths_________/!" )
 print("a: " + str(a) + "\n" + "b: " + str(b) +"\n" + "c: " + str(c) + "\n" + "d: "  + str(d) + "\n" + "!\_________END_________/!"   )
 #showing the aw and number them
 print(" " + "\n")
 print("!\_________User Input Maths_________/!")
 user_number_one  = (input("What is Your Number: "))
 #Getting the first Number From the User
 user_number_two  = (input("What is Your Number: "))
 #Getting a sec Number  From the User
 e = int(user_number_one) / int(user_number_two)
 #Pytohn is Div the number
 print(user_number_one +" / "+ user_number_two +  " = " + str(e) )
 #Showing The User Number And What That = To
 print("\n!\_________END_________/!")


 Main()
def Python_Control_Statements():
    print("\n!\_________Python Control Statements_________/!")
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

def Loops():
    print("\n\___________Loops_________/!")
    user_type_of_loop = input("What Loop Do You What\n1:Fibonacci series, \n2:TimeTable, \n3:Back, \nI Pick: ")
    if(user_type_of_loop == "1" or user_type_of_loop == "Fibonacci series" or user_type_of_loop == "fibonacci"):
      x = 1
      y = 0
      #making the number
      while x < 100:
          #max number is 100 then it will stop
          x += y
          y += x
          #they are add each of
          print(x)
          print(y)
          #printing the x and y
          if(x < 100 ):
              continue
      print(x)
      Loops()
    elif(user_type_of_loop == "2" or user_type_of_loop == "TimeTable"):
        user_number_of_time_table = input("What Number (Only One , two or six)")
        x = 0
        if(user_number_of_time_table  == "1"):
            for x in one_time_table:
                print(x)

            Loops()
                #going for the in the  list and print all in the list
        elif(user_number_of_time_table == "2"):
            for x in two_time_table:
                print(x)
            Loops()
                # going for the in the  list and print all in the list
        elif(user_number_of_time_table == "6"):
            for x in six_time_table:
                print(x)
            Loops()
                # going for the in the e list and print all in the list
        else:
            for x in six_time_table:
                print(x)
            Loops()
    # going for the in the  list and print all in the list
    elif(user_type_of_loop == "Back" or user_type_of_loop == "back" or user_type_of_loop == "3"):
        Loops()
    else:
        Loops()




def Python_collections():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_list_two = [20, 30, 25, 35, -16, 60, -100]
    number_list_three = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
    #div the number than div it by 0.102
    math = number_list_two[0] + number_list_two[1]
    maths = math + number_list_two[2]
    math = maths + number_list_two[3]
    maths = math + number_list_two[4]
    math =  maths + number_list_two[5]
    maths = math + number_list_two[6]
    math = maths / len(number_list_two)
     #add all the number
    cat = number_list[0] + number_list[1]
    dog = cat + number_list[2]
    cat = dog + number_list[3]
    dog = cat + number_list[4]
    cat = dog + number_list[5]
    dog = cat + number_list[6]
    cat = dog + number_list[7]
    dog = cat + number_list[8]
    cat = dog + number_list[9]

    print("The Average Value Of The List  "+ str(math))
    print("1:The Sum is "+ str(cat))
    #puting it in to the order
    number_list_three.sort(reverse=True)
    print(number_list_three)
    ##not going the other way
    number_list_three.sort(reverse=False)
    print(number_list_three)
def pythone_funvtions(number):
    print(number)
    test = max(number)
    print("that Max Number Is: "+ str(test))









def Main():
    print("\n!\___________Main meun_________/!")
    #leting the user pick What function That what to go
    user = input("where do you what to go: " +"\n1:Maths or maths" + "\n2:Python Control Statements"+"\n3:Loops " +"\n4:Python_collections"+"\nI Pick: ")
    if(user == "Maths" or user == "maths" or user ==  "1"):
        print("\n!\____________END______________________/!")
        Maths()

    elif(user == "Python Control Statements" or user == "2"):
        print("\n!\____________END______________________/!")
        Python_Control_Statements()
    elif(user == "Loops" or user == "loop" or user == "3"):
        print("\n!\____________END______________________/!")
        Loops()
    elif(user == "4" or user == "Python_collections"):
        Python_collections()
    elif(user == "5"):
        fruts = [10, 2, 3, 4, 7]
        pythone_funvtions(fruts)



Main()
