src = open("game.py", encoding="utf-8").read()   # <- change game.py to your file's real name


top = src[:src.index("class Handler")]
ns = {}
exec(top, ns)

open("index.html", "w", encoding="utf-8").write(ns["PAGE"])
print("Made index.html!")
