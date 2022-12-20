import pygame as pg
import random, names

class Applicant:
    def __init__(self):
        
        self.gender = 'male' #random.choice(['male', 'female'])
        self.name = names.get_first_name(self.gender).capitalize()
        self.race = random.choice(['black', 'white', 'hispanic', 'asian'])
        self.exp = random.randint(0, 15)
        self.license = random.choice([False,False,False,True])
        
        # which company the user chose for applicant
        self.decision = None

        #I need real information about conviction rates based on race to make this accurate
        self.criminal = False  # as in criminal history.
        if self.license == False:
            difficulty_boost = .1
            criminal_chance_multipliers = {'male': {'black': .3, 'white': .2, 'hispanic': .2, 'asian':.1}, 'female': {'black': .25, 'white': .15, 'hispanic': .15, 'asian':.05}}
            threshold = 1 - criminal_chance_multipliers[self.gender][self.race]
            if random.random() + difficulty_boost > 0 + threshold:
                self.criminal = True


        self.pos = (100,100)
        self.source_image = pg.image.load('images\\characters\\people.webp').convert() 
        self.image_rect = self._image_rect()
        self.image = pg.Surface.subsurface(self.source_image, self.image_rect)
        
    
    def _image_rect(self):
        x, y, w, h = self.source_image.get_rect()
        rect = {
            'male': {
                'black': pg.Rect(1*w/4, 0, w/4, h/2), 
                'white': pg.Rect(2*w/4, 0, w/4, h/2), 
                'hispanic': pg.Rect(0*w/4, 0, w/4, h/2), 
                'asian': pg.Rect(3*w/4, 0, w/4, h/2)
                }, 

            'female': {
                'black': .25, 
                'white': .15, 
                'hispanic': .15, 
                'asian':.05
            }
        }
        return rect[self.gender][self.race]

    def resume_str(self):
        return f"""
        Name: {self.name.upper()}
        Gender: {self.gender.upper()}
        Ethnicity: {self.race.upper()}
        Licensed: {str(self.license).upper()}
        Experience: {self.exp} years
        """
    
    def expected_choice(self):
        if (self.criminal): return 's' #small company
        if (self.exp >10): return 'b'
        if (self.exp >3): return 'm'
        return 's'
    
    def decision(self, d):
        self.decision = d