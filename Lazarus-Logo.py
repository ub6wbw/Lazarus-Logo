from graphics import *
from math import sin, cos

#вращение координат x, y относительно центра в x0, y0
def RotateXY(x, y, x0, y0, angle):
    NewX = (x-x0) * cos(angle*0.0174) - (y-y0) * sin(angle*0.017453) + x0
    NewY = (x-x0) * sin(angle*0.0174) + (y-y0) * cos(angle*0.017453) + y0
    return NewX, NewY

#вычисление координаты точки кривой Безье
def BCoord(x0, x1, x2, x3, t):
    return (1-t)*(1-t)*(1-t)*x0 +\
           3*t*(1-t)*(1-t)*x1 +\
           3*t*t*(1-t)*x2 + t*t*t*x3;

#рисование кривой Безье
def BezierCurve(StartX, StartY, deflectorX1, deflectorY1, deflectorX2, deflectorY2, EndX, EndY):
    t = 0
    while t < 1:
        x = BCoord(StartX, deflectorX1, deflectorX2, EndX, t)
        y = BCoord(StartY, deflectorY1, deflectorY2, EndY, t)
        cir = Circle(Point(x, y), 4)
        cir.setFill('black')
        cir.draw(win)
        t = t + 0.01
    return 'BezierOk'

#создаём окно 550x550, фон - белый
win = GraphWin('Lazarus Logo', 550, 550)
win.setBackground('white')

#координаты центра Логотипа Lazarus
Xc, Yc = 271, 274

#координаты точек 1 и 2
FirstPointX = 248
FirstPointY = 48
SecondPointX = 336
SecondPointY = 58
deflector1X = FirstPointX+8
deflector1Y = FirstPointY-8
deflector2X = SecondPointX-8
deflector2Y = SecondPointY-8

#рисуем ободок (шестерёнку), внешние дуги
#вращением координат точек 1 и 2 каждый раз на 60гр.
#после чего вызываем функцию BezierCurve для отрисовки кривой через пару точек
BezierCurve(FirstPointX, FirstPointY,  deflector1X, deflector1Y, deflector2X, deflector2Y, SecondPointX, SecondPointY)
print(FirstPointX, FirstPointY,  deflector1X, deflector1Y, deflector2X, deflector2Y, SecondPointX, SecondPointY)
print()

BezierCurve(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 60)[0], RotateXY(FirstPointX, FirstPointY, Xc, Yc, 60)[1],\
            RotateXY(deflector1X, deflector1Y, Xc, Yc, 60)[0], RotateXY(deflector1X, deflector1Y, Xc, Yc, 60)[1],\
            RotateXY(deflector2X, deflector2Y, Xc, Yc, 60)[0], RotateXY(deflector2X, deflector2Y, Xc, Yc, 60)[1],\
            RotateXY(SecondPointX, SecondPointY, Xc, Yc, 60)[0], RotateXY(SecondPointX, SecondPointY, Xc, Yc, 60)[1])
print(int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 60)[0]), int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 60)[1]),\
      int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 60)[0]), int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 60)[1]),\
      int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 60)[0]), int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 60)[1]),\
      int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 60)[0]), int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 60)[1]))
print()

BezierCurve(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 120)[0], RotateXY(FirstPointX, FirstPointY, Xc, Yc, 120)[1],\
            RotateXY(deflector1X, deflector1Y, Xc, Yc, 120)[0], RotateXY(deflector1X, deflector1Y, Xc, Yc, 120)[1],\
            RotateXY(deflector2X, deflector2Y, Xc, Yc, 120)[0], RotateXY(deflector2X, deflector2Y, Xc, Yc, 120)[1],\
            RotateXY(SecondPointX, SecondPointY, Xc, Yc, 120)[0], RotateXY(SecondPointX, SecondPointY, Xc, Yc, 120)[1])
print(int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 120)[0]), int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 120)[1]),\
      int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 120)[0]), int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 120)[1]),\
      int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 120)[0]), int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 120)[1]),\
      int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 120)[0]), int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 120)[1]))
print()

BezierCurve(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 180)[0], RotateXY(FirstPointX, FirstPointY, Xc, Yc, 180)[1],\
            RotateXY(deflector1X, deflector1Y, Xc, Yc, 180)[0], RotateXY(deflector1X, deflector1Y, Xc, Yc, 180)[1],\
            RotateXY(deflector2X, deflector2Y, Xc, Yc, 180)[0], RotateXY(deflector2X, deflector2Y, Xc, Yc, 180)[1],\
            RotateXY(SecondPointX, SecondPointY, Xc, Yc, 180)[0], RotateXY(SecondPointX, SecondPointY, Xc, Yc, 180)[1])
print(int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 180)[0]), int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 180)[1]),\
      int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 180)[0]), int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 180)[1]),\
      int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 180)[0]), int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 180)[1]),\
      int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 180)[0]), int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 180)[1]))
print()

BezierCurve(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 240)[0], RotateXY(FirstPointX, FirstPointY, Xc, Yc, 240)[1],\
            RotateXY(deflector1X, deflector1Y, Xc, Yc, 240)[0], RotateXY(deflector1X, deflector1Y, Xc, Yc, 240)[1],\
            RotateXY(deflector2X, deflector2Y, Xc, Yc, 240)[0], RotateXY(deflector2X, deflector2Y, Xc, Yc, 240)[1],\
            RotateXY(SecondPointX, SecondPointY, Xc, Yc, 240)[0], RotateXY(SecondPointX, SecondPointY, Xc, Yc, 240)[1])
print(int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 240)[0]), int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 240)[1]),\
      int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 240)[0]), int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 240)[1]),\
      int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 240)[0]), int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 240)[1]),\
      int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 240)[0]), int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 240)[1]))
print()

BezierCurve(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 300)[0], RotateXY(FirstPointX, FirstPointY, Xc, Yc, 300)[1],\
            RotateXY(deflector1X, deflector1Y, Xc, Yc, 300)[0], RotateXY(deflector1X, deflector1Y, Xc, Yc, 300)[1],\
            RotateXY(deflector2X, deflector2Y, Xc, Yc, 300)[0], RotateXY(deflector2X, deflector2Y, Xc, Yc, 300)[1],\
            RotateXY(SecondPointX, SecondPointY, Xc, Yc, 300)[0], RotateXY(SecondPointX, SecondPointY, Xc, Yc, 300)[1])
print(int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 300)[0]), int(RotateXY(FirstPointX, FirstPointY, Xc, Yc, 300)[1]),\
      int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 300)[0]), int(RotateXY(deflector1X, deflector1Y, Xc, Yc, 300)[1]),\
      int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 300)[0]), int(RotateXY(deflector2X, deflector2Y, Xc, Yc, 300)[1]),\
      int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 300)[0]), int(RotateXY(SecondPointX, SecondPointY, Xc, Yc, 300)[1]))
print()

#координаты точек 3 и 4
ThirdPointX = 116
ThirdPointY = 109
FourthPointX = 248
FourthPointY = 48
deflector3X = ThirdPointX+44
deflector3Y = ThirdPointY+24
deflector4X = FourthPointX-20
deflector4Y = FourthPointY+68

#рисуем ободок (шестерёнку), внутренние дуги
#вращением координат точек 1 и 2 каждый раз на 60гр.
#после чего вызываем функцию BezierCurve для отрисовки кривой через пару точек
BezierCurve(ThirdPointX, ThirdPointY, deflector3X, deflector3Y, deflector4X, deflector4Y, FourthPointX, FourthPointY)
print(ThirdPointX, ThirdPointY, deflector3X, deflector3Y, deflector4X, deflector4Y, FourthPointX, FourthPointY)
print()

BezierCurve(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 60)[0], RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 60)[1],\
            RotateXY(deflector3X, deflector3Y, Xc, Yc, 60)[0], RotateXY(deflector3X, deflector3Y, Xc, Yc, 60)[1],\
            RotateXY(deflector4X, deflector4Y, Xc, Yc, 60)[0], RotateXY(deflector4X, deflector4Y, Xc, Yc, 60)[1],\
            RotateXY(FourthPointX, FourthPointY, Xc, Yc, 60)[0], RotateXY(FourthPointX, FourthPointY, Xc, Yc, 60)[1])
print(int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 60)[0]), int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 60)[1]),\
      int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 60)[0]), int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 60)[1]),\
      int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 60)[0]), int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 60)[1]),\
      int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 60)[0]), int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 60)[1]))
print()

BezierCurve(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 120)[0], RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 120)[1],\
            RotateXY(deflector3X, deflector3Y, Xc, Yc, 120)[0], RotateXY(deflector3X, deflector3Y, Xc, Yc, 120)[1],\
            RotateXY(deflector4X, deflector4Y, Xc, Yc, 120)[0], RotateXY(deflector4X, deflector4Y, Xc, Yc, 120)[1],\
            RotateXY(FourthPointX, FourthPointY, Xc, Yc, 120)[0], RotateXY(FourthPointX, FourthPointY, Xc, Yc, 120)[1])
print(int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 120)[0]), int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 120)[1]),\
      int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 120)[0]), int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 120)[1]),\
      int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 120)[0]), int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 120)[1]),\
      int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 120)[0]), int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 120)[1]))
print()

BezierCurve(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 180)[0], RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 180)[1],\
            RotateXY(deflector3X, deflector3Y, Xc, Yc, 180)[0], RotateXY(deflector3X, deflector3Y, Xc, Yc, 180)[1],\
            RotateXY(deflector4X, deflector4Y, Xc, Yc, 180)[0], RotateXY(deflector4X, deflector4Y, Xc, Yc, 180)[1],\
            RotateXY(FourthPointX, FourthPointY, Xc, Yc, 180)[0], RotateXY(FourthPointX, FourthPointY, Xc, Yc, 180)[1])
print(int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 180)[0]), int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 180)[1]),\
      int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 180)[0]), int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 180)[1]),\
      int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 180)[0]), int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 180)[1]),\
      int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 180)[0]), int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 180)[1]))
print()

BezierCurve(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 240)[0], RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 240)[1],\
            RotateXY(deflector3X, deflector3Y, Xc, Yc, 240)[0], RotateXY(deflector3X, deflector3Y, Xc, Yc, 240)[1],\
            RotateXY(deflector4X, deflector4Y, Xc, Yc, 240)[0], RotateXY(deflector4X, deflector4Y, Xc, Yc, 240)[1],\
            RotateXY(FourthPointX, FourthPointY, Xc, Yc, 240)[0], RotateXY(FourthPointX, FourthPointY, Xc, Yc, 240)[1])
print(int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 240)[0]), int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 240)[1]),\
      int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 240)[0]), int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 240)[1]),\
      int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 240)[0]), int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 240)[1]),\
      int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 240)[0]), int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 240)[1]))
print()

BezierCurve(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 300)[0], RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 300)[1],\
            RotateXY(deflector3X, deflector3Y, Xc, Yc, 300)[0], RotateXY(deflector3X, deflector3Y, Xc, Yc, 300)[1],\
            RotateXY(deflector4X, deflector4Y, Xc, Yc, 300)[0], RotateXY(deflector4X, deflector4Y, Xc, Yc, 300)[1],\
            RotateXY(FourthPointX, FourthPointY, Xc, Yc, 300)[0], RotateXY(FourthPointX, FourthPointY, Xc, Yc, 300)[1])
print(int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 300)[0]), int(RotateXY(ThirdPointX, ThirdPointY, Xc, Yc, 300)[1]),\
      int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 300)[0]), int(RotateXY(deflector3X, deflector3Y, Xc, Yc, 300)[1]),\
      int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 300)[0]), int(RotateXY(deflector4X, deflector4Y, Xc, Yc, 300)[1]),\
      int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 300)[0]), int(RotateXY(FourthPointX, FourthPointY, Xc, Yc, 300)[1]))
print()

#рисуем лоб
x1=273
y1=120
dX1=273
dY1=159
dX2=273
dY2=159
x2=273
y2=198
BezierCurve(x1, y1, dX1, dY1, dX2, dY2, x2, y2)
print(x1, y1, dX1, dY1, dX2, dY2, x2, y2)
print()
x1=283
y1=153
dX1=278
dY1=147
dX2=278
dY2=147
x2=273
y2=142
BezierCurve(x1, y1, dX1, dY1, dX2, dY2, x2, y2)
print(x1, y1, dX1, dY1, dX2, dY2, x2, y2)
print()

#рисуем левый глаз
stX=120
stY=182
endX=123
endY=175
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=150
endY=170
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=180
endY=170
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=199
endY=180
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=206
endY=199
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=209
endY=256
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=183
endY=301
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=173
endY=338
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=208
stY=220
endX=197
endY=204
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=177
endY=205
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=163
endY=202
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=151
endY=192
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=138
endY=172
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=175
stY=350
endX=169
endY=362
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=183
stY=357
endX=174
endY=373
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=188
stY=370
endX=181
endY=382
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=197
stY=374
endX=189
endY=388
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

#рисуем правый глаз
stX=430
stY=195
endX=414
endY=180
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=389
endY=175
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=372
endY=175
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=358
endY=175
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=349
endY=178
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=343
endY=184
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=340
endY=189
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=340
endY=200
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=340
endY=250
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=351
endY=278
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=363
endY=299
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=368
endY=318
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=373
endY=347
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=372
endY=363
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=367
endY=359
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=371
endY=349
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=377
endY=366
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()
##########
stX=363
stY=366
endX=374
endY=374
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=353
stY=370
endX=369
endY=382
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=359
stY=383
endX=364
endY=387
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=355
stY=386
endX=359
endY=392
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=349
stY=388
endX=354
endY=396
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()
##########
stX=396
stY=178
endX=390
endY=197
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=371
endY=209
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=360
endY=212
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=348
endY=209
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=341
endY=201
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

#рисуем левый зрачок
stX=340
stY=225
endX=347
endY=207
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=186
stY=173
endX=183
endY=182
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=180
endY=186
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=176
endY=186
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=171
endY=183
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=170
endY=179
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=170
stY=180
endX=182
endY=183
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=170
stY=180
endX=182
endY=183
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

#рисуем правый зрачок
stX=389
stY=199
endX=399
endY=179
BezierCurve(stX, stY, 5+(stX+endX)/2, ((stY+endY)/2)-20, ((stX+endX)/2), (stY+endY)/2, endX, endY)
print(stX, stY, 5+(stX+endX)/2, ((stY+endY)/2)-20, ((stX+endX)/2), (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=350
endY=179
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=356
endY=187
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=358
endY=188
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=361
endY=189
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=365
endY=187
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=369
endY=180
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=356
endY=182
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=363
endY=185
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

#нос льва
stX=226
stY=313
endX=247
endY=307
BezierCurve(stX, stY, (stX+endX)/2, 20+(stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, 20+(stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=307
endY=307
BezierCurve(stX, stY, (stX+endX)/2, 10+((stY+endY)/2), (stX+endX)/2, 10+((stY+endY)/2), endX, endY)
print(stX, stY, (stX+endX)/2, 10+((stY+endY)/2), (stX+endX)/2, 10+((stY+endY)/2), endX, endY)
print()

stX=endX
stY=endY
endX=328
endY=311
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, 20+(stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, (stX+endX)/2, 20+(stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=308
endY=345
BezierCurve(stX, stY, 10+(stX+endX)/2, (stY+endY)/2, 10+(stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, 10+(stX+endX)/2, (stY+endY)/2, 10+(stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=287
endY=363
BezierCurve(stX, stY, (stX+endX)/2, (stY+endY)/2, 5+(stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, (stY+endY)/2, 5+(stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=266
endY=363
BezierCurve(stX, stY, (stX+endX)/2, 15+(stY+endY)/2, (stX+endX)/2, 15+(stY+endY)/2, endX, endY)
print(stX, stY, (stX+endX)/2, 15+(stY+endY)/2, (stX+endX)/2, 15+(stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=245
endY=345
BezierCurve(stX, stY, ((stX+endX)/2)-5, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print(stX, stY, ((stX+endX)/2)-5, (stY+endY)/2, (stX+endX)/2, (stY+endY)/2, endX, endY)
print()

stX=endX
stY=endY
endX=226
endY=313
BezierCurve(stX, stY, ((stX+endX)/2)-10, (stY+endY)/2, ((stX+endX)/2)-10, (stY+endY)/2, endX, endY)
print(stX, stY, ((stX+endX)/2)-10, (stY+endY)/2, ((stX+endX)/2)-10, (stY+endY)/2, endX, endY)
print()

#волосики
stX=275
stY=375
endX=270
endY=390
BezierCurve(stX, stY, ((stX+endX)/2)-6, (stY+endY)/2, ((stX+endX)/2)-10, (stY+endY)/2, endX, endY)
print(stX, stY, ((stX+endX)/2)-6, (stY+endY)/2, ((stX+endX)/2)-10, (stY+endY)/2, endX, endY)
print()

stX=275
stY=375
endX=290
endY=390
BezierCurve(stX, stY, ((stX+endX)/2)-3, (stY+endY)/2, ((stX+endX)/2)-10, (stY+endY)/2, endX, endY)
print(stX, stY, ((stX+endX)/2)-3, (stY+endY)/2, ((stX+endX)/2)-10, (stY+endY)/2, endX, endY)
print()

#ждём нажатия кнопки мышки и закрываем окно с рисунком
win.getMouse()
win.close()
