from matplotlib import pyplot

data = open("./data/life_expectancies_usa.txt", "r").readlines()

dates = []
male_life_expectancies = []
female_life_expectancies = []

for row in data:
    date, male_life_expectancy, female_life_expectancy = row.split(",")
    dates.append(int(date))
    male_life_expectancies.append(float(male_life_expectancy))
    female_life_expectancies.append(float(female_life_expectancy))

pyplot.plot(dates, male_life_expectancies, "bo-", label="Men")
pyplot.plot(dates, female_life_expectancies, "mo-", label="Female")
pyplot.legend(loc="upper left")
pyplot.ylabel("Age")
pyplot.xlabel("Year")
pyplot.title("Life expectancies for women and men in the USA over time")
pyplot.show()

