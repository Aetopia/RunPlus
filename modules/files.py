#Modules
import os
import subprocess

def Explorer(Folder):
    subprocess.Popen(["explorer.exe", Folder])

def UserFolder(Folder):
    if Folder=="Downloads":
        Path=os.environ['USERPROFILE']+"\\Downloads"
    elif Folder=="Videos":
        Path=os.environ['USERPROFILE']+"\\Videos"
    elif Folder=="Documents":
        Path=os.environ['USERPROFILE']+"\\Documents"
    elif Folder=="Pictures":
        Path=os.environ['USERPROFILE']+"\\Pictures"    
    Explorer(Path)
    
def App(Folder):
    if Folder=="SendTo":
        Path=os.environ['APPDATA']+"\\Microsoft\Windows\SendTo"
    elif Folder=="WR":
        Path=os.environ['LOCALAPPDATA']+"\\Microsoft\WindowsApps"
    Explorer(Path)

def Drive():
    Path="C:\\"
    Explorer(Path)
