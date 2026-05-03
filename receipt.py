item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"   # 7.5% sales tax

subtotal = (
        float(item1_price) * int(item1_qty) + 
        float(item2_price) * int(item2_qty)+ 
        float(item3_price) * int(item3_qty)
)
Tax = subtotal * .075
total = subtotal + Tax
print (f""" 
{'':=^60}\n
{'':15}STORE RECEIPT\n
{'':=^60}\n 
{item1_name}{'':15}{'$'+item1_price+' x '+item1_qty}{'':19}{ f"${float(item3_price) * float(item1_qty):.2f}"}\n
{item2_name}{'':15}{'$'+item2_price+' x '+item2_qty}{'':20}{ f"${float(item2_price) * float(item2_qty):.2f}"}\n
{item3_name}{'':15}{'$'+item3_price+' x '+item3_qty}{'':19}{ f"${float(item3_price) * float(item3_qty):.2f}"}\n
{'':_^60}\n
Subtotal:{'':44}{f"${subtotal:.2f}"}
Tax (7.5%):{'':42}{f"${Tax:.2f}"}\n
{'':=^60}
Total:{'':47}{f"${total:.2f}"}\n
{'':=^60}\n

""")

""" 
All decimals used float; all integers used int; lastly all calculations ended with 2 decimal places
"""