This is the description file for timer.py

timer.py can work at macOS/Linux.
The function is to timing (normal timing or count down)

Here is the program running information

##      Short Cut For Functions
##  (Pin:i, Pause:p, Continue:c, Stop:t, Restart:r, Reset:e)
Set Count Down Time(XXmXXs)(or Enter for Normal Timing):10s  ## input string '10s' which means counting from 10s
          m  7s 49'       (I)        ## press key i to record the time
          m  6s 21'       (P)        ## press key p, the timer pauses. Then press key c, timer goes on.
          m   s   '                  ## count to zero
Set Count Down Time(XXmXXs)(or Enter for Normal Timing):     ## press Enter and timer starts
          m  9s 91'       (I)        ## press key i to record the time
          m  2s 33'       (I)(R)     ## press key r, timer starts from 0 and the pin the timer.
          m  4s 49'       (P)        
                  '                  ## press key t or Ctrl-c to exit
