import marshal,disas
x = marshal.loads('c\x01\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00C\x00\x00\x00s\x81\x00\x00\x00d\x01\x00|\x00\x00_\x00\x00d\x02\x00|\x00\x00_\x01\x00xc\x00t\x02\x00|\x00\x00j\x00\x00\x83\x01\x00D]R\x00}\x01\x00t\x03\x00j\x04\x00d\x03\x00\x83\x01\x00\x01|\x00\x00\x04j\x01\x00d\x04\x007\x02_\x01\x00qJ\x00d\xa6\x86t\x05\x00j\x06\x00j\x07\x00d\x05\x00t\x08\x00|\x00\x00j\x01\x00\x83\x01\x00\x17\x83\x01\x00\x01t\x05\x00j\x06\x00j\t\x00\x83\x00\x00\x01q"\x00Wd\x06\x00GHd\x00\x00S(\x07\x00\x00\x00Ni\n\x00\x00\x00i\x00\x00\x00\x00g\x00\x00\x00\x00\x00\x00\xe0?i\x01\x00\x00\x00s/\x00\x00\x00\r\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m Tunggu Sampai s/\x00\x00\x00\n\x1b[1;34m[\x1b[1;37m*\x1b[1;34m]\x1b[1;37m INI ISINYA !!!(\n\x00\x00\x00t\x05\x00\x00\x00angkat\x04\x00\x00\x00apest\x05\x00\x00\x00ranget\x04\x00\x00\x00timet\x05\x00\x00\x00sleept\x03\x00\x00\x00syst\x06\x00\x00\x00stdoutt\x05\x00\x00\x00writet\x03\x00\x00\x00strt\x05\x00\x00\x00flush(\x02\x00\x00\x00t\x04\x00\x00\x00selft\x01\x00\x00\x00i(\x00\x00\x00\x00(\x00\x00\x00\x00s\x06\x00\x00\x00tes.pys\x08\x00\x00\x00__init__\x04\x00\x00\x00s\x10\x00\x00\x00\x00\x01\t\x01\t\x01\x16\x01\r\x01\x0f\x01#\x01\x11\x01')
disas.dis(x)