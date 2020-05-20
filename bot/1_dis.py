# pydisasm version 4.5.1
# Python bytecode 3.8 (3413)
# Disassembled from Python 3.8.0 (default, Dec  5 2019, 10:18:50) 
# [Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6
# Timestamp in code: 1584148226 (2020-03-14 08:10:26)
# Source code size mod 2**32: 3567 bytes
# Method Name:       visit
# Filename:          <zen_ezz>
# Argument count:    0
# Position-only argument count: 0
# Keyword-only arguments: 0
# Number of locals:  14
# Stack size:        15
# Flags:             0x00000043 (NOFREE | NEWLOCALS | OPTIMIZED)
# First Line:        170
# Constants:
#    0: None
#    1: '\x1b[1;36m================================= \x1b[1;32m(VISITING BOT)\n'
#    2: 5000000
#    3: '\r'
#    4: '                                                              '
#    5: '\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mTrying to get an url'
#    6: 'ðŸ–¥ Visit sites'
#    7: ('entity', 'message')
#    8: 2
#    9: 1
#   10: 0
#   11: ('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash')
#   12: 'Sorry, there are no new ads available'
#   13: -1
#   14: '\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSorry, there are no new ads available. \x1a\n\n'
#   15: '\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mVisit '
#   16: 15
#   17: True
#   18: ('headers', 'timeout', 'allow_redirects')
#   19: 'html.parser'
#   20: 'div'
#   21: 'g-recaptcha'
#   22: ('class_',)
#   23: 'headbar'
#   24: ('id',)
#   25: 'You must stay'
#   26: 'Please stay on'
#   27: '([\\d.]*\\d+)'
#   28: '\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32m'
#   29: '\n'
#   30: 'container-fluid'
#   31: 'data-code'
#   32: 'data-timer'
#   33: 'data-token'
#   34: 'https://dogeclick.com/reward'
#   35: ('code', 'token')
#   36: ('data', 'headers', 'timeout', 'allow_redirects')
#   37: '\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32mYou earned '
#   38: 'reward'
#   39: ' '
#   40: ' for visiting a site!\n'
#   41: '                                                                '
#   42: '\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mCaptcha Detected'
#   43: ('data',)
#   44: '\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSkip Captcha...!       \n'
#   45: 3
# Names:
#    0: mengetik
#    1: range
#    2: sys
#    3: stdout
#    4: write
#    5: flush
#    6: client
#    7: send_message
#    8: channel_entity
#    9: sleep
#   10: GetHistoryRequest
#   11: messages
#   12: message
#   13: find
#   14: withdraw
#   15: reply_markup
#   16: rows
#   17: buttons
#   18: url
#   19: id
#   20: c
#   21: get
#   22: ua
#   23: BeautifulSoup
#   24: content
#   25: re
#   26: findall
#   27: tunggu
#   28: int
#   29: find_all
#   30: post
#   31: json
#   32: loads
#   33: text
#   34: currency
#   35: GetBotCallbackAnswerRequest
#   36: channel_username
#   37: data
# Varnames:
#	i, posts, url, id, r, soup, message, sec, messageres, dat, code, timer, tokena, js
# Local variables:
#    0: i
#    1: posts
#    2: url
#    3: id
#    4: r
#    5: soup
#    6: message
#    7: sec
#    8: messageres
#    9: dat
#   10: code
#   11: timer
#   12: tokena
#   13: js

# Method Name:       visit
# Filename:          <zen_ezz>
# Argument count:    0
# Position-only argument count: 0
# Keyword-only arguments: 0
# Number of locals:  14
# Stack size:        15
# Flags:             0x00000043 (NOFREE | NEWLOCALS | OPTIMIZED)
# First Line:        170
# Constants:
#    0: None
#    1: '\x1b[1;36m================================= \x1b[1;32m(VISITING BOT)\n'
#    2: 5000000
#    3: '\r'
#    4: '                                                              '
#    5: '\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mTrying to get an url'
#    6: 'ðŸ–¥ Visit sites'
#    7: ('entity', 'message')
#    8: 2
#    9: 1
#   10: 0
#   11: ('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash')
#   12: 'Sorry, there are no new ads available'
#   13: -1
#   14: '\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSorry, there are no new ads available. \x1a\n\n'
#   15: '\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mVisit '
#   16: 15
#   17: True
#   18: ('headers', 'timeout', 'allow_redirects')
#   19: 'html.parser'
#   20: 'div'
#   21: 'g-recaptcha'
#   22: ('class_',)
#   23: 'headbar'
#   24: ('id',)
#   25: 'You must stay'
#   26: 'Please stay on'
#   27: '([\\d.]*\\d+)'
#   28: '\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32m'
#   29: '\n'
#   30: 'container-fluid'
#   31: 'data-code'
#   32: 'data-timer'
#   33: 'data-token'
#   34: 'https://dogeclick.com/reward'
#   35: ('code', 'token')
#   36: ('data', 'headers', 'timeout', 'allow_redirects')
#   37: '\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32mYou earned '
#   38: 'reward'
#   39: ' '
#   40: ' for visiting a site!\n'
#   41: '                                                                '
#   42: '\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mCaptcha Detected'
#   43: ('data',)
#   44: '\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSkip Captcha...!       \n'
#   45: 3
# Names:
#    0: mengetik
#    1: range
#    2: sys
#    3: stdout
#    4: write
#    5: flush
#    6: client
#    7: send_message
#    8: channel_entity
#    9: sleep
#   10: GetHistoryRequest
#   11: messages
#   12: message
#   13: find
#   14: withdraw
#   15: reply_markup
#   16: rows
#   17: buttons
#   18: url
#   19: id
#   20: c
#   21: get
#   22: ua
#   23: BeautifulSoup
#   24: content
#   25: re
#   26: findall
#   27: tunggu
#   28: int
#   29: find_all
#   30: post
#   31: json
#   32: loads
#   33: text
#   34: currency
#   35: GetBotCallbackAnswerRequest
#   36: channel_username
#   37: data
# Varnames:
#	i, posts, url, id, r, soup, message, sec, messageres, dat, code, timer, tokena, js
# Local variables:
#    0: i
#    1: posts
#    2: url
#    3: id
#    4: r
#    5: soup
#    6: message
#    7: sec
#    8: messageres
#    9: dat
#   10: code
#   11: timer
#   12: tokena
#   13: js
def visit():
	mengetik('\x1b[1;36m================================= \x1b[1;32m(VISITING BOT)\n')
	for i in range(5000000):
		sys.stdout.write('\r')
		sys.stdout.write('                                                              ')
		sys.stdout.write('\r')
		sys.stdout.write('\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mTrying to get an url')
		sys.stdout.flush()
		client.send_message(entity=channel_entity, message='ðŸ–¥ Visit sites')
		sleep(2)
		posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None,
		  offset_id=0,
		  max_id=0,
		  min_id=0,
		  add_offset=0,
		  hash=0))
		if posts.messages[0].message.find('Sorry, there are no new ads available') != -1:
			sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSorry, there are no new ads available. \x1a\n\n')
			withdraw()
		else:
			try:
				url = posts.messages[0].reply_markup.rows[0].buttons[0].url
				sys.stdout.write('\r')
	
		
171:           0 LOAD_GLOBAL               0 (mengetik)
               2 LOAD_CONST                1 ('\x1b[1;36m================================= \x1b[1;32m(VISITING BOT)\n')
               4 CALL_FUNCTION             1
               6 POP_TOP

172:           8 LOAD_GLOBAL               1 (range)
              10 LOAD_CONST                2 (5000000)
              12 CALL_FUNCTION             1
              14 GET_ITER
         >>   16 EXTENDED_ARG              3 (768)
              18 FOR_ITER               1010 (to 1030)
              20 STORE_FAST                0 (i)

173:          22 LOAD_GLOBAL               2 (sys)
              24 LOAD_ATTR                 3 (stdout)
              26 LOAD_METHOD               4 (write)
              28 LOAD_CONST                3 ('\r')
              30 CALL_METHOD               1
              32 POP_TOP

174:          34 LOAD_GLOBAL               2 (sys)
              36 LOAD_ATTR                 3 (stdout)
              38 LOAD_METHOD               4 (write)
              40 LOAD_CONST                4 ('                                                              ')
              42 CALL_METHOD               1
              44 POP_TOP

175:          46 LOAD_GLOBAL               2 (sys)
              48 LOAD_ATTR                 3 (stdout)
              50 LOAD_METHOD               4 (write)
              52 LOAD_CONST                3 ('\r')
              54 CALL_METHOD               1
              56 POP_TOP

176:          58 LOAD_GLOBAL               2 (sys)
              60 LOAD_ATTR                 3 (stdout)
              62 LOAD_METHOD               4 (write)
              64 LOAD_CONST                5 ('\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mTrying to get an url')
              66 CALL_METHOD               1
              68 POP_TOP
# spati
177:          70 LOAD_GLOBAL               2 (sys)
              72 LOAD_ATTR                 3 (stdout)
              74 LOAD_METHOD               5 (flush)
              76 CALL_METHOD               0
              78 POP_TOP
### 
178:          80 LOAD_GLOBAL               6 (client)
              82 LOAD_ATTR                 7 (send_message)
              84 LOAD_GLOBAL               8 (channel_entity)
              86 LOAD_CONST                6 ('ðŸ–¥ Visit sites')
              88 LOAD_CONST                7 (('entity', 'message'))
              90 CALL_FUNCTION_KW          2 (2 total positional and keyword args)
              92 POP_TOP
# client.send_message(entity=channel_entity, message='ðŸ–¥ Visit sites')
179:          94 LOAD_GLOBAL               9 (sleep)
              96 LOAD_CONST                8 (2)
              98 CALL_FUNCTION             1
             100 POP_TOP
# sleep(2)
180:         102 LOAD_GLOBAL               6 (client)
             104 LOAD_GLOBAL              10 (GetHistoryRequest)
             106 LOAD_GLOBAL               8 (channel_entity)
             108 LOAD_CONST                9 (1)
             110 LOAD_CONST                0 (None)
             112 LOAD_CONST               10 (0)
             114 LOAD_CONST               10 (0)
             116 LOAD_CONST               10 (0)
             118 LOAD_CONST               10 (0)
             120 LOAD_CONST               10 (0)
             122 LOAD_CONST               11 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
             124 CALL_FUNCTION_KW          8 (8 total positional and keyword args)
             126 CALL_FUNCTION             1
             128 STORE_FAST                1 (posts)
posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None,
  offset_id=0,
  max_id=0,
  min_id=0,
  add_offset=0,
  hash=0))
181:         130 LOAD_FAST                 1 (posts)
             132 LOAD_ATTR                11 (messages)
             134 LOAD_CONST               10 (0)
             136 BINARY_SUBSCR
             138 LOAD_ATTR                12 (message)
             140 LOAD_METHOD              13 (find)
             142 LOAD_CONST               12 ('Sorry, there are no new ads available')
             144 CALL_METHOD               1
             146 LOAD_CONST               13 (-1)
             148 COMPARE_OP                3 (!=)
             150 POP_JUMP_IF_FALSE       172 (to 172)
if posts.messages[0].message.find('Sorry, there are no new ads available') != -1:
182:         152 LOAD_GLOBAL               2 (sys)
             154 LOAD_ATTR                 3 (stdout)
             156 LOAD_METHOD               4 (write)
             158 LOAD_CONST               14 ('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSorry, there are no new ads available. \x1a\n\n')
             160 CALL_METHOD               1
             162 POP_TOP
sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSorry, there are no new ads available. \x1a\n\n')
183:         164 LOAD_GLOBAL              14 (withdraw)
             166 CALL_FUNCTION             0
             168 POP_TOP
             170 JUMP_ABSOLUTE            16 (to 16)
withdraw()
185:     >>  172 EXTENDED_ARG              2 (512)
             174 SETUP_FINALLY           638 (to 814)
else:
	try:
		
186:         176 LOAD_FAST                 1 (posts)
             178 LOAD_ATTR                11 (messages)
             180 LOAD_CONST               10 (0)
             182 BINARY_SUBSCR
             184 LOAD_ATTR                15 (reply_markup)
             186 LOAD_ATTR                16 (rows)
             188 LOAD_CONST               10 (0)
             190 BINARY_SUBSCR
             192 LOAD_ATTR                17 (buttons)
             194 LOAD_CONST               10 (0)
             196 BINARY_SUBSCR
             198 LOAD_ATTR                18 (url)
             200 STORE_FAST                2 (url)
url = posts.messages[0].reply_markup.rows[0].buttons[0].url
187:         202 LOAD_GLOBAL               2 (sys)
             204 LOAD_ATTR                 3 (stdout)
             206 LOAD_METHOD               4 (write)
             208 LOAD_CONST                3 ('\r')
             210 CALL_METHOD               1
             212 POP_TOP
sys.stdout.write('\r')
188:         214 LOAD_GLOBAL               2 (sys)
             216 LOAD_ATTR                 3 (stdout)
             218 LOAD_METHOD               4 (write)
             220 LOAD_CONST               15 ('\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mVisit ')
             222 LOAD_FAST                 2 (url)
             224 BINARY_ADD
             226 CALL_METHOD               1
             228 POP_TOP
sys.stdout.write('\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mVisit ' + url)
189:         230 LOAD_GLOBAL               2 (sys)
             232 LOAD_ATTR                 3 (stdout)
             234 LOAD_METHOD               5 (flush)
             236 CALL_METHOD               0
             238 POP_TOP
sys.stdout.flush()
190:         240 LOAD_FAST                 1 (posts)
             242 LOAD_ATTR                11 (messages)
             244 LOAD_CONST               10 (0)
             246 BINARY_SUBSCR
             248 LOAD_ATTR                19 (id)
             250 STORE_FAST                3 (id)
id = posts.messages[0].id
191:         252 LOAD_GLOBAL              20 (c)
             254 LOAD_ATTR                21 (get)
             256 LOAD_FAST                 2 (url)
             258 LOAD_GLOBAL              22 (ua)
             260 LOAD_CONST               16 (15)
             262 LOAD_CONST               17 (True)
             264 LOAD_CONST               18 (('headers', 'timeout', 'allow_redirects'))
             266 CALL_FUNCTION_KW          4 (4 total positional and keyword args)
             268 STORE_FAST                4 (r)
r = c.get(url, headers=ua, timeout=15,
  allow_redirects=True)
192:         270 LOAD_GLOBAL              23 (BeautifulSoup)
             272 LOAD_FAST                 4 (r)
             274 LOAD_ATTR                24 (content)
             276 LOAD_CONST               19 ('html.parser')
             278 CALL_FUNCTION             2
             280 STORE_FAST                5 (soup)
soup = BeautifulSoup(r.content, 'html.parser')
193:         282 LOAD_FAST                 5 (soup)
             284 LOAD_ATTR                13 (find)
             286 LOAD_CONST               20 ('div')
             288 LOAD_CONST               21 ('g-recaptcha')
             290 LOAD_CONST               22 (('class_',))
             292 CALL_FUNCTION_KW          2 (2 total positional and keyword args) # soup.find("div",class_='g-recaptcha')
             294 LOAD_CONST                0 (None)
             296 COMPARE_OP                8 (is)
             298 EXTENDED_ARG              2 (512)
             300 POP_JUMP_IF_FALSE       528 (to 528) # if soup.find("div",class_='g-recaptcha') is None
             302 LOAD_FAST                 5 (soup)
             304 LOAD_ATTR                13 (find)
             306 LOAD_CONST               20 ('div')
             308 LOAD_CONST               23 ('headbar')
             310 LOAD_CONST               24 (('id',))
             312 CALL_FUNCTION_KW          2 (2 total positional and keyword args) # soup.find("div",id='headbar') is None:
             314 LOAD_CONST                0 (None)
             316 COMPARE_OP                8 (is)
             318 EXTENDED_ARG              2 (512)
             320 POP_JUMP_IF_FALSE       528 (to 528)
if soup.find("div",id='headbar') is None and soup.find("div",class_='g-recaptcha') is None:
194:         322 LOAD_GLOBAL               9 (sleep)
             324 LOAD_CONST                8 (2)
             326 CALL_FUNCTION             1
             328 POP_TOP
sleep(2)
195:         330 LOAD_GLOBAL               6 (client)
             332 LOAD_GLOBAL              10 (GetHistoryRequest)
             334 LOAD_GLOBAL               8 (channel_entity)
             336 LOAD_CONST                9 (1)
             338 LOAD_CONST                0 (None)
             340 LOAD_CONST               10 (0)
             342 LOAD_CONST               10 (0)
             344 LOAD_CONST               10 (0)
             346 LOAD_CONST               10 (0)
             348 LOAD_CONST               10 (0)
             350 LOAD_CONST               11 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
             352 CALL_FUNCTION_KW          8 (8 total positional and keyword args)
             354 CALL_FUNCTION             1
             356 STORE_FAST                1 (posts)
posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None,
  offset_id=0,
  max_id=0,
  min_id=0,
  add_offset=0,
  hash=0))
196:         358 LOAD_FAST                 1 (posts)
             360 LOAD_ATTR                11 (messages)
             362 LOAD_CONST               10 (0)
             364 BINARY_SUBSCR
             366 LOAD_ATTR                12 (message)
             368 STORE_FAST                6 (message)
message = posts.messages[0].message
197:         370 LOAD_FAST                 1 (posts)
             372 LOAD_ATTR                11 (messages)
             374 LOAD_CONST               10 (0)
             376 BINARY_SUBSCR
             378 LOAD_ATTR                12 (message)
             380 LOAD_METHOD              13 (find)
             382 LOAD_CONST               25 ('You must stay')
             384 CALL_METHOD               1
             386 LOAD_CONST               13 (-1)
             388 COMPARE_OP                3 (!=)
             390 EXTENDED_ARG              1 (256)
             392 POP_JUMP_IF_TRUE        418 (to 418) # if posts.messages[0].message.find('You must stay') != -1
             394 LOAD_FAST                 1 (posts)
             396 LOAD_ATTR                11 (messages)
             398 LOAD_CONST               10 (0)
             400 BINARY_SUBSCR
             402 LOAD_ATTR                12 (message)
             404 LOAD_METHOD              13 (find)
             406 LOAD_CONST               26 ('Please stay on')
             408 CALL_METHOD               1
             410 LOAD_CONST               13 (-1)
             412 COMPARE_OP                3 (!=)
             414 EXTENDED_ARG              3 (768)
             416 POP_JUMP_IF_FALSE       810 (to 810) # if posts.messages[0].message.find('Please stay on') != -1
if posts.messages[0].message.find('Please stay on') != -1 and posts.messages[0].message.find('You must stay') != -1:
198:     >>  418 LOAD_GLOBAL              25 (re)
             420 LOAD_METHOD              26 (findall)
             422 LOAD_CONST               27 ('([\\d.]*\\d+)')
             424 LOAD_FAST                 6 (message)
             426 CALL_METHOD               2
             428 STORE_FAST                7 (sec)
sec = re.findall('([\\d.]*\\d+)',message)
199:         430 LOAD_GLOBAL              27 (tunggu)
             432 LOAD_GLOBAL              28 (int)
             434 LOAD_FAST                 7 (sec)
             436 LOAD_CONST               10 (0)
             438 BINARY_SUBSCR
             440 CALL_FUNCTION             1
             442 CALL_FUNCTION             1
             444 POP_TOP
tunggu(int(sec[0]))
200:         446 LOAD_GLOBAL               9 (sleep)
             448 LOAD_CONST                9 (1)
             450 CALL_FUNCTION             1
             452 POP_TOP
sleep(1)
201:         454 LOAD_GLOBAL               6 (client)
             456 LOAD_GLOBAL              10 (GetHistoryRequest)
             458 LOAD_GLOBAL               8 (channel_entity)
             460 LOAD_CONST                8 (2)
             462 LOAD_CONST                0 (None)
             464 LOAD_CONST               10 (0)
             466 LOAD_CONST               10 (0)
             468 LOAD_CONST               10 (0)
             470 LOAD_CONST               10 (0)
             472 LOAD_CONST               10 (0)
             474 LOAD_CONST               11 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
             476 CALL_FUNCTION_KW          8 (8 total positional and keyword args)
             478 CALL_FUNCTION             1
             480 STORE_FAST                1 (posts)
posts = client(GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None,
  offset_id=0,
  max_id=0,
  min_id=0,
  add_offset=0,
  hash=0))
202:         482 LOAD_FAST                 1 (posts)
             484 LOAD_ATTR                11 (messages)
             486 LOAD_CONST                9 (1)
             488 BINARY_SUBSCR
             490 LOAD_ATTR                12 (message)
             492 STORE_FAST                8 (messageres)
messageres = posts.messages[1].message
203:         494 LOAD_GLOBAL               9 (sleep)
             496 LOAD_CONST                8 (2)
             498 CALL_FUNCTION             1
             500 POP_TOP
sleep(2)
204:         502 LOAD_GLOBAL               2 (sys)
             504 LOAD_ATTR                 3 (stdout)
             506 LOAD_METHOD               4 (write)
             508 LOAD_CONST               28 ('\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32m')
             510 LOAD_FAST                 8 (messageres)
             512 BINARY_ADD
             514 LOAD_CONST               29 ('\n')
             516 BINARY_ADD
             518 CALL_METHOD               1
             520 POP_TOP
             522 JUMP_FORWARD              0 (to 524)
sys.stdout.write('\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32m' + messageres + '\n')
206:     >>  524 EXTENDED_ARG              1 (256)
             526 JUMP_FORWARD            282 (to 810)

207:     >>  528 LOAD_FAST                 5 (soup)
             530 LOAD_ATTR                13 (find)
             532 LOAD_CONST               20 ('div')
             534 LOAD_CONST               23 ('headbar')
             536 LOAD_CONST               24 (('id',))
             538 CALL_FUNCTION_KW          2 (2 total positional and keyword args)
             540 LOAD_CONST                0 (None)
             542 COMPARE_OP                9 (is-not)
             544 EXTENDED_ARG              2 (512)
             546 POP_JUMP_IF_FALSE       684 (to 684) #
if soup.find('div', id='headbar') is not None
208:         548 LOAD_FAST                 5 (soup)
             550 LOAD_ATTR                29 (find_all)
             552 LOAD_CONST               20 ('div')
             554 LOAD_CONST               30 ('container-fluid')
             556 LOAD_CONST               22 (('class_',))
             558 CALL_FUNCTION_KW          2 (2 total positional and keyword args)
             560 GET_ITER
         >>  562 FOR_ITER                118 (to 682)
             564 STORE_FAST                9 (dat)
for dat in soup.find_all("div",class_='container-fluid'):
209:         566 LOAD_FAST                 9 (dat)
             568 LOAD_METHOD              21 (get)
             570 LOAD_CONST               31 ('data-code')
             572 CALL_METHOD               1
             574 STORE_FAST               10 (code)
code = dat.get('data-code')
210:         576 LOAD_FAST                 9 (dat)
             578 LOAD_METHOD              21 (get)
             580 LOAD_CONST               32 ('data-timer')
             582 CALL_METHOD               1
             584 STORE_FAST               11 (timer)
timer = dat.get('data-timer')
211:         586 LOAD_FAST                 9 (dat)
             588 LOAD_METHOD              21 (get)
             590 LOAD_CONST               33 ('data-token')
             592 CALL_METHOD               1
             594 STORE_FAST               12 (tokena)
tokena = dat.get('data-token')
212:         596 LOAD_GLOBAL              27 (tunggu)
             598 LOAD_GLOBAL              28 (int)
             600 LOAD_FAST                11 (timer)
             602 CALL_FUNCTION             1
             604 CALL_FUNCTION             1
             606 POP_TOP
tunggu(int(timer))
213:         608 LOAD_GLOBAL              20 (c)
             610 LOAD_ATTR                30 (post)
             612 LOAD_CONST               34 ('https://dogeclick.com/reward')
             614 LOAD_FAST                10 (code)
             616 LOAD_FAST                12 (tokena)
             618 LOAD_CONST               35 (('code', 'token'))
             620 BUILD_CONST_KEY_MAP       2
             622 LOAD_GLOBAL              22 (ua)
             624 LOAD_CONST               16 (15)
             626 LOAD_CONST               17 (True)
             628 LOAD_CONST               36 (('data', 'headers', 'timeout', 'allow_redirects'))
             630 CALL_FUNCTION_KW          5 (5 total positional and keyword args)
             632 STORE_FAST                4 (r)
r = c.post('https://dogeclick.com/reward', data={'code':code,  'token':tokena}, headers=ua, timeout=15, allow_redirects=True)
214:         634 LOAD_GLOBAL              31 (json)
             636 LOAD_METHOD              32 (loads)
             638 LOAD_FAST                 4 (r)
             640 LOAD_ATTR                33 (text)
             642 CALL_METHOD               1
             644 STORE_FAST               13 (js)
js = json.loads(r.text)
215:         646 LOAD_GLOBAL               2 (sys)
             648 LOAD_ATTR                 3 (stdout)
             650 LOAD_METHOD               4 (write)
             652 LOAD_CONST               37 ('\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32mYou earned ')
             654 LOAD_FAST                13 (js)
             656 LOAD_CONST               38 ('reward')
             658 BINARY_SUBSCR
             660 BINARY_ADD
             662 LOAD_CONST               39 (' ')
             664 LOAD_GLOBAL              34 (currency)
             666 FORMAT_VALUE              0
             668 LOAD_CONST               40 (' for visiting a site!\n')
             670 BUILD_STRING              3
             672 BINARY_ADD
             674 CALL_METHOD               1
             676 POP_TOP
             678 EXTENDED_ARG              2 (512)
             680 JUMP_ABSOLUTE           562 (to 562)
         >>  682 JUMP_FORWARD            126 (to 810)
sys.stdout.write('\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32mYou earned ' + js['reward'] + f" {currency} for visiting a site!\n")
217:     >>  684 LOAD_GLOBAL               2 (sys)
             686 LOAD_ATTR                 3 (stdout)
             688 LOAD_METHOD               4 (write)
             690 LOAD_CONST                3 ('\r')
             692 CALL_METHOD               1
             694 POP_TOP
sys.stdout.write('\r')
218:         696 LOAD_GLOBAL               2 (sys)
             698 LOAD_ATTR                 3 (stdout)
             700 LOAD_METHOD               4 (write)
             702 LOAD_CONST               41 ('                                                                ')
             704 CALL_METHOD               1
             706 POP_TOP
sys.stdout.write('                                                                ')
219:         708 LOAD_GLOBAL               2 (sys)
             710 LOAD_ATTR                 3 (stdout)
             712 LOAD_METHOD               4 (write)
             714 LOAD_CONST                3 ('\r')
             716 CALL_METHOD               1
             718 POP_TOP
sys.stdout.write('\r')
220:         720 LOAD_GLOBAL               2 (sys)
             722 LOAD_ATTR                 3 (stdout)
             724 LOAD_METHOD               4 (write)
             726 LOAD_CONST               42 ('\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mCaptcha Detected')
             728 CALL_METHOD               1
             730 POP_TOP
sys.stdout.write('\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mCaptcha Detected')
221:         732 LOAD_GLOBAL               2 (sys)
             734 LOAD_ATTR                 3 (stdout)
             736 LOAD_METHOD               5 (flush)
             738 CALL_METHOD               0
             740 POP_TOP
sys.stdout.flush()
222:         742 LOAD_GLOBAL               9 (sleep)
             744 LOAD_CONST                8 (2)
             746 CALL_FUNCTION             1
             748 POP_TOP
sleep(2)
223:         750 LOAD_GLOBAL               6 (client)
             752 LOAD_GLOBAL              35 (GetBotCallbackAnswerRequest)

224:         754 LOAD_GLOBAL              36 (channel_username)

225:         756 LOAD_FAST                 3 (id)

226:         758 LOAD_FAST                 1 (posts)
             760 LOAD_ATTR                11 (messages)
             762 LOAD_CONST               10 (0)
             764 BINARY_SUBSCR
             766 LOAD_ATTR                15 (reply_markup)
             768 LOAD_ATTR                16 (rows)
             770 LOAD_CONST                9 (1)
             772 BINARY_SUBSCR
             774 LOAD_ATTR                17 (buttons)
             776 LOAD_CONST                9 (1)
             778 BINARY_SUBSCR
             780 LOAD_ATTR                37 (data)

223:         782 LOAD_CONST               43 (('data',))
             784 CALL_FUNCTION_KW          3 (3 total positional and keyword args)
             786 CALL_FUNCTION             1
             788 POP_TOP
client(GetBotCallbackAnswerRequest(channel_username, id, data=(posts.messages[0].reply_markup.rows[1].buttons[1].data)))
228:         790 LOAD_GLOBAL               2 (sys)
             792 LOAD_ATTR                 3 (stdout)
             794 LOAD_METHOD               4 (write)
             796 LOAD_CONST               44 ('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSkip Captcha...!       \n')
             798 CALL_METHOD               1
             800 POP_TOP
sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSkip Captcha...!       \n')
229:         802 LOAD_GLOBAL               9 (sleep)
             804 LOAD_CONST                8 (2)
             806 CALL_FUNCTION             1
             808 POP_TOP # sleep(2)
         >>  810 POP_BLOCK
             812 JUMP_ABSOLUTE            16 (to 16)
sleep(2)
230:     >>  814 POP_TOP
             816 POP_TOP
             818 POP_TOP # push stack

231:         820 LOAD_GLOBAL               9 (sleep)
             822 LOAD_CONST               45 (3)
             824 CALL_FUNCTION             1
             826 POP_TOP
sleep(3)
232:         828 LOAD_GLOBAL               6 (client)
             830 LOAD_GLOBAL              10 (GetHistoryRequest)
             832 LOAD_GLOBAL               8 (channel_entity)
             834 LOAD_CONST                9 (1)
             836 LOAD_CONST                0 (None)
             838 LOAD_CONST               10 (0)
             840 LOAD_CONST               10 (0)
             842 LOAD_CONST               10 (0)
             844 LOAD_CONST               10 (0)
             846 LOAD_CONST               10 (0)
             848 LOAD_CONST               11 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
             850 CALL_FUNCTION_KW          8 (8 total positional and keyword args)
             852 CALL_FUNCTION             1
             854 STORE_FAST                1 (posts)
posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None,                                                        offset_id=0,
  max_id=0,                                                          min_id=0,
  add_offset=0,
  hash=0))
233:         856 LOAD_FAST                 1 (posts)
             858 LOAD_ATTR                11 (messages)
             860 LOAD_CONST               10 (0)
             862 BINARY_SUBSCR
             864 LOAD_ATTR                12 (message)
             866 STORE_FAST                6 (message)
message = posts.messages[0].message
234:         868 LOAD_FAST                 1 (posts)
             870 LOAD_ATTR                11 (messages)
             872 LOAD_CONST               10 (0)
             874 BINARY_SUBSCR
             876 LOAD_ATTR                12 (message)
             878 LOAD_METHOD              13 (find)
             880 LOAD_CONST               25 ('You must stay')
             882 CALL_METHOD               1
             884 LOAD_CONST               13 (-1)
             886 COMPARE_OP                3 (!=)
             888 EXTENDED_ARG              3 (768)
             890 POP_JUMP_IF_TRUE        916 (to 916) if posts.messages[0].message.find('You must stay')-1
             892 LOAD_FAST                 1 (posts)
             894 LOAD_ATTR                11 (messages)
             896 LOAD_CONST               10 (0)
             898 BINARY_SUBSCR
             900 LOAD_ATTR                12 (message)
             902 LOAD_METHOD              13 (find)
             904 LOAD_CONST               26 ('Please stay on')
             906 CALL_METHOD               1
             908 LOAD_CONST               13 (-1)
             910 COMPARE_OP                3 (!=)
             912 EXTENDED_ARG              3 (768)
             914 POP_JUMP_IF_FALSE      1022 (to 1022) if posts.messages[0].message.find('Please stay on') != -1
if posts.messages[0].message.find('Please stay on') != -1 and posts.messages[0].message.find('You must stay') != -1:
235:     >>  916 LOAD_GLOBAL              25 (re)
             918 LOAD_METHOD              26 (findall)
             920 LOAD_CONST               27 ('([\\d.]*\\d+)')
             922 LOAD_FAST                 6 (message)
             924 CALL_METHOD               2
             926 STORE_FAST                7 (sec)
sec = re.findall('([\\d.]*\\d+)',message)
236:         928 LOAD_GLOBAL              27 (tunggu)
             930 LOAD_GLOBAL              28 (int)
             932 LOAD_FAST                 7 (sec)
             934 LOAD_CONST               10 (0)
             936 BINARY_SUBSCR
             938 CALL_FUNCTION             1
             940 CALL_FUNCTION             1
             942 POP_TOP
tunggu(int(sec[0]))
237:         944 LOAD_GLOBAL               9 (sleep)
             946 LOAD_CONST                9 (1)
             948 CALL_FUNCTION             1
             950 POP_TOP
sleep(1)
238:         952 LOAD_GLOBAL               6 (client)
             954 LOAD_GLOBAL              10 (GetHistoryRequest)
             956 LOAD_GLOBAL               8 (channel_entity)
             958 LOAD_CONST                8 (2)
             960 LOAD_CONST                0 (None)
             962 LOAD_CONST               10 (0)
             964 LOAD_CONST               10 (0)
             966 LOAD_CONST               10 (0)
             968 LOAD_CONST               10 (0)
             970 LOAD_CONST               10 (0)
             972 LOAD_CONST               11 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
             974 CALL_FUNCTION_KW          8 (8 total positional and keyword args)
             976 CALL_FUNCTION             1
             978 STORE_FAST                1 (posts)
posts = client(GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None,
  offset_id=0,
  max_id=0,
  min_id=0,
  add_offset=0,
  hash=0))
239:         980 LOAD_FAST                 1 (posts)
             982 LOAD_ATTR                11 (messages)
             984 LOAD_CONST                9 (1)
             986 BINARY_SUBSCR
             988 LOAD_ATTR                12 (message)
             990 STORE_FAST                8 (messageres)
messageres = posts.messages[1].message
240:         992 LOAD_GLOBAL               9 (sleep)
             994 LOAD_CONST                8 (2)
             996 CALL_FUNCTION             1
             998 POP_TOP
sleep(2)
241:        1000 LOAD_GLOBAL               2 (sys)
            1002 LOAD_ATTR                 3 (stdout)
            1004 LOAD_METHOD               4 (write)
            1006 LOAD_CONST               28 ('\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32m')
            1008 LOAD_FAST                 8 (messageres)
            1010 BINARY_ADD
            1012 LOAD_CONST               29 ('\n')
            1014 BINARY_ADD
            1016 CALL_METHOD               1
            1018 POP_TOP
            1020 JUMP_FORWARD              0 (to 1022)
sys.stdout.write('\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32m' + messageres + '\n')
243:     >> 1022 POP_EXCEPT
            1024 JUMP_ABSOLUTE            16 (to 16)
            1026 END_FINALLY
            1028 JUMP_ABSOLUTE            16 (to 16)
         >> 1030 LOAD_CONST                0 (None)
            1032 RETURN_VALUE

