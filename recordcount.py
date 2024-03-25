import os

s = 0
for f in os.listdir(p := input("path > ").strip("/") + "/"):
    with open(p + f) as r: print(s := s + int(r.read().split("\n")[0].strip("RecordCount: ")))
input()