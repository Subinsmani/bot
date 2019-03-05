
#!/usr/bin/env python

import os, json

paths = ['latest.json']

indents = 3

def main():
	for path in paths:
		if os.path.isdir(path):
			for file in os.listdir(path):
				formatter(path+'/'+file)
		elif os.path.isfile(path):
  			formatter(path)
def formatter(path):
	if not path.endswith('.json'):
		return
	try:
		data = json.loads(open(path).read())
		outfile = open(path, 'w')
		json.dump(data, outfile, indent=indents)
		print(path,"...SUCCESS")
	except:
		print(path,"...FAILED")

if __name__== "__main__":
  main()
