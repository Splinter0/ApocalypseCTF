newmap = {
        2: "PostFail",
        4: "a",
        5: "b",
        6: "c",
        7: "d",
        8: "e",
        9: "f",
        10: "g",
        11: "h",
        12: "i",
        13: "j",
        14: "k",
        15: "l",
        16: "m",
        17: "n",
        18: "o",
        19: "p",
        20: "q",
        21: "r",
        22: "s",
        23: "t",
        24: "u",
        25: "v",
        26: "w",
        27: "x",
        28: "y",
        29: "z",
        30: "1",
        31: "2",
        32: "3",
        33: "4",
        34: "5",
        35: "6",
        36: "7",
        37: "8",
        38: "9",
        39: "0",
        40: "Enter",
        41: "esc",
        42: "del",
        43: "tab",
        44: "space",
        45: "-",
        46: "=",
        47: "[",
        48: "]",
        52: "'",
        55: ".",
        56: "/",
        57: "CapsLock",
        79: "RightArrow",
        80: "LetfArrow"
}

myKeys = open('keystrokes.txt')
i = 1
for line in myKeys:
    bytesArray = bytearray.fromhex(line.strip())
    j = 0
    capital = 0
    if int(bytesArray[0]) == 2 or int(bytesArray[0]) == 20:
        capital = 1
    for byte in bytesArray:
#         print "Bytes: " + str(j) +   " " + str(bytesArray[j])
        j+=1
        if byte != 0:
            keyVal = int(byte)

            if keyVal in newmap:
    #print "Value map : " + str(keyVal) + " -> " + newmap[keyVal]
                if capital == 1:
                    if newmap[keyVal] == '[':
                        print "{"
                    elif newmap[keyVal] == ']':
                        print "}"
                    elif newmap[keyVal] == '-':
                        print "_"
                    elif newmap[keyVal] == '=':
                        print '+'
                    else:
                        print newmap[keyVal].capitalize()
                    continue
                print newmap[keyVal]
            else:
                print "No map found for this value: " + str(keyVal)
#print format(byte, '02X')
    i+=1
