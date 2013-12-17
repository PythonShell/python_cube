# -*- coding: uft-8 -*-
from visual import * 

scene.background = color.white 
scene.foreground = color.black

# 初始化所有小方块
mybox = []
for i in range(9):
    mybox.append(box(pos=[ 2.1,-2+(i/3*2),-2+(i%3*2)],size=[1.8,1.8,1.8],color=color.green ))
    mybox.append(box(pos=[-2+(i/3*2), 2.1,-2+(i%3*2)],size=[1.8,1.8,1.8],color=color.white ))
    mybox.append(box(pos=[-2+(i/3*2),-2+(i%3*2), 2.1],size=[1.8,1.8,1.8],color=color.yellow))
    mybox.append(box(pos=[-2.1,-2+(i/3*2),-2+(i%3*2)],size=[1.8,1.8,1.8],color=color.blue  ))
    mybox.append(box(pos=[-2+(i/3*2),-2.1,-2+(i%3*2)],size=[1.8,1.8,1.8],color=color.red   ))
    mybox.append(box(pos=[-2+(i/3*2),-2+(i%3*2),-2.1],size=[1.8,1.8,1.8],color=color.orange))


# 定义旋转函数
def G():
    for i in range(100):
        for rbox in mybox:
            if rbox.x>1:
                rbox.rotate(angle = 1*pi/200, axis=(1,0,0), origin=(0,0,0))
        rate(100)


def W():
    for i in range(100):
        for rbox in mybox:
            if rbox.y>1:
                rbox.rotate(angle = 1*pi/200, axis=(0,1,0), origin=(0,0,0))
        rate(100)


def Y():
    for i in range(100):
        for rbox in mybox:
            if rbox.z>1:
                rbox.rotate(angle = 1*pi/200, axis=(0,0,1), origin=(0,0,0))
        rate(100)


def B():
    for i in range(100):
        for rbox in mybox:
            if rbox.x<-1:
                rbox.rotate(angle = 1*pi/200, axis=(1,0,0), origin=(0,0,0))
        rate(100)

        
def R():
    for i in range(100):
        for rbox in mybox:
            if rbox.y<-1:
                rbox.rotate(angle = 1*pi/200, axis=(0,1,0), origin=(0,0,0))
        rate(100)

        
def O():
    for i in range(100):
        for rbox in mybox:
            if rbox.z<-1:
                rbox.rotate(angle = 1*pi/200, axis=(0,0,1), origin=(0,0,0))
        rate(100)

# 获取键盘输入并执行相对应的旋转
def keyInput(evt):
    s = evt.key
    if s == 'o':
        O()
    if s == 'g':
        G()
    if s == 'w':
        W()
    if s == 'y':
        Y()
    if s == 'b':
        B()
    if s == 'r':
        R()

scene.bind('keydown', keyInput)

