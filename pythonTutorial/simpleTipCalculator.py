# Simple tip calculator App...

food = float(input('Enter amount $: '))
tip_percentage = float(input('Tip amount %: ')) / 100
tip = food * tip_percentage

total = food + tip
print("========================================")
print(f"Food amount 🍟: ${food}")
print(f"Tip amount: {tip_percentage}%")
print(f"Total amount to be paid 👉: ${total}")
print("=========================================")
