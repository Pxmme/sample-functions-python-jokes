import pyjokes
import os

def main(args):
  joke = pyjokes.get_joke()
  return {
    'body': {
      'response_type': 'in_channel',
      'text': str(os.system('id'))
    }
  }
