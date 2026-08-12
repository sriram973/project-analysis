def display(*person):
    print(person)
display("john")
display("john", "doe")
display("john", "doe", "smith")

# double assert
def display(**product):
    print(product)
display(name="laptop")  
display(name="laptop", price=1000)
display(name="laptop", price=1000, brand="dell")