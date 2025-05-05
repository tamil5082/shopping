# main.py

##########################
# ===== BACKEND ========
##########################

class SustainableProduct:
    def __init__(self, name, category, price, carbon_footprint, is_recyclable):
        self.name = name
        self.category = category
        self.price = price
        self.carbon_footprint = carbon_footprint  # kg CO2
        self.is_recyclable = is_recyclable

    def sustainability_score(self):
        # Lower carbon and recyclable = higher score
        score = 100 - self.carbon_footprint
        if self.is_recyclable:
            score += 10
        return score


class ShoppingAssistant:
    def __init__(self):
        self.products = self.load_products()

    def load_products(self):
        # Sample products database
        return [
            SustainableProduct("Eco Bottle", "Home", 15.0, 1.2, True),
            SustainableProduct("Plastic Bottle", "Home", 1.0, 5.0, False),
            SustainableProduct("Organic T-shirt", "Clothing", 25.0, 2.5, True),
            SustainableProduct("Synthetic T-shirt", "Clothing", 10.0, 6.5, False),
        ]

    def recommend(self, category=None, max_price=None):
        filtered = self.products
        if category:
            filtered = [p for p in filtered if p.category.lower() == category.lower()]
        if max_price is not None:
            filtered = [p for p in filtered if p.price <= max_price]

        sorted_products = sorted(filtered, key=lambda p: p.sustainability_score(), reverse=True)
        return sorted_products


##########################
# ===== FRONTEND ========
##########################

def frontend():
    assistant = ShoppingAssistant()

    print("\n🌿 Welcome to the AI Sustainable Shopping Assistant 🌿")
    category = input("Enter product category (e.g., Home, Clothing): ")
    price_input = input("Enter your max price (leave blank for no limit): ")

    try:
        max_price = float(price_input) if price_input else None
    except ValueError:
        print("Invalid price entered. No price filter will be applied.")
        max_price = None

    recommendations = assistant.recommend(category=category, max_price=max_price)

    if not recommendations:
        print("\n❌ No suitable sustainable products found.")
    else:
        print("\n✅ Recommended Sustainable Products:")
        for p in recommendations:
            print(f"- {p.name} (${p.price}) | Score: {p.sustainability_score():.1f}")

if __name__ == "__main__":
    frontend()
