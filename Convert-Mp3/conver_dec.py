# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:23:16) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <script>
try:
    import requests, subprocess as a, urllib, sys, time as molor, re, logging, mechanize
except ImportError as bebek:
    print bebek
    sys.exit
else:

    class lagu:
        url = 'http://www.convertmp3.io/'

        def __init__(self, link):
            try:
                self.br = mechanize.Browser()
                self.br.set_handle_robots(False)
                self.br.set_handle_referer(True)
                self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0')]
                self.br._factory.is_html = True
                self.br.open(lagu.url)
                self.br.select_form(nr=0)
                self.br.form['video'] = link
                self.br.submit()
                self.get = self.br.geturl()
                self.rekues = requests.get(self.get)
                self.reg = re.findall('href="/download(.*?)">', self.rekues.text)
                self.cek = re.findall('<title>(.*?)</title>', self.rekues.text)
                self.title = re.findall('id="videoTitle">(.*?)</span>', self.rekues.text)
            except Exception as a:
                logging.error(a)
                sys.exit

        def donlot(self, output):
            try:
                print '(INFO) : Tunggu...'
                logging.warning((' Title Music : {}').format(self.title[0]))
                if 'Your MP3 Is Ready' in self.cek[0]:
                    print 'STATUS | Loading For Download'
                    self.gut = requests.get(('http://www.convertmp3.io/download{}').format(self.reg[0]))
                    self.bat = urllib.urlretrieve(self.gut.url, output + '.mp3')
                    print ('STATUS | (S)uccess!!\nOUTPUT | storage/emulated/0/{}').format(output + '.mp3')
                    a.call('mv ' + output + '.mp3 /sdcard', shell=True)
                elif 'No video was found' in self.title[0]:
                    logging.error('(T)idak Di Temukan')
                    sys.exit()
                else:
                    logging.error('(A)borted!')
                    sys.exit()
            except Exception as sayang:
                logging.error(sayang)
                sys.exit()


    def banner():
        baner = "\x1b[31;1m  ___                     _       __  __      ____\n\x1b[31;1m / __|___ _ ___ _____ _ _| |_ ___|  \\/  |_ __|__ /\n\x1b[31;1m| (__/ _ \\ ' \\ V / -_) '_|  _|___| |\\/| | '_ \\|_ \\ \n\x1b[0;37m \\___\\___/_||_\\_/\\___|_|  \\__|   |_|  |_| .__/___/\n\x1b[0;37m                                        |_|\n\x1b[30;1m<<|=============================================|>>\n\x1b[31;1m>> Coded By : Febry [ xNot_Found ]\n\x1b[32;1m>> Contact  : +62823-8637-2115\n\x1b[33;1m>> Email    : febryafriansyah@programmer.net\n\x1b[34;1m>> Website  : http://hatakecnk.noads.biz\n\x1b[37;1m>> Github   : https://github.com/hatakecnk\n\x1b[30;1m<<|=============================================|>>"
        print baner


    try:
        if __name__ == '__main__':
            a.call('clear', shell=True)
            banner()
            syes = raw_input('\x1b[36;1mLink Youtube : \x1b[0;37m')
            out = raw_input('\x1b[36;1mNama Lagu : \x1b[0;37m')
            bang = lagu(syes)
            bang.donlot(out)
    except KeyboardInterrupt:
        print '(CTRL+C) Detected, See You'
        sys.exit()
    except EOFError:
        print '(CTRL+D) Detected, See You'
        sys.exit()