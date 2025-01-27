laptop = { "brand": "dell", "model": "alienware", "year": 2010 }
print(list(laptop.values()))
laptop.update({"home": True})
print(laptop)
laptop["year"] = 2019
print(laptop)
