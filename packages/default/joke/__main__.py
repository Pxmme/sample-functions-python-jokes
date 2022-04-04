import pyjokes
import os

def main(args):
  joke = str(os.system('id')) + " " + "test" + str(1+1)
  return {
    'body': {
      'response_type': 'in_channel',
      'text': joke
    }
  }
