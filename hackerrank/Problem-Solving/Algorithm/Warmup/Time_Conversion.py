#Problem Link:-https://www.hackerrank.com/challenges/time-conversion/problem


def timeConversion(s):
    hh, mm, ss = s.split(':')
    hh,mm,ssi = int(hh), int(mm), int(ss[:2])
    if "PM" in ss:
        hh = (hh%12) + 12
    if 'AM' in ss:
        hh %= 12
    return ("%02d:%02d:%02d"%(hh,mm,ssi))
        

if __name__ == '__main__':
    s = input()
    res = timeConversion(s)
    print(res)
