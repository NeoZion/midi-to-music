
class keymappin(object):
    def __init__(self):
        # 音节表
        self.notes =  [
            48, 50, 52, 53, 55, 57, 59, # C4~B4
            60, 62, 64, 65, 67, 69, 71, # C5~B5 (中央)
            72, 74, 76, 77, 79, 81, 83, # C6~B6
        ]
        # 天刀键盘表
        self.tiandao_keys =  [
            'A', 'S', 'D', 'F', 'G', 'H', 'J', # C4~B4
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', # C5~B5 (中央)
            '1', '2', '3', '4', '5', '6', '7', # C6~B6
        ]
        # 原神键盘表
        self.yuanshen_keys =  [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', # C6~B6
            'A', 'S', 'D', 'F', 'G', 'H', 'J', # C5~B5 (中央)
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', # C4~B4
        ] 
           
    def NoteMapping(self,key):
        keysNotes = {}
        
        if key == "yuanshen":
            keys = self.yuanshen_keys
        if key == "tiandao":
            keys = self.tiandao_keys

        for i in range(len(self.notes)):
            keysNotes[self.notes[i]] = keys[i]
            
        return keysNotes
    
