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
    with open(a, "rb") as a2:
         return base64.b64encode(a2.read())
