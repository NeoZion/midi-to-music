
import matplotlib.pyplot as plt

class utilss(object):
    def __init__(self):
        pass
    
    def base_note(self):
        base_note = []
        for i in range(120):
            note = {"key":i,"val":0}
            base_note.append(note)
        return base_note

    def note_analysis(self,note):
        base_note = self.base_note()
        for i in note:
           if i["note"] in range(1,120) and (i["type"] == 'note_on' or i["type"] == 'note_off'):
               base_note[i["note"]]["val"] += 1 
        
        return base_note
    
    def note_analsis_pic(self,deal_note,old_note):
        fig = plt.figure()
        y = []
        x = []
        for i in old_note:
            x.append(i["key"])
            y.append(i["val"])
        
        y1 = []
        x1 = []
        for i in deal_note:
            x1.append(i["key"])
            y1.append(i["val"])
            
        plt.plot(x, y, color='r', linestyle='-')
        plt.plot(x1, y1, color='g', linestyle='-')
        plt.show()
        