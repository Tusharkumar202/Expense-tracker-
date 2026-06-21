file_name = "expense.txt"


# function to add expense
def addexp(date, category, amount, note):
    file = open(file_name, "a")

    record = date + "," + category + "," + str(amount) + "," + note + "\n"

    file.write(record)
    file.close()


# function to read all expenses
def getexp():

    expenses = []

    try:
        file = open(file_name, "r")

        for i in file:

            data = i.strip().split(",")

            expense = {
                "date": data[0],
                "category": data[1],
                "amount": float(data[2]),
                "note": data[3]
            }

            expenses.append(expense)

        file.close()

    except:
        pass

    return expenses


# function to calculate total expense
def total_expense():

    expenses = getexp()

    total = 0

    for t in expenses:
        total = total + t["amount"]

    return total


# function for category wise expense
def cat_exp():

    expenses = getexp()

    cardata = {}

    for y in expenses:

        category = y["category"]
        amount = y["amount"]

        if category in cardata:
            cardata[category] = cardata[category] + amount
        else:
            cardata[category] = amount

    return cardata