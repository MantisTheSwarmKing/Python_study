# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
#     • Пилешко меню –  10.35 лв.
#     • Меню с риба – 12.40 лв.
#     • Вегетарианско меню  – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.
# Вход
# От конзолата се четат 3 реда:
#     • Брой пилешки менюта – цяло число в интервала [0 … 99]
#     • Брой менюта с риба – цяло число в интервала [0 … 99]
#     • Брой вегетариански менюта – цяло число в интервала [0 … 99]
# Изход
# Да се отпечата на конзолата един ред:  "{цена на поръчката}"

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.50

orders_chicken = int(input())
orders_fish = int(input())
orders_vegetarian = int(input())

chicken_price = (orders_chicken * chicken_menu_price)
fish_price = (orders_fish * fish_menu_price)
vegetarian_price = (orders_vegetarian * vegetarian_menu_price)

total_price = (chicken_price + fish_price + vegetarian_price)
desert_price = (total_price * 0.20)
final_price = (total_price + desert_price + delivery_price)

print({final_price})