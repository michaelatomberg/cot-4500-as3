import numpy as np


def Question_One():
    # Declaring iteration #, start/end points
    N=10
    a=0
    b=2
    initial_y=1
    initial_t=0
    h=(b-a)/N

    # Starting t and y
    t=initial_t
    y=initial_y

    # Given f function
    def f(t, y):
        return t-y**2

    # Use Euler's Method
    # Calculate y at each new step of t
    for i in range(N):
        y=y+h*f(t, y)
        t+=h

    # Print last y
    print(y)

solution1=Question_One()


def Question_Two():
    # Declaring iterations, start/end points
    N=10
    a=0
    b=2
    initial_y=1
    initial_t=0
    h=(b-a)/N

    # Starting t and y
    t=initial_t
    y=initial_y

    # Given function of f
    def f(t, y):
        return t-y**2

    # Use Runge-Kutta Method
    # Calculate y at each step of t, including k formulas
    for i in range(N):
        k1=h*f(t, y)
        k2=h*f(t+(h/2), y+(1/2)*k1)
        k3=h*f(t+(h/2), y+(1/2)*k2)
        k4=h*f(t+h, y+k3)

        y=y+(1/6)*(k1+2*k2+2*k3+k4)
        t+=h

    # Print last y
    print(y)

solution2=Question_Two()
