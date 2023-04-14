from tkinter import *#line:1
from tkinter import ttk #line:2
import subprocess #line:3
class FeetToMeters :#line:5
    def __init__ (OO00000OO0O00O00O ,OO00OOOOOO0000000 ):#line:7
        OO00OOOOOO0000000 .title ("TNTFS")#line:8
        OOO0OOO0000O00000 =ttk .Frame (OO00OOOOOO0000000 ,padding ="5 5 15 15")#line:9
        OOO0OOO0000O00000 .grid (column =0 ,row =0 ,sticky =(N ,W ,E ,S ))#line:10
        ttk .Label (OOO0OOO0000O00000 ,text ="TNTFS Is Runing!").grid (column =2 ,row =1 ,sticky =S )#line:11
        ttk .Button (OOO0OOO0000O00000 ,text ='最小化',command =OO00OOOOOO0000000 .iconify ).grid (column =1 ,row =2 ,sticky =E )#line:12
        ttk .Button (OOO0OOO0000O00000 ,text ='退出',command =OO00OOOOOO0000000 .quit ).grid (column =3 ,row =2 ,sticky =W )#line:13
        OO00OOOOOO0000000 .iconify ()#line:14
        OO00OOOOOO0000000 .after (1000 ,OO00000OO0O00O00O .main )#line:15
    def shell_ini (O0OOO000O00OO0O00 ,OO0000O0OOOOOOO0O ):#line:17
        OO000O000OOOO000O =subprocess .run (OO0000O0OOOOOOO0O ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,encoding ='utf-8',timeout =30 ,executable ='/bin/bash')#line:20
        if OO000O000OOOO000O .returncode ==0 :#line:21
            return (OO000O000OOOO000O .stdout )#line:22
        else :#line:23
            return (False )#line:24
    def find_ntfs (OOOO0OO00O0O0O0OO ):#line:26
        O00000OOO0OO0O00O =[]#line:27
        O000OOO000O000O00 =OOOO0OO00O0O0O0OO .shell_ini ('df -h | grep ntfs://')#line:28
        if type (O000OOO000O000O00 )==bool and O000OOO000O000O00 ==False :#line:29
            pass #line:30
        else :#line:32
            for O0OOOO00OO000O0OO in (O000OOO000O000O00 .strip ("\n").split ("\n")):#line:33
                O0O0O0O0000OOO0O0 ="/dev/"+O0OOOO00OO000O0OO .strip ("\n").split (" ")[0 ].split ("/")[2 ]#line:34
                OOOO0O0OOOO0O00OO =O0OOOO00OO000O0OO .strip ("\n").split (" ")[-1 ]#line:35
                O00000OOO0OO0O00O .append ([O0O0O0O0000OOO0O0 ,OOOO0O0OOOO0O00OO ])#line:36
        return (O00000OOO0OO0O00O )#line:37
    def main (OOO0OO00O0OO00OO0 ):#line:39
        O000O00OO000O0O0O =OOO0OO00O0OO00OO0 .find_ntfs ()#line:40
        for O0OO0O00O0O0OOOOO in O000O00OO000O0O0O :#line:41
            O000O0O0000OO0000 ={}#line:42
            O000O0O0000OO0000 [O0OO0O00O0O0OOOOO [0 ]]={"Volumes":O0OO0O00O0O0OOOOO [1 ]}#line:43
            OOO00O000O0O0OOOO =OOO0OO00O0OO00OO0 .shell_ini ('ls '+O0OO0O00O0O0OOOOO [0 ])#line:44
            if OOO00O000O0O0OOOO :#line:45
                OOOOOO0O00O0000O0 =OOO0OO00O0OO00OO0 .shell_ini ('sudo umount '+O000O0O0000OO0000 [O0OO0O00O0O0OOOOO [0 ]]["Volumes"])#line:46
                O000OO0OO00O0O000 ="sudo /System/Volumes/Data/opt/homebrew/bin/ntfs-3g {} {} -olocal -oallow_other -o auto_xattr".format (O0OO0O00O0O0OOOOO [0 ],"/Volumes/"+str (O000O0O0000OO0000 [O0OO0O00O0O0OOOOO [0 ]]["Volumes"]).split ("/")[-1 ])#line:48
                O00O0O0O0000OOOOO =OOO0OO00O0OO00OO0 .shell_ini (O000OO0OO00O0O000 )#line:49
            else :#line:52
                pass #line:53
        root .after (1000 ,OOO0OO00O0OO00OO0 .main )#line:55
root =Tk ()#line:58
FeetToMeters (root )#line:59
root .mainloop ()