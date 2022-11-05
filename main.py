import time

from lib.midi import midi as midi
from lib.keymappin import keymappin
from lib.win32 import win32
from lib.utils import utils

def play_music(notelist,win32,mappin):
    for notes in notelist:
        note = mappin[notes["note"]]
        tick = int(notes["time"])
        tick = tick / 1000000
        print(notes["type"],note,tick)
        if notes["type"] == "note_on":
            win32.key_down(note)
        if notes["type"] == "note_off":
            win32.key_up(note)
            time.sleep(tick)

def run():
    name = "song/lan.mid"
    global midi,win32,utils,keymappin
    
    midi = midi()
    win32 = win32()
    utils = utils()
    keymappin = keymappin()
    
    
    # 获取曲谱
    notelist , old_notelist = midi.get_midi(name)
    
    # 分析曲谱音节分布
    utils.note_analsis_pic(utils.note_analysis(notelist), utils.note_analysis(old_notelist))
    
    # 获取按键对应参数
    mappin = keymappin.NoteMapping()
    
    # 获取窗口
    win32.mouse_click(win32.get_Hwnd())

    time.sleep(1)
    # 播放音乐
    play_music(notelist,win32,mappin)

    
if __name__ == "__main__":
    run()