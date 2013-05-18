'''
Created on 2013-5-19

@author: GunBar
'''
import zlib,bz2
st=open('21_package.pack').read()
log=''
log_len=len(log)
while True:
<<<<<<< HEAD
    try: #zlib
        st=zlib.decompress(st)
        log+=' '
    except:
        try: #bzip2
            st=bz2.decompress(st)
            log+='#'
        except: #reverse
            if log_len==len(log): break
            st=st[::-1]
            print log[log_len:]
            log_len=len(log)
=======
    try: #zlib
        st=zlib.decompress(st)
        log+=' '
    except:
        try: #bzip2
            st=bz2.decompress(st)
            log+='#'
        except: #reverse
            if log_len==len(log): break
            st=st[::-1]
            print log[log_len:]
            log_len=len(log)
>>>>>>> b69110a797f3503ae3cb3e3901ff5a257c464033
open('21_package.unpack','wb').write(st)