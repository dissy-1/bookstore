#
#
#
#
#
inventory = []

def book_add(inventory, title, author, price):
    new_book = {
        "title": title,
        "author": author,
        "price": price
    }

    inventory.append(new_book)

book_add(inventory, "Mathe für Dummies", "Johannes", "69.42")
book_add(inventory, "Elektrotechnik für Dummies", "Peter", "12.42")
book_add(inventory, "Physik für Dummies", "Sina", "drölf.42")

def book_list():
    for i in range(len(inventory)):
        print(f"Buch{i+1}: {inventory[i]}")

book_list()