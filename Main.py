import turtle
timer = int(input("How long should the timer be? "))

show_timer = input("Show timer in numbers! Type y for yes and n for no ")
#Can be turned off if needed
turtle.ht()

number_1 = timer*0.9
number_2 = timer*0.8
number_3 = timer*0.7
number_4 = timer*0.6
number_5 = timer*0.5
number_6 = timer*0.4
number_7 = timer*0.3
number_8 = timer*0.2
number_9 = timer*0.1
count = timer
def myfunc(count):
    if show_timer == "y":
        turtle.write(str(count), font=("Arial", 50, "normal"))
    
    

def countfunc1():
    turtle.speed(1)
    turtle.bgpic("hud.gif")

def countfunc2():
    turtle.speed(1)
    turtle.bgpic("hud2.gif")

def countfunc3():
    turtle.bgpic("hud3.gif")

def countfunc4():
    turtle.speed(1)
    turtle.bgpic("hud4.gif")

def countfunc5():
    turtle.speed(1)
    turtle.bgpic("hud5.gif")

def countfunc6():
    turtle.speed(1)
    turtle.bgpic("hud6.gif")
    
def countfunc7():
    turtle.speed(1)
    turtle.bgpic("hud7.gif")

def countfunc8():
    turtle.speed(1)
    turtle.bgpic("hud8.gif")

def countfunc9():
    turtle.bgpic("hud9.gif")

def countfunc10():
    turtle.speed(1)
    turtle.bgpic("hud10.gif")

def countfunc11():
    #trutle.speed(1)
    turtle.bgpic("hud11.gif")


    


for i in range(timer):
    if count == timer:
        countfunc1()
        
    count = count - 1
    i = i + 1
    if count == number_1:
        countfunc2()

    if count == number_2:
        countfunc3()

    if count == number_3:
        countfunc4()

    if count == number_4:
        countfunc5()

    if count == number_5:
        countfunc6()

    if count == number_6:
        countfunc7()

    if count == number_7:
        countfunc8()

    if count == number_8:
        countfunc9()

    if count == number_9:
        countfunc10()
        
    if i == timer:
        countfunc11()
        
        
    turtle.ontimer(myfunc(count), t=1000)
    turtle.clear()

turtle.write("End", font=("Arial", 50, "normal"))
    

