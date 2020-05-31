# uncompyle6 version 3.7.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: ex.py
# Compiled at: 2020-05-04 16:04:26
import time, sys
from random import choice as ch
__po__ = ['\x1b[1;31m', '\x1b[1;32m',
 '\x1b[1;33m', '\x1b[1;34m']

class ClAss:

    def __init__(self):
        self.time = 0.7
        self.ReturN()

    def DaTez_Kun(self, teks):
        for o in teks + '\n':
            sys.stdout.write(o)
            sys.stdout.flush()
            time.sleep(10.0 / 100)

    def ReturN(self):
        _ = 0
        for _ in range(10):
            _ += 1
            sys.stdout.write('\r%s[%s*%s]%s Wait A Second ! %s %s ' % (ch(__po__), ch(__po__), ch(__po__), ch(__po__), ch(__po__), str(_)))
            sys.stdout.flush()
            time.sleep(self.time)

        self.DaTez_Kun('\n%s[%s*%s]%s Thanks For Waiting' % (ch(__po__), ch(__po__), ch(__po__), ch(__po__)))


if __name__ == '__main__':
    ClAss()
# okay decompiling anti_decompile_patch.pyc
