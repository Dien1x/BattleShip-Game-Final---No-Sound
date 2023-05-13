"""
Για την εκπλήρωση των παρακάτω συναρτήσεων χρειαζόμαστε παράλληλα
τις εξείς μεταβλητές για την αποθήκευση και διαχειρηση κάποιον τιμών:
position # Μεταβλητή για την αποθήκευση της τρέχουσας θέσης την οποία εξετάζουμε
direction # Μεταβλητή η οποία δειχνει την τρέχουσα κατεύθηνση προς την οποία
            θα ενεργήσουμε
random_choice_list # Είναι μία λίστα με όλες τις πιθανές επιλογές που μπορούν
                     να πραγματοποιηθούν εντός του ταμπλό
enemy_set_up_table # Είναι το ταμπλό (ένας πίνακας δύοπ διαστάσεων) το οποίο
                     περιέχει τη θέση των πλοίων επισημανσμένη με "*" 
passes # Είναι μία μεταβλητή η οποία δειχνει πόσες διελεύσεις έχουν πραγματοποιηθεί
         καταμήκος του άξονα του εξεταζόμενου πλοίου, με σκοπό να ξέρουμε
        αν αυτό έχει καταστραφει.
"""

def check_hit_validity(position, direction, random_choice_list, passes, rows, columns, enemy_set_up_table):
    """
    Μία συνάρτηση η οποία ελέγχει την επιλογή του εχθρού.

    position = x, y μέσα σε [] --> [x, y]
    direction = ένα απο όλα τα παρακάτω:
                Σε περίπτωση που δεν έχουμε βρεί την κατεύθηνση του πλοίου:
                ("up", "right", "down", "left")
                Σε περίπτωση που το πλοίο είναι τοποθετημένο κατακόρυφα:
                ("y_up", "y_down")
                Σε περίπτωση που το πλοίο είναι τοποθετημένο οριζόντια:
                ("x_right", "x_left")
    random_choice_list = Μία λίστα η οποία περιέχει όλες τις πιθανές
                εναπομεινουσες επιλογές του εχθρού ως προς την επιλογή της
                επόμενης θέσεις που θέλει να χτυπήσει.
    passes = Μία μεταβλητή η οποία δειχνει πόσες διελέυσεις έχουν γίνει καταμήκος ενός πλοίου.
    (Αν το passes γίνει > 1, δηλαδή έχουμε ψάξει για κομμάτια
    και στις δύο κατευθήνσεις, τότε το πλοίο έχει καταστραφει.)
    rows = Ο αριθμός των γραμμών του πίνακα.
    columns = Ο αριθμός των στηλών του πίνακα.
    enemy_set_up_table = Το ταμπλό του αντιπάλου απο αυτόν που κάνει την επιλογή
                το οποίο περιέχει τις θέσεις όλων των πλοίων συμβολισμένες με
                "*".

    Η συνάρτηση αυτή επιστρέφει αν είναι έγκυρη η κατευθηνση που επιχειρει
    να ψάξει ο εχρός, αλλιώς επισρτέφει την αμέσως επόμενη έγκυρη κατευθηνση.
    Επίσης επιστρέφει τις φορές που έχει γίνει αλλαγή κατεύθηνσης.
    """

    # Είναι οι λίστες με όλες τις πιθανές κατευθήνσεις καθώς και τις τιμές
    # που πρέπει να πάρει η επόμενη θέση αντιστοίχως με την κάθε κατευθηνση.
    directions = [["up", [-1, 0]], ["right", [0, 1]], ["down", [1, 0]], ["left", [0, -1]]]
    y_directions = [["y_up", [-1, 0]], ["y_down", [1, 0]]]
    x_directions = [["x_right", [0, 1]], ["x_left", [0, -1]]]
    # Παιρνουμε ένα αντίγραφο της μεταβλητής της θέσεις, έτσι ώστε να μη
    # χάσουμε την τιμή της.
    enemy_choice = position[:]
    # Γίνεται έλεγχος ως προς το αν η κατεύθηνση που δώσαμε είναι έγκυρη.
    # (Έγκυρη είναι μια κατεύθηνση η οποία δεν μας βγάζει εκτός ορίων καθώς και μία
    # η οποία δεν έχει ήδη επιλεχθει.)
    # Αυτό επιτυγχάνεται ελέγχοντας αν η κατευθηνση που θέλουμε μετά υπάρχει μέσα στις
    # διαθέσιμες πιθανές επιλογές του εχθρού.
    if direction in ["up", "right", "down", "left"]:
        counter = 0
        enemy_choice[0] += directions[counter][1][0]
        enemy_choice[1] += directions[counter][1][1]
        # Η κατευθηνση που δώσαμε θα αλλάζει μέχρι να πάρουμε μία
        # έγκυρη κατευθησνη
        while enemy_choice not in random_choice_list:
            enemy_choice = position[:]
            counter += 1
            enemy_choice[0] += directions[counter][1][0]
            enemy_choice[1] += directions[counter][1][1]
            direction = directions[counter][0]
    elif direction == "y_up":
        counter = 0
        enemy_choice[0] += y_directions[counter][1][0]
        enemy_choice[1] += y_directions[counter][1][1]
        # Στην περίπτωση που δεν υπάρχει το επόμενο τετράγωνο, τότε αλλάζει η
        # κατεύθηνση της αναζήτησης.
        if enemy_choice not in random_choice_list:
            counter += 1
            direction = y_directions[counter][0]
            passes += 1
            # Αν και προς αυτή την κατευθηνση δεν υπάρχει τετράγωνο, τότε απλά
            # η μεταβλητή passes γίνεται μεγαλύτερη απο 1 και η συνάρτηση τελειώνει.
            # Ακό,η γίνεται έλεγχος για το αν υπάρχει κάποιο κομμάτι πλοίου έτσι ώστε ο υπολογιστής
            # να μην ξεπεράσει τα όρια πέρα απο το λευκό τετράγωνο.
            while enemy_choice not in random_choice_list:
                enemy_choice[0] += y_directions[counter][1][0]
                enemy_choice[1] += y_directions[counter][1][1]
                if enemy_choice[1] > rows or enemy_choice not in random_choice_list and enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == 1:
                    passes += 1
                    break
    #### Ομοίως και σε όλα τα υπόλοιπα.
    elif direction == "y_down":
        counter = 1
        enemy_choice[0] += y_directions[counter][1][0]
        enemy_choice[1] += y_directions[counter][1][1]
        if enemy_choice not in random_choice_list:
            counter -= 1
            direction = y_directions[counter][0]
            passes += 1
            while enemy_choice not in random_choice_list:
                enemy_choice[0] += y_directions[counter][1][0]
                enemy_choice[1] += y_directions[counter][1][1]
                if enemy_choice[1] < 0 or enemy_choice not in random_choice_list and enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == 1:
                    passes += 1
                    break
    elif direction == "x_right":
        counter = 0
        enemy_choice[0] += x_directions[counter][1][0]
        enemy_choice[1] += x_directions[counter][1][1]
        if enemy_choice not in random_choice_list:
            counter += 1
            direction = x_directions[counter][0]
            passes += 1
            while enemy_choice not in random_choice_list:
                enemy_choice[0] += x_directions[counter][1][0]
                enemy_choice[1] += x_directions[counter][1][1]
                if enemy_choice[1] < 0 or enemy_choice not in random_choice_list and enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == 1:
                    passes += 1
                    break
    elif direction == "x_left":
        counter = 1
        enemy_choice[0] += x_directions[counter][1][0]
        enemy_choice[1] += x_directions[counter][1][1]
        if enemy_choice not in random_choice_list:
            counter -= 1
            direction = x_directions[counter][0]
            passes += 1
            while enemy_choice not in random_choice_list:
                enemy_choice[0] += x_directions[counter][1][0]
                enemy_choice[1] += x_directions[counter][1][1]
                if enemy_choice[1] > columns or enemy_choice not in random_choice_list and enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == 1:
                    passes += 1
                    break

    # Με το πέρας της συνάρτηση επιστρέφεται η επόμενη έγκυρη κατευθηνση που
    # μπορει να επιλέξει ο εχθρός
    return direction, passes


def check_if_tile_is_ship(position, direction, random_choice_list, enemy_set_up_table):
    """
    Μία συνάρτηση η οποία ελέγχει την ύπαρξη πλοίου.

    position = x, y μέσα σε [] --> [x, y]
    direction = ένα απο όλα τα παρακάτω:
                Σε περίπτωση που δεν έχουμε βρεί την κατεύθηνση του πλοίου:
                ("up", "right", "down", "left")
                Σε περίπτωση που το πλοίο είναι τοποθετημένο κατακόρυφα:
                ("y_up", "y_down")
                Σε περίπτωση που το πλοίο είναι τοποθετημένο οριζόντια:
                ("x_right", "x_left")
    random_choice_list = Μία λίστα η οποία περιέχει όλες τις πιθανές
                εναπομεινουσες επιλογές του εχθρού ως προς την επιλογή της
                επόμενης θέσεις που θέλει να χτυπήσει.
    enemy_set_up_table = Το ταμπλό του αντιπάλου απο αυτόν που κάνει την επιλογή
                το οποίο περιέχει τις θέσεις όλων των πλοίων συμβολισμένες με
                "*".

    Η συνάρτηση αυτή δέχεται μία θέση και μία κατεύθηνση. Βρίσκει την επόμενη πιθανή επιλογή
    με βάση τη δοθεισα κατευθηνση και ελέγχει αν υπάρχει πλοίο σε αυτή τη θέση.
    Αν υπάρχει, προσπαθεί να το καταστρέψει όλο, κάνοντας κοντινές επιλογές πάνω στον άξονα
    του προσανατολισμού του πλοίου, αλλιώς ψάχνει κυκλικά μέχρι να βρει και δευτερη
    έγκυρη θέση ύπαρξης πλοίου.
    """

    # Παιρνουμε ένα αντίγραφο της μεταβλητής της θέσεις, έτσι ώστε να μη
    # χάσουμε την τιμή της.
    enemy_choice = position[:]
    # Αρχικά γίνεται έλεγχος τις δοθεισας κατευθηνσης.
    if direction == "up":
        enemy_choice[0] -= 1
        # Ελέγχεται αν προς τη δοθείσα κατεύθηνση υπάρχει κομμάτι πλοίου.
        if enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == "*":
            # Αν υπάρχει μετακεινειται ο έλεγχος αποκλιστικά
            # στον άξονα της προηγούμενης κατεύθηνσης (εδώ στον άξονα y)
            direction = "y_up"
            position = enemy_choice
            color = ["red",[enemy_choice[0], enemy_choice[1]]]
        else:
            # Αλλιώς γίνεται έλεγχος που ακολουθεί τη φορά του ρολογιού
            # (εδώ συνεχίζει προς τα δεξιά.
            direction = "right"
            color = ["white",[enemy_choice[0], enemy_choice[1]]]
        # Τέλος ειτε βρθεί πλοίο ειτε όχι, η εξεταζόμενη θέση διαγράφεται
        # απο τη λίστα τυχαιων επιλογών.
        random_choice_list.remove(enemy_choice)
    #### Ομοίως και τα υπόλοιπα.
    elif direction == "right":
        enemy_choice[1] += 1
        if enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == "*":
            direction = "x_right"
            position = enemy_choice
            color = ["red",[enemy_choice[0], enemy_choice[1]]]
        else:
            direction = "down"
            color = ["white",[enemy_choice[0], enemy_choice[1]]]
        random_choice_list.remove(enemy_choice)
    elif direction == "down":
        enemy_choice[0] += 1
        if enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == "*":
            direction = "y_down"
            position = enemy_choice
            color = ["red",[enemy_choice[0], enemy_choice[1]]]
        else:
             direction = "left"
             color = ["white",[enemy_choice[0], enemy_choice[1]]]
        random_choice_list.remove(enemy_choice)
    elif direction == "left":
        enemy_choice[1] -= 1
        if enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == "*":
            color = ["red",[enemy_choice[0], enemy_choice[1]]]
            direction = "x_left"
            position = enemy_choice
        random_choice_list.remove(enemy_choice)
    # Αν γίνει αλλαγή προς κάποιον άξονα
    elif direction == "y_up":
        enemy_choice[0] -= 1
        # Αρχικά γίνεται έλεγχος αν η εξεταζόμενη θέση υπάρχει στη λίστα
        # επιλογών με σκοπό κατα την αλλαγή κατεύθηνσης, όσες θέσεις έχουμε ήδη
        # εξετάσει να τις παραλειψουμε.
        while enemy_choice not in random_choice_list:
            enemy_choice[0] -= 1
        # Ελέγχουμε την πρώτη δυνατή θέση του προηγούμενου ελέγχου.
        # Αν ειναι πλοίο τότε συνεχίζουμε προς την ίδια κατεύθηνση.
        if enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == "*":
            position = enemy_choice
            color = ["red",[enemy_choice[0], enemy_choice[1]]]
        else:
            # Αλλιώς απλά σημειώνουμε το τετράγωνο με άπρο χρώμα και παραμένουμε
            # στην ίδια θέση για να γίνει έλεγχος κατεύθηνση με τη συνάρτηση
            # check_hit_validity.
            color = ["white",[enemy_choice[0], enemy_choice[1]]]
        # Τέλος ειτε βρθεί πλοίο ειτε όχι, η εξεταζόμενη θέση διαγράφεται
        # απο τη λίστα τυχαιων επιλογών.
        random_choice_list.remove(enemy_choice)
    #### Ομοίως και τα υπόλοιπα.
    elif direction == "y_down":
        enemy_choice[0] += 1
        while enemy_choice not in random_choice_list:
            enemy_choice[0] += 1
        if enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == "*":
            position = enemy_choice
            color = ["red",[enemy_choice[0], enemy_choice[1]]]
        else:
            color = ["white",[enemy_choice[0], enemy_choice[1]]]
        random_choice_list.remove(enemy_choice)
    elif direction == "x_right":
        enemy_choice[1] += 1
        while enemy_choice not in random_choice_list:
            enemy_choice[1] += 1
        if enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == "*":
            position = enemy_choice
            color = ["red",[enemy_choice[0], enemy_choice[1]]]
        else:
            color = ["white",[enemy_choice[0], enemy_choice[1]]]
        random_choice_list.remove(enemy_choice)
    elif direction == "x_left":
        enemy_choice[1] -= 1
        while enemy_choice not in random_choice_list:
            enemy_choice[1] -= 1
        if enemy_set_up_table[enemy_choice[0]][enemy_choice[1]] == "*":
            position = enemy_choice
            color = ["red",[enemy_choice[0], enemy_choice[1]]]
        else:
            color = ["white",[enemy_choice[0], enemy_choice[1]]]
        random_choice_list.remove(enemy_choice)
        
    # Η συνάρτηση αυτή επιστρέφει τη νέα ΘΕΣΗ απο την οποία θα συνεχίσει να ψάχνει
    # ο εχθρός,
    # Τη νέα ΚΑΤΕΥΘΗΝΣΗ προς την οποία θα ελέγξει ο εχθρός,
    # Τη νέα ΛΙΣΤΑ ΤΥΧΑΙΩΝ ΑΠΙΛΟΓΩΝ με όλες τις αλλαγές που της έχουν γίνει,
    # Πόσες ΔΙΑΠΕΡΑΣΕΙΣ έχουν γίνει κατα τη διάρκει εκτέλεσης,
    # Καθώς και το ΧΡΩΜΑ ανάλογα με το αν χτυπήθηκε πλοίο ή όχι (κόκκινο ή άσπρο).
    return position, direction, random_choice_list,color    
