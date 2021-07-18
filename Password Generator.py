#Password Generator
import secrets
asciilist = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!\"#¤%&/()=?+\`¨^~|§{[]}´€$£@")
passwd = list()
while len(passwd) < 20:
    passwd.append(secrets.choice(asciilist))
print(''.join(map(str, passwd)))