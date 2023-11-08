# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import subprocess


class FeetToMeters:

    def __init__(self, root):
        root.title("TNTFS")
        mainframe = ttk.Frame(root, padding="5 5 15 15")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(mainframe, text="TNTFS Is Runing!").grid(column=2, row=1, sticky=S)
        ttk.Button(mainframe, text='最小化', command=root.iconify).grid(column=1, row=2, sticky=E)
        ttk.Button(mainframe, text='退出', command=root.quit).grid(column=3, row=2, sticky=W)
        root.iconify()
        root.after(1000, self.main)

    def shell_ini(self,command):
        res = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8',
                            timeout=30,
                            executable='/bin/bash')
        if res.returncode == 0:
            return(res.stdout)
        else:
            return(False)

    def find_ntfs(self):
        return_list = []
        # resp = self.shell_ini('df -h | grep ntfs://')
        resp = self.shell_ini('df -t ntfs| grep -v "512-blocks"')
        if type(resp) == bool and resp == False:
            pass
            print("没有NTFS")
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
                print(umount_shell)
                umount = self.shell_ini(umount_shell)
                print("正在卸载",umount)
                mount_shell = "sudo /System/Volumes/Data/opt/homebrew/bin/ntfs-3g {} {} -olocal -oallow_other -o auto_xattr".format(r[0],"/Volumes/" + str(USB_info[r[0]]["Volumes"]).split("/")[-1])
                print(mount_shell)
                mount = self.shell_ini(mount_shell)
                print("正在挂载.",mount)
            else:
                pass
                # print("磁盘不存在.")
        root.after(1000, self.main)


root = Tk()
FeetToMeters(root)
root.mainloop()



