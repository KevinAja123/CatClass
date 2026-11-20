t=open('/home/claude/w/tpl.html').read()
A=open('/home/claude/w/assets.json').read()
for m in ('/*ASSETS*/',): assert m in t,m
t=t.replace('/*ASSETS*/','const A='+A+';',1)
open('/home/claude/catholic-classic.html','w').write(t);print('built',len(t)//1024,'KB')
