import pygame as pg

class Button:
    def __init__(self, text='', position = (0, 0), txt_color = (0, 0, 0), bkg_color=(255,255,255), shadowColor = (150,50,50), font='freesansbold.ttf', font_sz=18, company = None):
        self.font = pg.font.Font(font, font_sz)
        self.text = self.font.render(text, True, txt_color, bkg_color)
        self.rect = self.text.get_rect().move(position)
        self.center = (self.rect.x/2, self.rect.y/2)
        self.shadowRect_color = shadowColor
        self.company = company # as in 's', 'm'  or 'l'

    def show(self, surface):
        x, y, w, h = self.rect
        pg.draw.rect(surface, self.shadowRect_color, (x - 10, y - 10, w + 20, h + 20))
        surface.blit(self.text, self.rect)

    def isPressed(self, event):
        x, y = pg.mouse.get_pos()
        x0,y0, w, h = self. rect
        x2, y2 = x0 + w, y0 + h

        if x > x0 and x < x2 and y > y0 and y < y2 and event.type == pg.MOUSEBUTTONDOWN:
            return True

        return False 