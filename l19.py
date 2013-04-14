'''
Created on 2013-4-14

@author: GunBar
'''
import email
mail=email.message_from_file(open('19.txt'))
for part in mail.walk():
    if part.get_content_maintype()=='audio':
        audio=part.get_payload(decode=1)
        open('19_indian.wav', 'wb').write(audio)
        
import array,wave
wi = wave.open('19_indian.wav','rb')
wo = wave.open('19_indian_inv.wav', 'wb')
print(wi.getparams())
wo.setparams(wi.getparams())
a = array.array('i')
a.fromstring(wi.readframes(wi.getnframes()))
a.byteswap()
wo.writeframes(a.tostring())
wi.close(),wo.close()
if __name__ == '__main__':
    pass