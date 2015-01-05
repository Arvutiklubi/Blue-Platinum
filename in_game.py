import pygame, main, shared_vars

def init():
    global floor_tiles, map_layout, map_pos, char_pos, char_direction, char_move_speed, start_pos, char_img1

    char_direction = '0'

    char_move_speed = 64

    start_pos = [0, 0]
    
    map_pos = [100, 200]

    char_img1 = pygame.image.load('char_img.png').convert_alpha()
    
    floor_tile_raw = pygame.image.load('floor_tiles.png').convert_alpha()
    floor_tile_raw = pygame.transform.scale(floor_tile_raw, (320, 320))
    floor_tiles = {
        '1' : floor_tile_raw.subsurface((0, 0, 64, 64)),
        '70' : floor_tile_raw.subsurface((64, 0, 64, 64)),
        '2' : floor_tile_raw.subsurface((128, 0, 64, 64)),
        '60' : floor_tile_raw.subsurface((192, 0, 64, 64)),
        '61' : floor_tile_raw.subsurface((256, 0, 64, 64)),
        '59' : floor_tile_raw.subsurface((0, 64, 64, 64)),
        '58' : floor_tile_raw.subsurface((64, 64, 64, 64)),
        '57' : floor_tile_raw.subsurface((128, 64, 64, 64)),
        '56' : floor_tile_raw.subsurface((192, 64, 64, 64)),
        '55' : floor_tile_raw.subsurface((256, 64, 64, 64)),
        '54' : floor_tile_raw.subsurface((0, 128, 64, 64)),
        '53' : floor_tile_raw.subsurface((64, 128, 64, 64)),
        '52' : floor_tile_raw.subsurface((128, 128, 64, 64)),
        '62' : floor_tile_raw.subsurface((192, 128, 64, 64)),
        '63' : floor_tile_raw.subsurface((256, 128, 64, 64)),
        '3' : floor_tile_raw.subsurface((0, 192, 64, 64)),
        '0' : floor_tile_raw.subsurface((256, 256, 64, 64)),
        
        }

    map_layout = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,56,63,63,63,63,63,63,57],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,61,2,2,2,2,2,2,60],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,61,2,2,2,2,70,2,60],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,61,2,2,2,2,2,2,60],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,61,2,2,2,2,2,2,60],
                  [0,0,0,0,56,63,63,63,63,63,57,0,0,0,0,0,0,61,2,2,2,2,2,2,60],
                  [0,0,0,0,61,2,2,2,2,2,60,0,0,0,0,0,0,61,2,2,2,2,2,2,60],
                  [0,0,0,0,61,2,2,70,2,2,54,63,63,63,63,63,63,55,2,2,2,2,2,2,60],
                  [56,63,63,63,55,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,60],
                  [61,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,3,2,2,60],
                  [61,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,60],
                  [61,2,70,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,60],
                  [61,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,1,2,53,62,62,62,62,62,59],
                  [61,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,60],
                  [58,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,59],
                  ]

    char_pos = [8, 8]


def draw_char(screen):
    screen.blit(char_img1, (368, 268))


def collision_detection(direction, char_pos):
    if direction == 'N':
        if char_pos[1] - 1 < 0 or map_layout[char_pos[1]-1][char_pos[0]] >= 50:
            return True
        else:
            return False
        
    elif direction == 'S':
        if char_pos[1] + 1 == len(map_layout) or map_layout[char_pos[1] + 1][char_pos[0]] >= 50:
            return True
        else:
            return False
        
    elif direction == 'W':
        if char_pos[0] - 1 < 0 or map_layout[char_pos[1]][char_pos[0] - 1] >= 50:
            return True
        else:
            return False
        
    elif direction == 'E':
        if char_pos[0] + 1 == len(map_layout[char_pos[1]]) or map_layout[char_pos[1]][char_pos[0] + 1] >= 50:
            return True
        else:
            return False
    


def on_event(event, ms):
    global map_pos, char_move_speed #pikslit 
    global char_direction, start_pos, char_pos
    
    if event.type == pygame.KEYDOWN:
        if char_direction == '0':
            
            if event.key == pygame.K_UP:
                if collision_detection('N', char_pos) == False:
                
                    start_pos[1] = map_pos[1]
                    char_direction = 'N'
                    char_move_speed = 192

                    char_pos[1] -= 1
                
            if event.key == pygame.K_DOWN:
                if collision_detection('S', char_pos) == False:
                    
                    start_pos[1] = map_pos[1]
                    char_direction = 'S'
                    char_move_speed = 192

                    char_pos[1] += 1
                
            if event.key == pygame.K_LEFT:
                if collision_detection('W', char_pos) == False:
                    
                    start_pos[0] = map_pos[0]
                    char_direction = 'W'
                    char_move_speed = 192

                    char_pos[0] -= 1
                
            if event.key == pygame.K_RIGHT:
                if collision_detection('E', char_pos) == False:
                    
                    start_pos[0] = map_pos[0]
                    char_direction = 'E'
                    char_move_speed = 192

                    char_pos[0] += 1


def draw(screen, ms):
    global char_pos, map_pos, char_direction



    if char_direction == 'S' :
        map_pos[1] -= (char_move_speed//(1000/ms))

        if abs(start_pos[1] - map_pos[1]) >= 64:
            char_direction = '0'
            map_pos[1] = start_pos[1] - 64
            
    if char_direction == 'N' :
        map_pos[1] += (char_move_speed//(1000/ms))

        if abs(start_pos[1] - map_pos[1]) >= 64:
            char_direction = '0'
            map_pos[1] = start_pos[1] + 64
            
    if char_direction == 'W' :
        map_pos[0] += (char_move_speed//(1000/ms))

        if abs(start_pos[0] - map_pos[0]) >= 64:
            char_direction = '0'
            map_pos[0] = start_pos[0] + 64
            
    if char_direction == 'E' :
        map_pos[0] -= (char_move_speed//(1000/ms))

        if abs(start_pos[0] - map_pos[0]) >= 64:
            char_direction = '0'
            map_pos[0] = start_pos[0] - 64

    if char_direction == '0' :
        
        #lahutab tegelase asukohast ekraanil tegelase asukoha kaardil, et saada kaardi asukoht ekraanil
        map_pos[0] = 368 - char_pos[0]*64
        map_pos[1] = 268 - char_pos[1]*64
        
        
    
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
        
    draw_char(screen)
