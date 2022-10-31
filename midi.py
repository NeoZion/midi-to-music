import mido
import sys
import json

temp = []
for i in range(120):
    note = {"key":i,"val":0}
    temp.append(note)

time = 0
midi_object = mido.MidiFile("lan.mid", clip=True)
for track in midi_object.tracks:
    for i in track:
        if i.type == 'note_on' or i.type == 'note_off':
            time = i.time + time
            temp[i.note]["val"] += 1
            print(i)

for i in temp:
    if i['val'] > 0:
        print(i)
        
print(time / 60000)