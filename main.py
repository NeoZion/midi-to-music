import time

from lib.MIDI import MIDI as midi
from lib.KeyMappin import KeyMappin
from lib.Win32 import Win32
from lib.utilss import utilss

def run():
    name = "lan.mid"
    notelist , old_notelist = midi().get_midi(name)
    
    utilss().note_analsis_pic(utilss().note_analysis(notelist),utilss().note_analysis(old_notelist))
    
    mappin = KeyMappin().NoteMapping()
    win32 = Win32()
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
    
