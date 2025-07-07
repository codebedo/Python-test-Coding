def merge_sort(arr):
    # eğer dizemiz 1 veya 0 elemanlıysa , zaten sıralıdır, olduğu gibi döndürülür.

    if len(arr) <= 1:
        return arr


    # diziyi ortadan ikiye bölüceğiz bunun içinde ortayı bulmak gerekir.
    mid = len(arr) //2


    # sol yarısını reürsif olarak sırala
    # arr[mid:] -> mide olan kısmı al diyor ve geçici bir dize oluştur.

    left_half = merge_sort(arr[mid:])

    right_half = merge_sort(arr[:mid])


    # sıralı iki yarıyı birleştir ve sonucu döndür

    return merge(left_half,  right_half)

def merge(left, right):
    # birleştirilmiş sonucu tutacak dizi
    merged = []

    # sol ve sağ dizilerdeki indeksleri takip etmek için
    i = j = 0

    # her iki dizide de karşılaştırılacak eleman olduğu  sürece devam et
    while i < len(left) and j < len(right):
        # sol dizideki eleman küçükse , onu ekle ve sol indeks ilerlet
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
        # aksi haklde sağ dizideki eleman daha küçükk veya eşittir, onu ekle
             merged.append(right[j])


    # sol dizide kalan elemanları ekle (eğer varsa)
    merged.extend(left[i:])

    # sağ dizide kalan elemanları ekle (eğer varsa)

    merged.extend(right[j:])

    # Birleştirillmmiş sıralı diziyi döndğr

    return merged