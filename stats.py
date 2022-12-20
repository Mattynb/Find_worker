import matplotlib.pyplot as plt
import PySimpleGUI as sg
from button import Button

class Stats:
    def __init__(self):
        self.score = 0
        self.button = Button(f"score: {self.score}", (0, 0), shadowColor=(255,255,255))
        self.goal = Button("To Win: 100", (200, 0), shadowColor=(255,255,255))

        self.overqualification_vs_race_License =  {'name': 'overqualification_vs_race_NoLicense','male': {'black':0, 'white': 0, 'hispanic': 0, 'asian':0}, 'female': {'black': 0, 'white': 0, 'hispanic': 0, 'asian': 0}}
        self.underqualification_vs_race_License =  {'name': 'underqualification_vs_race_License','male': {'black': 0, 'white': 0, 'hispanic': 0, 'asian':0}, 'female': {'black': 0, 'white': 0, 'hispanic': 0, 'asian': 0}}
        self.expected_vs_race_License = {'name': 'expected_vs_race_License','male': {'black': 0, 'white': 0, 'hispanic': 0, 'asian':0}, 'female': {'black': 0, 'white': 0, 'hispanic': 0, 'asian': 0}}

        self.overqualification_vs_race_NoLicense =  {'name': 'overqualification_vs_race_NoLicense', 'male': {'black': 0, 'white': 0, 'hispanic': 0, 'asian':0}, 'female': {'black': 0, 'white': 0, 'hispanic': 0, 'asian': 0}}
        self.underqualification_vs_race_NoLicense =  {'name': 'underqualification_vs_race_NoLicense','male': {'black': 0, 'white':0, 'hispanic': 0, 'asian':0}, 'female': {'black': 0, 'white': 0, 'hispanic': 0, 'asian': 0}}
        self.expected_vs_race_NoLicense = {'name': 'expected_vs_race_NoLicense','male': {'black': 0, 'white': 0, 'hispanic': 0, 'asian':0}, 'female': {'black': 0, 'white': 0, 'hispanic': 0, 'asian': 0}}

        self.criminals_missed = {'name': 'criminals_missed','male': {'black': 0, 'white': 0, 'hispanic': 0, 'asian':0}, 'female': {'black': 0, 'white': 0, 'hispanic': 0, 'asian': 0}}
        self.criminals_spotted = {'name': 'criminals_spotted','male': {'black': 0, 'white': 0, 'hispanic': 0, 'asian':0}, 'female': {'black': 0, 'white': 0, 'hispanic': 0, 'asian': 0}}

        self.attr = [
            self.overqualification_vs_race_License,self.underqualification_vs_race_License,  self.expected_vs_race_License,
            self.overqualification_vs_race_NoLicense,self.underqualification_vs_race_NoLicense, self.expected_vs_race_NoLicense,
            self.criminals_missed, self.criminals_spotted
        ]

    # 's' > 'm' > 'b'
    def add(self, applicant):
        d = applicant.decision
        e = applicant.expected_choice()
        a = applicant
        if self.score >= 100: self.plt(); exit()
        if d == e: self.score += 10
        else: self.score -= 5
        if applicant.criminal: self.score -= 10

        if applicant.license: 
            if d == e : self.expected_vs_race_License[a.gender][a.race] += 1
            if d < e : self.overqualification_vs_race_License[a.gender][a.race] += 1 
            if d > e : self.underqualification_vs_race_License[a.gender][a.race] += 1

        else: 
            if d == e : 
                self.expected_vs_race_NoLicense[a.gender][a.race] += 1
                if applicant.criminal:
                    self.criminals_spotted[a.gender][a.race] += 1

            if d < e : 
                self.overqualification_vs_race_NoLicense[a.gender][a.race] += 1 
                if applicant.criminal:
                    self.criminals_missed[a.gender][a.race] += 1

            if d > e : self.underqualification_vs_race_NoLicense[a.gender][a.race] += 1
        
    def score_update(self):
        self.button = Button(f"score: {self.score}")


    def plt(self):
        l = [0,0,0,0]; races = ['black', 'white', 'hispanic', 'asian']; i =0
        s = self

        # counts 
        for a in s.attr: # attrb level
            for r in a['male']: # race level
                if i > 3: 
                    i = 0
                l[i] += a['male'][f'{r}']
                i += 1
        
            j = 0
            for n in l:
                j += n
            if j == 0:
                sg.popup(f"No instances of {a['name']}")
                continue

        fig, axs = plt.subplots(2)
        fig.suptitle(a['name'])
        axs[0].pie(l,labels=races, autopct="%1.1f%%")
        axs[1].hist(l)
        plt.show()

        l = [0,0,0,0]
        
        


def main():
    s = Stats()
    l = [0,0,0,0]; races = ['black', 'white', 'hispanic', 'asian']; i =0

    # counts 
    for a in s.attr: # attrb level
        for r in a['male']: # race level
            if i > 3: 
                i = 0
            l[i] += a['male'][f'{r}']
            i += 1
        
        j = 0
        for n in l:
            j += n
        if j == 0:
            sg.popup(f"No instances of {a['name']}")
            continue

        fig, axs = plt.subplots(2)
        fig.suptitle(a['name'])
        axs[0].pie(l,labels=races, autopct="%1.1f%%")
        axs[1].hist(l)
        plt.show()

        l = [0,0,0,0]

if __name__ == '__main__':
    main()