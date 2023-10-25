salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

month = 0
whole_mc = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

for money_capital in range (1, months + 1):
    month += 1
    if month >= 2:
        spend += spend * increase
    money_capital = -(salary - spend)
    whole_mc += money_capital


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(whole_mc, 2))
