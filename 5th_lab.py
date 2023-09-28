def count_purchases(records):
    purchases = {}
    for record in records:
        parts = record.split()
        buyer = parts[0]
        item = parts[1]
        quantity = int(parts[2])
        if buyer in purchases:
            purchases[buyer].append((item, quantity))
        else:
            purchases[buyer] = [(item, quantity)]
    return purchases
def print_purchase_list(purchase_list):
    for buyer, purchases in purchase_list.items():
        print("Покупатель:", buyer)
        print("Покупки:")
        for item, quantity in purchases:
            print(f"{item}: {quantity}")
        print()

n = int(input("Введите количество записей о покупках: "))
purchase_records = []
for i in range(n):
    record = input("Введите запись о покупке (Покупатель Товар Количество): ")
    purchase_records.append(record)
purchase_dict = count_purchases(purchase_records)
print_purchase_list(purchase_dict)
