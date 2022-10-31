
class keymappin(object):
    def __init__(self):
        # 音节表
        self.notes =  [
        48, 50, 52, 53, 55, 57, 59, # C4~B4
        60, 62, 64, 65, 67, 69, 71, # C5~B5 (中央)
        72, 74, 76, 77, 79, 81, 83, # C6~B6
    ]
        # 键盘表
        self.keys =  [
        '1', '2', '3', '4', '5', '6', '7', # C4~B4
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', # C5~B5 (中央)
        'A', 'S', 'D', 'F', 'G', 'H', 'J', # C6~B6
    ] 
           
    def NoteMapping(self):
        keysNotes = {}
        for i in range(len(self.notes)):
            keysNotes[self.notes[i]] = self.keys[i]
            
        return keysNotes
    
