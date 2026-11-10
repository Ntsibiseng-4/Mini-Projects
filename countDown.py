import sys
import time
import sevseg  # Imports our sevseg.py program

secondsLeft = 10

try:
    while True:
        print('\n' * 60)
        
        # Get the hours/minutes/seconds from secondsLeft:
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)
        
        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        
        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()
        
        # Display the digits:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        
        if secondsLeft == 0:
            print()
            print("   * * * * BOOM * * * *   ")
            break
        
        print()
        print("Press Ctrl-C to quit.")
        
        time.sleep(0.5) # Insert a one-second pause
        secondsLeft -= 1

except KeyboardInterrupt:
    print("Countdown!")
    sys.exit()