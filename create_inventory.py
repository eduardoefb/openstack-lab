#!/usr/bin/python3

import yaml
import sys

data = None
controller_ip = ""

with open(sys.argv[1]) as f:
	data = yaml.load(f, Loader=yaml.FullLoader)

fp = open("hosts", "w")

st = "controller"
fp.write("[" + str(st) + "]\n")
for n in data["nodes"]:
   if st in n["name"]:
      fp.write(n["oam_ip"] + "\n")
	
st = "compute"
fp.write("\n[" + str(st) + "]\n")
for n in data["nodes"]:
   if st in n["name"]:
      fp.write(n["oam_ip"] + "\n")

st = "storage"
fp.write("\n[" + str(st) + "]\n")
for n in data["nodes"]:
   if st in n["name"]:
      fp.write(n["oam_ip"] + "\n")


for n in data["nodes"]:
   fp.write("\n[" + str(n["name"]) + "]\n")
   fp.write(n["oam_ip"] + "\n")

fp.close()
