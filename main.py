internet_sozluk={
    'LOL':'Gülmek',
    'AFK':'Bilgisardan uzak',
    'RIP':'Allah rahmet eylesin'
}
while True:
    word=input('Anlamadığınız kelimeyi yazınız. Hepsini büyük harfle yazınız')
    if word in internet_sozluk.keys():
        print(internet_sozluk[word])

    else:
        print('Yazdığınız kelime sözlükte yok.')
