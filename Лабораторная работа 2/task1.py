money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
capital = money_capital + salary
mounth = 0
while spend <= capital:
    capital += salary - spend
    spend += spend * increase
    mounth += 1
print("Количество месяцев, которое можно протянуть без долгов:", mounth)