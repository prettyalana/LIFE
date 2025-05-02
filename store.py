class Store:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory


grocery_store_inventory = {
    "produce": {
        "fruits": {
            "apples": 0.69,
            "oranges": 1.99,
            "strawberries": 2.99,
            "bananas": 0.59,
        },
        "vegetables": {
            "potatoes": 0.50,
            "broccoli": 1.00,
            "squash": 1.99,
            "kale": 2.99,
            "spinach": 0.99,
        },
    },
    "snacks": {"chips": 2.99, "ice cream": 3.99, "candy bar": 0.99},
    "meat and poultry": {"beef": 7.99, "chicken": 5.99, "lamb": 10.99},
}

shopping_center_inventory = {
    "clothing": ["tops", "pants", "skirts", "dresses"],
    "shoes": ["pumps", "sneakers", "loafers"],
}


grocery_store = Store("LIFE Grocer Mart")
shopping_center = Store("LIFE Department Store")
