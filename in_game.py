import pygame, main, shared_vars

def init():
    global floor_tiles, map_layout
    
    floor_tile_raw = pygame.image.load('floor_tiles.png').convert_alpha()
    floor_tile_raw = pygame.transform.scale(floor_tile_raw, (320, 320))
    floor_tiles = {
        '1' : floor_tile_raw.subsurface((0, 0, 64, 64)),
        '2' : floor_tile_raw.subsurface((64, 0, 64, 64))
        }

    map_layout = [[1, 1, 2, 1, 1],
                  [1, 1, 2, 1, 1],
                  [1, 1, 2, 1, 1]]


def on_event(event, ms):
    pass


def draw(screen, ms):
    line_nr = 0
    list_nr = 0
    for a in map_layout:
        for b in map_layout[line_nr]:
            b = str(b)
            screen.blit(floor_tiles[b], (100+64*list_nr, 100+64*line_nr))
            list_nr +=1
        line_nr +=1
        list_nr = 0
        
    
