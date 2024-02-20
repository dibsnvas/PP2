import re
string = input()
l = re.compile('ab*?')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')
