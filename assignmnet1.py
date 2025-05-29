inventory = [ 
            # name,       category,    unit_price,  units_sold,  units_left
          ["Strawberry",  "Fruit",     3.50,         40,          10],
          ["Broccoli",    "Vegetable", 2.20,         25,           8],
          ["Cheddar",     "Dairy",     5.00,         18,           4],
          ["Baguette",    "Bakery",    2.80,         35,           2],
          ["Blueberry",   "Fruit",     4.00,         22,           6],
          ["Spinach",     "Vegetable", 1.80,         30,          12],
          ["Yogurt",      "Dairy",     1.20,         50,          15],
          ["Croissant",   "Bakery",    3.00,         28,           3],
]

#Total Revenue
total_revenue = sum(item[2] * item[3] for item in inventory)

# Low Stock Items (units_left < 5)
low_stock_items = [item[0] for item in inventory if item[4] < 5]

# Category-wise Revenue
category_revenue = {}
for name, category, price, sold, left in inventory:
    revenue = price * sold
    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

# Results
print("Total Revenue: $", round(total_revenue, 2))
print("Low Stock Items:", low_stock_items)
print("Category-wise Revenue:")
for cat, rev in category_revenue.items():
    print(f"  {cat}: ${round(rev, 2)}")