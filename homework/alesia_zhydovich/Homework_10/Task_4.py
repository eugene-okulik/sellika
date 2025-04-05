PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


# lines = PRICE_LIST.split('\n')
# price_dict = {}
# for line in lines:
#     parts = line.split()
#     item = parts[0]
#     price_str = parts[1]
#     price = int(price_str[:-1])
#     price_dict[item] = price


price_dict = {line.split()[0]: int(line.split()[1][:-1]) for line in PRICE_LIST.split('\n')}
print(price_dict)
