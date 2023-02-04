from cmu_112_graphics1 import *
import copy
from TP_classes import *
import cv2

def appStarted(app):
    app.startPage = True
    app.gameSelectPage = False
    app.breathingPage = False
    app.walkingPage = False
    app.sleepPage = False
    app.selfTalkPage = False
    app.colorTherapy = False
    app.progress = 0
    app.color = 'white'
    app.fill1 = 'white'
    app.fill2 = 'white'
    app.fill3 = 'white'
    app.fill4 = 'white'
    app.fill5 = 'white'
    app.fill6 = 'white'
    app.message = 'Press space to start'
    app.radius = 60
    app.cx = 400
    app.cy = 225
    app.growing = True
    app.paused = True
    app.timerDelay = 20
    app.stepCount = 0
    app.circleMsg = ''
    app.msgSize = 25
    app.background = scaleImage(app, app.loadImage('"C:\Users\MEDIHA OZCAN\Documents\15-112\TP\landing page.png"'), app.dimensions) #scaleImage needed

def keypressed(app, event):
    if event.key == 'space':
        app.paused = not app.paused
    if app.paused:
        app.message = 'Press space to resume'
        app.circleMsg = ''
    else:
        app.message = ''

def mousePressed(app, event):
    if app.startPage == True and 350 <event.x <450 and 300 < event.y <340:
        app.startPage = False
        app.gameSelectPage = True
    if app.gameSelectPage == True:
        app.gameSelectPage == False
        if event.x < 250 and event.y < 250:
            app.breathingPage == True
        if event.x>500:
            app.walkingPage == True #user inputs number of steps
        if 250<event.x<500 and event.y<250:
            app.sleepPage == True
        if event.x < 250 and event.y >250:
            app.selfTalkPage == True
        if 250<event.x<500 and event.y>250:
            app.colorTherapy == True
    #start of coloring
    if app.colorTherapy == True:
        if (event.x >= 80 and event.y >= 60 and event.x <= 100 and event.y <= 80):
            app.color = 'red'
        if (event.x >= 80 and event.y >= 100 and event.x <= 100 and event.y <= 120):
            app.color = 'orange'
        if (event.x >= 80 and event.y >= 140 and event.x <= 100 and event.y <= 160):
            app.color = 'yellow'
        if (event.x >= 80 and event.y >= 180 and event.x <= 100 and event.y <= 200):
            app.color = 'green'
        if (event.x >= 80 and event.y >= 220 and event.x <= 100 and event.y <= 230):
            app.color = 'blue'
        if (event.x >= 80 and event.y >= 260 and event.x <= 100 and event.y <= 280):
            app.color = 'purple'
        if (event.x >= 80 and event.y >= 300 and event.x <= 100 and event.y <= 320):
            app.color = 'pink'
        if (event.x >= 80 and event.y >= 340 and event.x <= 100 and event.y <= 360):
            app.color = 'brown'
        if (event.x >= 80 and event.y >= 380 and event.x <= 100 and event.y <= 400):
            app.color = 'white'

        if (event.x >= 360 and event.x <= 440 and event.y >= app.height - 175 and event.y <= app.height - 25):
            app.fill1 = app.color
        elif (event.x >= 450 and event.x <= 600 and event.y >= app.height - 270 and event.y <= app.height - 190):
            app.fill2 = app.color
        elif (event.x >= 360 and event.x <= 440 and event.y >= app.height - 425 and event.y <= app.height - 275):
            app.fill3 = app.color
        elif (event.x >= 200 and event.x <= 350 and event.y >= app.height - 270 and event.y <= app.height - 190):
            app.fill4 = app.color
        elif (event.x >= 350 and event.x <= 450 and event.y >= app.height - 275 and event.y <= app.height - 175):
            app.fill5 = app.color
        elif (event.x >= 200 and event.x <= 440 and event.y >= app.height - 425 and event.y <= app.height - 25):
            app.fill6 = app.color
    #End of coloring
    if event.y >425 and event.x >750:
        app.walkingPage = False
        app.gameSelectPage = True
        app.sleepPage = False
        app.selfTalkPage = False 
        app.breathingPage = False
        app.colorTherapy = False       

def takeStep(app):
    app.stepCount += 1
    # if circle is at bottom bound
    if app.radius >= 200:
        app.growing = False
        app.stepCount = 0
    elif app.radius <= 60:
        app.growing = True
        app.stepCount = 0
    if app.growing:
        app.circleMsg = 'Inhale'
        app.radius += 1.35
        app.msgSize += 1
    else:
        app.circleMsg = 'Exhale'
        app.radius -= 1.35
        app.msgSize -= 1

def timerFired(app):
    if app.paused == False:
        takeStep(app)

def drawBackground(app, canvas):
    width, height = app.dimensions
    # canvas.create_image(0, 300, image=ImageTk.PhotoImage(app.background))
    drawImage(app, canvas, app.background, app.width/2, height/2)

def redrawAll(app, canvas):
    if app.startPage == True:
        canvas.create_rectangle(350, 300, 450, 340, "black", "Start")
        drawBackground(app, canvas)

    if app.gameSelectPage ==True:
        app.background = scaleImage(app, app.loadImage("C:\Users\MEDIHA OZCAN\Documents\15-112\TP\home page.png"), app.dimensions) #need scaleImage
        drawBackground(app, canvas)

    if app.breathingPage == True:
        canvas.create_oval(app.cx,app.cy, 210, fill = 'blue', border = 'black')
        canvas.create_oval(app.cx, app.cy, app.radius, fill = 'lightBlue', border = 'white')
        canvas.create_text(app.cx, app.cy, app.circleMsg, font = app.msgSize,
              fill = 'white')
        canvas.create_text(400, 50, app.message, font = 50, border = 'black',
              fill = 'white')

    if app.walkingPage == True:
        steps = app.getUserInput("Today's steps")
        if 7500 > steps >= 5000:
            points = 10
        if 10000 > steps >= 7500:
            points = 15
        if steps >=10000:
            points = 20
        app.progress += points
        canvas.create_text(400,225, f'{steps} steps. {points}xp')
        canvas.create_rectangle(0,800,0,450, fill = 'beige')

    if app.sleepPage == True:
        hoursSlept = app.getUserInput("How many hours did you sleep?")
        if hoursSlept >= 8:
            points = 10
            app.progress +=10
        elif hoursSlept ==6 or hoursSlept==7:
            points = 5
            app.progress +=5
        else:
            points = 0
        canvas.create_text(400,225, f'{hoursSlept} hours slept. {points}xp')

    if app.selfTalkPage == True:
        canvas.create_text(400,225, "Give yourself 3 complements")

    if app.colorTherapy == True:
        canvas.create_oval(200, app.height-25, 600, app.height-425, fill = app.fill6)
        canvas.create_oval(350, app.height-175, 450, app.height-275, fill = app.fill5)
 
        canvas.create_oval(360, app.height-25, 440, app.height-175, fill = app.fill1)
        canvas.create_oval(450, app.height-190, 600, app.height-270, fill = app.fill2)
        canvas.create_oval(360, app.height-275, 440, app.height-425, fill = app.fill3)
        canvas.create_oval(200, app.height-190, 350, app.height-270, fill = app.fill4)

        canvas.create_oval(80, 60, 100, 80, fill = 'red')
        canvas.create_oval(80, 100, 100, 120, fill = 'orange')
        canvas.create_oval(80, 140, 100, 160, fill = 'yellow')
        canvas.create_oval(80, 180, 100, 200, fill = 'green')
        canvas.create_oval(80, 220, 100, 240, fill = 'blue')
        canvas.create_oval(80, 260, 100, 280, fill = 'purple')
        canvas.create_oval(80, 300, 100, 320, fill = 'pink')
        canvas.create_oval(80, 340, 100, 360, fill = 'brown')
        canvas.create_oval(80, 380, 100, 400, fill = 'white')
        canvas.create_text(90, 40, text = f'brush color: {app.color}', font = ('Arial','14','bold'))
        

runApp(width=800, height=450)  