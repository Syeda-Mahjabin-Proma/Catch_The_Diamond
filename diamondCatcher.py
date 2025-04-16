from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

width, height = 400, 600

diamond_x, diamond_y = random.randint(50, width - 50), height - 50 - 20
diamond_speed = 3
catcher_pos = width / 2
score = 0
game_over = False
paused = False
diamond_size = 20
diamond_color = (random.random(), random.random(), random.random())
catcher_color = (1.0, 1.0, 1.0)
button_width = 30
button_height = 25


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # background
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, width, 0, height)


def reshape(w, h):
    global width, height, catcher_pos
    width = w
    height = h
    catcher_pos = width / 2
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)


def midpoint_line(x1, y1, x2, y2):
    zone = find_zone(x1, y1, x2, y2)
    x1, y1, x2, y2 = zone0_conv(x1, y1, x2, y2, zone)

    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    moveE = 2 * dy
    moveNE = 2 * (dy - dx)
    x, y = x1, y1
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(*actual_zone_conv(x, y, zone))

    while x < x2:
        if d <= 0:
            d += moveE
        else:
            d += moveNE
            y += 1
        x += 1
        glVertex2f(*actual_zone_conv(x, y, zone))

    glEnd()
    glFlush()


def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0  # Zone 0
        elif dx >= 0 > dy:
            return 7  # Zone 7
        elif dx < 0 <= dy:
            return 3  # Zone 3
        else:
            return 4  # Zone 4
    else:
        if dx >= 0 and dy >= 0:
            return 1  # Zone 1
        elif dx >= 0 > dy:
            return 6  # Zone 6
        elif dx < 0 <= dy:
            return 2  # Zone 2
        else:
            return 5  # Zone 5


def zone0_conv(x1, y1, x2, y2, zone):
    if zone == 1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    elif zone == 2:
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2
    elif zone == 3:
        x1, y1 = -x1, y1
        x2, y2 = -x2, y2
    elif zone == 4:
        x1, y1 = -x1, -y1
        x2, y2 = -x2, -y2
    elif zone == 5:
        x1, y1 = -y1, -x1
        x2, y2 = -y2, -x2
    elif zone == 6:
        x1, y1 = -y1, x1
        x2, y2 = -y2, x2
    elif zone == 7:
        x1, y1 = x1, -y1
        x2, y2 = x2, -y2
    return x1, y1, x2, y2


def actual_zone_conv(x, y, zone):
    if zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y
    return x, y


def draw_diamond():
    global diamond_x, diamond_y, diamond_color, diamond_size
    glColor3f(*diamond_color)  # Set color for diamond
    midpoint_line(diamond_x, diamond_y + diamond_size, diamond_x + diamond_size, diamond_y)  # Top right
    midpoint_line(diamond_x + diamond_size, diamond_y, diamond_x, diamond_y - diamond_size)  # Bottom right
    midpoint_line(diamond_x, diamond_y - diamond_size, diamond_x - diamond_size, diamond_y)  # Bottom left
    midpoint_line(diamond_x - diamond_size, diamond_y, diamond_x, diamond_y + diamond_size)  # Top left


def coalition_check():
    global diamond_x, diamond_y, catcher_pos, diamond_size
    return abs(diamond_x - catcher_pos) < (80 + diamond_size) and diamond_y <= 50


def reset_diamond():
    global diamond_x, diamond_y, diamond_speed, diamond_color, diamond_size
    diamond_x = random.randint(50, width - 50)
    diamond_y = height - 50 - diamond_size
    diamond_speed += 0.5
    diamond_color = (random.random(), random.random(), random.random())


def draw_catcher():
    global catcher_pos, catcher_color
    glColor3f(*catcher_color)
    x1, y1 = catcher_pos - 80, 30  # up
    x2, y2 = catcher_pos + 80, 30  # up

    x3, y3 = catcher_pos - 50, 10  # down
    x4, y4 = catcher_pos + 50, 10  # down

    midpoint_line(x1, y1, x2, y2)
    midpoint_line(x3, y3, x4, y4)
    midpoint_line(x3, y3, x1, y1)
    midpoint_line(x2, y2, x4, y4)


def draw_buttons_and_boxes():
    global height, width, paused, button_height, button_width, diamond_size
    glColor3f(0.0, 0.0, 0.0)  # Border Colour
    margin = 20

    # Restart button box
    restart_x1 = margin
    restart_y1 = height - margin - button_height
    restart_x2 = restart_x1 + button_width
    restart_y2 = height - margin
    midpoint_line(restart_x1, restart_y1, restart_x2, restart_y1)  # Top side
    midpoint_line(restart_x2, restart_y1, restart_x2, restart_y2)  # Right side
    midpoint_line(restart_x2, restart_y2, restart_x1, restart_y2)  # Bottom side
    midpoint_line(restart_x1, restart_y2, restart_x1, restart_y1)  # Left side

    # Restart Button
    glColor3f(0.0, 0.0, 1.0)
    restart_center_x = (restart_x1 + restart_x2) // 2
    restart_center_y = (restart_y1 + restart_y2) // 2
    midpoint_line(restart_center_x - 10, restart_center_y, restart_center_x + 5, restart_center_y + 10)  # Top
    midpoint_line(restart_center_x - 10, restart_center_y, restart_center_x + 5, restart_center_y - 10)  # Bottom
    midpoint_line(restart_center_x - 10, restart_center_y, restart_center_x + 15, restart_center_y)  # Middle

    # Play/Pause button box
    glColor3f(0.0, 0.0, 0.0)
    play_pause_x1 = (width // 2) - (button_width // 2)
    play_pause_y1 = height - margin - button_height
    play_pause_x2 = play_pause_x1 + button_width
    play_pause_y2 = height - margin
    midpoint_line(play_pause_x1, play_pause_y1, play_pause_x2, play_pause_y1)  # Top side
    midpoint_line(play_pause_x2, play_pause_y1, play_pause_x2, play_pause_y2)  # Right side
    midpoint_line(play_pause_x2, play_pause_y2, play_pause_x1, play_pause_y2)  # Bottom side
    midpoint_line(play_pause_x1, play_pause_y2, play_pause_x1, play_pause_y1)  # Left side

    # Play/Pause Button
    glColor3f(1.0, 0.65, 0.0)
    play_pause_center_x = (play_pause_x1 + play_pause_x2) // 2
    play_pause_center_y = (play_pause_y1 + play_pause_y2) // 2
    if not paused:
        midpoint_line(play_pause_center_x - 5, play_pause_y1 + 3, play_pause_center_x - 5, play_pause_y2 - 3)
        midpoint_line(play_pause_center_x + 5, play_pause_y1 + 3, play_pause_center_x + 5, play_pause_y2 - 3)
    else:
        midpoint_line(play_pause_center_x - 7, play_pause_y1 + 3, play_pause_center_x + 7, play_pause_center_y)
        midpoint_line(play_pause_center_x + 7, play_pause_center_y, play_pause_center_x - 7, play_pause_y2 - 3)
        midpoint_line(play_pause_center_x - 7, play_pause_y1 + 3, play_pause_center_x - 7, play_pause_y2 - 3)

    # Exit button box
    glColor3f(0.0, 0.0, 0.0)
    exit_x1 = width - margin - button_width
    exit_y1 = height - margin - button_height
    exit_x2 = exit_x1 + button_width
    exit_y2 = height - margin
    midpoint_line(exit_x1, exit_y1, exit_x2, exit_y1)  # Top side
    midpoint_line(exit_x2, exit_y1, exit_x2, exit_y2)  # Right side
    midpoint_line(exit_x2, exit_y2, exit_x1, exit_y2)  # Bottom side
    midpoint_line(exit_x1, exit_y2, exit_x1, exit_y1)  # Left side

    # Exit button
    glColor3f(1.0, 0.0, 0.0)
    exit_center_x = (exit_x1 + exit_x2) // 2
    exit_center_y = (exit_y1 + exit_y2) // 2
    midpoint_line(exit_center_x - 10, exit_center_y - 10, exit_center_x + 10, exit_center_y + 10)
    midpoint_line(exit_center_x + 10, exit_center_y - 10, exit_center_x - 10, exit_center_y + 10)


def update(value):
    global diamond_y, game_over, score, paused, catcher_color

    if not paused:
        if not game_over:
            diamond_y -= diamond_speed

            if coalition_check():
                score += 1
                print(f"Score: {score}")
                reset_diamond()
            elif diamond_y <= 0:
                catcher_color = (1.0, 0.0, 0.0)
                draw_catcher()
                game_over = True

                print(f"Game Over. Final Score: {score}")

    glutPostRedisplay()
    glutTimerFunc(33, update, 0)  # Moving the Diamond


def display():
    global game_over, catcher_color

    glClear(GL_COLOR_BUFFER_BIT)
    draw_catcher()
    draw_diamond()
    draw_buttons_and_boxes()
    glutSwapBuffers()


def special_input(key, x, y):
    global catcher_pos, paused, game_over

    if game_over:
        return

    if key == GLUT_KEY_LEFT and catcher_pos > 50:
        catcher_pos -= 10
    elif key == GLUT_KEY_RIGHT and catcher_pos < width - 50:
        catcher_pos += 10

    glutPostRedisplay()


def mouse(button, state, x, y):
    global paused, game_over, score, diamond_speed, catcher_color, button_width, button_height, height, width
    margin = 20
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        restart_x1 = margin
        restart_y1 = height - margin - button_height
        restart_x2 = restart_x1 + button_width
        restart_y2 = height - margin

        play_pause_x1 = (width // 2) - (button_width // 2)
        play_pause_y1 = height - margin - button_height
        play_pause_x2 = play_pause_x1 + button_width
        play_pause_y2 = height - margin

        exit_x1 = width - margin - button_width
        exit_y1 = height - margin - button_height
        exit_x2 = exit_x1 + button_width
        exit_y2 = height - margin

        adjusted_y = height - y

        if restart_x1 <= x <= restart_x2 and restart_y1 <= adjusted_y <= restart_y2:
            game_over = False
            score = 0
            diamond_speed = 3
            catcher_color = (1.0, 1.0, 1.0)
            reset_diamond()
            print("Starting Over... ")

        elif play_pause_x1 <= x <= play_pause_x2 and play_pause_y1 <= adjusted_y <= play_pause_y2:
            paused = not paused
            if paused:
                print("Paused...")
            else:
                print("Resumed...")

        elif exit_x1 <= x <= exit_x2 and exit_y1 <= adjusted_y <= exit_y2:
            print(f"See you soon! Final Score: {score}")
            glutLeaveMainLoop()


def keyboard_input(key, x, y):
    global catcher_pos, paused, game_over, score, diamond_speed, catcher_color
    if game_over:
        return

    if key == b'a' or key == b'A':
        if catcher_pos > 50:
            catcher_pos -= 10

    elif key == b'd' or key == b'D':
        if catcher_pos < width - 50:
            catcher_pos += 10

    elif key == b' ':
        paused = not paused
        if paused:
            print("Paused...")
        else:
            print("Resumed...")

    elif key == b'\x1b':  # ESC key
        print(f"See you soon! Final Score: {score}")
        glutLeaveMainLoop()

    elif key == b'r' or key == b'R':
        game_over = False
        score = 0
        diamond_speed = 3
        reset_diamond()
        print("Game Reset...")

    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Catch the Diamonds")
init()
glutDisplayFunc(display)
glutSpecialFunc(special_input)
glutKeyboardFunc(keyboard_input)
glutReshapeFunc(reshape)
glutMouseFunc(mouse)
glutTimerFunc(0, update, 0)
glutMainLoop()
