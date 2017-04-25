def ch6_exe1():
    mystr = 'X-DSPAM-Confidence: 0.8475'
    colonposition = mystr.find(':')
    mystr = mystr[colonposition+1:]
    print float(mystr)


ch6_exe1()