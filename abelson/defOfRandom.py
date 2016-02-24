import base64

def formCheck(a):
    b = []
    for x in a:
        if x == "":
            b.append('0')
        else: 
            b.append('1')
    if "0" in b:
        return False 
    else:
        return True

def fileEncode(a):
    return base64.b64encode(a.read())
