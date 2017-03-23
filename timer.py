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
    try:
        ct = None
        print "##      Short Cut For Functions \n##  (Pin:i, Pause:p, Continue:c, Stop:t, Restart:r, Reset:e)"
        def prepro():
            global ct
            print ""
            while True:
                print "\033[FSet Count Down Time(XXmXXs)(or Enter for Normal Timing):"," "*10
                ipt=raw_input("\033[FSet Count Down Time(XXmXXs)(or Enter for Normal Timing):")
                ipt = ipt + " "
                pattern = re.compile(r'^(\d+m)?(\d+s)?\s')
                match = pattern.match(ipt)
                if match:
                    ct = TimeCount(ipt)
                    break
        prepro()
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        
        def setpro():
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        def revpro():
            termios.tcsetattr(fd, termios.TCSANOW, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        setpro()
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
                    print '  ','(P)',
                    ct.pause()
                    flag = 1
                elif uin == 'r':
                    flag = 2
                elif uin == 'e':
                    revpro()
                    print ""
                    prepro()
                    setpro()
                    ct.start()
                    flag=0
            except IOError:pass
            if flag == 0:
                ct.showtime()
                if uin == 'i':
                    print '  ','(I)'
            elif flag == 1:
                if uin == 'c':
                    ct.restart()
                    print ''
                    flag = 0
            elif flag == 2:
                ct.start()
                ct.showtime()
                print ' '*5,'(R)',
                flag = 0
    except KeyboardInterrupt:
        pass



