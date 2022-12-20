import pygame as pg
from pygame.locals import *
from sys import exit
from company import Company
from applicant import Applicant
from button import Button
from stats import Stats

FPS = 60
clock = pg.time.Clock()
SCREEN_SIZE = (800,600)
screen = pg.display.set_mode(SCREEN_SIZE, 0, 32)

def applicant_screen(s):
    bg = pg.transform.scale(pg.image.load('images\\office.png').convert(), SCREEN_SIZE)
    b1 = Button('Find me a Job!', position=(550,550))
    a = Applicant()
    #print(a.resume_str())

    while True:
        clock.tick(FPS)

        bq = Button('Quit/Show stats', (550,100))
        for e in pg.event.get():
            if e.type == QUIT or bq.isPressed(e):
                show_stats(s)
                pg.quit()
                exit()

            if b1.isPressed(e):
                company_screen(a, s)
        
        # background
        screen.blit(bg, (0,0))

        # resume text

        pg.draw.rect(screen,(55,52,52), pg.rect.Rect(40, 50, 270,170))
        pg.draw.rect(screen, (205,220,220), pg.rect.Rect(45, 55, 260,160))
        sys_font = pg.font.SysFont("Times New Roman", 18)
        text = f"RESUME" + a.resume_str()
        lines = text.splitlines()
        for i, l in enumerate(lines):
            screen.blit(sys_font.render(l, 0, (100,100,0)), (50, 60 + sys_font.get_height()*i))

        # character
        screen.blit(pg.transform.scale(a.image, (150,300)), (325,300))
        b1.show(screen)
        bq.show(screen)
        s.button.show(screen)
        s.goal.show(screen)
        
        pg.display.update()

def company_screen(a, s):
    bg = pg.transform.scale(pg.image.load('images\\office.png').convert(), SCREEN_SIZE)
    
    sc, mc, bc = Company('s'), Company('m'), Company()
    companies = [sc, mc, bc]

    while True:
        clock.tick(FPS)
        bq = Button('Quit/Show stats', (550,100))
        for e in pg.event.get():
            if e.type == QUIT or bq.isPressed(e):
                show_stats(s)
                pg.quit()
                exit()
            for c in companies:
                if c.button.isPressed(e):
                    manage_decision(a, c, s)
        
        screen.blit(bg, (0,0))
        
        pg.draw.rect(screen,(55,52,52), pg.rect.Rect(55, 45, 680,130))
        for c in companies:
            x, y = c.pos
            screen.blit(c.image, c.pos)
            c.button.show(screen)   

            pg.draw.rect(screen, (205,220,220), pg.rect.Rect(x- 40, 50, 220,120))
            sys_font = pg.font.SysFont("Times New Roman", 15)
            text = c._req_str()
            lines = text.splitlines()
            for i, l in enumerate(lines):
                screen.blit(sys_font.render(l, 0, (100,100,0)), (x- 40, 55 + sys_font.get_height()*i))
        
        s.button.show(screen)
        s.goal.show(screen)

        pg.display.update()
    


def manage_decision(a, c, s):
    a.decision = c.size
    s.add(a)
    s.score_update()

    if a.expected_choice() == c.size:
        text = "Match made in heaven! Thanks!"
    elif a.expected_choice() > c.size:
        text = " Not quite, possible criminal"
    else:
        text = " Too overqualified! Bad choice"
    bg = pg.transform.scale(pg.image.load('images\\office.png').convert(), SCREEN_SIZE)
    
    while True:
        clock.tick(FPS)
       
        b1 = Button('continue', (550,300 + 250))
        bq = Button('Quit/Show stats', (550,100))
        for e in pg.event.get():
            if e.type == QUIT or bq.isPressed(e):
                show_stats(s)
                pg.quit()
                exit()
            if b1.isPressed(e):
                applicant_screen(s)

        screen.blit(bg, (0,0))
        x,y = SCREEN_SIZE
        c.pos = (x/2) - 50, (y/2) + 25
        x, y = c.pos
        pg.draw.rect(screen,(55,52,52), pg.rect.Rect(x -125, y- 145, 350,60))

        screen.blit(c.image, c.pos)

        pg.draw.rect(screen, (205,220,220), pg.rect.Rect(x- 115,y- 140, 325,50))
        sys_font = pg.font.SysFont("Times New Roman", 25)
        
        lines = text.splitlines()
        for i, l in enumerate(lines):
            screen.blit(sys_font.render(l, 0, (100,100,0)), (x- 115, 195 + sys_font.get_height()*i))

        b1.show(screen)
        bq.show(screen)
        s.button.show(screen)
        s.goal.show(screen)
        pg.display.update()

def show_stats(s):
    s.plt()
    pg.quit()
    exit()

pg.init()

def main():
    pg.display.set_caption('Find me a Job!')
    s = Stats()
    applicant_screen(s)
    
    
if __name__ == '__main__':
    main()
    

"""
s = Stats()
a = Applicant()
c = Company('m')
x,y = SCREEN_SIZE
c.pos = (x/2) - 50, (y/2) + 25
manage_decision(a, c, s)
"""