import win32api
import win32gui
import time
import win32con
import mido
import threading
import numpy as np

windowName = u"天涯明月刀"

key_map = {
    "1": 49, "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, "7": 55,
    "Q": 81, "W": 87, "E": 69, "R": 82, "T": 84, "Y": 89, "U": 85,
    "A": 65, "S": 83, "D": 68, "F": 70, "G": 71, "H": 72, "J": 74,
}

def getHwnd():
    hwnd = win32gui.FindWindow(0,windowName)
    if (hwnd):
        rect = win32gui.GetWindowRect(hwnd)
        return rect[0],rect[1]
    return None
 
 
def key_down(key):
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code,win32api.MapVirtualKey(vk_code,0),0,0)
 
 
def key_up(key):
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)

def find(arr, time):
    result = []
    for i in arr:
        if i["time"] == time:
            result.append(i["note"])
    return result

def note_density(track):
    density_vector = np.zeros([128])
    # for note in track:
    #     print(note["note"])
    for note in track:
        density_vector[note["note"]] += 1
    return density_vector

def calculate_match(track, mapping_vec):
    track_note_density = note_density(track)
    match_ratio = np.dot(track_note_density, mapping_vec) / np.sum(track_note_density)
    return match_ratio

def get_shift_best_match(track, bounds=[-21,21]):
    best_shift = 0
    best_match = 0
    for shift in range(*bounds):
        shifted_keys = [int(k)+shift for k in notes]
        shifted_mapping = np.zeros([128])
        for key in shifted_keys:
            shifted_mapping[key] = 1  # higher pitch should be assigned more weight?
        match_score = calculate_match(track, shifted_mapping)
        if match_score > best_match:  # higher shift takes priority
            best_match = match_score
            best_shift = shift
    return -best_shift, best_match
    
def DealMidi(name):
    type = ['note_on','note_off']
    tracks = []
    end_track = []
    midi_object = mido.MidiFile(name, clip=True)
    try:
        flag = False
        for i in midi_object.tracks:
            for j in i :
                if j.dict()["type"] == "set_tempo":
                    flag = True
                    tempo = j.tempo
                    break
            if flag:
                break
        bpm = 60000000 / tempo
        tick_accuracy = bpm / 20
    except:
        tick_accuracy = int(input("计算失败，请检查文件是否完整，或者手动输入播放速度：（7）"))
    
    for i,track in enumerate(midi_object.tracks):
        last_time = 0
        last_on = 0
        for msg in track:
            info = msg.dict()
            info['pertime'] = info['time']
            info['time'] += last_time
            last_time = info['time']
            if (info['type'] in type):
                del info['channel']
                del info['velocity']
                info['time'] = round(info['time'] / tick_accuracy)
                if info['type'] == 'note_on':
                    del info['type']
                    del info['pertime']
                    last_on = info['time']
                    tracks.append(info)
                else:
                    del info['type']
                    del info['pertime']
                    last_on = info['time']
                    end_track.append(info)
    mmax = 0
    for i in tracks:
        mmax = max(mmax, i['time'] + 1)
    start = {}
    print("开始转换乐谱...")
    for i in range(mmax):
        start[str(i)] = find(tracks, i)
        
    shift, score = get_shift_best_match(tracks)
    
    return mmax, start, shift

    
    
def play_music(name):
    mmax, start, shift = DealMidi(name)
    
    for i in range(mmax):
        if i != 0:
            for note in start[str(i - 1)]:
                if note + shift in notes:
                    key_up(NoteMapping()[note + shift])
        for note in start[str(i)]:
            if note + shift in notes:
                key_down(NoteMapping()[note + shift])
        time.sleep(0.025)
        
if __name__ == '__main__':
    name = 'lan.mid'
    mouse_click(getHwnd())
    play_music(name)
    
    # t0 = threading.Thread(target=play_music, args=(midi,0))
    # t1 = threading.Thread(target=play_music, args=(midi,1))
    # t2 = threading.Thread(target=play_music, args=(midi,2))
    # t3 = threading.Thread(target=play_music, args=(midi,3))
    # t4 = threading.Thread(target=play_music, args=(midi,4))
    # t5 = threading.Thread(target=play_music, args=(midi,5))
    # t6 = threading.Thread(target=play_music, args=(midi,6))
    # t7 = threading.Thread(target=play_music, args=(midi,7))
    # t0.start()
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    # t7.start()

    