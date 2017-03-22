#!/usr/bin/python
import time as t
import threading
class TimeCount:
    def __init__(self, ceiling=""):
        """This is timer, and ceiling != 0 means reversed order

        :ceiling: for count down, the total time
        :returns: nothing

        """
        self.begin=0
        self.temp =0
        self.ceiling=0
        if ceiling=="":
            self.ceiling=0
        if 'm' in ceiling:
            self.ceiling += int(ceiling[:ceiling.index('m')]) * 60 *100
            ceiling = ceiling[ceiling.index('m')+1:]
        if 's' in ceiling:
            self.ceiling += int(ceiling[:ceiling.index('s')]) * 100
        pass
    
    def start(self):
        self.begin = round(t.time() * 100)
        
    def showtime(self):
        """TODO: Docstring for showtime.
        :returns: TODO"""
        self.temp = round(t.time()*100)
        m,s,ms = 0,0,0
        if self.ceiling==0:
            temp = self.temp - self.begin
            ms = temp % 100
            s = (temp/100)%60
            m = temp/6000
        else:
            temp = self.ceiling + self.begin - self.temp
            temp = temp > 0 and temp or 0
            ms = temp % 100
            s = (temp/100)%60
            m = temp/6000
        print '\r','%10.dm%3.ds%3.d\'   '%(m,s,ms),
        pass
    
    def pause(self):
        self.temp = round(t.time()*100)
        
    def restart(self):
        nt = round(t.time()*100)
        self.begin = self.begin + (nt - self.temp)




if __name__ == "__main__":
    import termios, fcntl, sys, os, re

    while True:
        ipt=raw_input("\rSet Count Down Time(XXmXXs)(or Enter for Normal Timing):")
        pattern = re.compile(r'^(\d+m)?(\d+s)?')
        match = pattern.match(ipt)
        if match:
            ct = TimeCount(ipt)
            break

    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    ct.start()
    flag = 0
    while True:
        t.sleep(0.005)
        uin = ''
        try:
            uin = sys.stdin.read(1)
            if uin == "t":
                break
            elif uin == 'p':
                ct.showtime()
                ct.pause()
                print '#(c)ontinue/(r)estart/s(t)op#',
                flag = 1
            elif uin == 'r':
                flag = 2
        except IOError:pass
        if flag == 0:
            ct.showtime()
            print '#(r)estart/s(t)op/(p)ause#',
        elif flag == 1:
            if uin == 'c':
                ct.restart()
                print ''
                flag = 0
        elif flag == 2:
            ct.start()
            ct.showtime()
            flag = 0




