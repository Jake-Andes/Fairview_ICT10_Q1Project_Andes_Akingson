from js import document

menu_items = [
            ("Hot White Chocolate Mocha", 150),
            ("Matcha Green Tea Latte", 140),
            ("Iced Raspberry Mocha Kiss", 160),
            ("Caramel Macchiato Frappuccino", 155),
            ("Chocolate Hazelnut Latte", 150)
        ]

container = document.getElementById("menu-container")
html_table = "<table class='table table-striped'><thead class='table-dark'><tr><th>Drink</th><th>Price</th></tr></thead><tbody>"

for drink, price in menu_items:
    html_table += f"<tr><td>{drink}</td><td>₱{price}</td></tr>"

html_table += "</tbody></table>"
container.innerHTML = html_table
