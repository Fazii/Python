from pip._vendor.distlib.compat import raw_input

line = raw_input()
while (line != 'stop'):
    try:
        p = pow(float(line), 3)
        print(line, p)
    except ValueError:
        print('Bledny parametr')
    line = raw_input()
