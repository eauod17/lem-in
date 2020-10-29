import pygame, math
import sys
from typing import List

# we use frames, so that the game doesn't run faster then what the player can see.
#       FPS = 60 # frames per second setting
#       fpsClock = pygame.time.Clock()

listof_inst: List[str] = []


def parcing():
    listof_rooms = []
    listof_connections = {}
    dictof_connections = {}

    global listof_inst
    x_max = -1
    y_max = -1
    x_min = 1000000
    y_min = 1000000

    for line in sys.stdin:
        line = line.strip()
        if line == 'exit':
            break
        if len(line) > 0:
            if line[0] == 'L':  # todo find someway to stock this data, the good way !
                listof_inst.append(line)
            elif line.find('-') != -1:  # updating a dict that contains each room neighbers
                r1, r2 = line.split('-')
                dictof_connections[r1].append(r2)
            #  dictof_connections[r2].append(r1)
            else:
                listof_rooms.append(line)
                tpl = line.split()
                if len(tpl) == 3:
                    dictof_connections[tpl[0]] = []
                    if (int(tpl[1]) > x_max):
                        x_max = int(tpl[1])
                    if (int(tpl[2]) > y_max):
                        y_max = int(tpl[2])

                    if (int(tpl[1]) < x_min):
                        x_min = int(tpl[1])
                    if (int(tpl[2]) < y_min):
                        y_min = int(tpl[2])

    for temp in listof_rooms:
        tpl = temp.split()
        if len(tpl) == 3:
            # room = [x, y, list of connections]
            listof_connections[tpl[0]] = [int(tpl[1]), int(tpl[2]), dictof_connections[tpl[0]]]
    pad_x = int(width / (x_max + 1))
    pad_y = int(height / (y_max + 1))
    change_cordinates(listof_connections, pad_x, pad_y)
    return(listof_connections)

def change_cordinates(rooms: dict, padx: int, pady: int):
    """
    this changes the cords from the basic ones we get to the new screen scale
    """
    for rm in rooms:
        rooms[rm][0] = rooms[rm][0] * padx
        rooms[rm][1] = rooms[rm][1] * pady
"""
def center_screen(zoom, z):
    x_delta = 0
    y_delta = 0
    if z == -1:
        #hadi ba9i
        x_delta = 1
        y_delta = 1
    if z == 1:
        x_delta = int(((width * zoom) - width) / 2)
        y_delta = int(((height * zoom) - height) / 2)
    return(x_delta, y_delta)
"""

def draw_ants():
    for line in listof_inst:
        splt = line.split()
        for ant in


def draw_room_edg(screen, rooms, zoom, z, offset_x, offset_y, line: str):
    line_width = 8
    (x_map, y_map) = (0, 0)
    #center screan
    if z == -1:
        x_map = int((width - (width * zoom)) / 2)
        y_map = int((height - (height * zoom)) / 2)
    if z == 1:
        x_map = int(((width * zoom) - width) / 2) * -1
        y_map = int(((height * zoom) - height) / 2) * -1

    for rm in rooms:
        x_room = int((rooms[rm][0] * zoom) + offset_x + int(x_map))
        y_room = int((rooms[rm][1] * zoom) + offset_y + int(y_map))
        if rooms[rm][2]:
            edgs = rooms[rm][2]
            for r in edgs:
                x_edg = rooms[r][0]
                y_edg = rooms[r][1]
                x_edg = int((x_edg * zoom) + offset_x + int(x_map))
                y_edg = int((y_edg * zoom) + offset_y + int(y_map))
                # draw edg
                pygame.draw.line(screen, edg_color, (x_room, y_room), (x_edg, y_edg), line_width)
                pygame.draw.circle(screen, room_color, (x_edg, y_edg), radius_of_room)
        pygame.draw.circle(screen, room_color, (x_room, y_room), radius_of_room)

    splt = line.split()
    for inst in splt:
    for inst in splt:


   # print(z, x_map, y_map)
"""
def moveing_with_keybord(event, offset_x, offset_y):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            offset_x -= 10
        if event.key == pygame.K_RIGHT:
            offset_x += 10
        if event.key == pygame.K_UP:#
            offset_y -= 10
        if event.key == pygame.K_DOWN:
            offset_y += 10
    return (offset_x, offset_y)
"""
def main(zoom, offset_x, offset_y):
    z = 0
    rooms = {}
    rooms = parcing()
    # open window
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Lem-in')
    # loop
    for line in listof_inst:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #zooming
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom *= 1.09
                    z = 1
                elif event.button == 5:
                    if zoom > 0:
                        zoom /= 1.09
                        z = -1
                else:
                    #hadi wa9ila  hiya li kat khalini mni n kliki yw9a3 dak moxkil
                    z = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    offset_x -= 20
                if event.key == pygame.K_RIGHT:
                    offset_x += 20
                if event.key == pygame.K_UP:
                    offset_y -= 20
                if event.key == pygame.K_DOWN:
                    offset_y += 20

        # coloring background
        screen.fill(background_color)

        # draw room and edg
        draw_room_edg(screen, rooms, zoom, z, offset_x, offset_y, line)
        pygame.display.update()
        # pygame.display.flip()
        # we don't need the fps clock, the game is already slow.
        #       fpsClock.tick(FPS)


# initialization
background_color = (183, 135, 86)
room_color = (204, 193, 105)
edg_color = (208, 152, 57)
(width, height) = (2000, 1000)
radius_of_room = 20
#now manual it will become automated (offset_x, offset_y)
offset_x = 0
offset_y = 0
zoom = 1

if __name__ == "__main__":
    main(zoom, offset_x, offset_y)
