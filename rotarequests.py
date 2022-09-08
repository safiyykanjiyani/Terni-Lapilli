import requests

URL = "https://rota.praetorian.com/rota/service/play.php"
email = "lol"

# COMMANDS

new = "?request=new&email=" + email
place = "?request=place&location="
movefrom = "?request=move&from="
moveto = "&to="
status = "?request=status"
next = "?request=next"

# FUNCTIONS

def move(current, destination):
    pr = requests.get(URL + movefrom + str(current) + moveto + str(destination))
    return pr.text[37:45]

def newgame():
    #get page response and parse
    pr = requests.get(URL + new)
    if "hash" in pr.text:
        f = open("flag.txt", "a")
        f.write(pr.text)
        f.close()
    return pr.text[37:45]

def place(destination):
    pr = requests.get(URL + place + str(destination))
    return pr.text[37:45]

# NOT SUPPORTED (yet!)
def next():
    pr = requests.get(URL + next)
    return pr.text[37:45]

def status():
    pr = requests.get(URL + status)
