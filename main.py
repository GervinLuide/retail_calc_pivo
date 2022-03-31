print( "kui sooritate ostu mis on rohkem või võrdne 5000$ saate lisa soodustust!!")
kauba_valik = input("sisestage kaup mida soovite osta: ")
kauba_kogus = int(input("Sisestage kauba kogus: "))
asukoht = input("Sisestage State: ").upper()
esialgne_kauba_hind = kauba_kogus
print( "kauba alghind on",esialgne_kauba_hind, "$",)

if kauba_kogus < 1000:
    taxed_hind5 = kauba_kogus + (kauba_kogus * float(asukoht))
    print("Kogusumma maksudega" ,taxed_hind5, "$")


if kauba_kogus >= 1000 and kauba_kogus < 5000:
    discounted_hind =  kauba_kogus - (kauba_kogus * 0.03)
    taxed_hind = (discounted_hind * float(asukoht) + discounted_hind)
    print("Kogusumma koos soodustuse ja maksudega" ,taxed_hind, "$")

if kauba_kogus >= 5000 and kauba_kogus < 7000:
    discounted_hind1 =  (kauba_kogus - (kauba_kogus * 0.05)) - 100
    taxed_hind1 = (discounted_hind1 * float(asukoht) + discounted_hind1)

    print("Kogusumma koos soodustuse ja maksudega", taxed_hind1, "$")

if kauba_kogus >= 7000 and kauba_kogus < 10000:
    discounted_hind2 =  (kauba_kogus - (kauba_kogus * 0.07)) - 200
    taxed_hind2 = (discounted_hind2 * float(asukoht) + discounted_hind2)
    print("Kogusumma koos soodustuse ja maksudega", taxed_hind2, "$")

if kauba_kogus >= 10000 and kauba_kogus < 50000:
    discounted_hind3 =  (kauba_kogus - (kauba_kogus * 0.15)) - 300
    taxed_hind3 = (discounted_hind3 * float(asukoht) + discounted_hind3)
    print("Kogusumma koos soodustuse ja maksudega", taxed_hind3, "$")




