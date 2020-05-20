# uncompyle6 version 3.6.6
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: fftool.py
import os, sys, requests
from tqdm import tqdm
import time
lonte = '    \x1b[1;91m    \xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x93 \xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x93 \xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x93 \xe2\x94\x8f     \xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x93\n        \xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81   \xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab \xe2\x94\xa3 \xe2\x94\x81\xe2\x94\x81\xe2\x94\x93 \xe2\x94\x83     \xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\n        \xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x9b \xe2\x94\xbb   \xe2\x94\xbb \xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x9b \xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x9b \xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x9b\n  \x1b[0m<\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81>\n     [\x1b[1;92m+\x1b[0m] Creator : Jhosua Kz         [\x1b[1;92m+\x1b[0m]\n     [\x1b[1;92m+\x1b[0m] Channel : Anonymous Central [\x1b[1;92m+\x1b[0m]\n     [\x1b[1;92m+\x1b[0m] Program : Python            [\x1b[1;92m+\x1b[0m]\n     [\x1b[1;92m+\x1b[0m] Type    : Tools Free Fire   [\x1b[1;92m+\x1b[0m]\n'

def on():
    os.system('cd /sdcard/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/avatar/')
    os.system('rm assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D')
    os.system('clear')
    print '[!] Sedang Memasang ...'
    chunk_size = 5000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/asu/assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/avatar/assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m] Anthena On [\x1b[1;92m\xe2\x9c\x94\x1b[0m]'
    time.sleep(4.5)
    menu()


def off():
    os.system('cd /sdcard/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/avatar/')
    os.system('rm assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D')
    os.system('clear')
    print '[+] Uninstall... '
    chunk_size = 5000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/test/assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/avatar/assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m] Anthena Off [\x1b[1;91m\xe2\x9c\x96\x1b[0m]'
    time.sleep(4.5)
    menu()


def head():
    print '[~] SELECT : '
    print '\n[\x1b[1;91m1\x1b[0m]. Turn (\x1b[1;92mOn\x1b[0m)'
    print '[\x1b[1;91m2\x1b[0m]. Turn (\x1b[1;91mOff\x1b[0m)'
    print '[\x1b[1;91m0\x1b[0m]. \x1b[1;91mBack\x1b[0m'
    xc = raw_input('\n-> ')
    if xc == '1':
        on()
    elif xc == '2':
        off()
    elif xc == '0':
        menu()
    else:
        zx = raw_input('\n\n[\x1b[1;91m!\x1b[0m] \x1b[1;91mWrong\x1b[0m Input... Press \x1b[1;91mEnter\x1b[0m to Back!!!')
        menu()


def handon():
    os.system('cd /sdcard/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/avatar/')
    os.system('rm assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D')
    os.system('clear')
    print '[!] Sedang Memasang ...'
    chunk_size = 5000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/key/assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/avatar/assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m] Anthena Hand On [\x1b[1;92m\xe2\x9c\x94\x1b[0m]'
    time.sleep(4.5)
    menu()


def handoff():
    os.system('cd /sdcard/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/avatar/')
    os.system('rm assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D')
    os.system('clear')
    print '[+] Uninstall... '
    chunk_size = 5000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/test/assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/avatar/assetindexer.P55WLj4N0lYAZDYI48MHMRu0lZ8~3D")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m]nthena Off [\x1b[1;91m\xe2\x9c\x96\x1b[0m]'
    time.sleep(4.5)
    menu()


def hand():
    print '[~] SELECT : '
    print '\n[\x1b[1;91m1\x1b[0m]. Turn (\x1b[1;92mOn\x1b[0m)'
    print '[\x1b[1;91m2\x1b[0m]. Turn (\x1b[1;91mOff\x1b[0m)'
    print '[\x1b[1;91m0\x1b[0m]. \x1b[1;91mBack\x1b[0m'
    fucek = raw_input('\n\xe2\x9e\x9b ')
    if fucek == '1':
        handon()
    elif fucek == '2':
        handoff()
    elif fucek == '0':
        menu()
    else:
        zx = raw_input('\n\n[\x1b[1;91m!\x1b[0m] \x1b[1;91mWrong\x1b[0m Input... Press \x1b[1;91mEnter\x1b[0m to Back!!!')
        menu()


def random():
    os.system('clear')
    print lonte
    print '\n[\x1b[1;91m!\x1b[0m] Please installed the Free Fire Support ID'
    print '[\x1b[1;92m+\x1b[0m] Enter 15 numbers randomly'
    jhosua = raw_input('\n[\x1b[1;92m>\x1b[0m] Enter Number : \x1b[1;93m')
    time.sleep(5)
    gago = open('/sdcard/ffid.txt', 'w')
    gago.write(jhosua)
    gago.close()
    print '\x1b[0m[>] Bypass Imei Succes [\x1b[1;91m!\x1b[0m]'
    time.sleep(4.5)
    menu()


def fake():
    os.system('clear')
    print lonte
    print '[\x1b[1;92m1\x1b[0m]. Create Imei'
    print '[\x1b[1;91m0\x1b[0m]. \x1b[1;91mBack\x1b[0m'
    kz = raw_input('\n\xe2\x9e\x9b ')
    if kz == '1':
        random()
    if kz == '0':
        menu()
    else:
        zx = raw_input('\n\n[\x1b[1;91m!\x1b[0m] \x1b[1;91mWrong\x1b[0m Input... Press \x1b[1;91mEnter\x1b[0m to Back!!!')
        menu()


def headshot():
    os.system('clear')
    print '[+] Install... '
    time.sleep(3)
    os.system('cd auto')
    os.system('cp optionalab_01.GfmkTHeehfGq5K6L4YL2Av7YlR27~2D /sdcard/Android/data/com.dts.freefireth/files/contentcache/Optional/android/optionallocres/gameassetbundles/')
    os.system('clear')
    print lonte
    print '[+] Config Auto Headshot [\x1b[1;92m\xe2\x9c\x94\x1b[0m]'
    time.sleep(4.5)
    menu()


def china():
    os.system('clear')
    print '[+]. Install...'
    chunk_size = 50000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/setan/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/ui/background/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m] Success [\x1b[1;92m\xe2\x9c\x94\x1b[0m]'
    time.sleep(4.5)
    menu()


def akatsuki():
    os.system('clear')
    print '[+] Install... '
    chunk_size = 5000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/Santuy/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/ui/background/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m] Success [\x1b[1;92m\xe2\x9c\x94\x1b[0m]'


def mikasa():
    os.system('clear')
    print '[+] Install... '
    chunk_size = 5000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/asu/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/ui/background/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m] Success [\x1b[1;92m\xe2\x9c\x94\x1b[0m]'
    time.sleep(4.5)
    menu()


def grafity():
    os.system('clear')
    print '[+] Install..  '
    chunk_size = 5000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/key/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/ui/background/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m] Success [\x1b[1;92m\xe2\x9c\x94\x1b[0m]'
    time.sleep(4.5)
    menu()


def konoha():
    os.system('clear')
    print '[+] Install... '
    chunk_size = 5000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/hello/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/ui/background/lobby_snowbg_halloween.2n65YN5HAOCfUGBrwme2S8dqvK4~3D")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m] Success [\x1b[1;92m\xe2\x9c\x94\x1b[0m]'
    time.sleep(4.5)
    menu()


def fix():
    os.system('clear')
    print lonte
    print '[\x1b[1;91m1\x1b[0m]. Background China'
    print '[\x1b[1;91m2\x1b[0m]. Background Akatsuki'
    print '[\x1b[1;91m3\x1b[0m]. Background Mikasa'
    print '[\x1b[1;91m4\x1b[0m]. Background FF Graffity'
    print '[\x1b[1;91m5\x1b[0m]. Background Konoha'
    print '[\x1b[1;91m0\x1b[0m]. \x1b[1;91mBack\x1b[0m'
    jancok = raw_input('\n\xe2\x9e\x9b ')
    if jancok == '1':
        china()
    elif jancok == '2':
        akatsuki()
    elif jancok == '3':
        mikasa()
    elif jancok == '4':
        grafity()
    elif jancok == '5':
        konoha()
    elif jancok == '0':
        menu()
    else:
        zx = raw_input('\n\n[\x1b[1;91m!\x1b[0m] \x1b[1;91mWrong\x1b[0m Input... Press \x1b[1;91mEnter\x1b[0m to Back!!!')
        menu()


def hoki():
    os.system('clear')
    print '[+] Install... '
    chunk_size = 5000
    url = 'https://github.com/B4TAK/HelloQimak/blob/master/hello/script1.spinhoki.file?raw=true'
    r = requests.get(url, stream=True)
    size = int(r.headers['content-length'])
    filename = url.split('/')[(-1)]
    with open(filename, 'wb') as (f):
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=size / chunk_size, unit=' KB'):
            f.write(data)

    os.system("mv 'script1.spinhoki.file?raw=true' /storage/emulated/0/Android/data/com.dts.freefireth/files/contentcache/Compulsory/android/gameassetbundles/ui/script1.spinhoki.file")
    os.system('clear')
    print lonte
    print '[\x1b[1;92m+\x1b[0m] Script Spin Hoki Active[\x1b[1;92m\xe2\x9c\x94\x1b[0m]'
    time.sleep(4.5)
    menu()


def menu():
    os.system('am start https://www.youtube.com/c/AnonymousCentral')
    os.system('clear')
    print lonte
    print '\x1b[1;95m-\xe2\x9e\x9b\x1b[0m [\x1b[1;91m1\x1b[0m]. Anthena Head'
    print '\x1b[1;95m-\xe2\x9e\x9b\x1b[0m [\x1b[1;91m2\x1b[0m]. Anthena Hand'
    print '\x1b[1;95m-\xe2\x9e\x9b\x1b[0m [\x1b[1;91m3\x1b[0m]. Bypass Imei(\x1b[1;93mUnbanned\x1b[0m)'
    print '\x1b[1;95m-\xe2\x9e\x9b\x1b[0m [\x1b[1;91m4\x1b[0m]. Config Auto Headshot (\x1b[1;91m75%\x1b[0m)'
    print '\x1b[1;95m-\xe2\x9e\x9b\x1b[0m [\x1b[1;91m5\x1b[0m]. Change Background Free Fire'
    print '\x1b[1;95m-\xe2\x9e\x9b\x1b[0m [\x1b[1;91m6\x1b[0m]. Script Spin Hoki'
    garox = raw_input('\n\xe2\x9e\x9b ')
    if garox == '1':
        head()
    elif garox == '2':
        hand()
    elif garox == '3':
        fake()
    elif garox == '4':
        headshot()
    elif garox == '5':
        fix()
    elif garox == '6':
        hoki()
    else:
        zx = raw_input('\n\n[\x1b[1;91m!\x1b[0m] \x1b[1;91mWrong\x1b[0m Input... Press \x1b[1;91mEnter\x1b[0m to Back!!!')
        menu()


menu()
