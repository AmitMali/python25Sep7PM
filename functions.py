def hello(name="user"):
    print(f"Hello {name}")

def add(no1,no2):
    return no1+no2
def mrp(price,gst=5):
    per=price*gst/100
    return price+per


hello("amit")
hello("rakesh")
hello()
print(add(10,20)*10)

print(mrp(100,8))
print(mrp(100))
