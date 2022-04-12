import sqlite3

#The purpose of pet_person is to map owner to pet by ID.

if __name__ == "__main__":

    while True:
        
        con = sqlite3.connect('pets.db')
        ID = input("What is your ID?" + "\n")
        cur = con.cursor()

        if ID == '-1':
            print('Exiting database.')
            raise SystemExit

        if len(ID) == 0:
            print('You did not enter a ID.')
            raise SystemExit

        exists = cur.execute("SELECT first_name,last_name FROM person WHERE id = (?)", ID)
        rows = cur.fetchall()

        if rows != []:
            name = cur.execute("SELECT first_name, last_name, person.age, name, breed,"
                    "pet.age, dead FROM person, pet, person_pet "
                    "WHERE person.id = person_pet.person_id AND "
                    "pet.id = person_pet.pet_id AND person.id=(?)", (ID))
            rows = cur.fetchall() 

        elif rows == []:
            print("User doesn't exist. Exiting database.")
            raise SystemExit

        for row in rows:
            print ("{} {} owned a {} named {}, who was {} years old.".format(row[0], row[1], row[3],row[4],row[5])) 