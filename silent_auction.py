print("Welcome to silent bid!")
dictionary = {}
while True:
    name = input("What is your name? ")
    price = int(input("What is your bid value?($)"))

    dictionary[name] = price

    more_users = input("Are there more bidders?(Y/N)").upper()

    if more_users == 'Y':
        print("\n"*100)
    else:
        break


print("\n"*100)
highest_bid = 0
highest_bidder = ''
for key in dictionary:
    if dictionary[key] > highest_bid:
        highest_bid = dictionary[key]
        highest_bidder = key
    else:
        pass
print(f"The winner of the auction is {highest_bidder} with a bid amount of ${highest_bid}!")
