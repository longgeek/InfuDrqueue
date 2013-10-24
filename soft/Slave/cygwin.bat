net use Z: \\172.16.39.248\logs Aa123456 /user:administrator /persistent:yes
net use Y: \\172.16.39.248\tmp Aa123456 /user:administrator /persistent:yes

@echo off

c:
chdir c:\cygwin64\bin
bash --login -i /cygdrive/c/cygwin64/usr/local/drqueue/bin/slave -f
pause
