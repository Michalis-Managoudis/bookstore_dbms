import mysql.connector
from prettytable import PrettyTable
#
#-----------------------------------------------------------------------------------------------
'''Λεξικά'''
#-----------------------------------------------------------------------------------------------

d_tables = {
    "ergazomenoi" : "Eργαζόμενοι", "Exei" : "Έχει", "Ekdosi " : "Έκδοση", "TilefonaE" : "Τηλέφωνα Εργαζομένων", "Biblio " : "Βιβλίο",
    "Graftike_Apo " : "Γράφτηκε από", "Siggrafeas " : "Συγγραφέας", "Agorazoun ": "Αγοράζουν", "Anikei" : "Ανοίκει", "Apothema" : "Απόθεμα",
    "Brabeia " : "Βραβεία", "Katigoria" : "Κατηγορία", "Partida " : "Παρτίδα", "Pelatis" : "Πελάτης", "Pragmateuetai": "Πραγματεύεται",
    "Thema": "Θέμα", "TilefonaP " : "Τηλέφωνα Πελατών", "TilefonaS" : "Τηλέφωνα Συγγραφφέων", "Typos" : "Τύπος"
    }

d_pk = {
    "Ergazomenoi" : "id_ergazomenou",
    "Exei" : ["id_ergazomenou","id_ekdosis"],
    "Ekdosi" : "id_ekdosis",
    "TilefonaE" : ["id_ergazomenou","Etilefono"],
    "Biblio" : "id_bibliou",
    "Graftike_Apo" : ["id_bibliou","id_siggrafea"],
    "Siggrafeas" : "id_siggrafea",
    "Agorazoun": ["id_apothematos","id_pelati","im_agoras"],
    "Anikei" : ["id_thematos","id_katigorias"],
    "Apothema" : "id_apothematos",
    "Brabeia" : "brabeio",
    "Katigoria" : "id_katigorias",
    "Partida" : ["id_ekdosis","aa"],
    "Pelatis" : "id_pelati",
    "Pragmateuetai": ["id_bibliou","id_thematos"],
    "Thema": "id_thematos",
    "TilefonaP" : ["id_pelati","Ptilefono"],
    "TilefonaS" : ["id_siggrafea","Stilefono"],
    "Typos" : ["id_ekdosis","Etypos"]
    }

d_a = {
    "id_bibliou": "ID βιβλίου", "titlos": "Τίτλος", "perigrafi" : "Περιγραφή", "glossa_prototypou" : "Γλώσσα Προτοτύπου", "metafrasmeno" : "Μεταφρασμένο",
    "etos_kikloforias" : "Έτος κυκλοφορίας", "best_seller" : "Καλύτερες Πολήσεις", "url_ekdosis" : "URL Έκδοσης", "ISBN" : "ISBN", "eksofyllo" : "Εξώφυλλο",
    "bibliodesia" : "Βιβλιοδεσία", "selides" : "Σελίδες", "poiotita_fyllou" : "Ποιότητα Φύλλου", "melani" : "Μελάνι", "megethos_selidas" : "Μέγεθος σελίδας",
    "varos_fyllou" : "Βάρος φύλλου", "id_siggrafea" : "ID Συγγραφέα", "AFM" : "ΑΦΜ", "onoma" : "Όνομα", "eponimo" : "Επώνυμο", "fylo" : "Φύλο", "aa" : "ΑΑ", 
    "ethnikotita" : "Εθνικότητα", "xora" : "Χώρα", "poli" : "Πόλη", "dieuthinsi" : "Διεύθυνση", "TK" : "ΤΚ", "email" : "e-mail", "IBAN" : "ΙΒΑΝ", "idiotita" : "Ιδιότητα",
    "Konoma" : "Όνομα Κατηγορίας", "Tonoma" : "Όνομα Θέματος", "id_thematos" : "ID Θέματος", "id_katigorias" : "ID Κατηγορίας ", "Stilefono" : "Τηλέφωνο Συγγραφέα",
    "id_ergazomenou" : "ID Εργαζόμενου", "typeErgazomenou" : "Τύπος Εργαζόμενου", "Etilefono" : "Τηλέφωνο Εργαζόμενου", "Apothema" : "Απόθεμα", "id_apothematos" : "ID Αποθέματος",
    "posotita_apothematos" : "Ποσότητα σε απόθεμα", "timi_lianikis" : "Τιμή Λιανικής", "timi_xondrikis" : "Τιμή Χονδρικής", "ekptosi" : "Έκπτωση", "thesi_apothikis" : "Θέση Αποθήκης",
    "id_ekdosis" : "ID Έκδοσης", "id_apothematos" : "ID Αποθέματος", "arithmos_antitipwn" : "Αριθμός Αντιτύπων", "im_tiposis " : "Ημερομηνία Τύπωσης ", "id_pelati" : "ID Πελάτη",
    "eidiki_ekptosi" : "Ειδική Έκπτωση", "typePelati" : "Τύπος Πελάτη", "eponimia_etairias" : "Επωνυμία Εταιρείας", "idiotita_etairias" : "Ιδιότητα Εταιρείας",
    "Ptilefono" : "Τηλέφωνο Πελάτη", "id_thematos" : "ID Θέματος", "brabeio" : "Βραβείο", "Etypos" : "Τύπος Εργαζόμενου", "Proairetiki dieu8insi apostolis" : "Προαιρετική Διεύθυνση Αποστολής",
    "gia agores lianikis" : "Για αγορές Λιανικής", "posotita" : "Ποσότητα", "teliki_timi" : "Τελική Τιμή", "im_agoras" : "Ημερομηνία Αγοράς", "agora_allagis" : "Αγορά από Επιστροφή"
    }

#-----------------------------------------------------------------------------------------------
'''Γενικές-Βασικές Συναρτήσεις'''
#-----------------------------------------------------------------------------------------------
# δημιουργία σύνδεσης με την βάση
def create_connection():
    try:
        conn = mysql.connector.connect(host="localhost",
                                     user="root",passwd="1059398",
                                     database="ekdotikos_oikos")
        return conn
    except mysql.connector.Error as e:
        print("\n",e,"\n")
        
# γενικές επιλογές χρήστη
def choice(conn,c1):
        s_info = '''Πατήστε : \n (1) για Κατάλογο των Βιβλίων, \n (2) για Έκδοση συγκεκριμένου βιβλίου, \n (3) για Ebook, \n (4) για τη ποσότητα και τη τελική τιμή που πουλήθηκαν τον Οκτώβρη του 2020, \n (5) για το συγγραφέα που έχει γράψει τα περισσότερα βιβλία, 
 (6) για μεταφρασμένα βιβλία, \n (7) για όλα τα βιβλία της κατηγορίας, \n (8) για όλα τα βιβλία με θέμα..., \n (9) για τα θέματα που ανήκουν στην κατηγορία..., \n (10) για το συγγραφέα του βιβλίου..., 
 (11) για τους εργαζόμενους που δούλεψαν στην έκδοση ... του βιβλίου ..., \n (12) για τα best seller βιβλία, \n (13) για τα βραβευμένα βιβλία, \n (14) για τις συνολικές παρτίδες στην έκδοση ... του βιβλίου ..., \n (15) για όλες τις εκδόσεις του βιβλίου ... στο απόθεμα και τη ποσότητα του καθένα, σε φθίνουσα σειρά, 
 (16) για τη ποσότητα σε απόθεμα της ... έκδοσης του βιβλίου ..., \n (17) για τους συχνούς πελάτες λιανικής, δηλαδή αυτούς που αγόρασαν 5 βιβλία τo προηγούμενο χρόνο, \n (18) για όλους τους πελάτες χονδρικής [σε φθίνουσα σειρά βάση της συνολικής ποσότητας βιβλίων που έχουν αγοράσει], \n (19) για τα βασικά γνωρίσματα ενός πίνακα..., \n (20) για όλα τα γνωρίσματα για μία εγγραφή ενός πίνακα..., \n (0) για Έξοδο \n\n --> '''
        
        if c1 == 1 :   insert_choice(conn)
        elif c1 == 2 : update_choice(conn)
        elif c1 == 3 : delete_choice(conn)
        
        elif c1 == 4 :
            c = input(s_info)
            if c.isdigit(): # επιλογές εμφάνισης δεδομένων
                c=int(c)
                if c == 1: e1(conn)
                elif c == 2: e2(conn)
                elif c == 3: e3(conn)
                elif c == 4: e4(conn)
                elif c == 5: e5(conn)
                elif c == 6: e6(conn)
                elif c == 7: e7(conn)
                elif c == 8: e8(conn)
                elif c == 9: e9(conn)
                elif c == 10: e10(conn)
                elif c == 11: e11(conn)
                elif c == 12: e12(conn)
                elif c == 13: e13(conn)
                elif c == 14: e14(conn)
                elif c == 15: e15(conn)
                elif c == 16: e16(conn)
                elif c == 17: e17(conn)
                elif c == 18: e18(conn)
                elif c == 19:
                    tab = input("Πίνακας : ")
                    print_info(conn, d_pk[tab], tab)
                elif c == 20:
                    tab = input("Πίνακας : ")
                    val = input("Κλειδιά του πίνακα χωρισμένα με κόμμα ")
                    if not val.isdigit() :
                        val=val.split(",")
                        val[2]="'"+val[2]+"'"
                    print_detailed_info(conn, tab, d_pk[tab], val)
                else: return

# επιστρέφει τα μεταφρασμένα γνωρίσματα
def trnslt(attributes):
    att=[]
    for m in attributes:
        att.append(d_a[m])
    x = PrettyTable(att)
    return x
     
# τυπώνει τα βασικά γνωρίσματα ενός πίνακα
def print_info(db, attributes, table):
    try:
        cur = db.cursor()
        if type(attributes) == str : attributes = [attributes]
        
        x = trnslt(attributes) # translate
        
        attributes = ", ".join(attributes) # transform data for sql
        
        cur.execute("SELECT "+attributes+" FROM "+table+";") #Κώδικας SQL
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data) # display
            data = cur.fetchone()
        print (x,"\n") # display
    except mysql.connector.Error as e:
        print("\n",e,"\n")
        
    finally:
        cur.close()

# τυπώνει όλα τα γνωρίσματα για μία εγγραφή ενός πίνακα
def print_detailed_info(db, table, id_name, id_value):
    attributes=[]
    print(id_value)
    
    try:
        cur = db.cursor()
        cur.execute("SHOW COLUMNS FROM "+table+";") #get columns names
        for i in cur: # transform data for sql
            attributes.append(i[0])
            
        x = trnslt(attributes) # translate

        if table == "Agorazoun" :
            cur.execute("SELECT * FROM "+table+" WHERE "+id_name[0]+"="+id_value[0]+" AND "+id_name[1]+"="+id_value[1]+" AND "+id_name[2]+"="+id_value[2]+";") #Κώδικας SQL 
        elif type(id_name) == str :
            cur.execute("SELECT * FROM "+table+" WHERE "+id_name+"="+id_value+";") #Κώδικας SQL
        elif type(id_name) == list :
            cur.execute("SELECT * FROM "+table+" WHERE "+id_name[0]+"="+id_value[0]+" AND "+id_name[1]+"="+id_value[1]+";") #Κώδικας SQL
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)# display
            data = cur.fetchone()
        print (x,"\n")# display
    except mysql.connector.Error as e:
        print("\n",e,"\n")
        
    finally:
        cur.close()

#-----------------------------------------------------------------------------------------------
'''Insert'''
#-----------------------------------------------------------------------------------------------

def insert_(db, table):
    attributes =[]
    values = []
    try:
        cur = db.cursor()
        cur.execute("SHOW COLUMNS FROM "+table+";") #get columns names
        for i in cur:
            attributes.append(i[0])
            v = input("Εισάγετε τιμή για το γνώρισμα  "+d_a[i[0]]+" : ")
            values.append(v)
            
        x = trnslt(attributes) # translate
        
        x.add_row(values)
        if table == "Partida":
            val = values[3]
            key = values[2]
        if table == "Agorazoun":
            key1 = values[0]
            key2 = values[1]
            key3 = values[8]
            val = values[6]
            
        # transform data for sql
        values = "', '".join(values)
        values = "'"+values+"'"
        attributes = ", ".join(attributes)
        
        cur.execute("INSERT INTO "+table+" ("+attributes+") VALUES ("+values+");") #Κώδικας SQL
        db.commit()
        if cur.rowcount==1 and table != "Agorazoun": print("\nΕισήχθησε επιτυχώς η γραμμή : \n",x,"\n")
        else: print("Η εισαγωγή στοιχείων απέτυχε!")
        # if tilefono is needed
        if table == "Ergazomenoi": insert_(db,"TilefonaE")
        elif table == "Siggrafeas": insert_(db,"TilefonaS")
        elif table == "Pelatis": insert_(db,"TilefonaP")
        elif table == "Partida": update_apothema(db, key, int(val))

        # Περίπτωση Αγοράς
        elif table == "Agorazoun":
            z = update_apothema(db, key1, -int(val))
            if z == -1: return z
            compute_teliki_timi(db, key1, key2, key3)
            
    except mysql.connector.Error as e:
        print("\n",e,"\n")
        print("Η εισαγωγή στοιχείων απέτυχε!")
        return -1
    finally:
        cur.close()

def insert_choice(conn):
    common = 0
    i_info = '''Πατήστε (για να προσθέσετε νέα δεδομένα) : \n (1) για Βιβλίο, \n (2) για Έκδοση, 
 (3) για Πελάτη, \n (4) για Παρτίδα, \n (5) για Αγορά, \n (6) για Βραβεία, \n (7) για Τηλέφωνο Εργαζομένου, 
 (8) για Τηλέφωνο Συγγραφέα, \n (9) για Τηλέφωνο Πελάτη, \n (10) για Τύπο Εκδοσης, \n (0) για Έξοδο \n\n --> '''
    c = input(i_info)
    if c.isdigit(): # επιλογές εισαγωγής δεδομένων
        c=int(c)
    
        if c == 0 : return
        elif c== 1 : # Νέο Βιβλίο
            z = insert_(conn, "Biblio")
            if z == -1: return
            a = input("Ο Συγγραφέας είναι ήδη καταχωρημένος στην βάση (Ναι/Όχι);")
            if a != "Ναι": # Νέος συγγραφέας
                z = insert_(conn, "Siggrafeas")
                if z == -1: return
            insert_(conn, "Graftike_Apo")
                
            a = input("Το θέμα είναι ήδη καταχωρημένο στην βάση (Ναι/Όχι);")
            if a != "Ναι": # Νέο Θέμα
                a = input("Η κατηγορία του θέματος είναι ήδη καταχωρημένη στην βάση (Ναι/Όχι);")
                if a != "Ναι": # Νέα Κατηγορία
                    z = insert_(conn, "Katigoria")
                    if z == -1: return

                z = insert_(conn, "Thema")
                if z == -1: return
                z = insert_(conn, "Anikei")
                if z == -1: return
                insert_(conn, "Pragmateuetai")
                    
            insert_(conn, "Pragmateuetai")

        elif c== 2 : # Νέα Έκδοση
            z = insert_(conn, "Ekdosi")
            if z == -1: return
            
            while(input("Προσθήκη νέου εργαζομένου για αυτήν την έκδοση (Ναι/Όχι);")=="Ναι"):
                a = input("Ο Εργαζόμενος είναι ήδη καταχωρημένος στην βάση (Ναι/Όχι);")
                if a != "Ναι": # Νέος εργαζόμενος
                    z = insert_(conn, "Ergazomenoi")
                    if z == -1: return
                insert_(conn, "Exei")

            while(input("Προσθήκη νέου τύπου για αυτήν την έκδοση (Ναι/Όχι);")=="Ναι"):
                    z = insert_(conn, "Typos")
            
        elif c== 3 : # Νέος Πελάτης
            t = "Pelatis"
            common = 1
            
        elif c== 4 : # Νέα Παρτίδα
            a = input("Είναι η πρώτη παρτίδα για αυτήν την έκδοση (Ναι/Όχι);")
            if a == "Ναι": # Νέος συγγραφέας
                print("Δημιουργία νέου αποθέματος")
                insert_(conn, "Apothema") #new apothema
            print("Δημιουργία νέας παρτίδας")
            insert_(conn, "Partida") 

                    
        elif c== 5 :
            t = "Agorazoun" # update apothema
            common = 1
            
        elif c== 6 :
            t = "Brabeia"
            common = 1
        elif c== 7 :
            t = "TilefonaE"
            common = 1
        elif c== 8 :
            t = "TilefonaS"
            common = 1
        elif c== 9 :
            t = "TilefonaP"
            common = 1
        elif c== 10 :
            t = "Typos"
            common = 1
        else : return
        
        if common == 1: # if simple insert
            insert_(conn, t)
    

#-----------------------------------------------------------------------------------------------
'''Update'''
#-----------------------------------------------------------------------------------------------
def update_apothema(db, key, val):
    # add val to key row
    try:
        cur = db.cursor()
        #get posotita before b_val
        cur.execute("SELECT posotita_apothematos FROM Apothema WHERE id_apothematos="+key+";")#Κώδικας SQL
        b_val = int(cur.fetchone()[0]) # past value
        n_val = str(b_val+val) # new value
        cur.execute("UPDATE Apothema SET posotita_apothematos="+n_val+" WHERE id_apothematos="+key+";")#Κώδικας SQL
        db.commit()
        if cur.rowcount==1: print("Το απόθεμα ενημερώθηκε επιτυχώς \n")
        else: print("Η ενημέρωση του αποθέματος απέτυχε!")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
        print("Η ενημέρωση του αποθέματος απέτυχε!")
    finally:
        cur.close()

def compute_teliki_timi(db, key1, key2, key3):
    try:
        cur = db.cursor()
        cur.execute("SELECT typePelati, eidiki_ekptosi FROM Pelatis WHERE id_pelati="+key2+";")#Κώδικας SQL
        data = cur.fetchone()
        # transform data from sql
        t = str(data[0]) 
        ekp = int(data[1])
        
        if t == "X":
            cur.execute("SELECT timi_xondrikis, ekptosi FROM Apothema WHERE id_apothematos="+key1+";")#Κώδικας SQL
        elif t == "L":
            cur.execute("SELECT timi_lianikis, ekptosi FROM Apothema WHERE id_apothematos="+key1+";")#Κώδικας SQL
        data2 = cur.fetchone()

        # transform data from sql
        timi = int(data2[0])
        ekp = ekp + int(data2[1])
        timi = timi * (1 - ekp / 100)
        
        update_(db, "Agorazoun", "teliki_timi", str(timi), ["id_apothematos","id_pelati","im_agoras"], [key1,key2,key3])
        
    except mysql.connector.Error as e:
        print("\n",e,"\n")
        print("Η ενημέρωση του αποθέματος απέτυχε!")
    finally:
        cur.close()

def update_(db, table, attribute, value, id_name, id_value):
    #if table != "Agorazoun":
    x = input("Είστε σίγουρος? (Ναι/Όχι)\n")
    if x != "Ναι" : return
    
    try:
        cur = db.cursor()
        if table == "Agorazoun" :
            cur.execute("UPDATE "+table+" SET "+attribute+"='"+value+"' WHERE "+id_name[0]+"='"+id_value[0]+"' AND "+id_name[1]+"='"+id_value[1]+"' AND "+id_name[2]+"="+id_value[2]+";")#Κώδικας SQL
        elif type(id_name) == str :
            cur.execute("UPDATE "+table+" SET "+attribute+"="+value+" WHERE "+id_name+"="+id_value+";")#Κώδικας SQL
        elif type(id_name) == list :
            cur.execute("UPDATE "+table+" SET "+attribute+"="+value+" WHERE "+id_name[0]+"="+id_value[0]+" AND "+id_name[1]+"="+id_value[1]+";")#Κώδικας SQL
        db.commit()
        if cur.rowcount==1:
            print("Η ενημέρωση στοιχείων πέτυχε \n")
            print_detailed_info(db,table, id_name, id_value)
        else: print("Η ενημέρωση στοιχείων απέτυχε!")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
        print("Η ενημέρωση στοιχείων απέτυχε!")
    finally:
        cur.close()
        
def update_choice(conn):
    u_info = '''Πατήστε (για να ενημερώσετε δεδομένα) : \n (1) για Εργαζόμενους, \n (2) για Συγγραφέα, 
 (3) για Έκδοση, \n (4) για Βιβλίο, \n (5) για Πελάτη, \n (6) για Απόθεμα, \n (7) για Βραβείο, 
 (8) για Θέμα, \n (9) για Κατηγορία, \n (10) για Αγορά, \n (11) για Τηλέφωνο Εργαζομένου, 
 (12) για Τηλέφωνο Συγγραφέα, \n (13) για Τηλέφωνο Πελάτη, \n (14) για Σχέση Εργαζομένου-Έκδοσης, 
 (15) για Σχέση Συγγραφέα-Βιβλίου, \n (16) για Τύπο Εκδοσης, \n (17) για Σχέση Βιβλίου-Θέματος, 
 (18) για Σχέση Θέματος-Κατηγορίας, \n (19) για Παρτίδα, \n (0) για Έξοδο \n\n --> '''
    
    c = input(u_info)
    if c.isdigit(): # επιλογές ενημέρωσης δεδομένων
        c=int(c)

        if c == 0 : return
        elif c == 1 :
            t = "Ergazomenoi"
            a = [d_pk[t],"AFM","onoma","eponimo","typeErgazomenou"]
        elif c == 2 :
            t = "Siggrafeas"
            a = [d_pk[t],"AFM","onoma","eponimo"]
        elif c == 3 :
            t = "Ekdosi"
            a = [d_pk[t],"id_bibliou","ISBN"]
        elif c == 4 :
            t = "Biblio"
            a = [d_pk[t],"titlos"]
        elif c == 5 :
            t = "Pelatis"
            a = [d_pk[t],"onoma","eponimo","typePelati"]
        elif c == 6 :
            t = "Apothema"
            a = [d_pk[t],"thesi_apothikis"]
        elif c == 7 :
            t = "Brabeia"
            a = d_pk[t]
        elif c == 8 :
            t = "Thema"
            a = [d_pk[t],"Tonoma"]
        elif c == 9 :
            t = "Katigoria"
            a = [d_pk[t],"Konoma"]
        elif c == 10 :
            t = "Agorazoun"
            a1,a2,a3=d_pk[t]
            a = [a1,a2,a3,"posotita","teliki_timi"]
        elif c == 11 :
            t = "TilefonaE"
            a = d_pk[t]
        elif c == 12 :
            t = "TilefonaS"
            a = d_pk[t]
        elif c == 13 :
            t = "TilefonaP"
            a = d_pk[t]
        elif c == 14 :
            t = "Exei"
            a = d_pk[t]
        elif c == 15 :
            t = "Graftike_Apo"
            a = d_pk[t]
        elif c == 16 :
            t = "Typos"
            a = d_pk[t]
        elif c == 17 :
            t = "Pragmateuetai"
            a = d_pk[t]
        elif c == 18 :
            t = "Anikei"
            a = d_pk[t]
        elif c == 19 :
            t = "Partida"
            a = d_pk[t]
        else : return
        k = d_pk[t]
            
        print_info(conn, a, t)

        if t=="Agorazoun":
            v = input("Εισάγετε τα 3 Id του πίνακα που θέλετε να ενημερώσετε (χωρισμένα με κόμμα π.χ. 123,456,122) :")
            v = v.split(",")
            v[2] = "'"+v[2]+"'"
            if v[0].isdigit() and v[1].isdigit(): print_detailed_info(conn, t, k, v)
            else:
                print("Σφάλμα τα Id πρέπει να είναι ακέραιοι")
                return
            
            a = input("Εισάγετε το πεδίο που θέλετε να ενημερώσετε και την νέα του τιμή (χωρισμένα με κόμμα (π.χ. 'πεδίο,νέα τιμή')) :")
            a = a.split(",") # transform data for sql
            update_(conn,t ,a[0] ,a[1] ,k, v)
            
        elif type(k) == str :
            v = input("Εισάγετε το Id της εγγραφής που θέλετε να ενημερώσετε :")
            if v.isdigit(): print_detailed_info(conn, t, k, v)
            else:
                print("Σφάλμα το Id πρέπει να είναι ακέραιος")
                return

            a = input("Εισάγετε το πεδίο που θέλετε να ενημερώσετε και την νέα του τιμή (χωρισμένα με κόμμα (π.χ. 'πεδίο,νέα τιμή')) :")
            a = a.split(",") # transform data for sql
            a = [a[0],"'"+a[1]+"'"] # transform data for sql
            update_(conn,t ,a[0] ,a[1] ,k, v)
            
        elif type(k) == list :
            v = input("Εισάγετε τα 2 Id του πίνακα που θέλετε να ενημερώσετε (χωρισμένα με κόμμα π.χ. 123,456) :")
            v = v.split(",")
            if t!="Typos":
                if v[0].isdigit() and v[1].isdigit(): print_detailed_info(conn, t, k, v)
                else:
                    print("Σφάλμα τα Id πρέπει να είναι ακέραιοι")
                    return
            else:
                if v[0].isdigit() and (v[1]=="E" or v[1]=="A"): print_detailed_info(conn, t, k, v)
                print("Σφάλμα το Id πρέπει να είναι ακέραιος και ο τύπος βιβλίου 'E' για Ebook ή 'A' για Audiobook (τα 'E' και 'A' στα αγγλικά!)")
                return
            
            a = input("Εισάγετε το πεδίο που θέλετε να ενημερώσετε και την νέα του τιμή (χωρισμένα με κόμμα (π.χ. 'πεδίο,νέα τιμή')) :")
            a = a.split(",") # transform data for sql
            update_(conn,t ,a[0] ,a[1] ,k, v)

#-----------------------------------------------------------------------------------------------
'''Delete'''
#-----------------------------------------------------------------------------------------------
def delete_(db,table,id_name,id_value):
    x = input("Είστε σίγουρος? (Ναι/Όχι)\n")
    if x != "Ναι" : return
    try:
        cur = db.cursor()
        if type(id_name) == str :
            cur.execute("DELETE FROM "+table+" WHERE "+id_name+"="+id_value+";")#Κώδικας SQL
        elif type(id_name) == list :
            cur.execute("DELETE FROM "+table+" WHERE "+id_name[0]+"="+id_value[0]+" AND "+id_name[1]+"="+id_value[1]+";")#Κώδικας SQL
        db.commit()
        if cur.rowcount==1: print("Η διαγραφή ολοκληρώθηκε επιτυχώς \n")
        else: print("Η διαγραφή απέτυχε!")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
        print("Η διαγραφή απέτυχε!")
    finally:
        cur.close()

def delete_choice(conn):

    d_info = '''Πατήστε (για να διαγράψετε δεδομένα) : \n (1) για Εργαζόμενο, \n (2) για Συγγραφέα, 
 (3) για Έκδοση, \n (4) για Βιβλίο, \n (5) για Πελάτη, \n (6) για Απόθεμα, 
 (7) για Τηλέφωνο Εργαζομένου, \n (8) για Τηλέφωνο Συγγραφέα, \n (9) για Τηλέφωνο Πελάτη, 
 (10) για Θέμα, \n (11) για Κατηγορία, \n (12) για Τύπο Έκδοσης, \n (0) για Έξοδο \n\n --> '''
    c = input(d_info)
    if c.isdigit(): # επιλογές διαγραφής δεδομένων
        c=int(c)
    
        if c == 0 : return
        elif c== 1 :
            t = "Ergazomenoi"
            a = [d_pk[t],"AFM","onoma","eponimo","typeErgazomenou"]
        elif c== 2 :
            t = "Siggrafeas"
            a = [d_pk[t],"AFM","onoma","eponimo"]
        elif c== 3 :
            t = "Ekdosi"
            a = [d_pk[t],"id_bibliou","aa","ISBN"]
        elif c== 4 :
            t = "Biblio"
            a = [d_pk[t],"titlos"]
        elif c== 5 :
            t = "Pelatis"
            a = [d_pk[t],"onoma","eponimo","typePelati"]
        elif c== 6 :
            t = "Apothema"
            a = [d_pk[t],"thesi_apothikis"]
        elif c== 7 : t = "TilefonaE"
        elif c== 8 : t = "TilefonaS"
        elif c== 9 : t = "TilefonaP"
        elif c== 10 :
            t = "Thema"
            a = [d_pk[t],"Tonoma"]
        elif c== 11 :
            t = "Katigoria"
            a = [d_pk[t],"Konoma"]
        elif c== 12 : t = "Typos"
        else : return
        n = d_pk[t]
        
        if type(n) == str :
            print_info(conn, a, t)
            i = input("Εισάγετε το Id της εγγραφής που θέλετε να διαγράψετε :")
            if i.isdigit(): delete_(conn,t ,n ,i )
            else: print("Σφάλμα το Id πρέπει να είναι ακέραιος")
        elif type(n) == list :
            if t == "Agorazoun" :
                print_info(conn, a, t)
            else:
                print_info(conn, n, t)
            i = input("Εισάγετε το πεδίο που θέλετε να ενημερώσετε και την νέα του τιμή (χωρισμένα με κόμμα (π.χ. 'πεδίο,νέα τιμή')) :")
            i = i.split(",") # transform data for sql
            if t!="Typos":
                if i[0].isdigit() and i[1].isdigit(): delete_(conn,t ,n ,i )
                else: print("Σφάλμα τα Id πρέπει να είναι ακέραιοι")
            else:
                if i[0].isdigit() and (i[1]=="E" or i[1]=="A"): delete_(conn,t ,n ,i )
                else: print("Σφάλμα το Id πρέπει να είναι ακέραιος και ο τύπος βιβλίου 'E' για Ebook ή 'A' για Audiobook (τα 'E' και 'A' στα αγγλικά!)")
            
#-----------------------------------------------------------------------------------------------
'''Τυπικά Σενάρια'''
#-----------------------------------------------------------------------------------------------
#0-
def print_perigrafi_of_book(db):
    e1(db)
    _id = input("Τύπωσε περιγραφή του βιβλίου με id : ")
    try:
        cur = db.cursor()
        cur.execute("SELECT id_bibliou, titlos, perigrafi FROM Biblio WHERE id_bibliou="+_id+";") #Κώδικας SQL
        x = PrettyTable(["ID", "Titlos", "Perigrafi"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()
        
#1-
def e1(db):
    try:
        cur = db.cursor()
        cur.execute("SELECT id_bibliou, titlos FROM Biblio ORDER BY id_bibliou;") #Κώδικας SQL
        x = PrettyTable(["ID", "Τίτλος"])# display
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)# display
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()
        
#2-
def e2(db):
    e1(db)
    _id = input("Τίτλος βιβλίου : ")
    try:
        cur = db.cursor()
        cur.execute("SELECT aa, ISBN FROM Ekdosi WHERE id_bibliou=(SELECT id_bibliou FROM Biblio WHERE titlos='"+_id+"');")#Κώδικας SQL
        x = PrettyTable(["Έκδοση", "ISBN"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)# display
            data = cur.fetchone()
        print (x,"\n")# display
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()
     
#3-
def e3(db):
    try:
        cur = db.cursor()
        print("\n Audiobooks : ")
        x = PrettyTable(["Τίτλος"])
        cur.execute('''SELECT titlos FROM Biblio WHERE id_bibliou IN (SELECT id_bibliou FROM Ekdosi WHERE id_ekdosis IN (SELECT id_ekdosis FROM Typos WHERE Etypos="A"));''' ) #Κώδικας SQL
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#4-
def e4(db):
    try:
        cur = db.cursor()
        x = PrettyTable(["Τίτλος"])
        cur.execute("SELECT id_pelati, sum(posotita) AS agores FROM Agorazoun WHERE DATE_FORMAT(im_agoras,'%Y-%m')='2020-10' AND agora_allagis=0 GROUP BY id_pelati;" ) #Κώδικας SQL
        x = PrettyTable(["ID Πελάτη","Αγορές"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#5-
def e5(db):
    try:
        cur = db.cursor()
        x = PrettyTable(["ID Συγγραφέα"])
        cur.execute("SELECT id_siggrafea FROM Graftike_Apo GROUP BY id_siggrafea HAVING COUNT(id_siggrafea)=(SELECT COUNT(id_siggrafea) AS max_ekdoseis FROM Graftike_Apo GROUP BY id_siggrafea ORDER BY max_ekdoseis DESC LIMIT 1);") #Κώδικας SQL
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#6-
def e6(db):
    try:
        cur = db.cursor()
        cur.execute("SELECT titlos FROM Biblio WHERE metafrasmeno=1;") #Κώδικας SQL
        x = PrettyTable(["Τίτλος"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#7-
def e7(db):
    katigoria = input("Τύπωσε όλα τα βιβλία της κατηγορίας : ")
    try:
        cur = db.cursor()
        cur.execute("SELECT b.titlos FROM Biblio AS b WHERE b.id_bibliou IN (SELECT p.id_bibliou FROM (Pragmateuetai AS p JOIN Thema AS t ON p.id_thematos=t.id_thematos) WHERE t.id_thematos IN (SELECT id_thematos FROM (Anikei AS a JOIN Katigoria AS k ON a.id_katigorias=k.id_katigorias) WHERE k.Konoma='"+katigoria+"' ));") #Κώδικας SQL
        x = PrettyTable(["Τίτλος"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#8-        
def e8(db):
    thema = input("Τύπωσε όλα τα βιβλία με θέμα : ")
    try:
        cur = db.cursor()        
        cur.execute("SELECT b.titlos FROM Biblio AS b WHERE b.id_bibliou IN (SELECT p.id_bibliou FROM (Pragmateuetai AS p JOIN Thema AS t ON p.id_thematos=t.id_thematos) WHERE t.Tonoma='"+thema+"');") #Κώδικας SQL
        x = PrettyTable(["Τίτλος"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#9-
def e9(db):
    katigoria = input("Τύπωσε τα θέματα που ανήκουν στην κατηγορία : ")
    try:
        cur = db.cursor()        
        cur.execute("SELECT Tonoma FROM Thema WHERE id_thematos IN (SELECT id_thematos FROM Anikei WHERE id_katigorias=(SELECT id_katigorias FROM Katigoria WHERE Konoma = '"+katigoria+"'));") #Κώδικας SQL
        x = PrettyTable(["Θέμα"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#10-
def e10(db):
    titlos=input("Τύπωσε το συγγραφέα του βιβλίου : ")
    try:
        cur = db.cursor()        
        cur.execute("SELECT onoma, eponimo FROM Siggrafeas WHERE id_siggrafea IN (SELECT id_siggrafea FROM Graftike_Apo WHERE id_bibliou = (SELECT id_bibliou FROM `Biblio` WHERE titlos = '"+titlos+"'));" ) #Κώδικας SQL
        x = PrettyTable(["Όνομα","Επίθετο"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#11-
def e11(db):
    ekdosi=input("Τύπωσε τους εργαζόμενους που δούλεψαν στην έκδοση : ")
    # ekdosi=int(ekdosi, base=10)
    titlos=input("του βιβλίου : ")
    try:
        cur = db.cursor()        
        cur.execute("SELECT onoma, eponimo FROM Ergazomenoi WHERE id_ergazomenou IN (SELECT id_ergazomenou FROM Exei WHERE id_ekdosis = (SELECT id_ekdosis FROM Ekdosi WHERE aa = '"+ekdosi+"' AND id_bibliou=(SELECT id_bibliou FROM `Biblio` WHERE titlos = '"+titlos+"')));") #Κώδικας SQL
        x = PrettyTable(["Όνομα","Επίθετο"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()


#12-
def e12(db):
    try:
        cur = db.cursor()
        cur.execute("SELECT titlos FROM Biblio WHERE id_bibliou = (SELECT id_bibliou FROM Ekdosi WHERE best_seller = 1);") #Κώδικας SQL
        x = PrettyTable(["Τίτλος"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#13-
def e13(db):
    try:
        cur = db.cursor()
        cur.execute("SELECT titlos FROM Biblio WHERE id_bibliou IN (SELECT id_bibliou FROM Brabeia);") #Κώδικας SQL
        x = PrettyTable(["Τίτλος"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#14-
def e14(db):
    ekdosi=input("Τύπωσε τις συνολικές παρτίδες στην έκδοση : ")
    titlos=input("του βιβλίου : ")
    try:
        cur = db.cursor()        
        cur.execute("SELECT aa AS Sinolikes_Partides FROM Partida WHERE id_ekdosis = (SELECT id_ekdosis FROM Ekdosi WHERE aa = '"+ekdosi+"' AND id_bibliou=(SELECT id_bibliou FROM Biblio WHERE titlos = '"+titlos+"')) ORDER BY aa DESC LIMIT 1;") #Κώδικας SQL
        x = PrettyTable(["Παρτίδα"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#15-
def e15(db):
    titlos=input(" Τύπωσε όλες τις εκδόσεις στο απόθεμα και τη ποσότητα της κάθε έκδοσης,  σε φθίνουσα σειρά, του βιβλίου : ")
    try:
        cur = db.cursor()
        cur.execute("SELECT R.id_ekdosis, S.posotita_apothematos FROM (SELECT DISTINCT E.id_ekdosis, E.id_bibliou, P.id_apothematos FROM (Ekdosi as E join Partida as P on E.id_ekdosis=P.id_ekdosis)) as R, Apothema as S WHERE R.id_apothematos=S.id_apothematos AND R.id_bibliou =(SELECT id_bibliou FROM Biblio WHERE titlos = '"+titlos+"') order by S.posotita_apothematos DESC;") #Κώδικας SQL
        x = PrettyTable(["ID Έκδοσης","Ποσότητα"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#16-
def e16(db):
    ekdosi=input("Τύπωσε τη ποσότητα σε απόθεμα της έκδοσης : ")
    titlos=input("του βιβλίου : ")
    try:
        cur = db.cursor()
        cur.execute("SELECT posotita_apothematos FROM Apothema WHERE id_apothematos IN (SELECT id_apothematos FROM Partida WHERE id_ekdosis = (SELECT id_ekdosis FROM Ekdosi WHERE aa= '"+ekdosi+"' AND id_bibliou=(SELECT id_bibliou FROM Biblio WHERE titlos = '"+titlos+"')));") #Κώδικας SQL
        x = PrettyTable(["Ποσότητα"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()       

#17-
def e17(db):
    try:
        cur = db.cursor()
        cur.execute("SELECT id_pelati, sum(posotita) AS agores FROM Agorazoun WHERE DATE_FORMAT(im_agoras,'%Y')=DATE_FORMAT(CURDATE(),'%Y')-1 AND agora_allagis=0 AND id_pelati IN (SELECT id_pelati FROM Pelatis WHERE typePelati = 'Λ' AND id_pelati>0) GROUP BY id_pelati having agores>=5") #Κώδικας SQL
        x = PrettyTable(["ID Πελάτη","Αγορές"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()

#18-
def e18(db):
    try:
        cur = db.cursor()
        cur.execute("SELECT Pel.onoma, Pel.eponimo, sum(Agorazoun.posotita) AS sinolo FROM ((SELECT P.id_pelati, P.onoma, P.eponimo FROM (Pelatis AS P JOIN Agorazoun AS A ON P.id_pelati=A.id_pelati) WHERE P.typePelati =  'Χ' AND A.agora_allagis = 0) AS Pel JOIN Agorazoun ON Pel.id_pelati=Agorazoun.id_pelati ) GROUP BY Pel.id_pelati ORDER BY sinolo DESC;") #Κώδικας SQL
        x = PrettyTable(["Όνομα","Επίθετο","Ποσότητα"])
        data = cur.fetchone() #Διαλέγει πλειάδα
        while data is not None:
            x.add_row(data)
            data = cur.fetchone()
        print (x,"\n")
    except mysql.connector.Error as e:
        print("\n",e,"\n")
    finally:
        cur.close()


#-----------------------------------------------------------------------------------------------
'''Main'''
#-----------------------------------------------------------------------------------------------
    
def main():
    conn = create_connection()
    
    while True:
        info = '''Πατήστε : \n (1) για Εισαγωγή, \n (2) για Ενημέρωση, \n (3) για Διαγραφή, \n (4) για Πληροφορίες Εγγραφών, \n (0) για Έξοδο \n\n --> '''
        c = input(info)
        if c.isdigit():
            c=int(c)
            if c == 0:
                break
            else:
                choice(conn,c)
        else: print("Εισάγετε έναν έγκυρο αριθμό σύμφωνα με τις παραπάνω επιλογές")

    conn.close()
if __name__ == '__main__':
    main()
