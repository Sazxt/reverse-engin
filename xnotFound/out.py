# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:23:16) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <xNot_Found>
import marshal, base64, sys, os, time
B = '\x1b[34;1m'
R = '\x1b[31;1m'
G = '\x1b[32;1m'
W = '\x1b[0m'
Y = '\x1b[33;1m'

def banner():
    os.system('clear')
    print R + '                                          _    _  __'
    print ' ___ _ _  _ __ _  _ ___ _ __  __ _ _ _ __| |_ / |/ /'
    print "/ -_) ' \\| '_ \\ || |___| '  \\/ _` | '_(_-< ' \\| / _ \\ "
    print W + '\\___|_||_| .__/\\_, |   |_|_|_\\__,_|_| /__/_||_|_\\___/'
    print '         |_|   |__/'
    print Y + '0{' + 49 * '=' + '}0'
    print Y + '|' + B + ' Author  : ' + W + 'xNot_Found' + Y + '                              |'
    print Y + '|' + B + ' Contact : ' + W + '+62823-8637-2115' + Y + '                        |'
    print Y + '|' + B + ' Email   : ' + W + 'febryafriansyah@programmer.net' + Y + '          |'
    print Y + '|' + B + ' Website : ' + W + 'http://hatakecnk.noads.biz' + Y + '              |'
    print Y + '|' + B + ' Github  : ' + W + 'https://github.com/hatakecnk' + Y + '            |'
    print Y + '0{' + 49 * '=' + '}0\n'


try:
    banner()
    file = raw_input('\x1b[0m[\x1b[31m Input Your File /path/file.py \x1b[0m]> \x1b[36m')
except IndexError:
    print R + '[' + W + '!' + R + '] ' + W + 'there is an error'
    sys.exit()
except KeyboardInterrupt:
    print R + '[' + W + '!' + R + '] ' + W + 'ctrl+c detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
    time.sleep(3)
    sys.exit()
except EOFError:
    print R + '\n[' + W + '!' + R + '] ' + W + 'ctrl+d detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
    time.sleep(3)
    sys.exit()
else:
    try:
        fileopen = open(file).read()
    except IOError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file not exist\n'
        sys.exit()

    try:
        a = compile(fileopen, 'dg', 'exec')
        b = marshal.dumps(a)
        c = base64.b16encode(b)
    except TypeError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file already encrypted\n'
        sys.exit()

d = '#Encrypted By xNot_Found\n#Github : https://github.com/hatakecnk/\n#Do Not Edit The Script To Avoid Errors\nimport marshal, base64\nexec(marshal.loads(base64.b16decode("' + c + '")))'
e = file.replace('.py', '_enc.py')
f = open(e, 'w')
f.write(d)
f.close()
banner()
print B + '[' + W + '+' + B + '] ' + G + 'file saved : ' + W + e