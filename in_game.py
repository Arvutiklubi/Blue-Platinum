import pygame, main, shared_vars

def init():
    global floor_tiles, map_layout, map_pos, char_pos, char_direction, char_move_speed, start_pos

    char_direction = '0'

    char_move_speed = 64

    start_pos = [0, 0]
    
    map_pos = [100, 200]
    
    floor_tile_raw = pygame.image.load('floor_tiles.png').convert_alpha()
    floor_tile_raw = pygame.transform.scale(floor_tile_raw, (320, 320))
    floor_tiles = {
        '1' : floor_tile_raw.subsurface((0, 0, 64, 64)),
        '2' : floor_tile_raw.subsurface((64, 0, 64, 64))
        }

    map_layout = [[1, 1, 2, 1, 1],
                  [1, 1, 2, 1, 1],
                  [1, 1, 2, 1, 1]]

    char_pos = [0, 0]


def on_event(event, ms):
    global map_pos, char_move_speed #pikslit 
    global char_direction, start_pos
    
    if event.type == pygame.KEYDOWN:
        if char_direction == '0':
            
            if event.key == pygame.K_UP:            
                start_pos[1] = map_pos[1]
                char_direction = 'N'
                char_move_speed = 128
                
            if event.key == pygame.K_DOWN:            
                start_pos[1] = map_pos[1]
                char_direction = 'S'
                char_move_speed = 128
                
            if event.key == pygame.K_LEFT:
                start_pos[0] = map_pos[0]
                char_direction = 'W'
                char_move_speed = 128
                
            if event.key == pygame.K_RIGHT:
                start_pos[0] = map_pos[0]
                char_direction = 'E'
                char_move_speed = 128


def draw(screen, ms):
    global char_pos, map_pos, char_direction


    if char_direction == 'N' :
        map_pos[1] -= (char_move_speed//(1000/ms))

        if abs(start_pos[1] - map_pos[1]) >= 64:
            char_direction = '0'
            map_pos[1] = start_pos[1] - 64
            
    if char_direction == 'S' :
        map_pos[1] += (char_move_speed//(1000/ms))

        if abs(start_pos[1] - map_pos[1]) >= 64:
            char_direction = '0'
            map_pos[1] = start_pos[1] + 64
            
    if char_direction == 'E' :
        map_pos[0] += (char_move_speed//(1000/ms))

        if abs(start_pos[0] - map_pos[0]) >= 64:
            char_direction = '0'
            map_pos[0] = start_pos[0] + 64
            
    if char_direction == 'W' :
        map_pos[0] -= (char_move_speed//(1000/ms))

        if abs(start_pos[0] - map_pos[0]) >= 64:
            char_direction = '0'
            map_pos[0] = start_pos[0] - 64
        
        
        
    
    screen.fill((0, 0, 0))

    
    line_nr = 0
    list_nr = 0
    for a in map_layout:
        for b in map_layout[line_nr]:
            b = str(b)
            screen.blit(floor_tiles[b], (map_pos[0]+64*list_nr, map_pos[1]+64*line_nr))
            list_nr +=1
        line_nr +=1
        list_nr = 0
        
    
