def calc_consumption(auton_kulutus_litra, polttoaineen_hinta_euro, matka_km):
    kulunut_polttoaine=(auton_kulutus_litra/100)*matka_km
    hinta=kulunut_polttoaine*polttoaineen_hinta_euro
    print("Polttoainetta on kulunut matkalle " + str(kulunut_polttoaine) + " litraa "+ "Polttoaineen hinta matkalle on: " + str(hinta) + " euroa")