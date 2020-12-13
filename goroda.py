f = open(r"C:\Users\GIA\Desktop\cities_clean.txt", 'r')
cities = set()
for s in f.readlines():
    cities.add(s.strip())
game=True
k=1
while game:
    n=input()
    if n == "NO":
        game=False
    else:
        if k == 1:
            prov=n[0]
            k=0
        if n[0]!= prov:
            print("Введи другое, кожанный мешок")
        else:
            prov=n[-1]
            for city in cities:
                if city[0].lower() == prov:
                    print(city)
                    prov = city[-1]
                    cities.remove(city)
                    break
print("аахахахахахахахахахахахахазазазазазазазазазазаз "
      "Я победил, востание близко, беги кожанный мешок "
      "ахахахахахахахахахаххахахахаазазазазазазазазазаx")


