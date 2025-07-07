def bubble_sort(arr):
    n = len(arr)

    # dış döngü tüm listeyi kaç kez geçeceğmizi belirleer
    for i in range(n):
        # iç döngü her geçişte son i elemano sıralandığı için daha az  karşılaştırma yapar
        for j in range(0, n - i - 1):
            # ğer önceki eleman sonraki eleman dan büyük se yer dğiştir
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j] # python kolay değişim



# örnek kullanım

liste = [64, 34, 23, 12,22, 11, 90]
print("Sıralama öncesi", liste)

bubble_sort(liste)

print("Sıralama sonrası", liste)