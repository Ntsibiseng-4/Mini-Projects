def getSevSegStr(number, minWidth=0):
    number = str(number).zfill(minWidth)
    rows = ['', '', '']
    for n in number:
        if n == '0':
          rows[0] += ' _ '
          rows[1] += '| |'
          rows[2] += '|_|'
        elif n == '1':
            rows[0] += ' '
            rows[1] += ' |'
            rows[2] += ' |'
        elif n == '2':
            rows[0] += ' _ '
            rows[1] += ' _|'
            rows[2] += '|_ '
        elif n == '3':
            rows[0] += ' _ '
            rows[1] += ' _|'
            rows[2] += ' _|'
        elif n == '4':
            rows[0] += ' '
            rows[1] += '|_|'
            rows[2] += ' |'
        elif n == '5':
            rows[0] += ' _ '
            rows[1] += '|_ '
            rows[2] += ' _|'
        elif n == '6':
            rows[0] += ' _ '
            rows[1] += '|_ '
            rows[2] += '|_|'
        elif n == '7':
            rows[0] += '_ '
            rows[1] += ' |'
            rows[2] += ' |'
        elif n == '8':
            rows[0] += ' _ '
            rows[1] += '|_|'
            rows[2] += '|_|'
        elif n == '9':
            rows[0] += ' _ '
            rows[1] += '|_|'
            rows[2] += ' _|'
        else: 
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
            
    #Add space between digits
    rows[0] += ' '
    rows[1] += ' '
    rows[2] += ' '
    
    return '\n'.join(rows)
    