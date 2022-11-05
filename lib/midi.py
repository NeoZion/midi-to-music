import mido

class midi(object):
    def __init__(self):
        self.blackKey = [22,25,27,30,32,34,37,39,42,44,46,49,51,54,56,58,61,63,66,68,70,73,75,78,80,82,85,87,90,92,94,97,99,102,104,106]
        self.whithkey = [48,50,52,53,55,57,59,60,62,64,65,67,69,71,72,74,76,77,79,81,83]
        
        
    def To_key(self,note):
        if note in self.whithkey:
            return note
        if note in self.blackKey:
            note += 1
        if (24 <= note < 36):
            return note + 24
        if (36 <= note < 48):
            return note + 12
        if (83 < note <= 95):
            return note - 12
        if (95 < note <= 107):
            return note - 24
        return -1
            
        
    def total_blackKey(self,notelist):
        black_total = 0
        for note in notelist:
            if note in self.blackKey:
                black_total += 1
                
        return black_total

    def Deal_blackKey(self,notelist):
        temp_note = []
        Ttemp_note = []
        temp = 10000000
        total = len(notelist)
        for j in range(-11,11):
            for i in notelist:
                temp_note.append(i + j)
            total_blackKey = total_blackKey(temp_note)
            total_min = total - total_blackKey
            if total_min < temp:
                temp = total_min
                Ttemp_note = temp
            else:
                temp = temp
                
        return Ttemp_note

    
    def get_midi(self,midi_object):
        old_notelist = []
        notelist = []
        tempo = 0
        ticks_per_beat = midi_object.ticks_per_beat
        
        for track in midi_object.tracks:
            for i in track:
                if i.type == "set_tempo":
                    tempo = i.tempo
                tick = i.time * (tempo / ticks_per_beat) / 1000000
                if i.type == 'note_on' or i.type == 'note_off':
                    old_temp = {"type": i.type, "note": i.note, "time": tick,"channel":i.channel}
                    old_notelist.append(old_temp)
                    note_21 = self.To_key(i.note)
                    if note_21 != -1 :
                        temp = {"type": i.type, "note": note_21, "time": tick,"channel":i.channel}
                        notelist.append(temp)
                    
        return notelist, old_notelist
