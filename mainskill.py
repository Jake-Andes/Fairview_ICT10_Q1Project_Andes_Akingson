from pyscript import document, display

HotWhiteChocolateMocha_price = document.getElementById("check1")
MatchaGreenTeaLatte_price = document.getElementById("check2")
IcedRaspberryMochaKiss_price = document.getElementById("check3")


HotWhiteChocolateMocha_price = 150
MatchaGreenTeaLatte_price = 180
IcedRaspberryMochaKiss_price = 200


Customer_name = document.getElementById("name").value
Customer_phonenumber = document.getElementById("phonenumber").value
Customer_address = document.getElementById("address").value


def show_checked(e):
    total = 0
    order_summary = "Order Summary:\n"
    
    if document.getElementById("check1").checked:
        total += HotWhiteChocolateMocha_price
        order_summary += f"- Hot White Chocolate Mocha: ${HotWhiteChocolateMocha_price}\n"
    
    if document.getElementById("check2").checked:
        total += MatchaGreenTeaLatte_price
        order_summary += f"- Matcha Green Tea Latte: ${MatchaGreenTeaLatte_price}\n"
    
    if document.getElementById("check3").checked:
        total += IcedRaspberryMochaKiss_price
        order_summary += f"- Iced Raspberry Mocha Kiss: ${IcedRaspberryMochaKiss_price}\n"
    
    order_summary += f"\nTotal Price: ${total}\n"
    order_summary += f"Customer Name: {document.getElementById('name').value}\n"
    order_summary += f"Customer Address: {document.getElementById('address').value}\n"
    
    display(order_summary, target="output1")
    #this was python auto adding system👍

















