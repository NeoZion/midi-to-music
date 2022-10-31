import time

from lib.midi import midi as midi
from lib.keymappin import keymappin
from lib.win32 import win32
from lib.utils import utils

def run():
    name = "song/lan.mid"
    global midi,win32,utils,keymappin
    
    midi = midi()
    win32 = win32()
    utils = utils()
    keymappin = keymappin()
    
    notelist , old_notelist = midi.get_midi(name)
    
    utils.note_analsis_pic(utils.note_analysis(notelist), utils.note_analysis(old_notelist))
    
    mappin = keymappin.NoteMapping()
    win32.mouse_click(win32.get_Hwnd())
    for notes in notelist:
        note = mappin[notes["note"]]
        tick = int(notes["time"])
        tick = tick / 1000000
        if notes["channel"] == 1 :
            if notes["type"] == "note_on":
                print(notes["type"],note,time)
                win32.key_down(note)
                time.sleep(tick)
            if notes["type"] == "note_off":
                win32.key_up(note)
                time.sleep(tick)

    
if __name__ == '__main__':
    run()
    
