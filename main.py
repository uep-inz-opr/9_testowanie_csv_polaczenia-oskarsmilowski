import csv
from operator import itemgetter
slownik_polaczen = dict()

def main():
    nazwa_pliku = input()
    # path_to_file+nazwa_pliku = ../repozytorium_z_plikiem_polaczenia/phoneCalls.csv
    with open(nazwa_pliku, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['From'] in slownik_polaczen:
                slownik_polaczen[row['From']] += 1
            else:
                slownik_polaczen[row['From']] = 1
    result_niesortowany = list(slownik_polaczen.items())
    result_posortowany = sorted(result_niesortowany,key=itemgetter(1), reverse=True)
    print(result_posortowany[0][0])
    result = (int(result_posortowany[0][0]), result_posortowany[0][1])
    print(result)

if __name__ == "__main__":
    main()
