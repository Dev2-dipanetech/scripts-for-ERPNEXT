# Doctype : Blanket Order : Before Save : to get the product of auntity with rate

for d in doc.get("items"):
    d.amount = (int(d.qty))*(int(d.rate))
