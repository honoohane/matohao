import re
import os


def zhuanyigepu(pumian, shuchu):
    def measureoutput(time):
        strr = str(time)
        spa = (8 - len(strr)) * " "
        ff.write(spa)
        ff.write(strr)
        ff.write(',MEASURE ,       0')
        ff.write('\n')

    def hakuoutput(time):
        strr = str(time)
        spa = (8 - len(strr)) * " "
        ff.write(spa)
        ff.write(strr)
        ff.write(',HAKU    ,       0')
        ff.write('\n')

    def endoutput(time):
        strr = str(time)
        spa = (8 - len(strr)) * " "
        ff.write(spa)
        ff.write(strr)
        ff.write(',END     ,       0')
        ff.write('\n')

    def playoutput(time, canshu):
        strr = str(time)
        spa = (8 - len(strr)) * " "
        strrr = str(canshu)
        spaa = (8 - len(strrr)) * " "
        ff.write(spa)
        ff.write(strr)
        ff.write(',PLAY    ,')
        ff.write(spaa)
        ff.write(strrr)
        ff.write('\n')

    def longoutput(time, canshu):
        strr = str(time)
        spa = (8 - len(strr)) * " "
        strrr = str(canshu)
        spaa = (8 - len(strrr)) * " "
        ff.write(spa)
        ff.write(strr)
        ff.write(',LONG    ,')
        ff.write(spaa)
        ff.write(strrr)
        ff.write('\n')

    def tempooutput(time, canshu):
        strr = str(time)
        spa = (8 - len(strr)) * " "
        strrr = str(canshu)
        spaa = (8 - len(strrr)) * " "
        ff.write(spa)
        ff.write(strr)
        ff.write(',TEMPO   ,')
        ff.write(spaa)
        ff.write(strrr)
        ff.write('\n')

    def calculatetime(a):
        b = list(eval(a))
        return cumulatetime + ((b[0] - cumulatejie) + b[1] / b[2]) * unittime

    def longprocess(a):
        lastone = str(hex(int(a[4])))
        last1 = lastone[-1]
        t = int(a[4]) - int(a[5])
        if t == 1:
            last2 = '6'
        elif t == 2:
            last2 = 'a'
        elif t == 3:
            last2 = 'e'
        elif t == 4:
            last2 = '4'
        elif t == 8:
            last2 = '8'
        elif t == 12:
            last2 = 'c'
        elif t == -1:
            last2 = '7'
        elif t == -2:
            last2 = 'b'
        elif t == -3:
            last2 = 'f'
        elif t == -4:
            last2 = '5'
        elif t == -8:
            last2 = '9'
        elif t == -12:
            last2 = 'd'
        timediff = int(calculatetime(a[3])) - int(calculatetime(a[2]))
        first = str(hex(timediff))
        first1 = first[2:]
        total = first1 + last2 + last1
        return int(total, 16)

    f = open(pumian, encoding='UTF-8-sig')
    data = f.readlines()
    ff = open(shuchu, "w")
    bpm = []
    xiaojiebianhua = 0
    offsetenable = 1
    twosecondoffset = 1
    for i in data:
        print(i)
        if i.find('title') != -1:
            t = re.findall(r'\".*?\"', i)
            title = t[1]
            t = title.lstrip('"')
            title = t.rstrip('"')
        if i.find('artist') != -1:
            t = re.findall(r'\".*?\"', i)
            artist = t[1]
            t = artist.lstrip('"')
            artist = t.rstrip('"')
        if i.find('bpm') != -1:
            t = re.findall(r': .*?$', i)
            a = t[0]
            b = a.lstrip(': ')
            a = b.rstrip(',')
            b = a
            bpm.append(b)
        if i.find('offset') != -1:
            t = re.findall(r': .*?$', i)
            a = t[0]
            b = a.lstrip(': ')
            c = b.rstrip(',')
            offset = c
        if i.find('sound') != -1:
            t = re.findall(r'\".*?\"', i)
            sound = t[1]
    measureoutput(0)
    hakuoutput(0)
    tempooutput(0, int(60000000 / float(bpm[0])))
    songlength = 129
    offset1 = (float(offset) * offsetenable - 2000 * twosecondoffset) / 1000 * 300
    t = 0
    tt = 0
    for i in range(len(data)):
        a = '    "time": ['
        b = '    "note": ['
        if data[i].find(a) != -1:
            t = i
        if data[i].find(b) != -1:
            tt = i
    qian = []
    hou = []
    for i in range(t, tt):
        if data[i].find('        {') != -1:
            qian.append(i)
        if data[i].find('        }') != -1:
            hou.append(i)
    bpmchange = []
    for i in range(len(hou)):
        a = data[qian[i] + 1].lstrip('            "beat": [')
        aa = a.rstrip('],\n')
        aaa = list(eval(aa))
        b = data[hou[i] - 1].lstrip('            "bpm": ')
        bb = b.rstrip('\n')
        k = []
        k.append('tempo')
        k.append(aaa[0])
        k.append(aaa)
        k.append(bb)
        bpmchange.append(k)
    t = 0
    tt = 0
    for i in range(len(data)):
        a = '    "note": ['
        b = '            "beat": ['
        if data[i].find(a) != -1:
            t = i
        if data[i].find(b) != -1:
            tt = i
    qian = []
    hou = []
    finalbeat = tt

    for i in range(t, tt - 1):
        if data[i].find('        {') != -1:
            qian.append(i)
        if data[i].find('        },') != -1:
            hou.append(i)
    mcjian = []
    for i in range(len(hou)):
        if hou[i] - qian[i] == 3:
            a = data[qian[i] + 1].lstrip('            "beat": [')
            aa = a.rstrip('],\n')
            aaa = list(eval(aa))

            aaa[0] = aaa[0] + xiaojiebianhua
            ttt = []
            for kkk in aaa:
                tttt = str(kkk)
                ttt.append(tttt)
            aa = ','.join(ttt)
            b = data[hou[i] - 1].lstrip('            "index": ')
            bb = b.rstrip('\n')
            k = []
            k.append('play')
            k.append(aaa[0])
            k.append(aa)
            k.append(bb)
            mcjian.append(k)
        if hou[i] - qian[i] == 5:
            a = data[qian[i] + 1].lstrip('            "beat": [')
            aa = a.rstrip('],\n')
            aaa = list(eval(aa))
            aaa[0] = aaa[0] + xiaojiebianhua
            ttt = []
            for kkk in aaa:
                tttt = str(kkk)
                ttt.append(tttt)
            aa = ','.join(ttt)
            c = data[qian[i] + 2].lstrip('            "endbeat": [')
            cc = c.rstrip('],\n')
            ccc = list(eval(cc))
            ccc[0] = ccc[0] + xiaojiebianhua
            ttt = []
            for kkk in ccc:
                tttt = str(kkk)
                ttt.append(tttt)
            cc = ','.join(ttt)
            b = data[hou[i] - 2].lstrip('            "index": ')
            bb = b.rstrip(',\n')
            d = data[hou[i] - 1].lstrip('            "endindex": ')
            dd = d.rstrip('\n')
            k = []
            k.append('long')
            k.append(aaa[0])
            k.append(aa)
            k.append(cc)
            k.append(bb)
            k.append(dd)
            mcjian.append(k)
    mcjian.append(['play', 999, 'aqaaa', '9'])
    k = 0
    kkk = 1

    if mcjian[-2][0] == 'play':
        finalxiaojie = mcjian[-2][1] + 12
    else:
        aaa = list(eval(mcjian[-2][3]))
        finalxiaojie = aaa[0] + 12
    bpmchange.append(['play', 999, 'aqaaa', '9'])
    for i in range(1, finalxiaojie):
        while mcjian[k][1] < i:
            k = k + 1
        if i % 4 == 0:
            mcjian.insert(k, ['measure', i])
            mcjian.insert(k + 1, ['haku', i])
            lastmeasure = i
            if bpmchange[kkk][1] == i:
                mcjian.insert(k + 2, ['tempo', i, float(bpmchange[kkk][3])])
                kkk = kkk + 1
        else:
            mcjian.insert(k, ['haku', i])
            if bpmchange[kkk][1] == i:
                mcjian.insert(k + 1, ['tempo', i, float(bpmchange[kkk][3])])
                kkk = kkk + 1
    unittime = 60 / float(bpm[0]) * 300
    mcjian.remove(['play', 999, 'aqaaa', '9'])
    cumulatetime = 0
    cumulatejie = 0
    aaaa = data[finalbeat].lstrip('            "beat": [')
    bbbb = aaaa.rstrip('],\n')
    offset1 = offset1 + calculatetime(bbbb)
    for i in mcjian:
        if i[0] == 'tempo':
            a = str(i[1]) + ',0,4'
            cumulatetime = int(calculatetime(a))
            cumulatejie = i[1]
            unittime = 60 / float(i[2]) * 300
        if i[0] == 'haku':
            a = str(i[1]) + ',0,4'
            if not (int(calculatetime(a)) - int(offset1) < 0):
                hakuoutput(int(calculatetime(a)) - int(offset1))
        if i[0] == 'measure':
            a = str(i[1]) + ',0,4'
            if i[1] == lastmeasure:
                endoutput(int(calculatetime(a)) - int(offset1))
            if not (int(calculatetime(a)) - int(offset1) < 0):
                measureoutput(int(calculatetime(a)) - int(offset1))
        if i[0] == 'play':
            if not (int(calculatetime(i[2])) - int(offset1) < 0):
                playoutput(int(calculatetime(i[2])) - int(offset1), int(i[3]))
        if i[0] == 'long':
            if not (int(calculatetime(i[2])) - int(offset1) < 0):
                longoutput(int(calculatetime(i[2]) - int(offset1)), longprocess(i))

    f.close()
    ff.close()
