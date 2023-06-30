# your code here
def main():
    canvas = Canvas(PATCH_SIZE, PATCH_SIZE)
    background(canvas, 0, 0)
    background_deco(canvas, 0, 0)
    ears(canvas, PATCH_SIZE/4, PATCH_SIZE/4)
    head(canvas, (PATCH_SIZE/4)/2, PATCH_SIZE/4)
    blush(canvas, (PATCH_SIZE/4)/2, PATCH_SIZE/2)
    eyes(canvas, PATCH_SIZE/4, PATCH_SIZE/4)
    nose(canvas, PATCH_SIZE/4, PATCH_SIZE-PATCH_SIZE/2)
    mouth(canvas, PATCH_SIZE/4+PATCH_SIZE/4/3, PATCH_SIZE/2)
    nose_2(canvas, PATCH_SIZE/4, PATCH_SIZE/2)
  
    #second part is needed to create the nose above the mouth
    text(canvas, PATCH_SIZE/4, PATCH_SIZE/4*3)

def background(canvas, start_x, start_y):
    #main square
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'pink')
    #internal square
    border = 6
    canvas.create_rectangle(start_x+border, start_y+border, end_x-border, end_y - border, 'white')

def background_deco(canvas, start_x, start_y):
    circle_dim= 12
    end_x = start_x + circle_dim
    end_y = start_y + circle_dim
    on_corner = PATCH_SIZE-circle_dim
    
    canvas.create_oval(start_x, start_y, end_x, end_y, 'pink')
    canvas.create_oval(start_x, start_y+on_corner, end_x, end_y+on_corner, 'pink')
    canvas.create_oval(start_x+on_corner, start_y, PATCH_SIZE, end_y, 'pink')
    canvas.create_oval(start_x+on_corner, start_y+on_corner, PATCH_SIZE, PATCH_SIZE, 'pink')
    
def ears(canvas, start_x, start_y):
    circle_dim = 10
    half_circle = circle_dim/2
    end_x = start_x + circle_dim
    end_y = start_y + circle_dim
    canvas.create_oval(start_x-half_circle, start_y-half_circle, end_x, end_y, 'brown')
    increment= 2
    for i in range (3):
        canvas.create_oval(start_x-half_circle-increment, start_y-half_circle-increment, end_x-increment, end_y-increment, 'brown')
        increment += 2
    second_ear = (PATCH_SIZE/4)*2
    canvas.create_oval(start_x+second_ear-half_circle, start_y-half_circle, end_x+second_ear, end_y, 'brown')
    increment_bis = 2
    for i in range (3):
        canvas.create_oval(start_x+second_ear-half_circle-increment_bis, start_y-half_circle-increment_bis, end_x+second_ear-increment_bis, end_y-increment_bis, 'brown')
        increment_bis += 2

def head(canvas, start_x, start_y):
    end_x = PATCH_SIZE-(PATCH_SIZE/4)/2
    end_y = PATCH_SIZE-PATCH_SIZE/4
    increment=4
    canvas.create_oval(start_x+increment, start_y, end_x+increment, end_y, "pink")
    canvas.create_oval(start_x-increment, start_y, end_x-increment, end_y, "yellow")
    canvas.create_oval(start_x, start_y, end_x, end_y, "white")
    
def blush(canvas, start_x, start_y):
    oval_width = 10
    oval_height=6
    end_x= start_x+oval_width
    end_y= start_y + oval_height
    canvas.create_oval(start_x, start_y, end_x, end_y, 'red')
    second_blush = (PATCH_SIZE/4)*2.3
    #needed to define the second blush x
    canvas.create_oval(start_x+second_blush, start_y, end_x+second_blush, end_y, 'red')

def eyes(canvas, start_x, start_y):
    oval_width = 10
    oval_height=25
    blink_width= (oval_width/4)*3
    blink_height = (oval_height/4)*1.5
    #blink references to the white part in the eye!
    end_x = start_x + oval_width
    end_y = start_y + oval_height
    shift = 5
    blink_shift = 2.5
    canvas.create_oval(start_x-shift, start_y+shift, end_x, end_y, 'brown')
    canvas.create_oval(start_x-blink_shift, start_y+blink_shift +shift, end_x-blink_width, end_y-blink_height, 'white')
    
    other_side = (PATCH_SIZE/4)+(PATCH_SIZE/4)/3
    canvas.create_oval(start_x+other_side, start_y+shift, end_x+other_side+shift, end_y, 'brown')
    canvas.create_oval(start_x+other_side+blink_shift, start_y+shift+blink_shift, end_x+other_side+shift-blink_width, end_y-blink_height, 'white')

def nose(canvas, start_x, start_y):
    shift=5
    oval_width= PATCH_SIZE/2-shift
    oval_height=PATCH_SIZE/4
    end_x=start_x+oval_width
    end_y= start_y+oval_height-shift

    canvas.create_oval(start_x, start_y-shift, end_x, end_y, 'pink')
    canvas.create_oval(start_x+shift/2, start_y-shift/2, end_x, end_y, 'white')

def mouth(canvas, start_x, start_y):
    circle=10
    end_x= start_x + circle
    end_y= start_y+circle
    increment=5
    increment_bis=6
    canvas.create_oval(start_x, start_y+increment, end_x, end_y+increment, 'black')
    canvas.create_oval(start_x-increment_bis, start_y+increment, end_x-increment_bis, end_y+increment, 'white')
    canvas.create_oval(start_x+increment_bis, start_y+increment-0.5, end_x+increment*1.5, end_y+increment-0.5, 'white')

def nose_2 (canvas, start_x, start_y):
    oval_width= 15
    oval_height=6
    shift=5
    end_x = start_x+oval_width
    end_y= start_y+oval_height
    
    blink_width=shift
    blink_height=5
    
    canvas.create_oval(start_x+shift, start_y-shift, end_x+shift, end_y, 'brown')
    canvas.create_oval(start_x+blink_width, start_y-3, end_x-shift, end_y-blink_height, 'white')
    
def text(canvas, start_x, start_y):
    text_height = 15
    choices=['<3<3<3', 'nice day']
    text_random= random.choice(choices)
    #here the text will be randomly chosen

    if text_random == '<3<3<3':
        adjustment_left=2
    if text_random == 'nice day':
        adjustment_left=5
    #adjustments depending on the text
    adjustment_height=4
   
    canvas.create_text(start_x-adjustment_left, start_y+adjustment_height, font='Bitter', font_size=text_height, text=text_random, color='brown')
