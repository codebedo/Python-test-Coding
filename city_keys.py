data = """1 ADANA
2 ADIYAMAN
3 AFYONKARAHİSAR
4 AĞRI
5 AKSARAY
6 AMASYA
7 ANKARA
8 ANTALYA
9 ARDAHAN
10 ARTVİN
11 AYDIN
12 BALIKESİR
13 BARTIN
14 BATMAN
15 BAYBURT
16 BİLECİK
17 BİNGÖL
18 BİTLİS
19 BOLU
20 BURDUR
21 BURSA
22 ÇANAKKALE
23 ÇANKIRI
24 ÇORUM
25 DENİZLİ
26 DİYARBAKIR
27 DÜZCE
28 EDİRNE
29 ELAZIĞ
30 ERZİNCAN
31 ERZURUM
32 ESKİŞEHİR
33 GAZİANTEP
34 GİRESUN
35 GÜMÜŞHANE
36 HAKKARİ
37 HATAY
38 IĞDIR
39 ISPARTA
40 İSTANBUL
41 İZMİR
42 KAHRAMANMARAŞ
43 KARABÜK
44 KARAMAN
45 KARS
46 KASTAMONU
47 KAYSERİ
48 KIRIKKALE
49 KIRKLARELİ
50 KIRŞEHİR
51 KİLİS
52 KOCAELİ
53 KONYA
54 KÜTAHYA
55 MALATYA
56 MANİSA
57 MARDİN
58 MERSİN
59 MUĞLA
60 MUŞ
61 NEVŞEHİR
62 NİĞDE
63 ORDU
64 OSMANİYE
65 RİZE
66 SAKARYA
67 SAMSUN
68 SİİRT
69 SİNOP
70 SİVAS
71 ŞANLIURFA
72 ŞIRNAK
73 TEKİRDAĞ
74 TOKAT
75 TRABZON
76 TUNCELİ
77 UŞAK
78 VAN
79 YALOVA
80 YOZGAT
81 ZONGULDAK"""


satirlar = data.strip().splitlines()


"""
sehirler = []


for satir in satirlar:
    parcalar = satir.strip().split(maxsplit=1)
    if parcalar[0].isdigit():
        sehirler.append(parcalar[1])
    else:
        sehirler.append(satir.strip())"""

sehirler = []

for satir in satirlar:
    parcalar = satir.strip().split(maxsplit=1)
    if parcalar[0].isdigit():
        sehirler.append(parcalar[1])
    else:
        sehirler.append(satir.strip())


citys = []
for row in  satirlar:
    splt = splt.strip().split(maxsplit=1)
    if splt[0].isdigit():
        citys.append(splt[1])
    else:
        citys.append(row.strip())


for sehir in sehirler:
    print(sehir)