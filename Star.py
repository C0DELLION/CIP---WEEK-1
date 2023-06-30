def draw_star_patch(canvas, start_x, start_y):
    # draw a five-point star at (start_x, start_y) with center to point distance 50
    canvas.create_polygon(start_x+2,start_y+35,start_x+98,start_y+35,
    start_x+21,start_y+90,start_x+50,start_y,start_x+79,start_y+90, color = 'yellow')
