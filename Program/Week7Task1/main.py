NUM_CHARITIES = 3
DONATION_PERCENTAGE = 0.01

# Initialize charity names and donation totals
charity_names = []
charity_totals = [0] * NUM_CHARITIES

# Get charity names
for i in range(1, NUM_CHARITIES + 1):
    charity_name = input(f"Enter the name of Charity {i}: ")
    charity_names.append(charity_name)

# Display charity names with numbers
print("\nCharity Options:")
for i in range(NUM_CHARITIES):
    print(f"{i + 1}. {charity_names[i]}")

# Get customer's charity choice
charity_choice = int(input(f"\nEnter the number (1-{NUM_CHARITIES}) for the chosen charity: "))

# Validate charity choice
if 1 <= charity_choice <= NUM_CHARITIES:
    # Get customer's shopping bill
    shopping_bill = float(input("Enter the customer's shopping bill amount: "))

    # Calculate donation amount
    donation_amount = shopping_bill * DONATION_PERCENTAGE

    # Update total donation for the chosen charity
    charity_totals[charity_choice - 1] += donation_amount

    # Display donation details
    print(f"\nDonation Details:")
    print(f"Chosen Charity: {charity_names[charity_choice - 1]}")
    print(f"Donation Amount: ${donation_amount:.2f}")

    # Display total donations for all charities
    for i in range(NUM_CHARITIES):
        print(f"Total donation for {charity_names[i]}: ${charity_totals[i]:.2f}")

else:
    print("Error: Invalid charity choice. Please choose a number within the specified range.")
