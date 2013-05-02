#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, string

# UTILS

def rotate_string(s, factor):
    """
    Takes a string and a shift factor. Returns a string whose characters'
    position have been moved of <factor> times forward (or backward if factor
    is negative)
    """
    if abs(factor) >= len(s):
        factor = factor % len(s)
    return s[factor:] + s[:factor]

def text_from(filename):
    return open(filename, 'rb').read()

def equality_tuples(text):
    return re.findall('[^A-Z]([A-Z]{3})([a-z])([A-Z]{3})[^A-Z]', text)

# PYTHON CHALLENGES

def ex_zero():
    return 0, 2**38

def ex_map(text=None):
    alphabet = string.ascii_lowercase
    alphabet_shifted_2 = rotate_string(alphabet, 2)
    if not text:
        text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    return 1, text.translate(string.maketrans(alphabet, alphabet_shifted_2))

def ex_ocr(text):
    elements = {}
    counter = 0
    for elem in text:
        if elem == '\n':
            continue
        counter = elements.setdefault(elem, 0)
        counter += 1
        elements[elem] = counter
    single_elements = [char for char in elements if elements[char] == 1]
    result = ''
    for elem in text:
        if elem in single_elements:
            result += elem
    return 2, result

def ex_ocr_regex(text):
    return re.sub('[^a-z]', '', text)

def ex_equality(text):
    results = equality_tuples(text)
    return 3, ''.join([match[1] for match in results])

def ex_linkedlist():
    return 4, 'peak'
    import urllib2
    def curl(num):
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(num)
        usock = urllib2.urlopen(url)
        try:
            result = usock.read()
        finally:
            usock.close()
        return result
    num = 66831 # 12345->...->16044->25357->...->66831 which outputs "peak.html"
    nums = [num]
    out = curl(num)
    while True:
        nums.append(num)
        regex = re.search("([0-9]+)$", out)
        if not regex:
            break
        num = regex.groups()[0]
        out = curl(num)
    return 4, out

def ex_peak(text):
    import pickle
    result = ''
    table = pickle.loads(text)
    for row in table:
        for point in row:
            result += point[0]*point[1]
        result += '\n'
    return 5, 'channel' # result.splitlines()

def ex_channel(src, equality_src):
    """
    The picture seems to suggest that some data in riddle #3 should be either
    zipped or unzipped.
    """
    import zipfile
    re_next = re.compile('(?<=Next nothing is )([0-9]+)')
    def zip_find_next(next_nothing, content):
        content = content
        try:
            next_nothing = re_next.findall(content)[0]
        except IndexError:
            return False
        return next_nothing
    def reduce_nothings(archive, next_nothing):
        result = []
        while next_nothing:
            next_nothing_fname = '{}.txt'.format(next_nothing)
            result.append(archive.getinfo(next_nothing_fname).comment)
            with archive.open(next_nothing_fname) as unzipped:
                next_nothing = zip_find_next(next_nothing, unzipped.read())
        return ''.join(result)
    with zipfile.ZipFile(src, 'r') as archive:
        next_nothing = '90052'
        reduce_nothings(archive, next_nothing) # result = this
    return 6, 'oxygen' # result

def ex_oxygen(img):
    from PIL.PngImagePlugin import PngImageFile as Png
    coreimg = Png(img)
    w = coreimg.getbbox()[2]
    h = coreimg.getbbox()[3] // 2
    chars = [coreimg.getpixel((i, h))[0] for i in range(0, w, 7)]
    message = ''.join(map(chr, chars))
    result = ''.join(map(lambda x: chr(int(x)), message[43:-4].split(',')))
    return 7, result

def ex_integrity():
    import bz2
    data = {
            'un': 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084',
            'pw': 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
        }

    return 8, (bz2.decompress(data['un']), bz2.decompress(data['pw']))

def ex_good():
    return 9, "bull"
    # using turtle these coordinates draw a bull
    import turtle
    first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
        310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
        190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
        389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
        215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
        290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
        279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
        327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
        328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
        259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
        352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
        120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
        214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
        102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
        113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
        133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
        111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
        332,155,348,156,353,153,366,149,379,147,394,146,399]
    second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
        157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
        125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
        77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
        158,121,157,128,156,134,157,136,156,136]
    def pairify(l):
        return zip(l[::2], l[1::2])
    pairs = pairify(first) + pairify(second)
    for pair in pairs:
        turtle.setpos(pair)
        turtle.dot()

def ex_bull():
    seq = ['1']
    def say_it(x):
        result = []
        current = prev = x[0]
        x = x[1:]
        count = 1
        for current in x:
            if current == prev:
                count += 1
            else:
                result.append(str(count))
                result.append(prev)
                prev = current
                count = 1
        result.append(str(count))
        result.append(current)
        return ''.join(result)
    x = seq[-1]
    while len(seq) < 31:
        x = say_it(x)
        seq.append(x)
    return 10, len(seq[30])

def ex_5808(imgfile):
    from JpegImagePlugin import JpegImageFile
    img = JpegImageFile(imgfile)
    outs = []
    outs.append(JpegImageFile('out_1.jpg'))
    outs.append(JpegImageFile('out_2.jpg'))
    JpegImageFile()
    h, w = img.size
    curh = curh = curout = 0
    while curh < h:
        curout = (curout + 1) % 2
        curimg = outs[curout]
        while curw < w:
            curimg.setpixel(img.getpixel(()))

    return 11, None

print( ex_zero() )
print( ex_map('map') )
print( ex_ocr(text_from('ocr.txt')) )
print( ex_equality(text_from('equality.txt')) )
print( ex_linkedlist() )
print( ex_peak(text_from('peak.txt')) )
print( ex_channel('channel.zip', text_from('equality.txt')) )
print( ex_oxygen('oxygen.png') )
print( ex_integrity() )
print( ex_good() )
print( ex_bull() )
print( ex_5808('cave.jpg') )
