# Read the currency data from file
with open('currencyData.txt') as f:
    currencies = f.readlines()

# Main function to handle currency conversion
def main():
    # Get user input for the currency to change
    want_to_change = input("Enter the currency name to which you want to convert: ").strip()
    currency_found = False

    # Process each line in the currencies list
    for currency in currencies:
        # Split the line into currency name and value
        currency_data = currency.strip().split("\t")

        # Print the currency data for debugging
        #print(f"Currency Data: {currency_data}")

        # Check if the currency matches the user's input
        if currency_data[0].lower() == want_to_change.lower():
            # Currency found, proceed with conversion
            currency_found = True
            print(f"1 Indian Rupee in {currency_data[0]} is equal to {currency_data[1]} in that country")
            try:
                # Get the amount to convert
                amount = float(input("Enter the amount you want to convert: "))
                # Convert the amount
                converted_amount = amount * float(currency_data[1])
                print(f"The converted amount is {converted_amount:.2f} {currency_data[0]}")
            except ValueError:
                # Handle invalid input
                print("Invalid amount entered. Please enter a numeric value.")
            break

    # If the currency was not found
    if not currency_found:
        print("Currency not found. Please check the currency name and try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
