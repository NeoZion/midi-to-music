import win32api
import win32gui
import win32con

class win32(object):
    def __init__(self):
        self.key_map = {
            "1": 49, "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, "7": 55,
            "Q": 81, "W": 87, "E": 69, "R": 82, "T": 84, "Y": 89, "U": 85,
            "A": 65, "S": 83, "D": 68, "F": 70, "G": 71, "H": 72, "J": 74,
        }
        self.windowName = u"天涯明月刀"

    def get_Hwnd(self):
        hwnd = win32gui.FindWindow(0,self.windowName)
        if (hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            return rect[0],rect[1]
        return None

    def key_down(self,key):
        key = key.upper()
        vk_code = self.key_map[key]
        win32api.keybd_event(vk_code,win32api.MapVirtualKey(vk_code,0),0,0)
    
    def key_up(self,key):
        key = key.upper()
        vk_code = self.key_map[key]
        win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)

    def mouse_click(self,x):
        win32api.SetCursorPos([x[0]+10,x[1]+10])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        return True