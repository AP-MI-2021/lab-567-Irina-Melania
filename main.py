# parcurs
# 3.1 adaugare date / editare / visualizare  - biblioteca cu key uri specifice
# 3.2 adaugare


def add(ad):
    ad_id = input('ID-ul persoanei este :')
    ad['ID'].append(ad_id)
    print(ad)
    ad_nume = input('Numele persoanei: ')
    ad['NUME'].append(ad_nume)
    ad_clasa = input('Clasa persoanei: ')
    ad['CLASA'].append(ad_clasa)
    ad_pret = input('Pret bilet: ')
    ad['PRET'].append(ad_pret)
    ad_check = input('Checkin (DA/NU): ')
    if ad_check == 'DA' or ad_check == 'NU':
        ad['CHECKIN'].append(ad_check)
    else:
        while True:
            ad_check = input('Checkin (DA/NU): ')
            if ad_check == 'DA' or ad_check == 'NU':
                break
        ad['CHECKIN'].append(ad_check)

    print(ad)


def modificare(mod):
    id_persoana_modif = input('ID persoana care trebuie modificata: ')
    cont = 0
    for id in mod['ID']:
        cont += 1
        if id_persoana_modif == id:
            break

    if cont == len(mod['ID']):
        print('ID incorect sau inexistent.')
    else:
        while True:
            mod_el = input('Ce se modifica? (scrie: ID/NUME/CLASA/PRET/CHECKIN/LEAVE').upper
            if mod_el == 'LEAVE':
                break
            mod[mod_el[cont]] = input()


def stergere(sterg):

    id_stergere = input('ID element de sters: ')
    cont = 0
    for id in sterg['ID']:
        cont += 1
        if id_stergere == id:
            break

    sterg['ID[cont]'].remove
    sterg['NUME[cont]'].remove
    sterg['CLASA[cont]'].remove
    sterg['PRET[cont]'].remove
    sterg['CHECKIN[cont]'].remove


def vizualizare(viz):
    print(viz)


companie = {
    'ID': [],
    'NUME': [],
    'CLASA': [],
    'PRET': [],
    'CHECKIN': [],
}

while True:
    x = int(input('Ce operatie doriti ? (adaugare 1 ; vizualizare 2; modificare 3; stergere 4;exit 0) : '))
    if x == 1:
        add(companie)

    if x == 3:
        modificare(companie)

    if x == 0:
        break

    if x == 2:
        vizualizare(companie)
    if x == 4:
        stergere(companie)
