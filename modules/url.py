import subprocess
def search(engine, query):
    if engine.lower()=="google" or engine.lower()=="g":
        url='https://www.google.com/search?q='
    if engine.lower()=="emoji":
        url='https://emojipedia.org/search/?q='
    if engine.lower()=="wikipedia":
        url='https://wikipedia.org/w/index.php?search='
    if engine.lower()=="duckduckgo" or engine.lower()=="ddg":
        url='https://www.duckduckgo.com/?t=ffab&q='
    if engine.lower()=="duckduckgolite" or engine.lower()=="ddgl":
        url='https://lite.duckduckgo.com/lite/?q='
    if engine.lower()=="qwant" or engine.lower()=="qw":
        url='https://www.qwant.com/?q='
    if engine.lower()=="brave" or engine.lower()=="b":
        url='https://search.brave.com/search?q='
    query=query.replace(" ", "+")
    subprocess.Popen(["start",url+query],shell=True)

def github(query):
    subprocess.Popen(["start",'https://github.com/'+query],shell=True)

def translate(langfrom,langto,text):
    text=text.replace(" ", "+")
    subprocess.Popen(["start",'https://translate.google.com/?sl='+langfrom+'from&tl='+langto+'&text='+text], shell=True)

def open(url):
    subprocess.Popen(["start","https://"+url], shell=True)
