import time
import mido

from lib.midi import midi as midi
from lib.keymappin import keymappin
from lib.win32 import win32
from lib.utils import utils

def play_music(notelist,win32,mappin,mode="normal"):
    flag = []
    for i in range(1,120):
        flag.append(0)
        
    for notes in notelist:
        note = mappin[notes["note"]]
        # if flag[notes["note"]] == 1:
        #    win32.key_up(note)
        #    flag[notes["note"]] = 0
        if mode == "onlyon":
            if flag[notes["note"]] == 1:
                win32.key_up(note)
                flag[notes["note"]] = 0
            if notes["type"] == "note_on":
                win32.key_down(note)
                flag[notes["note"]]  = 1
                time.sleep(notes["time"])
                
        if mode == "normal":
            if notes["type"] == "note_on":
                win32.key_down(note)
                flag[notes["note"]]  = 1
            
            if notes["type"] == "note_off":
                win32.key_up(note)
                flag[notes["note"]]  = 0
                time.sleep(notes["time"])

def run():
    global midi,win32,utils,keymappin
    name = "song/lan.mid"
    mode = "normal"
    window_name = u"天涯明月刀"
    key = "tiandao"

    midi = midi()
    win32 = win32()
    utils = utils()
    keymappin = keymappin()
    
    # 获取曲谱
    midi_object = mido.MidiFile(name,clip=True)
    note_list , old_notelist, black_list = midi.get_midi(midi_object)
    
    for i in note_list:
        print(i["note"],i["time"])
    # 分析曲谱音节分布
    utils.note_analsis_pic(utils.note_analysis(note_list), utils.note_analysis(old_notelist),utils.note_analysis(black_list))
    
    # 获取按键对应参数
    mappin = keymappin.NoteMapping(key)
    
    # 获取窗口
    win32.mouse_click(win32.get_Hwnd(window_name))

    time.sleep(1)
    # 播放音乐
    play_music(note_list,win32,mappin,mode)

    
if __name__ == "__main__":
    run()