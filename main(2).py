ip = list(map(int, '172.17.167.18'.split('.')))
print(f'{bin(ip[0])[2:].zfill(8)}.{bin(ip[1])[2:].zfill(8)}.{bin(ip[2])[2:].zfill(8)}.{bin(ip[3])[2:].zfill(8)}')


ip = list(map(int, '255.255.240.0'.split('.')))
print(f'{bin(ip[0])[2:].zfill(8)}.{bin(ip[1])[2:].zfill(8)}.{bin(ip[2])[2:].zfill(8)}.{bin(ip[3])[2:].zfill(8)}')
