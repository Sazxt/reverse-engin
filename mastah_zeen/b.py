import marshal,base64,zlib,dis

x = ('\n=gHnV35yOSTyR25ouRyhU3VKl5o73BB0rgQABIAtULIhWT0Dr2dFdTyeAneW\nMAaHn5RQL1blegUVRGhZfnjZ5P7FajGQ8PZnVGR4u52ljdMz9YZZ5pfxyH/z6X/b+Lf/7+t/n+4z\n/kvf9XO/db/+v/X+5/1fyfxH/zyPP/nv+9v7X/1v/xn+Rf/H/zLfe1P/L+dbf338xHe97/z+qv/7\n+d/mf139r/8S/+P/t/qf9v7vcs/f9X8+X9d/mP+0bf/f1X97/9f1X/9/V/Z7f/v/7/8Z8y3/r+Vf\n/v/7+z/tb/qf1H/n/0Pv7/0Pfk3Hgf+s/FfxB2+/8f7zf7P/Xeb5pvdZZbZZu863+5/+5/b5ynXy\n/lPfWLH/f/6fY3/PHQP99736f//jf9+g9P/r+t7///c67Di//n/5Tx1/hf+vc5p/wyz/hlXnXXvt\n8ydJ32nf4f/HL0bXXee/r+39+pUdb96uc9TB85n+3++yb7i6/Nvf76yy3u8v+9P/v+4m8v69l/lv\nve96+deecn/X8++1+xN8f+7L/ze/zv6f69H2Hf1/k9L9jb3f6nfYd/2d/Kfb/Zd79b3Oeax3tPo+\n4uc999/rvd5f8+TY/a/H9+yl3/8D/D3fE7Pj/B3HAxd+5D9kzZ7xQ5uuz5I/65f9v/7hAYd/3937\n9l/uvf9Q493Zf+83e/hdb/RcKQ/b9+9B6HXxP79lf67xgf/r+TChyP5UCcfMte5zP/jff5H9eMou\nmSgPeCvdXShn2H/1X/Yc8+VMJP/w1Y6ib3dLlnfHLUf87fafk8p2/H/v/nfot/f80K6ndY380PQr\noGrUKau/hHZlusb+t+Vv/n9b/qfzPA3U6D75f+v8S6J4t7zqH8w+83/2H2ELv/f/1P+nPsN+TXe5\nv5nd5cMOyP8xf9H2PY5H9NLv9NLv+hTy/6PXV+4ff59l/kv5/Hcn/wu9H9hCCWR/8Df8DmXOVumn\nX2uCyL3/zjdh/4uNyTwy8zPMgu/zi+2Y/PecPmpXg7qP7333iH2l8H+09PsR3APF3vT/Knq0j8Xd\nNG88hdefvGziYcCPNj4GrOfot84ckMzpxmKBeL+q01gLtH5TdaekuPSeLfEPZX75vbca9fXOmfVK\nVOfaxY62HuGewq32pAYGepuvEEjlc+cpxhgLl3fEvGPiMAQx9yKWRxi2pi55aGkP0/bejfzFFL/k\n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'[::-1].decode("base64"))
p = x[::-1].decode("zlib")
co = marshal.loads(p[::-1])