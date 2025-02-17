ip = list(map(int, '172.16.168.0'.split('.')))
print(f'{bin(ip[0])[2:].zfill(8)}.{bin(ip[1])[2:].zfill(8)}.{bin(ip[2])[2:].zfill(8)}.{bin(ip[3])[2:].zfill(8)}')


ip = list(map(int, '255.255.248.0'.split('.')))
print(f'{bin(ip[0])[2:].zfill(8)}.{bin(ip[1])[2:].zfill(8)}.{bin(ip[2])[2:].zfill(8)}.{bin(ip[3])[2:].zfill(8)}')