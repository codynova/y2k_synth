import sys
from . import synth

def main():
    try:
        args = sys.argv

        if '-n' not in args:
            raise Exception('ERROR: Must pass a value for note (-n)')
        
        note = args[args.index('-n') + 1]
        synth.test(note)

    except Exception as error:
        print(error)
        sys.exit()

if __name__ == '__main__':
    main()