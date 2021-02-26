def ConvDecimal(x):
    return x

def ConvOctal(x):
    return oct(x)

def ConvHexa(x):
    return hex(x)

def ConvBin(x):
    return bin(x)

def loop():
    print('''Decimal    Octal  Hexadecimal    Binario
------------- --------- --------------------- -----------------
    ''')
    for c in range(0, 226):
        print(f' {ConvDecimal(c)}          {ConvBin(c)}       {ConvHexa(c)}         {ConvOctal(c)}')


loop()
