# Румен иска да пребоядиса хола и за целта е наел майстори. Напишете програма,
# която изчислява разходите за ремонта, предвид следните цени:
#     • Предпазен найлон - 1.50 лв. за кв. метър
#     • Боя - 14.50 лв. за литър
#     • Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м.
# найлон, разбира се и 0.40 лв. за торбички. Сумата, която се заплаща на майсторите за 1 час работа,
# е равна на 30% от сбора на всички разходи за материали.
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
#     1. Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
#     2. Необходимо количество боя (в литри) - цяло число в интервала [1…100]
#     3. Количество разредител (в литри) - цяло число в интервала [1…30]
#     4. Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
# Изход
# Да се отпечата на конзолата един ред:
#     • "{сумата на всички разходи}"

nylon_price = 1.5
paint_price = 14.50
thinner_price = 5.00
bag = 0.40

nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_total_price = float(nylon + 2) * nylon_price
paint_total_price = float(paint + (paint * (10/100))) * paint_price
thinner_total_price = float (thinner * thinner_price)
total_price_materials = nylon_total_price + paint_total_price + thinner_total_price + bag
total_price = (total_price_materials * (30/100)) * hours
all_expenses = total_price + total_price_materials

print(all_expenses)