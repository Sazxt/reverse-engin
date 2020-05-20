# decompile By sazxt
# Python bytecode 3.8 (3413)
# Error Selector Visit instruction at offset 806_0
# filenames : <zen_ezz>
from telethon import TelegramClient, sync, events, errors
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json, re, sys, os, requests, time, random, colorama, threading, itertools
from bs4 import BeautifulSoup
with open('cfg.json', 'r') as fh:
    json_str = fh.read()
    json_value = json.loads(json_str)
    ltcwallet = json_value['walletltc']
    dogewallet = json_value['walletdoge']
    zecwallet = json_value['walletzec']
    bchwallet = json_value['walletbch']
    btcwallet = json_value['walletbtc']
print('\n\n\x1b[1;32mclear')
print('\x1b[1;35mBot nuyul bot telegram')
time.sleep(3)
print(colorama.ansi.clear_screen())
done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        else:
            sys.stdout.write('\x1b[1;36m\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
    else:
        sys.stdout.write('\rDone!     ')


t = threading.Thread(target=animate)
t.start()
time.sleep(4)
done = True
lines = [
 ' Jangan lupa bahagia, jika ada bugs \n          lapor » anthesphong1998@gmail.com !']
for line in lines:
    for c in line:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    else:
        print('')
        sleep(3)

else:
    c = requests.Session()
    if not os.path.exists('session'):
        os.makedirs('session')
    if len(sys.argv) < 2:
        print('\n\n\n\x1b[1;32mUsage : python bot.py +62 doge')
        sys.exit()
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    api_id = 800812
    api_hash = 'db55ad67a98df35667ca788b97f771f5'
    phone_number = sys.argv[1]
    pilihan = sys.argv[2]

    def tunggu(x):
        sys.stdout.write('\r')
        sys.stdout.write('                                                               ')
        for remaining in range(x, 0, -1):
            sys.stdout.write('\r')
            sys.stdout.write('\x1b[1;30m[\x1b[1;32m+\x1b[1;30m]\x1b[1;0m{:2d} \x1b[1;32mseconds remaining'.format(remaining))
            sys.stdout.flush()
            sleep(1)


    def mengetik(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random() * 0.1)


    client = TelegramClient('session/' + phone_number, api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone_number)
            me = client.sign_in(phone_number, input('\n\n\n\x1b[1;0mEnter Your Code : '))
        except SessionPasswordNeededError:
            passw = input('\x1b[1;0mYour 2fa Password : ')
            me = client.start(phone_number, passw)

    myself = client.get_me()
    os.system('clear')
    banner = '\x1b[1;35m\n                                              \neeeee  eeeee e    e eeee eeeee       e  eeeee \n8   8  8   8 8    8 8    "   8       8  8   8 \n8eee8e 8eee8 8eeee8 8eee eeee8       8e 8e  8 \n88   8 88  8   88   88   88          88 88  8 \n88   8 88  8   88   88ee 88ee8       88 88ee8 \n                               eeeee\n\x1b[1;36m=============================================\n\x1b[1;32m ~ anthesphong1998@gmail.com (+6282195663814)   \n\x1b[1;36m=============================================\n'
    r = requests.get('https://ipinfo.io/json')
    data = json.loads(r.text)
    text = '\x1b[1;35mYOUR LOCATION\t: \x1b[1;36m{1}\t({2})\n\x1b[1;35mYOUR OWN IP\t: \x1b[1;36m{0}'
    text = text.format(data.get('ip', '[NO DATA]'), data.get('region', '[NO DATA]'), data.get('country', '[NO DATA]'))
    print(banner)
    mengetik(text)
    mengetik(f"\x1b[1;35mWELCOME         :\x1b[1;36m {myself.first_name}\n\x1b[1;35mYOUR NUMBER     :\x1b[1;36m {phone_number}")
    try:
        try:
            if pilihan == 'doge':
                channel_entity = client.get_entity('@Dogecoin_click_bot')
                channel_username = '@Dogecoin_click_bot'
                currency = 'DOGE'
                dompet = dogewallet
            if pilihan == 'ltc':
                channel_entity = client.get_entity('@Litecoin_click_bot')
                channel_username = '@Litecoin_click_bot'
                currency = 'LTC'
                dompet = ltcwallet
            if pilihan == 'zec':
                channel_entity = client.get_entity('@Zcash_click_bot')
                channel_username = '@Zcash_click_bot'
                currency = 'ZEC'
                dompet = zecwallet
            if pilihan == 'bch':
                channel_entity = client.get_entity('@BCH_clickbot')
                channel_username = '@BCH_clickbot'
                currency = 'BCH'
                dompet = bchwallet
            if pilihan == 'btc':
                channel_entity = client.get_entity('@BitcoinClick_bot')
                channel_username = '@BitcoinClick_bot'
                currency = 'BTC'
                dompet = btcwallet

            def withdraw():
                mengetik('\x1b[1;36m============================= \x1b[1;32m(WITHDRAW BALANCE)\n')
                for i in range(5000000):
                    sys.stdout.write('\r')
                    sys.stdout.write('                                                              ')
                    sys.stdout.write('\r')
                    sys.stdout.write('\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mTrying to withdraw')
                    sys.stdout.flush()
                    client.send_message(entity=channel_entity, message='ðŸ’° Balance')
                    sleep(1)
                    posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    message = posts.messages[0].message
                    doge_msg = message
                    doge_bal = doge_msg.strip('Available balance: ')
                    sleep(1)
                    client.send_message(entity=channel_entity, message='/withdraw')
                    sleep(1)
                    posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    if posts.messages[0].message.find('Your balance is too small to') != -1:
                        sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33m{doge_msg}\n")
                        sys.exit()
                    else:
                        client.send_message(entity=channel_entity, message=dompet)
                        sleep(1)
                        client.send_message(entity=channel_entity, message=doge_msg)
                        sleep(1)
                        client.send_message(entity=channel_entity, message='/Confirm')
                        sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32mSucces withdraw {doge_bal} {channel_username}\n")
                        sys.exit()
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
                            sys.stdout.write('\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mVisit ' + url)
                            sys.stdout.flush()
                            id = posts.messages[0].id
                            r = c.get(url, headers=ua, timeout=15,allow_redirects=True)
                            soup = BeautifulSoup(r.content, 'html.parser')
                            if soup.find("div",id='headbar') is None and soup.find("div",class_='g-recaptcha') is None:
                                sleep(2)
                                posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                                message = posts.messages[0].message
                                if posts.messages[0].message.find('Please stay on') != -1 and posts.messages[0].message.find('You must stay') != -1:
                                    sec = re.findall('([\\d.]*\\d+)',message)
                                    tunggu(int(sec[0]))
                                    sleep(1)
                                    posts = client(GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                                    messageres = posts.messages[1].message
                                    sleep(2)
                                    sys.stdout.write('\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32m' + messageres + '\n')
                                elif soup.find('div', id='headbar') is not None:
                                    for dat in soup.find_all("div",class_='container-fluid'):
                                        code = dat.get('data-code')
                                        timer = dat.get('data-timer')
                                        tokena = dat.get('data-token')
                                        tunggu(int(timer))
                                        r = c.post('https://dogeclick.com/reward', data={'code':code,  'token':tokena}, headers=ua, timeout=15, allow_redirects=True)
                                        js = json.loads(r.text)
                                sys.stdout.write('\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32mYou earned ' + js['reward'] + f" {currency} for visiting a site!\n")
                                sys.stdout.write('\r')
                                sys.stdout.write('                                                                ')
                                sys.stdout.write('\r')
                                sys.stdout.write('\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mCaptcha Detected')
                                sys.stdout.flush()
                            sleep(2)
                            client(GetBotCallbackAnswerRequest(channel_username, id, data=(posts.messages[0].reply_markup.rows[1].buttons[1].data)))
                            sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSkip Captcha...!       \n')
                            sleep(2)
                            sleep(3)
                            posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                            message = posts.messages[0].message
                            if posts.messages[0].message.find('Please stay on') != -1 and posts.messages[0].message.find('You must stay') != -1:
                                sec = re.findall('([\\d.]*\\d+)',message)
                                tunggu(int(sec[0]))
                                sleep(1)
                                posts = client(GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None,  offset_id=0,  max_id=0,  min_id=0,  add_offset=0,  hash=0))
                                messageres = posts.messages[1].message
                                sleep(2)
                                sys.stdout.write('\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32m' + messageres + '\n')
                        except:
                            pass

            def join():
                mengetik('\x1b[1;36m================================== \x1b[1;32m(JOINING BOT)\n')
                for i in range(10):
                    sys.stdout.write('\r')
                    sys.stdout.write('                                                              ')
                    sys.stdout.write('\r')
                    sys.stdout.write('\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mTrying to join channel')
                    sys.stdout.flush()
                    client.send_message(entity=channel_entity, message='ðŸ“£ Join chats')
                    sleep(3)
                    posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    messag = posts.messages[0].message
                    msg_id = posts.messages[0].id
                    if posts.messages[0].message.find('Sorry, there are no new ads available') != -1:
                        sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSorry, there are no new ads available. \x1a\n\n')
                        visit()
                    else:
                        bot = re.search('You must join (.*?) to earn', messag).group(1)
                        channel_name = client.get_entity(bot)
                        try:
                            client(JoinChannelRequest(channel_name))
                            sleep(2)
                            client(GetBotCallbackAnswerRequest(channel_entity,
                              msg_id,
                              data=(posts.messages[0].reply_markup.rows[0].buttons[1].data)))
                            sys.stdout.write('\r')
                            sys.stdout.write('                                                                ')
                            sys.stdout.write('\r')
                            sys.stdout.write(f"\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mJoining bot {bot}")
                            sys.stdout.flush()
                            sleep(5)
                            posts_ = client(GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                            id = posts_.messages[1].id
                            msg = posts_.messages[1].message
                            musang = re.findall('([\\d.]*\\d+)', msg)
                            if posts_.messages[0].message.find('cannot find you') != -1:
                                client(GetBotCallbackAnswerRequest(channel_entity,
                                  id,
                                  data=(posts_.messages[1].reply_markup.rows[1].buttons[1].data)))
                                sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSkip task...!                                                            \n')
                                sleep(5)
                            else:
                                sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32mYou earned after {musang[0]} hours for joining bot!\n")
                                sleep(5)
                        except Exception:
                            client(GetBotCallbackAnswerRequest(channel_entity,
                              msg_id,
                              data=(posts.messages[0].reply_markup.rows[1].buttons[1].data)))
                        except errors.FloodWaitError as e:
                            try:
                                sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33m{channel_username} must sleep {e.seconds} seconds\n\n")
                                visit()
                            finally:
                                e = None
                                del e

                        except Exception:
                            client(GetBotCallbackAnswerRequest(channel_entity,
                              msg_id,
                              data=(posts.messages[0].reply_markup.rows[1].buttons[1].data)))

                else:
                    sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSorry, there are no new ads available. \x1a\n\n')
                    visit()


            def mesg():
                mengetik('\x1b[1;36m================================ \x1b[1;32m(MESSAGING BOT)\n')
                for i in range(5000000):
                    sys.stdout.write('\r')
                    sys.stdout.write('                                                              ')
                    sys.stdout.write('\r')
                    sys.stdout.write('\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33mTrying to messaging channel')
                    sys.stdout.flush()
                    client.send_message(entity=channel_entity, message='ðŸ¤– Message bots')
                    sleep(2)
                    posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    if posts.messages[0].message.find('Sorry, there are no new ads available') != -1:
                        sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSorry, there are no new ads available. \x1a\n\n')
                        join()
                    else:
                        try:
                            url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                            r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
                            soup = BeautifulSoup(r.content, 'html.parser')
                            dat = soup.find('div', class_='tgme_page_extra')
                            bot = dat.text.strip()
                            channel_name = client.get_entity(bot)
                            sys.stdout.write('\r')
                            sys.stdout.write('                                                                ')
                            sys.stdout.write('\r')
                            sys.stdout.write(f"\x1b[1;30m[\x1b[1;33m-\x1b[1;30m] \x1b[1;33mMessaging bot {bot}")
                            sys.stdout.flush()
                            sleep(2)
                            client.send_message(entity=channel_name, message='/start')
                            sleep(2)
                            posts_ = client(GetHistoryRequest(peer=channel_name, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                            msg_id = posts_.messages[0].id
                            client.forward_messages(channel_entity, msg_id, channel_name)
                            sleep(2)
                            posts__ = client(GetHistoryRequest(peer=channel_entity, limit=3, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                            msg = posts__.messages[1].message
                            msgc = posts__.messages[0].message
                            id = posts__.messages[2].id
                            if posts__.messages[0].message.find('not a valid') != -1:
                                client(GetBotCallbackAnswerRequest(channel_entity,
                                  id,
                                  data=(posts__.messages[2].reply_markup.rows[1].buttons[1].data)))
                                sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSkip task...!                                                            \n')
                                sleep(2)
                            else:
                                sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;32m+\x1b[1;30m] \x1b[1;32m{msg}\n")
                                sleep(2)
                        except Exception:
                            sys.stdout.write('\r\x1b[1;30m[\x1b[1;31mx\x1b[1;30m] \x1b[1;31mSorry, there are no new ads available. \x1a\n\n')
                            join()


            try:
                mengetik(f"\x1b[1;35mBOT             : \x1b[1;36m{channel_username}\n")
                mesg()
            except Exception:
                mengetik('\x1b[1;35mBOT             : \x1b[1;36m\n')
                mesg()

        except errors.FloodWaitError as e:
            try:
                sys.stdout.write(f"\r\x1b[1;30m[\x1b[1;33m!\x1b[1;30m] \x1b[1;33maccount must sleep {e.seconds} seconds\n")
            finally:
                e = None
                del e

    finally:
        client.disconnect()
# 
# decompile failed
