def convertList(lst):
    tmp = [line[:-1] + '<br>\n' for line in lst]
    str = "".join(tmp)
    return str

def addLineBreaks(str):
    return '<br>\n'.join(str.split('\n'))