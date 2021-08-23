from utils import*

kulutus=float(input("Miten paljon auto kuluttaa? (litra/100km) "))
polttoaineen_hinta=float(input("Miten paljon polttoaine maksaa? (€/litra) "))
kuljettu_matka=float(input("miten pitkä matka on kuljettu? (km) "))
calc_consumption(kulutus, polttoaineen_hinta, kuljettu_matka)


