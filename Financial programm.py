# Бухгалтерская программа, которая распределяет мои расходы и в процентном соотношении от дохода выводит всё на экран

from tabulate import tabulate


your_income = float(input("Please type your month income >>> "))

housing_and_utilities = float(1600)
the_precentege_from_housing_and_utilities = round(
    float(housing_and_utilities / your_income * 100)
)


investments = float(600)
the_precentege_from_investments = round(float(investments / your_income * 100))


hairdresser = float(40)
the_precentege_from_hairdresser = round(float(hairdresser / your_income * 100))


the_internet = float(60)
the_precentege_from_the_internet = round(float(the_internet / your_income * 100))


telephone = float(35)
the_precentege_from_telephone = round(float(telephone / your_income * 100))


spotify_subscription = float(19.99)
the_precentege_from_spotify_subscription = float(
    spotify_subscription / your_income * 100
)


food_and_household_chemicals = float(1000)
the_precentege_from_food_and_household_chemicals = round(
    float(food_and_household_chemicals / your_income * 100)
)


def summ(a, b, c, d, e, f, g, h):
    return a - b - c - d - e - f - g - h


the_rest_of_money = round(
    summ(
        your_income,
        housing_and_utilities,
        investments,
        hairdresser,
        the_internet,
        telephone,
        spotify_subscription,
        food_and_household_chemicals,
    )
)

the_precentege_from_the_rest_of_money = round(
    float(the_rest_of_money / your_income * 100)
)

print(
    tabulate(
        [
            [
                "housing and utilities",
                housing_and_utilities,
                the_precentege_from_housing_and_utilities,
            ],
            [
                "investments",
                investments,
                the_precentege_from_investments,
            ],
            [
                "hairdresser",
                hairdresser,
                the_precentege_from_hairdresser,
            ],
            [
                "Internet",
                the_internet,
                the_precentege_from_the_internet,
            ],
            [
                "telephone",
                telephone,
                the_precentege_from_telephone,
            ],
            [
                "spotify subscription",
                spotify_subscription,
                the_precentege_from_spotify_subscription,
            ],
            [
                "food and household chemicals",
                food_and_household_chemicals,
                the_precentege_from_food_and_household_chemicals,
            ],
            [
                "the rest of money",
                the_rest_of_money,
                the_precentege_from_the_rest_of_money,
            ],
        ],
        headers=[
            "Type",
            "PLN",
            "%",
        ],
    )
)
