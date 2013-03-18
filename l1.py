'''
Created on 2013-3-13

@author: GunBar
'''
src = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result = []
asctab = [ chr(ord('a')+i) for i in range(26)]
transtab = asctab[2:] + asctab[:2]
tab = str.maketrans("".join(asctab),"".join(transtab))
ans = src.translate(tab)
ans = "map".translate(tab)
print(ans)

for char in src:
    if char.isalpha():
        num = ord(char) + 2
        if num > ord('z'):
            num -= 26
            
        result.append(chr(num))
    else:
        result.append(char)
string = "".join(result)
print(string)
     
if __name__ == '__main__':
    pass