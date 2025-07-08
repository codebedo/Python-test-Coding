inv = ["sword", None,None]

if all(inv): # all ile kontrol edilebilyor , bu yeni bir liste fonksiyonu
    print('Inventory full!')
elif any(inv): # bir tane bile var mı kontrolü bu bizim için iyi bir fonksiyon
    print("Inventory has items!")
else:
    print("Inventory empty")