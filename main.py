import pygame, sys, shared_vars, in_game

pygame.init()

screen = pygame.display.set_mode(shared_vars.disp_res)
pygame.display.set_caption('Blue_Platinum   ver0.01')

def quit_funct():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':

    clock = pygame.time.Clock()
    
    shared_vars.state = in_game #mäng läheb esimesena in_game staatusesse
    state = shared_vars.state #esimest korda sean state'i mängu seisu väärtuseks
    state.init() #enne uute state'i minemist tuleks kutsuda init funktsioon

    ms = 0 #loon ms muutuja et kood ei crash'iks

    while True:
        
        state = shared_vars.state
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                quit_funct()
                
            else:
                state.on_event(event, ms)
                

        ms = clock.tick(40) #maksimum fps on 40


        state.draw(screen, ms)

        pygame.display.flip()

        
