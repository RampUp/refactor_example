from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

world.clear()

def fdlt(turtle, length=0, angle=90):
  turtle.fd(length)
  turtle.lt(angle)

def fdrt(turtle, length=0, angle=90):
  turtle.fd(length)
  turtle.rt(angle)

fdlt(bob, 30)
fdrt(bob, 20)
fdrt(bob, 10)
fdlt(bob, 20)
bob.bk(10)
fdlt(bob, 40)
fdlt(bob, 40, 45)
fdlt(bob, 50)
fdlt(bob, 50, 45)
fdlt(bob, 40)
bob.lt()
fdrt(bob, 40)
fdrt(bob, 70)
fdlt(bob, 40)

wait_for_user()