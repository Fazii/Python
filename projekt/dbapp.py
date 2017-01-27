import mysql.connector
import sys
from mysql.connector import errorcode
from pip._vendor.distlib.compat import raw_input
from tabulate import tabulate


class DataBase:
    user = raw_input('LOGIN: ')
    password = raw_input('HASLO: ')

    try:
       con = mysql.connector.connect(user=user, password=password,
                                      host='127.0.0.1',
                                      database='wypozyczalnia_filmow')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Bledny login lub haslo")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Baza danych nie istnieje")
        else:
            print(err)
    else:
        print("Zalogowano")
        cur = con.cursor(buffered=True)

        def view(self, q):
            """Metoda pozwalająca na wyświetlanie sformatowanych danych z bazy danych"""
            try:
                self.cur.execute(q)
                result = self.cur.fetchall()

                title = []
                for i in range(len(self.cur.description)):
                    desc = self.cur.description[i]
                    title.append(desc[0])

                print(tabulate([i for i in result], headers=[i for i in title], tablefmt='orgtbl'))

            except mysql.connector.Error as e:
                print("Błąd: {}".format(e.errno))
            finally:
                self.main_menu()

        def executequery(self, q):
            """Metoda pozwalająca na wysyłanie zapytań do bazy danych"""
            try:
                self.cur.execute(q)
                self.con.commit()
                print("Wykonano!")
            except mysql.connector.Error as e:
                print("Błąd: {}".format(e.errno))
                try:
                    self.con.rollback()
                except mysql.connector.Error as e:
                    print('Rollback error')
                    print(str(e.errno))
            finally:
                self.main_menu()


        def addclient(self, user_table):
            """Metoda pozwalająca na dodawanie nowych klientów do bazy danych"""
            q = """\
            INSERT INTO wypozyczajacy(nazwisko, imie,Nr_dokumentu, PESEL, ulica, miejscowosc, numer_domu, kod_pocztowy, numer_mieszkania, ID_wojewodztwa, telefon_domowy, data_urodzenia)
             VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s')""" % (
                user_table[0], user_table[1], user_table[2], user_table[3], user_table[4], user_table[5], user_table[6],
                user_table[7], user_table[8], user_table[9], user_table[10], user_table[11])
            self.executequery(q)


        def showclientinfo(self, ident):
            """Metoda pozwalająca na wyświetlanie informacji o kliencie z bazy dancyh"""
            q = """\
            SELECT wypozyczajacy.nazwisko, wypozyczajacy.imie, wypozyczajacy.Nr_dokumentu, wypozyczajacy.PESEL, wypozyczajacy.ulica, wypozyczajacy.miejscowosc, wypozyczajacy.numer_domu, wypozyczajacy.kod_pocztowy, wypozyczajacy.numer_mieszkania, wojewodztwa.wojewodztwo, wypozyczajacy.telefon_domowy, wypozyczajacy.data_urodzenia
            FROM wypozyczajacy JOIN wojewodztwa ON wypozyczajacy.ID_wojewodztwa = wojewodztwa.id AND wypozyczajacy.Nr_karty_wypozyczajacego = %s""" % ident
            self.view(q)


        def addfilm(self, film_table):
            """Metoda pozwalająca na dodawanie nowych filmów do bazy danych"""
            q = """\
            INSERT INTO filmy(tytul_filmu, rok_wydania, ID_rezysera, ID_gatunku, ID_produkcji, ID_nosnika, ID_kategorii, cena_zakupu_filmu, krotki_opis_filmu, czas_trwania_filmu)
            VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s','%s')""" % (
                film_table[0], film_table[1], film_table[2], film_table[3], film_table[4], film_table[5], film_table[6],
                film_table[7], film_table[8], film_table[9])
            self.executequery(q)


        def addrental(self, rental_table):
            """Metoda pozwalająca na dodawanie nowych wypożyczeń filmu do bazy danych"""
            q = """\
            INSERT INTO rejestr_wypozyczen(Nr_karty_wypozyczajacego, ID_egzemplarza, data_wypozyczenia, na_ile_dni, data_oddania, zaplata, doplata)
            VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                rental_table[0], rental_table[1], rental_table[2], rental_table[3], rental_table[4], rental_table[5],
                rental_table[6])
            self.executequery(q)


        def addtoarchive(self, ident):
            """Metoda pozwalająca na przeniesienie wypożyczenia, z rejestru wypożyczeń, do archiwum wypożyczeń w bazie danych"""
            try:
                q = """INSERT archiwum_wypozyczen SELECT * FROM rejestr_wypozyczen WHERE id = %s""" % ident
                q1 = """DELETE FROM rejestr_wypozyczen WHERE id = %s""" % ident
                self.cur.execute(q)
                self.cur.execute(q1)
                self.con.commit()
                print('WYKONANO')
            except mysql.connector.Error as e:
                print("Błąd: {}".format(e.errno))
                try:
                    self.con.rollback()
                except mysql.connector.Error as e:
                    print('Rollback error')
                    print(str(e.errno))


        def archivetorental(self, ident):
            """Metoda pozwalająca na przenisienie wypożyczenia, z archiwum wypożyczeń, do rejestru wypożyczeń w bazie danych"""
            try:
                q = """INSERT rejestr_wypozyczen SELECT * FROM archiwum_wypozyczen WHERE id = %s""" % ident
                q1 = """DELETE FROM archiwum_wypozyczen WHERE id = %s""" % ident
                self.cur.execute(q)
                self.cur.execute(q1)
                self.con.commit()
                print('WYKONANO')
            except mysql.connector.Error as e:
                print("Błąd: {}".format(e.errno))
                try:
                    self.con.rollback()
                except mysql.connector.Error as e:
                    print('Rollback error')
                    print(str(e.errno))


        def addcopyofthefilm(self, filmid, condition):
            """Metoda pozwalająca dodanie egzemplarza istniejącego już filmu w bazie danych"""
            q = """INSERT INTO egzemplarze(film_ID, stan) VALUES('%s','%s')""" % (filmid, condition)
            self.executequery(q)


        def addactor(self, name):
            """Metoda pozwalająca na dodanie nowego aktora do bazy danych"""
            q = """INSERT INTO aktorzy(aktor) VALUES('%s')""" % name
            self.executequery(q)


        def adddirector(self, name):
            """Metoda pozwalająca na dodanie nowego reżysera do bazy danych"""
            q = """INSERT INTO rezyserzy(rezyser_filmu) VALUES('%s')""" % name
            self.executequery(q)


        def addgenre(self, name):
            """Metoda pozwalająca na dodanie nowego gatunku filmu do bazy danych"""
            q = """INSERT INTO gatunki(gatunek_filmu) VALUES('%s')""" % name
            self.executequery(q)


        def addcategory(self, name):
            """Metoda pozwalająca na dodanie nowej kategorii filmu do bazy danych"""
            q = """INSERT INTO kategorie(kategoria_filmu) VALUES('%s')""" % name
            self.executequery(q)


        def addcarrier(self, name):
            """Metoda pozwalająca na dodanie nowego nośnika filmu do bazy danych"""
            q = """INSERT INTO nosniki(nosnik_filmu) VALUES('%s')""" % name
            self.executequery(q)


        def addproduction(self, name):
            """Metoda pozwalająca na dodanie nowej produkcji filmu do bazy danych"""
            q = """INSERT INTO produkcje(produkcja_filmu) VALUES('%s')""" % name
            self.executequery(q)


        def addactortofilm(self, filmid, actorid):
            """Metoda pozwalająca na powiązanie aktora z istniejącym filmem w bazie danych"""
            q = """INSERT INTO film_aktorzy(ID_filmu, ID_aktora) VALUES('%s', '%s')""" % (filmid, actorid)
            self.executequery(q)


        def selectactors(self, ident):
            """Metoda pozwalająca na wyświetlenie aktora z bazy danych"""
            q = """\
            SELECT aktorzy.aktor FROM filmy INNER JOIN film_aktorzy ON filmy.ID_filmu = film_aktorzy.ID_filmu
            INNER JOIN aktorzy ON aktorzy.id = film_aktorzy.ID_aktora AND filmy.ID_filmu = %s""" % ident
            self.view(q)


        def selectfilm(self, ident):
            """Metoda pozwalająca na wyświetlenie pełnych informacji o filmie z bazy danych"""
            q = """\
            SELECT filmy.ID_filmu, filmy.tytul_filmu, filmy.rok_wydania, filmy.cena_zakupu_filmu, filmy.krotki_opis_filmu, rezyserzy.rezyser_filmu, gatunki.gatunek_filmu, produkcje.produkcja_filmu, nosniki.nosnik_filmu,  kategorie.kategoria_filmu
            FROM filmy JOIN rezyserzy ON rezyserzy.id = filmy.ID_rezysera
            JOIN gatunki ON gatunki.id = filmy.ID_gatunku
            JOIN produkcje ON produkcje.id = filmy.ID_produkcji
            JOIN nosniki ON nosniki.id = filmy.ID_nosnika
            JOIN kategorie ON kategorie.id = filmy.ID_kategorii AND filmy.ID_filmu = %s""" % ident
            self.view(q)
            self.selectactors(ident)


        def viewcopy(self, ident):
            """Metoda pozwalająca na wyświetlenie informacji o kopii danego filmu w bazie danych"""
            q = """\
            SELECT egzemplarze.ID_egzemplarza, filmy.tytul_filmu, egzemplarze.stan FROM egzemplarze
            JOIN filmy ON filmy.ID_filmu = egzemplarze.film_ID AND egzemplarze.ID_egzemplarza = %s""" % ident
            self.view(q)


        def viewallcopys(self,ident):
            """Metoda pozwalająca na wyświetlenie wszystkich istniejących kopii danego filmu w bazie danych"""
            q = """\
            SELECT egzemplarze.ID_egzemplarza, filmy.tytul_filmu, egzemplarze.stan FROM egzemplarze
            JOIN filmy ON filmy.ID_filmu = egzemplarze.film_ID AND filmy.ID_filmu = %s""" % ident
            self.view(q)


        def deletefilm(self, ident):
            """Metoda pozwalająca na usunięcie filmu z bazy danych"""
            q = """\
            DELETE FROM filmy WHERE ID_filmu = '%s'""" % ident
            self.selectfilm(ident)
            print('USUNĄĆ FILM? T/N')
            pick = raw_input()

            if pick == 'T':
                self.executequery(q)
            elif pick == 'N':
                print('ANULOWANO')
            else:
                print('BLEDNY ZNAK')


        def deletecopy(self, ident):
            """Metoda pozwalająca na usunięcie kopii filmu z bazy danych"""
            q = """\
            DELETE FROM egzemplarze WHERE ID_egzemplarza = '%s'""" % ident
            self.viewcopy(ident)
            print('USUNĄĆ KOPIE? T/N')
            pick = raw_input()

            if pick == 'T':
                self.executequery(q)
            elif pick == 'N':
                print('ANULOWANO')
            else:
                print('BLEDNY ZNAK')


        def deleteclient(self, ident):
            """Metoda pozwalająca na usunięcie klienta z bazy dancyh"""
            q = """\
            DELETE FROM wypozyczajacy WHERE Nr_karty_wypozyczajacego= '%s'""" % ident
            self.showclientinfo(ident)
            print('USUNĄĆ KLIENTA? T/N')
            pick = raw_input()

            if pick == 'T':
                self.executequery(q)
            elif pick == 'N':
                print('ANULOWANO')
            else:
                print('BLEDNY ZNAK')

        def showrental(self, ident):
            """Metoda pozwalająca na wyświetlenie wypożyczeń z rejestru wypożyczeń w bazie danych"""
            q = """SELECT * FROM rejestr_wypozyczen WHERE id = %s""" % ident
            self.view(q)

        def showarchive(self, ident):
            """Metoda pozwalająca na wyświetlenie wypożyczeń z archiwum wypożyczeń w bazie danych"""
            q = """SELECT * FROM archiwum_wypozyczen WHERE id = %s""" % ident
            self.view(q)

        def addtoblacklist(self, ident):
            """Metoda pozwalająca na dodanie klienta do czarnej listy w bazie danych"""
            q = """UPDATE wypozyczajacy SET czy_jest_na_czarnej_liscie = 1 WHERE Nr_karty_wypozyczajacego = %s""" % ident
            self.executequery(q)

        def deletefromblacklist(self, ident):
            """Metoda pozwalająca na usunięcie klienta z czarnej listy w bazie danych"""
            q = """UPDATE wypozyczajacy SET czy_jest_na_czarnej_liscie = 0 WHERE Nr_karty_wypozyczajacego = %s""" % ident
            self.executequery(q)

        def quickcontact(self):
            """Metoda pozwalająca na wyświetlenie imienia i nazwiska klienta oraz przypisanego do niego nr. tel. przy pomocy procedury w bazie danych"""
            self.cur.callproc('find_all')
            for result in self.cur.stored_results():
                print(result.fetchall())


        ################# MENU ########################

        def main_menu(self):
            """Metoda pozwalająca na wyświetlenie menu głównego aplikacji"""
            print("Wybierz sekcję, do której chcesz przejść:")
            print("1. Dodaj...")
            print("2. Pokaż...")
            print("3. Usuń...")
            print("4. Zmień/Przenieś...")
            print("\n0. Wyjdź.")
            choice = raw_input(" >>  ")
            self.exec_menu(choice)
            return


        def exec_menu(self, choice):
            """Metoda pozwalająca na wybranie do jakiego podmenu chcemy przejść"""
            ch = choice.lower()
            if ch == '':
                self.menu_actions['main_menu'](self)
            else:
                try:
                    self.menu_actions[ch](self)
                except KeyError:
                    print("Błędny wybór, spróbuj ponownie.\n")
                    self.menu_actions['main_menu'](self)
            return


        def menu1(self):
            """Metoda pozwalająca na wyświetlenie podmenu Dodaj..."""
            print("1. DODAJ KLIENTA")
            print("2. DODAJ FILM")
            print("3. DODAJ KOPIE FILMU")
            print("4. DODAJ WYPORZYCZENIE")
            print("5. DODAJ AKTORA")
            print("6. DODAJ REŻYSERA")
            print("7. DODAJ KATEGORIE")
            print("8. DODAJ GATUNEK")
            print("9. DODAJ NOŚNIK")
            print("10. DODAJ PRODUKCJE")
            print("11. DODAJ AKTORA DO FILMU")
            print("99. WRÓĆ")
            print("0. WYJDŹ")

            choice = int(raw_input(">> "))

            if choice == 1:
                client = [raw_input('NAZWISKO: '), raw_input('IMIĘ: '), raw_input('NUMER DOKUMENTU TOŻSAMOSCI: '), raw_input('PESEL: '), raw_input('ULICA: '),
                          raw_input('MIASTO: '), raw_input('NUMER DOMU: '), raw_input('KOD POCZTOWY: '), raw_input('NUMER MIESZKANIA: '),
                          raw_input('NUMER WOJEWODZTWA: '), raw_input('NUMER KOMÓRKOWY: '), raw_input('DATA URODZENIA (RRRR-MM-DD):'),]
                self.addclient(client)



            elif choice == 2:
                film = [raw_input('TYTUŁ: '), raw_input('ROK PUBLIKACJI: '), raw_input('ID REZYSERA: '), raw_input('ID GATUNKU: '),
                        raw_input('ID PRODUKCJI: '), raw_input('ID NOSNIKA: '), raw_input('ID KATEGORII: '), raw_input('KOSZT ZAKUPU: '),
                        raw_input('KRÓTK OPIS: '), raw_input('DŁUGOŚĆ(GG-MM-SS:')]
                self.addfilm(film)

            elif choice == 3:
                film_id = raw_input('ID FILMU: ')
                condition = raw_input('STAN: ')
                self.addcopyofthefilm(film_id, condition)

            elif choice == 4:
                rental = [raw_input('NUMER KARTY KLIENTA: '), raw_input('ID KOPII FILMU: '), raw_input('DATA WYPOZYCZENIA: '),
                          raw_input('NA ILE DNI: '), raw_input('DATA ODDANIA: '), raw_input('ZAPŁATA: '), raw_input('DOPŁATA: ')]
                self.addrental(rental)

            elif choice == 5:
                input = raw_input('IMIE I NAZWISKO AKTORA: ')
                self.addactor(input)

            elif choice == 6:
                input = raw_input('IMIE I NAZWISKO REZYSERA: ')
                self.adddirector(input)

            elif choice == 7:
                input = raw_input('KATEGORIA FILMU: ')
                self.addcategory(input)

            elif choice == 8:
                input = raw_input('GATUNEK FILMU: ')
                self.addgenre(input)

            elif choice == 9:
                input = raw_input('NOŚNIK FILMU: ')
                self.addcarrier(input)

            elif choice == 10:
                input = raw_input('PRODUKCJA FILMU: ')
                self.addproduction(input)

            elif choice == 11:
                input = raw_input('ID FILMU: ')
                input1 = raw_input('ID AKTORA: ')
                self.addactortofilm(input, input1)
            else:
                self.exec_menu(str(choice))
                return


        def menu2(self):
            """Metoda pozwalająca na wyświetlenie podmenu Wyświetl..."""
            print("1. WYŚWIETL INFORMACJE O FILMIE")
            print("2. WYŚWIETL KOPIE FILMU")
            print("3. WYŚWIETL INFORMACJE O KLIENCIE")
            print("4. WYŚWIETL WYPOŻYCZENIE")
            print("5. WYŚWIETL ARCHIWIWALNE WYPOZYCZENIE")
            print("6. SZYBKI KONTAKT")
            print("99. WRÓĆ")
            print("0. WYJDŹ")

            choice = int(raw_input(">> "))

            if choice == 1:
                input = raw_input('ID FILMU: ')
                self.selectfilm(input)

            elif choice == 2:
                input = raw_input('ID FILMU: ')
                self.viewallcopys(input)

            elif choice == 3:
                input = raw_input('ID KLIENTA: ')
                self.showclientinfo(input)

            elif choice == 4:
                input = raw_input('ID WYPOŻYCZENIA: ')
                self.showrental(input)

            elif choice == 5:
                input = raw_input('ID WYPOŻYCZENIA: ')
                self.showarchive(input)

            elif choice == 6:
                self.quickcontact()

            else:
                self.exec_menu(str(choice))
                return


        def menu3(self):
            """Metoda pozwalająca na wyświetlenie podmenu Usuń..."""
            print("1. USUŃ FILM")
            print("2. USUŃ KOPIE FILMU")
            print("3. USUŃ KLIENTA")
            print("99. WRÓĆ")
            print("0. WYJDŹ")

            choice = int(raw_input(">> "))

            if choice == 1:
                input = raw_input('ID FILMU: ')
                self.deletefilm(input)

            elif choice == 2:
                input = raw_input('ID KOPII: ')
                self.deletecopy(input)

            elif choice == 3:
                input = raw_input('NR KARTY WYPOZYCZAJCEGO: ')
                self.deleteclient(input)
            else:
                self.exec_menu(str(choice))
                return


        def menu4(self):
            """Metoda pozwalająca na wyświetlenie podmenu Zmień/Przenieś..."""
            print("1. PRZENIEŚ WYPOZYCZENIE DO ARCHIWUM")
            print("2. PRZENIEŚ Z ARCHIWUM DO WYPOŻYCZEŃ")
            print("3. DODAJ KLIENTA NA CZARNĄ LISTĘ")
            print("4. USUŃ KLIENTA Z CZARNEJ LISTY")
            print("99. WRÓĆ")
            print("0. WYJDŹ")

            choice = int(raw_input(">> "))

            if choice == 1:
                input = int(raw_input("ID WYPOZYCZENIA: "))
                self.addtoarchive(input)

            elif choice == 2:
                input = int(raw_input("ID WYPOZYCZENIA: "))
                self.archivetorental(input)

            elif choice == 3:
                input = int(raw_input("ID KLIENTA: "))
                self.addtoblacklist(input)

            elif choice == 4:
                input = int(raw_input("ID KLIENTA: "))
                self.deletefromblacklist(input)
            else:
                self.exec_menu(str(choice))
                return


        def back(self):
            """Metoda pozwalająca na wybranie opcji powrotu do menu głównego"""
            self.menu_actions['main_menu'](self)


        def exit(self):
            """Metoda pozwalająca na zamknięcie aplikacji"""
            self.con.close()
            sys.exit()


        menu_actions = {
            'main_menu': main_menu,
            '1': menu1,
            '2': menu2,
            '3': menu3,
            '4': menu4,
            '99': back,
            '0': exit,
        }


if __name__ == "__main__":
    d = DataBase()
    DataBase.main_menu(d)
