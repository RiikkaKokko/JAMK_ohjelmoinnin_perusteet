indeksi=int(input("Mihin kohtaan taulukkoa haluat syöttää uuden tekstin? "))
teksti=input("Syötä teksti: ")

merkkijono=["Joe", "Sally", "Liam", "Robert", "Emma"]
try:
    merkkijono[indeksi]=teksti
except IndexError:
    print("Ei toimi, syötä indeksi uudestaan")
    indeksi=int(input("Mihin kohtaan taulukkoa haluat syöttää uuden tekstin? "))
    merkkijono[indeksi]=teksti
print(merkkijono)