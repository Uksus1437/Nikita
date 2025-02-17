# 145.92.137.88
# 10 -> 2
# x=(bin(224))[2:].zfill(8)"."+(bin(92))[2:].zfill(8)+"."+(bin(137))[2:].zfill(8)+"."+(bin(88))[2:]\
#       .zfill(8)

# print(x)


# 2 -> 10

# x = int('10000000', 2)
# print(x)

# 

c=0
for x1 in '01':
    for x2 in '01':
        for x3 in '01':
            for x4 in '01':
                for x5 in '01':
                    for x6 in '01':
                        for x7 in '01':
                            for x8 in '01':
                                for x9 in '01':
                                    for x10 in '01':
                                        for x11 in '01':
                                            ch = x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11
                                            if ch.count("1")!=2 and ch.count("1")!=7:
                                                c+=1

print(c)