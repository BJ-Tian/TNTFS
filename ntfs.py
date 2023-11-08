# -*- coding: utf-8 -*-
import os
import time
import subprocess
from tkinter import *
from tkinter import ttk

class FeetToMeters:
    def __init__(self, root):
        os.environ['LC_CTYPE'] = 'en_US.UTF-8'
        root.title("TNTFS")
        mainframe = ttk.Frame(root, padding="5 5 15 15")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(mainframe, text="TNTFS Is Runing!").grid(column=2, row=1, sticky=S)
        self.output_text = Text(mainframe, wrap=WORD, width=120, height=10)
        self.output_text.grid(column=1, row=3, columnspan=3, sticky=(N, W))
        self.output_text.insert(END, "TNTFS 输出:\n")
        ttk.Button(mainframe, text='最小化', command=root.iconify).grid(column=1, row=2, sticky=E)
        ttk.Button(mainframe, text='退出', command=root.quit).grid(column=3, row=2, sticky=W)
        root.iconify()
        root.after(1000, self.main)

    def print_to_output(self, message):
        self.output_text.insert(END, str(self.custom_time()) + message + "\n")
        self.output_text.see(END)

    def shell_ini(self,command):
        res = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8',
                            timeout=30,
                            executable='/bin/bash')
        if res.returncode == 0:
            return(res.stdout)
        else:
            return(False)

    def custom_time(self):
        time_local = time.localtime(int(time.time()))
        resp_time = time.strftime("[%Y-%m-%d %H:%M:%S] ", time_local)
        return(resp_time)

    def find_ntfs(self):
        return_list = []
        # resp = self.shell_ini('df -h | grep ntfs://')
        resp = self.shell_ini('df -t ntfs| grep -v "512-blocks"')
        if type(resp) == bool and resp == False:
            # self.print_to_output("没有NTFS.")
            pass
        else:
            for i in (resp.strip("\n").split("\n")):
                USB_disk = "/dev/" + i.strip("\n").split(" ")[0].split("/")[2]
                USB_Volumes = i.strip("\n").split(" ")[-1]
                return_list.append([USB_disk,USB_Volumes])
        return(return_list)

    def main(self):
        ntfs_list = self.find_ntfs()
        for r in ntfs_list:
            USB_info = {}
            USB_info[r[0]] = {"Volumes":r[1]}
            disk_status = self.shell_ini('ls ' + r[0])
            if disk_status:
                umount_shell = 'sudo umount ' + USB_info[r[0]]["Volumes"]
                self.print_to_output("正在卸载.\n" + str(umount_shell))
                umount = self.shell_ini(umount_shell)
                if umount == "":
                    self.print_to_output("状态: SUCCESS.")
                else:
                    self.print_to_output("状态: FAILED.")
                    self.print_to_output("INFO: " + str(mount))
                mount_shell = "sudo /System/Volumes/Data/opt/homebrew/bin/ntfs-3g {} {} -olocal -oallow_other -o auto_xattr".format(r[0],"/Volumes/" + str(USB_info[r[0]]["Volumes"]).split("/")[-1])
                self.print_to_output("正在挂载.\n" + str(mount_shell))
                mount = self.shell_ini(mount_shell)
                if mount == "":
                    self.print_to_output("状态: SUCCESS.")
                else:
                    self.print_to_output("状态: FAILED.")
                    self.print_to_output("INFO: " + str(mount))
            else:
                self.print_to_output("磁盘不存在.")
        root.after(1000, self.main)

root = Tk()
root.tk_setPalette(background='#f0f0f0', foreground='black',activeBackground='black', activeForeground='white')
FeetToMeters(root)
root.mainloop()

