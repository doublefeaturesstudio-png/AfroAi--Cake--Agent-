# AfroAi - Cake Cost Calculator for Lagos Bakers
# AMD Hackathon Submission

def calculate_cake_cost():
    print("🎂 AfroAi Cake Cost Calculator - Lagos Edition 🎂")
    print("Helping bakers stop guesswork, start profit\n")

    try:
        # Get inputs
        flour = float(input("Flour cost (NGN): "))
        sugar = float(input("Sugar cost (NGN): "))
        eggs = float(input("Eggs cost (NGN): "))
        butter = float(input("Butter/oil cost (NGN): "))
        other = float(input("Other ingredients + packaging (NGN): "))

        # Calculate
        ingredient_cost = flour + sugar + eggs + butter + other
        labor = ingredient_cost * 0.3  # 30% labor
        overhead = ingredient_cost * 0.2  # 20% gas/electricity
        total_cost = ingredient_cost + labor + overhead

        # Profit margin suggestion
        selling_price = total_cost * 1.5  # 50% profit margin
        profit = selling_price - total_cost

        print("\n" + "="*40)
        print(f"TOTAL COST: NGN{total_cost:.2f}")
        print("="*40)
        print(f"Ingredients: NGN{ingredient_cost:.2f}")
        print(f"Labor 30%: NGN{labor:.2f}")
        print(f"Overhead 20%: NGN{overhead:.2f}")
        print(f"\nSuggested selling price: NGN{selling_price:.2f}")
        print(f"Your profit per cake: NGN{profit:.2f}")
        print("\nAfroAi says: Know your cost, own your profit! 💪")

    except ValueError:
        print("Error: Please enter numbers only. Try again!")

# Run the calculator
if __name__ == "__main__":
    calculate_cake_cost()