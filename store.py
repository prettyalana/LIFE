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
        "vegetables": ["potatoes", "broccoli", "squash", "kale", "spinach"],
    },
    "snacks": ["chips", "ice cream"],
    "meat and poultry": ["beef", "chicken", "lamb"],
}

shopping_center_inventory = {
    "clothing": ["tops", "pants", "skirts", "dresses"],
    "shoes": ["pumps", "sneakers", "loafers"],
}


grocery_store = Store("LIFE Grocer Mart")
shopping_center = Store("LIFE Department Store")
