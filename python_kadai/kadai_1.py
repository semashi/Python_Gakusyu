# money_list = []
# while True:
#     money = int(input("あなたの所持金を教えてください："))
#     if money == 0:
#         break
#     money_list.append(money)

# s = sum(money_list)
# n = len(money_list)

# avarage = s/n

# print("皆さんの所持金の金額の平均は" ,avarage,"円です")

total_money = 0
h_count = 0
while True :
    money = int(input("あなたの所持金を教えてください："))
    if money == 0:
        break
    total_money += money
    h_count += 1

avarage = total_money/h_count

print("皆さんの所持金の金額の平均は",avarage,"円です")