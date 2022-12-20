import pygame as pg
from button import Button

class Company: 
    def __init__(self, size ='b'):
        self.size = size
        self.name = {'s': 'McDonalds', 'm': 'MidCorp', 'b': 'The Enterprise'}[self.size]
        self.pay = {'s': 15, 'm': 30, 'b': 50}[self.size]
        self.requirements = {'s': 0, 'm': 3, 'b': 10}[self.size]
        
        self.source_image = pg.image.load('images\\characters\\people.webp').convert()
        self.image_rect = self._image_rect()
        self.image = pg.Surface.subsurface(self.source_image, self.image_rect) 
        self.pos = {'s': (100,300), 'm': (325,300), 'b': (550,300)}[self.size]
        
        x, y = self.pos
        self.button = Button('Get Job!', (x, y +250), company=self.size)
        #self.req_txt = Text(self._req_str(), (x, y -250), font_sz=10)

    def _image_rect(self):
        x, y, w, h = self.source_image.get_rect()
        rect = {
            'b': pg.Rect(0*w/4, h/2, w/4, h/2), 
            's': pg.Rect(1*w/4, h/2, w/4, h/2), 
            'm': pg.Rect(3*w/4, h/2, w/4, h/2)
        }
        
        return rect[self.size]

    def _req_str(self):
        s = {'s': 'small', 'm': 'medium', 'b': 'big'}
        c = {'s': '', 'm': 'and we do NOT\nwant ex-fellons', 'b': 'and we do NOT\nwant ex-fellons'}
        return f"""  {self.name} is a {s[self.size]} company.\n\n  We pay {self.pay}$ per hour \n  we expect {self.requirements}+ yrs of experience."""