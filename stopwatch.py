#"Stopwatch: The Game", built in CodeSkulptor

import simplegui

# define global variables
time = 0
running = False
stops = 0
perfect_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    ones = (t // 10) % 10
    tens = (t // 100) % 6
    minutes = t // 600
    format_time = str(minutes) + ":" + str(tens) + str(ones) + "." + str(tenths)
    return format_time

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    if running == False:
        running = True
        return timer.start()
    else:
        return None
def stop():
    global time
    global running
    global stops
    global perfect_stops
    if running == True:
        running = False
        stops += 1
        if time % 10 == 0:
            perfect_stops += 1
            return timer.stop()
        else:
            return timer.stop()
    else:
        return None
def reset():
    global running
    global time
    global stops
    global perfect_stops
    timer.stop()
    time = 0
    running = False
    stops = 0
    perfect_stops = 0
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    return time

# define draw handler
def draw(canvas):
    global time
    global stops
    global perfect_stops
    # draws the current time on the stopwatch
    canvas.draw_text(str(format(time)), (100,150), 36, "Red")
    # draws how many times you've stopped the watch, and how many times you've stopped it on exactly a second
    canvas.draw_text(str(str(stops) + "/" + str(perfect_stops)), (250,25), 24, "Red")
                     

# create frame

frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)
frame.set_draw_handler(draw)
                     
# register event handlers

frame.add_button("Start!", start)
frame.add_button("Stop!", stop)
frame.add_button("Reset", reset)


timer = simplegui.create_timer(100, tick)
                     
# start frame
frame.start()