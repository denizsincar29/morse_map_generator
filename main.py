import os
import json
with open("template.map", "r", encoding="UTF-8") as f: t=f.read()
with open("morse.json", "r", encoding="UTF-8") as f: morse=json.loads(f.read())
try: os.remove("result.map")
except: pass
text=input("enter text that should be morse coded")
i=20
with open("result.map", "a", encoding="UTF-8") as f:
	f.write(t)
	t="ambience {} {} 0 5 alarm15.ogg 0 100\n"
	for char in text:
		try: c=morse[char]
		except KeyError: c=" "
		for dot in c:
			match dot:
				case ".":
					f.write(t.format(i, i+1))
					i+=4
				case "-":
					f.write(t.format(i, i+5))
					i+=8
				case " ":
					i+=16
		i+=6