import win32api
import win32gui
import win32con
import win32security
class win32(object):
    def __init__(self):
        
        """ key_map = {
            "1": 49, "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, "7": 55, "8": 56, "9": 57, "0": 58,
            "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
            "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
            "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90
        } """

        self.key_map = {
            "1": 49, "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, "7": 55,
            "Q": 81, "W": 87, "E": 69, "R": 82, "T": 84, "Y": 89, "U": 85,
            "A": 65, "S": 83, "D": 68, "F": 70, "G": 71, "H": 72, "J": 74,
            "Z": 90, "X": 88, "C": 67, "V": 86, "B": 66, "N": 78, "M": 77,
        }

    def get_Hwnd(self,window_name):
        self.process_privileges(0)
        hwnd = win32gui.FindWindow(0,window_name)
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
    
    def process_privileges(self,pid):
        priv_list = ""
        try:
            hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION,False,pid)
            htok = win32security.OpenProcessToken(hproc,win32con.TOKEN_QUERY)
            privs = win32security.GetTokenInformation(htok,win32security.TokenPrivileges)
            
            for i in privs:
                if i[1] == 3:
                    priv_list += "%s|" % win32security.LookupPrivilegeName(None,i[0])
        except Exception as e:
            priv_list = "N/A"
 
        return priv_list
