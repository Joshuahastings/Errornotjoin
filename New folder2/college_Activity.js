console.log("Hello World")
var a = -5 + 8 * 6 
var b = (55+9) % 9 
var c = 20 + -3*5 / 8 


var d =  5 + 15 / 3 * 2 - 8 % 3
console.log(a.toString(), b.toString(), c.toString(),d.toString())
var user_input  = prompt("Pick A Number ")
var User_input_two = prompt("Pick A Number ")
var User_input_three = prompt("picK A number ")

if(User_input_two == 2 )
{
    console.log("you pick " + User_input_two.toString())

}
else if(User_input_two == 3 )
{
    console.log("you pick " + User_input_two.toString())
}
else
console.log("you pick " + User_input_two.toString())

if(user_input > User_input_two & user_input > User_input_three)
{
    if(User_input_two > User_input_three)
    {
        console.log(  user_input.toString() +" "+ User_input_two.toString() +" "+   User_input_three.toString() )
    }
    else
    {
         console.log(  user_input.toString() +" "+   User_input_three.toString() +" "+   User_input_two.toString())
    }
}
else if(User_input_two > User_input_three )
{

    if(user_input > User_input_three)
    {
        console.log(  User_input_two.toString() +" "+ user_input.toString() +" "+   User_input_three.toString() )
    }
    else
    {
         console.log(  User_input_two.toString() +" "+   User_input_three.toString() +" "+   user_input.toString())
    }
}
else 
{
    if(user_input > User_input_two)
    {
        console.log(  User_input_three.toString() +" "+ user_input.toString() +" "+   User_input_two.toString() )
    }
    else
    {
        console.log(  User_input_three.toString() +" "+   User_input_two.toString() +" "+   user_input.toString())
    }
}
console.log(user_input / User_input_two)
var y = 6
for(i = 0; i < 11; i++)
{
   console.log(y .toString() , " * " ,i.toString(), "  = ",  y * i )
}
for (x = 0; x < 15; x++)
{
    if((x % 2) ==0  )
    {
        console.log("this is even ")
    }
    else
    {
        console.log("this is odd")
    }
}
