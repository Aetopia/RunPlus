#Modules
import sys
sys.path.insert(1, 'modules')
import files
import url
import argparse

#Arguments
parser = argparse.ArgumentParser(prog="Run+")
command = parser.add_mutually_exclusive_group(required=True)
#---------Internet---------
#Search
command.add_argument('-s',
                     action='store',
                     nargs=2,
                     metavar=("<Search Engine>","<Query>"),
                     help="<Search Engine>: Google/DuckDuckGo/DuckDuckGoLite/QWant/Brave or g/ddg/ddgl/qw/b")
#Emoji Search
command.add_argument('-em',
                     action='store',
                     nargs=1,
                     metavar="<Emoji Name>",
                     help="Lookup an emoji on Emojipedia.")
#GitHub Search
command.add_argument('-gh','-github',
                     action='store',
                     nargs=1,
                     metavar="<Username/Repository>",
                     help="Lookup a Username/Repsitory on Github.")
#Wikipedia Search
command.add_argument('-wk',
                     action='store',
                     nargs=1,
                     metavar="<Query>",
                     help="Lookup something on Wikipedia (EN).")
#Translate
command.add_argument('-t',
                     action='store',
                     nargs=3,
                     metavar=("<Language From>","<Language To>","<Query>"),
                     help="Translate some text from one language to another using Google Translate.")
#URL
command.add_argument('-url',
                      action='store',
                      nargs=1,
                      metavar=("<URL>"),
                      help="Opens up a URL.")

#---------Files/Folders---------
#Downloads
command.add_argument('-dl',
                     action='store_true',
                     help="Opens up the Downloads Folder in Windows Explorer.")
#Videos
command.add_argument('-vids',
                     action='store_true',
                     help="Opens up the Videos Folder in Windows Explorer.")
#Pictures
command.add_argument('-pics',
                     action='store_true',
                     help="Opens up the Pictures Folder in Windows Explorer.")
#Documents
command.add_argument('-docs',
                     action='store_true',
                     help="Opens up the Documents Folder in Windows Explorer.")
#WindowsApps Folder
command.add_argument('-wr',
                     action='store_true',
                     help="Opens up the WindowsApps Folder in Windows Explorer.")
#C:\ Drive
command.add_argument('-hd',
                     action='store_true',
                     help="Opens up the C:\ Drive Folder in Windows Explorer.")
#SendTo Folder
command.add_argument('-sendto',
                     action='store_true',
                     help="Opens up the SendTo Folder in Windows Explorer.")
args = parser.parse_args()

#Internet
if args.s != None:
    url.search(args.s[0],
               args.s[1])
    
elif args.em != None:
    url.search(emoji,
               args.em[0])
    
elif args.t != None:
    url.translate(args.t[0],
                  args.t[1],
                  args.t[2])
    
elif args.gh != None:
    url.github(args.gh[0])

elif args.url != None:
    url.open(args.url[0])
    

#Files/Folders
elif args.dl == True:
    files.UserFolder("Downloads")
    
elif args.vids == True:
    files.UserFolder("Videos")
    
elif args.pics == True:
    files.UserFolder("Pictures")
    
elif args.docs == True:
    files.UserFolder("Documents")
    
elif args.wr == True:
    files.App("WR")
    
elif args.sendto == True:
    files.App("SendTo")
    
elif args.hd == True:
    files.Drive()
    
    
                     
    
