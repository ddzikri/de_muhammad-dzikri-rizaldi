def get_breads(breads, flour_stock):
    jenis_roti_dapat_dibuat = []
    for i in breads:
        if flour_stock >= i["flour"]:
          jenis_roti_dapat_dibuat.append(i["name"])
          flour_stock = i["flour"]
    return jenis_roti_dapat_dibuat

bread1 = [
  {"name": "donut", "flour": 25},
  {"name": "mini puff", "flour": 15},
  {"name": "baguette", "flour": 75},
  {"name": "cupcake", "flour": 15},
]

bread2 = [
  {"name": "pancake", "flour": 15},
  {"name": "waffle", "flour": 25},
  {"name": "bagel", "flour": 15},
  {"name": "cupcake", "flour": 15},
  {"name": "choco chips", "flour": 10},
  {"name": "mini puff", "flour": 5},
  {"name": "bread", "flour": 30},
]

print(get_breads(bread1, 100))  # ['mini puff', 'cupcake', 'donut']
print(
  get_breads(bread2, 75)
)  # ['mini puff', 'choco chips', 'pancake', 'bagel', 'cupcake']

