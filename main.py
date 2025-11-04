import getpass
import oracledb

params = oracledb.ConnectParams(host="bd-dc.cs.tuiasi.ro", port=1539, service_name="orcl")
connection = oracledb.connect(
    user="bd117",
    password="bd117",
    params=params
)

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# Create a table

def dropTablesBefore(cursor):
    # Delete already existing tables if there are
    cursor.execute("drop table Echipe")
    cursor.execute("drop table Jucatoare")
    cursor.execute("drop table Istoric")
    cursor.execute("drop table Sponsori")
    cursor.execute("drop table Sponsorizari")

def createTableEchipe(cursor):
    cursor.execute("""
        CREATE TABLE if not exists Echipe(
        team_id NUMBER(2) CONSTRAINT team_id_pk PRIMARY KEY,
        number_players NUMBER(2),
        team_name VARCHAR2(30) CONSTRAINT echipe_team_name_nn NOT NULL,
        CONSTRAINT echipe_pk PRIMARY KEY (team_id)
    )""")
    print('ok1')
    # Insert some data
    cursor.execute("""INSERT INTO Echipe VALUES (1, 15, 'CSM_BUCURESTI')""")
    cursor.execute("""INSERT INTO Echipe VALUES (2, 11, 'RAPID_BUCURESTI')""")
    cursor.execute("""INSERT INTO Echipe VALUES (3, 10, 'BISTRITA')""")
    cursor.execute("""INSERT INTO Echipe VALUES (4, 11, 'DUNAREA_BRAILA')""")

#connection.commit()

def createTableJucatoare(cursor):
    cursor.execute("""CREATE TABLE if not exists Jucatoare (
        player_id NUMBER(5) CONSTRAINT player_id_pk PRIMARY KEY,
        player_name VARCHAR2(50) CONSTRAINT player_name_nn NOT NULL,
        salary NUMBER(5),
        origin_country VARCHAR2(40) CONSTRAINT countries_country_name_nn NOT NULL,
        posision VARCHAR2(12), 
        echipa varchar2(30),
        foreign key (echipa) references Echipe(team_name)
    )""")
    print('ok2')
    cursor.execute(
        """INSERT INTO Jucatoare VALUES (3, 'Emilie Artzen', 12000, 'NORVEGIA', 'INTER STANGA', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(8, 'Cristina Neagu', 21500, 'ROMANIA', 'INTER STANGA', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(20, 'Laura Flippes', 7500, 'FRANTA', 'INTER DREAPTA', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(28, 'Monika Kobylińska', 8000, 'POLONIA', 'INTER DREAPTA', 'CSM BUCURESTI')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(1, 'Laura Glauser', 12000, 'FRANTA', 'PORTAR', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(12, 'Marie Davidsen', 6000, 'NORVEGIA', 'PORTAR', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(16, 'Evelina Eriksson', 6000, 'SUEDIA', 'PORTAR', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(18, 'Jennifer Gutiérrez', 4500, 'SPANIA', 'EXTREMA STANGA', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(21, 'Alexandra Dindiligan', 6500, 'ROMANIA', 'EXTREMA STANGA', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(14, 'Željka Nikolić', 4500, 'SERBIA', 'EXTREMA DREAPTA', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(25, 'Trine Østergaard', 5000, 'DANEMARCA', 'EXTREMA DREAPTA', 'CSM BUCURESTI')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(7, 'Grâce Zaadi', 10000, 'FRANTA', 'CENTRU', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(17, 'Elizabeth Omoregie', 8000, 'SLOVENIA', 'CENTRU', 'CSM BUCURESTI')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(51, 'Vilde Ingstad', 9000, 'NORVEGIA', 'PIVOT', 'CSM BUCURESTI')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(77, 'Crina Pintea', 10000, 'ROMANIA', 'PIVOT', 'CSM BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(22, 'Orlane Kanor', 6000, 'FRANTA', 'INTER STANGA', 'RAPID BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(88, 'Anđela Janjušević', 3500, 'SERBIA', 'INTER DREAPTA', 'RAPID BUCURESTI')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(12, 'Diana Ciucă', 6000, 'ROMANIA', 'PORTAR', 'RAPID BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(23, 'Ivana Kapitanović', 6000, 'CROATIA', 'PORTAR', 'RAPID BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(20, 'Dorina Korsós', 3000, 'UNGARIA', 'EXTREMA STANGA', 'RAPID BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(17, 'Marta López', 4500, 'SPANIA', 'EXTREMA DREAPTA', 'RAPID BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(77, 'Alexandra Badea', 2000, 'ROMANIA', 'EXTREMA DREAPTA', 'RAPID BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(7, 'Eliza Buceschi', 7000, 'ROMANIA', 'CENTRU', 'RAPID BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(34, 'Alicia Fernández', 5000, 'SPANIA', 'CENTRU', 'RAPID BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(10, 'Albertina Kassoma', 3500, 'ANGOLA', 'PIVOT', 'RAPID BUCURESTI')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(27, 'Lorena Ostase', 2000, 'ROMANIA', 'PIVOT', 'RAPID BUCURESTI')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(29, 'Gnonsiane Niombla', 5000, 'SENEGAL', 'INTER STANGA', 'BISTRITA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(14, 'Bianca Bazaliu', 3500, 'ROMANIA', 'INTER STANGA', 'BISTRITA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(98, 'Seynabou Mbengue', 1500, 'SPANIA', 'INTER DREAPTA', 'BISTRITA')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(20, 'Iulia Dumanska', 4000, 'ROMANIA', 'PORTAR', 'BISTRITA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(2, 'Nicoleta Dincă', 3500, 'ROMANIA', 'EXTREMA STANGA', 'BISTRITA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(30, 'Sonia Seraficeanu', 3000, 'ROMANIA', 'EXTREMA DREAPTA', 'BISTRITA')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(4, 'Laura Pristăvița', 6500, 'ROMANIA', 'CENTRU', 'BISTRITA')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(13, 'Cristina Laslo', 7000, 'ROMANIA', 'CENTRU', 'BISTRITA')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(7, 'Tamires Araújo', 4000, 'BRAZILIA', 'PIVOT', 'BISTRITA')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(31, 'Ida-Marie Dahl', 4500, 'DANEMARCA', 'PIVOT', 'BISTRITA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(5, 'Alexandra Severin, 2000, 'ROMANIA', 'INTER STANGA'', 'DUNAREA BRAILA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(99, 'Mireya Gonzalez', 2500, 'SPANIA', 'INTER DREAPTA'', 'DUNAREA BRAILA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(9, 'Jelena Lavko', 3000, 'SERBIA', 'INTER DREAPTA'', 'DUNAREA BRAILA')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(1, 'Elena Șerban', 2500, 'ROMANIA', 'PORTAR'', 'DUNAREA BRAILA')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(44, 'Kira Trusova', 1500, 'RUSIA', 'PORTAR'', 'DUNAREA BRAILA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(89, 'Corina Lupei', 1500, 'ROMANIA', 'EXTREMA STANGA'', 'DUNAREA BRAILA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(2, 'Aneta Udriștioiu', 5000, 'ROMANIA', 'EXTREMA DREAPTA'', 'DUNAREA BRAILA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(8, 'Kristina Liščević', 4000, 'ROMANIA', 'CENTRU'', 'DUNAREA BRAILA')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(70, 'Andreea Popa', 3500, 'ROMANIA', 'CENTRU'', 'DUNAREA BRAILA')""")
    cursor.execute(
        """INSERT INTO Jucatoare VALUES(24, 'Meike Schmelzer', 3000, 'GERMANIA', 'PIVOT'', 'DUNAREA BRAILA')""")
    cursor.execute("""INSERT INTO Jucatoare VALUES(17, 'Katarina Ježić', 2000, 'CROATIA', 'PIVOT'', 'DUNAREA BRAILA')""")

def createTableIstoric(cursor):
    cursor.execute("""CREATE TABLE if not exists Istoric (
        istoric_id NUMBER(5) CONSTRAINT istoric_id_pk PRIMARY KEY,
        player_name NUMBER(5) CONSTRAINT istoric_player_fk REFERENCES jucatoare(player_id),
        previous_team VARCHAR2(25)
    )""")
    print('ok3')
    cursor.execute("""INSERT INTO Istoric VALUES (1, 'Andreea Popa', 'CSM BUCURESTI')""")
    cursor.execute("""INSERT INTO Istoric VALUES (2, 'Aneta Udriștioiu', 'CSM BUCURESTI')""")
    cursor.execute("""INSERT INTO Istoric VALUES (3, 'Mireya Gonzalez', 'RAPID BUCURESTI')""")
    cursor.execute("""INSERT INTO Istoric VALUES (4, 'Jennifer Gutiérrez', 'RAPID BUCURESTI')""")
    cursor.execute("""INSERT INTO Istoric VALUES (5, 'Alexandra Dindiligan', 'BISTRITA')""")
    cursor.execute("""INSERT INTO Istoric VALUES (6, 'Anđela Janjušević', 'BISTRITA')""")
    cursor.execute("""INSERT INTO Istoric VALUES (7, 'Alexandra Severin', 'BISTRITA')""")
    cursor.execute("""INSERT INTO Istoric VALUES (8, 'Željka Nikolić', 'DUNAREA BRAILA')""")
    cursor.execute("""INSERT INTO Istoric VALUES (9, 'Crina Pintea', 'DUNAREA BRAILA')""")
    cursor.execute("""INSERT INTO Istoric VALUES (10, 'Iulia Dumanska', 'CSM BUCURESTI')""")
    cursor.execute("""INSERT INTO Istoric VALUES (11, 'Kristina Liščević', 'RAPID BUCURESTI')""")

def createTableSponsori(cursor):
    cursor.execute("""CREATE TABLE if not exists Sponsori (
        sponsor_id NUMBER(5) CONSTRAINT sponsori_id_pk PRIMARY KEY,
        nume_sponsor VARCHAR2(50) CONSTRAINT sponsori_nume_nn NOT NULL
    )""")
    print('ok4')
    cursor.execute("""INSERT INTO Sponsori VALUES (1, 'BIANCE')""")
    cursor.execute("""INSERT INTO Sponsori VALUES (2, 'ENGIE')""")
    cursor.execute("""INSERT INTO Sponsori VALUES (3, 'MHS TRUCK')""")

def createTableSponsorizari(cursor):
    cursor.execute("""CREATE TABLE if not exists Sponsorizari (
        sponsorizare_id NUMBER(8) CONSTRAINT sponsorizari_id_pk PRIMARY KEY,
        sponsor_id NUMBER(5) CONSTRAINT sponsorizari_sponsor_fk REFERENCES Sponsori(sponsor_id),
        team_id NUMBER(2) CONSTRAINT sponsorizari_echipa_fk REFERENCES Echipe(team_id),
        CONSTRAINT sponsorizari_sponsor_team_uniq UNIQUE (sponsor_id, team_id)
    )""")
    print('ok5')
    cursor.execute("""INSERT INTO Sponsorizari VALUES (1, 1, 1)""")
    cursor.execute("""INSERT INTO Sponsorizari VALUES (2, 1, 2)""")
    cursor.execute("""INSERT INTO Sponsorizari VALUES (3, 2, 2)""")
    cursor.execute("""INSERT INTO Sponsorizari VALUES (4, 2, 3)""")
    cursor.execute("""INSERT INTO Sponsorizari VALUES (5, 1, 4)""")
    cursor.execute("""INSERT INTO Sponsorizari VALUES (6, 3, 4)""")


#cursor.execute("""SELECT * FROM Jucatoare WHERE origin_country = 'ROMANIA'""")
#cursor.execute("""SELECT * FROM Jucatoare WHERE salary BETWEEN 1000 AND 5000""")
#cursor.execute("""SELECT Sponsori.nume_sponsor
#FROM Sponsori
#JOIN Sponsorizari ON Sponsori.sponsor_id = Sponsorizari.sponsor_id
#WHERE Sponsorizari.team_id = 1""")
#cursor.execute("""SELECT Jucatoare.player_name, SUM(Jucatoare.salary * 12) AS total_salary_per_year
#FROM Jucatoare
#WHERE Jucatoare.player_name = 'Cristina Neagu'
#GROUP BY Jucatoare.player_name""")
#cursor.execute("""INSERT INTO Istoric (istoric_id, player_name, previous_team)
#VALUES
 # (11, 'Cristina Neagu', 'CSM BUCURESTI'),
  #(12, 'Laura Flippes', 'CSM BUCURESTI'),
  #(13, 'Anđela Janjušević', 'RAPID BUCURESTI')""")
#cursor.execute("""INSERT INTO Echipe (team_id, number_players, team_name)
#VALUES
 # (5, 12, 'NEW TEAM 1'),
  #(6, 14, 'NEW TEAM 2'),
  #(7, 10, 'NEW TEAM 3')""")
#cursor.execute("""DELETE FROM Istoric
#WHERE player_name = 'Cristina Neagu'""")




connection.commit()


def main():
    try:


        # Drop tables

        #dropTablesBefore(cursor)


        # Create tables
        createTableEchipe(cursor)
        print('ok1')
        createTableJucatoare(cursor)
        print('ok2')
        createTableIstoric(cursor)
        print('ok3')
        createTableSponsori(cursor)
        createTableSponsorizari(cursor)

        # Perform some queries
        cursor.execute("""SELECT * FROM Jucatoare WHERE origin_country = 'ROMANIA'""")
        print(cursor.fetchall())

        cursor.execute("""SELECT * FROM Jucatoare WHERE salary BETWEEN 1000 AND 5000""")
        print(cursor.fetchall())

        cursor.execute("""SELECT Jucatoare.player_name, SUM(Jucatoare.salary * 12) AS total_salary_per_year
                          FROM Jucatoare
                          WHERE Jucatoare.player_name = 'Cristina Neagu'
                          GROUP BY Jucatoare.player_name""")
        print(cursor.fetchall())

        # Commit the changes
        connection.commit()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()