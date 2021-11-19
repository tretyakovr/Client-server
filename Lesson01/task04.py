"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""


encode_list = [item.encode('utf-8') for item in ['разработка', 'администрирование', 'protocol', 'standard']]
print(encode_list)

decode_list = [item.decode('utf-8') for item in encode_list]
print(decode_list)

# result:
# [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0', b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', b'protocol', b'standard']
# ['разработка', 'администрирование', 'protocol', 'standard']
