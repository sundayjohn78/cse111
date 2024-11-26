import csv
from datetime import datetime

def main():
    KEY_INDEX = 0
    products_dict = read_dictionary("products.csv", KEY_INDEX)

    try:
        print(f"Inkom Emporium")
        print()
        # Here is my exceeding requirements
        # Check if today is Tuesday or Wednesday to apply a 10% discount
        current_day = datetime.now().weekday()
        discount_percentage = 0.1 if current_day in [1, 2] else 0

        with open("request.csv", 'rt') as request_csv:
            reader = csv.reader(request_csv)
            next(reader)

            NAME_INDEX = 1
            PRICE_INDEX = 2
            number_of_items = 0
            sub_total = 0

            for request_list in reader:
                try:
                    request_key = request_list[0]
                    quantity = request_list[1]

                    values = products_dict[request_key]
                    product_name = values[NAME_INDEX]
                    original_price = float(values[PRICE_INDEX])
                    
                    # Apply discount if applicable
                    discounted_price = original_price - (original_price * discount_percentage)
                    price = discounted_price if discounted_price > 0 else original_price

                    print(f"{product_name}: {quantity} @ {price:.2f}")

                    number_of_items += int(quantity)
                    sub_total += (int(quantity) * price)
                except KeyError as key_err:
                    print(f"Error: unknown product ID in the request.csv file\n'{request_key}'")

            # Calculate sales_tax, total, and print receipt details
            sales_tax_rate = 0.06
            sales_tax = sales_tax_rate * sub_total
            total = sub_total + sales_tax

            print()
            print(f"Number of Items: {number_of_items}")
            print(f"Subtotal: {sub_total:.2f}")
            print(f"Sales Tax: {sales_tax:.2f}")
            print(f"Total: {total:.2f}")
            print()
            current_date_and_time = datetime.now()
            print(f"Thank you for shopping at the Inkom Emporium.")
            print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

    except FileNotFoundError as not_found_err:
        print(f"Error: missing file\n[Errno 2] No such file or directory: 'request.csv'")

def read_dictionary(products, KEY_INDEX):
    try:
        filename = "products.csv"
        dictionary = {}

        with open(products, 'rt') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[0]
                    dictionary[key] = row_list

    except FileNotFoundError as not_found_err:
        print(f"Error: missing file\n[Errno 2] No such file or directory: 'products.csv'")

    return dictionary

if __name__ == "__main__":
    main()
