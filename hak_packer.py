import os
import subprocess
import yaml
import sys
import time
from os.path import join

# usage is:
#     python hak_packer.py pack
#     python hak_packer.py unpack


def main():
    command = str(sys.argv[1])

    # config = yaml.safe_load(open("packer_settings.yaml"))
    # targetDir = 'target'

    print(f'Command is to {str(sys.argv[1])}')
    # if not os.path.isdir(targetDir):
    #     os.mkdir(targetDir)
    #     return
    
    if command == 'pack':
        pack()
    elif command == 'unpack':
        unpack('raw', 'hak')
    else:
        print('ERROR - unrecognized command. Use pack or unpack.')
    # clean up

    print(f'{command} complete')

def pack():
    print('todo')

def unpack(hakDir, targetDir):
    print(f'Unpacking hak files from {hakDir}')
    unpackTic = time.perf_counter()
    
    absHak = os.path.abspath(hakDir)
    for root, subdirs, files in os.walk(hakDir):
        for f in files:
            currentHak = join(absHak, f)
            targetHakDir = join(targetDir, os.path.splitext(f)[0])
            try:
                os.makedirs(targetHakDir)
            except FileExistsError:
                # directory already exists
                pass
            print(f'Unpacking {currentHak}')
            p = subprocess.Popen(["nwn_erf", '-f', currentHak, '-x'], cwd=targetHakDir)
            p.wait()
            print(f'Unpacked to {targetHakDir}')

    unpackToc = time.perf_counter()
    print(f'Unpacked hak files to {targetDir} in {unpackToc - unpackTic:0.1f}s')


if __name__ == "__main__":
    main()