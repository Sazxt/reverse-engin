# pydisasm version 4.5.1
# Python bytecode 2.7 (62211)
# Disassembled from Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Timestamp in code: 1586398052 (2020-04-09 09:07:32)
# Method Name:       <module>
# Filename:          tes.py
# Argument count:    0
# Number of locals:  0
# Stack size:        5
# Flags:             0x00000040 (NOFREE)
# First Line:        1
# Constants:
#    0: -1
#    1: None
#    2: 'EzzKun'
#    3: <code object EzzKun at 0xb67b9728, file "tes.py", line 3>
#    4: ()
# Names:
#    0: time
#    1: sys
#    2: EzzKun
#    3: EOFError
  1:           0 LOAD_CONST                0 (-1)
               3 LOAD_CONST                1 (None)
               6 IMPORT_NAME               0 (time) # import time
               9 STORE_NAME                0 (time)
              12 LOAD_CONST                0 (-1)
              15 LOAD_CONST                1 (None)
              18 IMPORT_NAME               1 (sys) # import sys
              21 STORE_NAME                1 (sys)
              24 LOAD_CONST                2 ('EzzKun') # EzzKun()
              27 LOAD_CONST                4 (())

  3:          30 LOAD_CONST                3 (<code object EzzKun at 0xb67b9728, file "tes.py", line 3>)
              33 MAKE_FUNCTION             0
              36 CALL_FUNCTION             0 (0 positional, 0 named)
              39 BUILD_CLASS # class
              40 STORE_NAME                2 (EzzKun) # EzzKun --> class EzzKun:
              43 SETUP_EXCEPT             11 (to 57) # try:
              46 LOAD_NAME                 2 (EzzKun) # EzzKun()
              
              try:
                  EzzKun()


 14:          49 CALL_FUNCTION             0 (0 positional, 0 named)

 15:          52 POP_TOP
              53 POP_BLOCK
              54 JUMP_FORWARD             17 (to 74)  # None
         >>   57 DUP_TOP
              58 LOAD_NAME                 3 (EOFError) # EOFError 
              61 COMPARE_OP               10 (exception-match) # except EOFError:
              64 POP_JUMP_IF_FALSE        79 (to 79)
              67 POP_TOP
              68 POP_TOP
              69 POP_TOP
              70 JUMP_FORWARD              1 (to 74)
              73 END_FINALLY # pass
         >>   74 LOAD_CONST                1 (None)
              77 RETURN_VALUE
              
          //////
          try:
              EzzKun()
          except EOFError:
              pass


# Method Name:       EzzKun
# Filename:          tes.py
# Argument count:    0
# Number of locals:  0
# Stack size:        1
# Flags:             0x00000042 (NOFREE | NEWLOCALS)
# First Line:        3
# Constants:
#    0: <code object __init__ at 0xb67b97b8, file "tes.py", line 4>
# Names:
#    0: __name__
#    1: __module__
#    2: __init__
  3:           0 LOAD_NAME                 0 (__name__) # __module__ = __name__
               3 STORE_NAME                1 (__module__)

  4:           6 LOAD_CONST                0 (<code object __init__ at 0xb67b97b8, file "tes.py", line 4>)
               9 MAKE_FUNCTION             0 # def 
              12 STORE_NAME                2 (__init__) # __init__
              15 LOAD_LOCALS # self
              16 RETURN_VALUE

# Class Init ZeenKun <----->

  5           0 LOAD_CONST               1 (10)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (angka) # angka
              # parsing
              self.angka = 10

  6           9 LOAD_CONST               2 (0)
             12 LOAD_FAST                0 (self)
             15 STORE_ATTR               1 (apes)
             # parsing
             self.apes = 0

  7          18 SETUP_LOOP              99 (to 120)
             21 LOAD_GLOBAL              2 (range) # range
             24 LOAD_FAST                0 (self) # self
             27 LOAD_ATTR                0 (angka) # .angka
             30 CALL_FUNCTION            1
             33 GET_ITER            # in 
        >>   34 FOR_ITER                82 (to 119) # for 
             37 STORE_FAST               1 (i) # i
             # parsing 
             for i in range(self.angka):

  8          40 LOAD_GLOBAL              3 (time)
             43 LOAD_ATTR                4 (sleep) # sleep(0.5)
             46 LOAD_CONST               3 (0.5)
             49 CALL_FUNCTION            1
             52 POP_TOP             
            # parsing
            time.sleep(0.5)

  9          53 LOAD_FAST                0 (self) # self
             56 DUP_TOP             
             57 LOAD_ATTR                1 (apes) # .apes
             60 LOAD_CONST               4 (1) # di tambah 1
             63 INPLACE_ADD         # +=
             64 ROT_TWO             
             65 STORE_ATTR               1 (apes) # apes
             # parsing
             self.apes += 1

 10          68 JUMP_ABSOLUTE           74
             71 LOAD_CONST           34470 ( CORUP CODE ) # ga ada anjink.....
        >>   74 LOAD_GLOBAL              5 (sys) # sys.
             77 LOAD_ATTR                6 (stdout) # stdout
             80 LOAD_ATTR                7 (write) # write
             83 LOAD_CONST               5 ('\r\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m Tunggu Sampai ')
             86 LOAD_GLOBAL              8 (str)
             89 LOAD_FAST                0 (self)
             92 LOAD_ATTR                1 (apes)
             95 CALL_FUNCTION            1
             98 BINARY_ADD          # + 
             99 CALL_FUNCTION            1 # ()
            102 POP_TOP             
            # parsing
            sys.stdout.write('\r\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m Tunggu Sampai '+str(self.apes))

 11         103 LOAD_GLOBAL              5 (sys) # sys
            106 LOAD_ATTR                6 (stdout) # .stdout
            109 LOAD_ATTR                9 (flush) # .flush
            112 CALL_FUNCTION            0 # ()
            115 POP_TOP             
            116 JUMP_ABSOLUTE           34
        >>  119 POP_BLOCK           # end loncat block
        # parsing
        sys.stdout.flush()

 12     >>  120 LOAD_CONST               6 ('\n\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m INI ISINYA !!!')
            123 PRINT_ITEM          # print 
            124 PRINT_NEWLINE       # cetak garis baru
            125 LOAD_CONST               0 (None)
            128 RETURN_VALUE        
            # parsing
            print '\n\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m INI ISINYA !!!'

