class Ship:

    ROWS = 10
    COLUMNS = 11 
    AIRCRAFT_CARRIER = 5
    BATTLESHIP = 4
    CRUISER = 3
    DESTROYER = 2
    ACTIVE_PLAYER_NAME = "Όνομα Παίχτη"

    def __init__(self):
        self.is_ocupied = [[0 for x in range(self.COLUMNS)] for x in range(self.ROWS)]
        # Θέση των πλοίων στο ταμπλό. Στην πρώτη θέση μπαίνουν οι συντεταγμένες
        # κάθε κομματιού του πλοίου και στη δέυτερη, οι συντεταγμένες
        # της περίμετρός του.
        self.aircraft_carrier = {"position": [], "adjacent": []}
        self.battleship = {"position": [], "adjacent": []}
        self.cruiser = {"position": [], "adjacent": []}
        self.destroyer = {"position": [], "adjacent": []}
        # Μεταβλητές τις οποίες χρειαζόμαστε με σκοπό να λειτουργήσει ο
        # αλγόριθμος επιλογής πλοίων του εχθρού.
        self.position = []
        self.direction = ""
        self.passes = 0
        self.hit = False # Δείχνει αν έχει χτυπηθεί φίλιο πλοίο
        self.counter = 0 # Μετράει πόσα κομμάτια πλοιου έχουν καταστραφεί
        # Μεταβλητή η οποία κρατάει το score και ειναι απαραιτητη
        # για τη λήξη του παιχνιδιου.
        self.score = 0
        # Λίστα με τις όλες τις πιθανές επιλογές του υπολογιστή.
        self.choice = []
        for x in range(self.ROWS):
            for y in range(self.COLUMNS):
                self.choice.append([x, y])


    def reset(self):
        """
        Ξανα διμηουγει τα αντικειμενο στην αρχική του κατάσταση.
        """

        self.is_ocupied = [[0 for x in range(self.COLUMNS)] for x in range(self.ROWS)]
        self.aircraft_carrier = {"position": [], "adjacent": []}
        self.battleship = {"position": [], "adjacent": []}
        self.cruiser = {"position": [], "adjacent": []}
        self.destroyer = {"position": [], "adjacent": []}
        self.position = []
        self.direction = ""
        self.passes = 0
        self.hit = False
        self.counter = 0
        self.score = 0
        self.recreate_choice()


    def recreate_choice(self):
        """
        Ξανά δημιουργία του choice.
        """

        self.choice = []
        for x in range(self.ROWS):
            for y in range(self.COLUMNS):
                self.choice.append([x, y])


    def choice_update(self, length):
        """
        Αφαιρεση στοιχείων απο το choice.
        
        length = Το μήκος του πλοίου, ενα απο self.AIRCRAFT_CARRIER = 5
                                              self.BATTLESHIP = 4
                                              self.CRUISER = 3
                                              self.DESTROYER = 2
        """

        # Επιλογή πλοίου.
        if length == self.AIRCRAFT_CARRIER:
            some_ship = self.aircraft_carrier
        elif length == self.BATTLESHIP:
            some_ship = self.battleship
        elif length == self.CRUISER:
            some_ship = self.cruiser
        elif length == self.DESTROYER:
            some_ship = self.destroyer

        # Διαγραφή πλοίου απο το choice!
        for x, y in some_ship["position"]:
            if [x, y] in self.choice:
                self.choice.remove([x, y])
        for x, y in some_ship["adjacent"]:
            if [x, y] in self.choice:
                self.choice.remove([x, y])


    def check_in_direction(self, position, direction, length):
        """
        Έλεγχος διευθυνσης.

        position = Η θέση της κεφαλής του πλοίου σε μορφή [row, column]
        direction = Κατεύθηνση σε ""
        length = Το μήκος του πλοίου, ενα απο self.AIRCRAFT_CARRIER = 5
                                              self.BATTLESHIP = 4
                                              self.CRUISER = 3
                                              self.DESTROYER = 2
        Επιστρέφει True ή False ανάλογα με το αν μπορεί να τοποθετηθει πλοίο!
        """

        # Αρχικά ελέγχουμε σε ποιόν άξονα θα μπει το πλοίο και κρατάμε σταθερή
        # την γραμμή για τον άξονα χ'χ position[0]
        # την στήλη για τον άξονα y'y position[1]
        if direction == "left" or direction == "right":
            const = position[0]
            position = position[1]
        else:
            const = position[1]
            position = position[0]      
        # Ελέγχουμε πρώτα αν ξεφευγει απο τα όρια του πίνακα
        if direction == "left" or direction == "up":
            if position - length+1 < 0:
                return False
        # Και τελικά αν το μήκος του πλοίου συναντάει κάποιο εμπόδιο
            if direction == "left":
                for x in range(1, length):
                    if self.is_ocupied[const][position - x]==1:
                        return False
                return True
            if direction == "up":
                for x in range(1, length):
                    if self.is_ocupied[position - x][const]==1:
                        return False
                return True
        elif direction == "right":
            if position + length-1 > self.COLUMNS-1:
                return False
            for x in range(1, length):
                if self.is_ocupied[const][position + x]==1:
                    return False
            return True
        elif direction == "down":
            if position + length-1 > self.ROWS-1:
                return False
            for x in range(1, length):
                if self.is_ocupied[position + x][const]==1:
                    return False
            return True


    def place(self, position, direction, length):
        """
        Τοποθέτηση πλοίου.

        position = Η θέση της κεφαλής του πλοίου σε μορφή [row, column]
        direction = Κατεύθηνση σε ""
        length = Το μήκος του πλοίου, ενα απο self.AIRCRAFT_CARRIER = 5
                                              self.BATTLESHIP = 4
                                              self.CRUISER = 3
                                              self.DESTROYER = 2
        Τοποθετεί το πλοίο στο ταμπλό!
        """
        # Γίνεται επιλογή μεταβλητής για γέμισμα με τις συντεταγμένες του πλοίου.
        if length == self.AIRCRAFT_CARRIER:
            fill = self.aircraft_carrier["position"]
        elif length == self.BATTLESHIP:
            fill = self.battleship["position"]
        elif length == self.CRUISER:
            fill = self.cruiser["position"]
        elif length == self.DESTROYER:
            fill = self.destroyer["position"]
            
        # Αρχικά ελέγχουμε σε ποιόν άξονα θα μπει το πλοίο και κρατάμε σταθερή
        # την γραμμή για τον άξονα χ'χ position[0]
        # την στήλη για τον άξονα y'y position[1]
        if direction == "left" or direction == "right":
            const = position[0]
            position = position[1]
        else:
            const = position[1]
            position = position[0]      
        # Και τελικά γίνεται η τοποθέτηση του πλοίου.
        if direction == "left":
            for x in range(length):
                self.is_ocupied[const][position - x]="*"
                fill.append([const, position - x])
        elif direction == "up":
            for x in range(length):
                self.is_ocupied[position - x][const]="*"
                fill.append([position - x, const])
        elif direction == "right":
            for x in range(length):
                self.is_ocupied[const][position + x]="*"
                fill.append([const, position + x])
        elif direction == "down":
            for x in range(length):
                self.is_ocupied[position + x][const]="*"
                fill.append([position + x, const])


    def fill_adjacent_space(self, direction, length):
        """
        Τοποθέτηση πλοίου.

        direction = Κατεύθηνση σε ""
        length = Το μήκος του πλοίου, ενα απο self.AIRCRAFT_CARRIER = 5
                                              self.BATTLESHIP = 4
                                              self.CRUISER = 3
                                              self.DESTROYER = 2
                                              
        Γεμίζει το χώρο γύρο από το πλοίο στο ταμπλό!
        """
        # Γίνεται επιλογή μεταβλητής για γέμισμα με τις συντεταγμένες του πλοίου.
        if length == self.AIRCRAFT_CARRIER:
            position = self.aircraft_carrier["position"]
            adjacent = self.aircraft_carrier["adjacent"]
        elif length == self.BATTLESHIP:
            position = self.battleship["position"]
            adjacent = self.battleship["adjacent"]
        elif length == self.CRUISER:
            position = self.cruiser["position"]
            adjacent = self.cruiser["adjacent"]
        elif length == self.DESTROYER:
            position = self.destroyer["position"]
            adjacent = self.destroyer["adjacent"]
        # Τελικά επιλέγεται η κατευθησνση κατα την οποία ειναι προσανατολισμένο το
        # πλοίο
        if direction == "left":
            a = position[0][0]
            b = position[0][1] + 1
            if b < self.COLUMNS:
                adjacent.append([a, b])
                if a-1 >= 0:
                    adjacent.append([a-1, b])
                if a+1 < self.ROWS:
                    adjacent.append([a+1, b])
            for x, y in position:
                if x-1 >= 0:
                    adjacent.append([x-1, y])
                if x+1 < self.ROWS:
                    adjacent.append([x+1, y])
            a = position[length-1][0]
            b = position[length-1][1] - 1        
            if b >= 0:
                adjacent.append([a, b])
                if a-1 >= 0:
                    adjacent.append([a-1, b])
                if a+1 < self.ROWS:
                    adjacent.append([a+1, b])
        elif direction == "right":
            a = position[0][0]
            b = position[0][1] - 1
            if b >= 0:
                adjacent.append([a, b])
                if a-1 >= 0:
                    adjacent.append([a-1, b])
                if a+1 < self.ROWS:
                    adjacent.append([a+1, b])
            for x, y in position:
                if x-1 >= 0:
                    adjacent.append([x-1, y])
                if x+1 < self.ROWS:
                    adjacent.append([x+1, y])
            a = position[length-1][0]
            b = position[length-1][1] + 1        
            if b < self.COLUMNS:
                adjacent.append([a, b])
                if a-1 >= 0:
                    adjacent.append([a-1, b])
                if a+1 < self.ROWS:
                    adjacent.append([a+1, b])
        elif direction == "up":
            a = position[0][0] + 1
            b = position[0][1]
            if a < self.ROWS:
                adjacent.append([a, b])
                if b-1 >= 0:
                    adjacent.append([a, b-1])
                if b+1 < self.COLUMNS:
                    adjacent.append([a, b+1])
            for x, y in position:
                if y-1 >= 0:
                    adjacent.append([x, y-1])
                if y+1 < self.COLUMNS:
                    adjacent.append([x, y+1])
            a = position[length-1][0] - 1
            b = position[length-1][1]        
            if a >= 0:
                adjacent.append([a, b])
                if b-1 >= 0:
                    adjacent.append([a, b-1])
                if b+1 < self.COLUMNS:
                    adjacent.append([a, b+1])
        elif direction == "down":
            a = position[0][0] - 1
            b = position[0][1]
            if a >= 0:
                adjacent.append([a, b])
                if b-1 >= 0:
                    adjacent.append([a, b-1])
                if b+1 < self.COLUMNS:
                    adjacent.append([a, b+1])
            for x, y in position:
                if y-1 >= 0:
                    adjacent.append([x, y-1])
                if y+1 < self.COLUMNS:
                    adjacent.append([x, y+1])
            a = position[length-1][0] + 1
            b = position[length-1][1]        
            if a < self.ROWS:
                adjacent.append([a, b])
                if b-1 >= 0:
                    adjacent.append([a, b-1])
                if b+1 < self.COLUMNS:
                    adjacent.append([a, b+1])

        # Γέμισμα του ταμπλό με τις Γύρο θέσεις!!
        for x, y in adjacent:
            self.is_ocupied[x][y] = 1


    def remove(self, length):
        """
        Αφαίρεση πλοίου.

        length = Το μήκος του πλοίου, ενα απο self.AIRCRAFT_CARRIER = 5
                                              self.BATTLESHIP = 4
                                              self.CRUISER = 3
                                              self.DESTROYER = 2
                                              
        Αφαιρει πλοίο από το ταμπλό και επιπλέον ενημερώνει το ταμπλό για τυχών
        αλλαγές πάνω σε αυτό!
        """

        # Επιλογή πλοίου προς διαγραφή
        if length == self.AIRCRAFT_CARRIER:
            self.aircraft_carrier = {"position": [], "adjacent": []}
        elif length == self.BATTLESHIP:
            self.battleship = {"position": [], "adjacent": []}
        elif length == self.CRUISER:
            self.cruiser = {"position": [], "adjacent": []}
        elif length == self.DESTROYER:
            self.destroyer = {"position": [], "adjacent": []}

        # Διαγραφή επιλεγμένου πλοίου και ενημέρωση του ταμπλό
        self.is_ocupied_update()
        

    def is_ocupied_update(self):
        """
        Συνάρτηση η οποία ενημερώνει το ταμπλό.

        Για κάθε πλοίο το οποίο διαγράφεται θα πρέπει να αλλάζουν και τα
        σύμβολα στο ταμλό του πίνακα is_ocupied!!
        """
        
        self.is_ocupied = [[0 for x in range(self.COLUMNS)] for x in range(self.ROWS)]
        for some_ship in [self.aircraft_carrier,
                          self.battleship,
                          self.cruiser,
                          self.destroyer]:
            if some_ship["position"]:
                for x, y in some_ship["position"]:
                    self.is_ocupied[x][y] = "*"
                for x, y in some_ship["adjacent"]:
                    self.is_ocupied[x][y] = 1


    def prnt(self):
        """
        Συνάρτηση η οποία εκτυπώνει το ταμπλό.

        Προς διευκόλυνσή μας για να μπορούμε να δούμε πως όλα δουλεύουν
        καθώς και τη θέση των πλοίων στο ταμπλό, τόσο του εχθρού, όσο και τα
        φίλια!!
        """
        
        print("  ", end="")
        for y in range(len(self.is_ocupied[0])):
            print(f"({y})", end="")
        print("")
        for x in range(len(self.is_ocupied)):
            print(f"({x})", end="")
            for y in self.is_ocupied[x]:
                print(f"{y}  ", end="")
            print("\n")

        for some_ship in [[self.aircraft_carrier,"Aircraft Carrier"],
                          [self.battleship, "Battleship"],
                          [self.cruiser, "Cruiser"],
                          [self.destroyer, "Destroyer"]]:
            print(some_ship[1]+":")
            if some_ship[0]["position"]:
                for i in some_ship[0]["position"]:
                    print(i, end="")
                print("\t", end="")
                for i in some_ship[0]["adjacent"]:
                    print(i, end="")
                print("\n")
            else:
                print("Δεν έχει τοποθετηθεί ακόμα.\n")


#####
if __name__=="__main__":
    ship = Ship()
    ship.prnt() 
    
