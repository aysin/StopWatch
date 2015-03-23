# template for "Stopwatch: The Game"

# define global variables
import simplegui
import random

interval = 100
time = 0
position = [140,120]
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minu = int(t // 600)
    if minu > 9:
        return timer.stop()  
    sec = (t % 600) // 10
    decsec = t % 10
    if sec < 10:
        formatted = str(minu) +':0' + str(sec) +'.'+ str(decsec)
    else:
        formatted = str(minu) + ':' + str(sec) + '.' + str(decsec)
    return formatted
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def timer_start():
    global time
    timer.start()
    
def timer_stop():
    global time, x, y
    if timer.is_running():
        timer.stop()
        if time % 10 == 0:
            x += 1
        y += 1
    
def timer_reset():
    global time, x ,y
    time = 0
    x = 0
    y = 0
    timer.stop()


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    if timer.is_running():
        time += 1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), position, 54, "Blue")
    canvas.draw_text(str(x) + '/' + str(y), [320, 30], 34, "Red")


# create frame
f = simplegui.create_frame("StopWatch", 400, 200)
timer = simplegui.create_timer(interval, tick)

# register event handlers
f.add_button("Start",timer_start, 100)
f.add_button("Stop", timer_stop, 100)
f.add_button("Reset", timer_reset, 100)
f.set_draw_handler(draw)

# start frame
f.start()

# Please remember to review the grading rubric
