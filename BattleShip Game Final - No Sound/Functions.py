from tkinter import *
from Ship_Class import *
from Enemy_Algorythm import *
import random
import time

# Αρχικοποίηση διαφορετικής αλληλουχίας για να έχουμε κάθε φορά διαφορετικά αποτελέσματα
random.seed(time.time())

def center_window(window):
    """
    Μία Συνάρτηση κεντραρίσματος.

    Κεντράρει το παράθυρο αφού λάβει υπόψη τα νέα δεδομένα για το μέγεθός του!
    """

    window.update_idletasks()
    x = int(window.winfo_screenwidth()/2 - window.winfo_width()/2)
    y = int(window.winfo_screenheight() / 2 - window.winfo_height() / 2)
    window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{x}+{y}")


def create_ship_button(topwindow1, player):
    """
    Τοποθέτηση πλοίου.

    topwindow1 = Το παράθυρο το οποίο περιέχει όλα τα διαθέσιμα προς εισαγωγή πλοια
    player = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον παίχτη

    Μία συνάρτηση η οποία τοποθετεί πλοία στο ταμπλό.
    """

    # Αρχικά ελέγχουμε αν έχει τοποθετηθεί κάθε ένα απο τα πλοία και αν έχει όντως τοποθετηθει
    # κάποιο από αυτά τότε απενεργοποιούμε το κουμπί που κάνει την εισαγωγή τους.

    # Για το aircraft_carrier
    if not player.aircraft_carrier["position"]:
        topwindow1.nametowidget("frame_choose_ship.aircraft_carrier_add").config(state=NORMAL)
    else:
        topwindow1.nametowidget("frame_choose_ship.aircraft_carrier_add").config(state=DISABLED)
    # Για το battleship
    if not player.battleship["position"]:
        topwindow1.nametowidget("frame_choose_ship.battleship_add").config(state=NORMAL)
    else:
        topwindow1.nametowidget("frame_choose_ship.battleship_add").config(state=DISABLED)
    # Για το cruiser
    if not player.cruiser["position"]:
        topwindow1.nametowidget("frame_choose_ship.cruiser_add").config(state=NORMAL)
    else:
        topwindow1.nametowidget("frame_choose_ship.cruiser_add").config(state=DISABLED)
    # Για το destroyer
    if not player.destroyer["position"]:
        topwindow1.nametowidget("frame_choose_ship.destroyer_add").config(state=NORMAL)
    else:
        topwindow1.nametowidget("frame_choose_ship.destroyer_add").config(state=DISABLED)

    center_window(topwindow1)

    topwindow1.deiconify()

    topwindow1.lift()
    topwindow1.grab_set()


def choose_ship_length(window, topwindow1, topwindow2, player, length):
    """
    Επιλογή μεγέθους πλοίου.

    window = Το κύριο παράθυρο του παιχνιδιού.
    topwindow1 = Το παράθυρο το οποίο περιέχει όλα τα διαθέσιμα προς εισαγωγή πλοια
    topwindow2 = Το παράθυρο το οποίο έχει την επιλογή κατυεύθηνσης
    player = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον παίχτη
    length = Το μήκος του πλοίου που χρειαζόμαστε το οποίο δίνεται σε self.AIRCRAFT_CARRIER = 5
                                                                      self.BATTLESHIP = 4
                                                                      self.CRUISER = 3
                                                                      self.DESTROYER = 2
    
    Μία συνάρτηση η οποία αφού γινει η επιλογή του μεγέθους πλοίου, διμηουγει συναρτήσεις
    για κάθε κουμπί του ταμπλό ξεχωριστά.
    """

    check_buttons(window, player)
    
    topwindow1.withdraw()
    topwindow1.grab_release()
    
    player.current_length = length

    def head(x, y, window, topwindow2, player):
        """
        Η συνάρτηση head επιστρέφει μία συνάρτηση

        Τα x και y θα αλλάζουν ανάλογα με τα ορίσματα που θα τις δίνονται.
        Τα ορίσματα window, topwindow2 και player παραμένουν σταθερά και τα παιρνει
        απο τη συνάρτηση choose_ship_length.

        Τελικά η συνάρτηση αυτή επιστρέφει μία άλλη συνάρτηση η οποία θα δέχεται
        όλα τα ορίσματα τις head και θα έχει σταθερά αλλα διαφορετικά για κάθε κλήση
        της head x και y.
        """
        
        def choose_ship_head():
            """
            Η συνάρτηση αυτή ειναι μία σταθερή επιστρεφόμενη τιμή της head η οποία θα
            δίνεται σε κάθε κουμπί το οποίο έχει να κάνει με τοποθέτηση πλοίων στο ταμπλό
            και θα κάνει την ίδια κάθε φορά δουλειά για τις διάφορες συντεταγμένες που
            έχουν τα διάφορα κουμπιά μέσα στο ταμπλό.
            """
            
            player.current_head = [x, y]

            if not player.check_in_direction(player.current_head, "up", player.current_length):
                topwindow2.nametowidget("arrows_frame.up").config(state=DISABLED)
            else:
                topwindow2.nametowidget("arrows_frame.up").config(state=NORMAL)
            if not player.check_in_direction(player.current_head, "down", player.current_length):
                topwindow2.nametowidget("arrows_frame.down").config(state=DISABLED)
            else:
                topwindow2.nametowidget("arrows_frame.down").config(state=NORMAL)
            if not player.check_in_direction(player.current_head, "right", player.current_length):
                topwindow2.nametowidget("arrows_frame.right").config(state=DISABLED)
            else:
                topwindow2.nametowidget("arrows_frame.right").config(state=NORMAL)
            if not player.check_in_direction(player.current_head, "left", player.current_length):
                topwindow2.nametowidget("arrows_frame.left").config(state=DISABLED)
            else:
                topwindow2.nametowidget("arrows_frame.left").config(state=NORMAL)

            center_window(topwindow2)
            
            topwindow2.deiconify()

            topwindow2.lift()
            topwindow2.grab_set()
        return choose_ship_head
       

    # Για κάθε κουμπί με διαφορετικό x και y δίνεται και η ανάλογη συνάρτηση.
    for y in range(11):
        for x in range(10):
            ship = head(x, y, window, topwindow2, player)
            window.nametowidget(f"frame_enemy.enemy{x}{y}").config(command=ship)


def cancel_direction(window, player, topwindow2):
    """
    Συνάρτηση που ακυρώνει την καταχώρηση κατευθηνσης.

    window = Το κύριο παράθυρο του παιχνιδιού.
    player = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον παίχτη
    topwindow2 = Το παράθυρο το οποίο έχει την επιλογή κατυεύθηνσης
    """

    check_buttons(window, player)

    topwindow2.withdraw()
    topwindow2.grab_release()


def choose_ship_direction(window, topwindow2, player, direction, ship_color):
    """
    Επιλογή κατεύθηνσης πλοίου.

    window = Το κύριο παράθυρο του παιχνιδιού.
    topwindow2 = Το παράθυρο το οποίο έχει την επιλογή κατυεύθηνσης
    player = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον παίχτη
    direction = με την κατεύθηνση που θέλουμε μέσα σε ""
    ship_color = είναι η εικόνα που θα έχει το κάθε πλοίο που θα τοποθετειται στο ταμπλό
    
    Μία συνάρτηση η οποία αφού γινει η επιλογή του μεγέθους πλοίου και διμηουγηθούν συναρτήσεις
    για κάθε κουμπί του ταμπλό ξεχωριστά, επιλέγει την καυεύθηνση του.
    """
    
    player.place(player.current_head, direction, player.current_length)
    player.fill_adjacent_space(direction, player.current_length)
    

    # Επιλογή πλοίου.
    # Το current_length ειναι μία μεταβλητή η οποία έχει διμηουργηθεί
    # στη συνάρτηση choose_ship_length
    if player.current_length == player.AIRCRAFT_CARRIER:
        some_ship = player.aircraft_carrier
    elif player.current_length == player.BATTLESHIP:
        some_ship = player.battleship
    elif player.current_length == player.CRUISER:
        some_ship = player.cruiser
    elif player.current_length == player.DESTROYER:
        some_ship = player.destroyer

    # Απενεργοποίηση commands
    for y in range(11):
        for x in range(10):
            window.nametowidget(f"frame_enemy.enemy{x}{y}").config(command="")
    # Απενεργοποίηση κουμπιών σε περίπτωση ύπαρξης πλοίου.
    for x, y in some_ship["position"]:
        window.nametowidget(f"frame_enemy.enemy{x}{y}").config(state=DISABLED, image=ship_color)
    for x, y in some_ship["adjacent"]:
        window.nametowidget(f"frame_enemy.enemy{x}{y}").config(state=DISABLED)


    check_buttons(window, player)
    
    topwindow2.withdraw()
    topwindow2.grab_release()


def remove_ship(topwindow3, player):
    """
    Aφαιρεση πλοίου.
    
    topwindow3 = Το παράθυρο το οποίο περιέχει όλα τα διαθέσιμα προς διαγραφή πλοια
    player = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον παίχτη

    Μία συνάρτηση η οποία ανοίγει ένα παράθυρο με σκοπό να αφαιρει πλοία από το ταμπλό.
    """

    # Δουλεύει ακριβώ όμοια με την create_ship_button
    if player.aircraft_carrier["position"]:
        topwindow3.nametowidget("frame_remove_ship.aircraft_carrier_remove").config(state=NORMAL)
    else:
        topwindow3.nametowidget("frame_remove_ship.aircraft_carrier_remove").config(state=DISABLED)
    if player.battleship["position"]:
        topwindow3.nametowidget("frame_remove_ship.battleship_remove").config(state=NORMAL)
    else:
        topwindow3.nametowidget("frame_remove_ship.battleship_remove").config(state=DISABLED)
    if player.cruiser["position"]:
        topwindow3.nametowidget("frame_remove_ship.cruiser_remove").config(state=NORMAL)
    else:
        topwindow3.nametowidget("frame_remove_ship.cruiser_remove").config(state=DISABLED)
    if player.destroyer["position"]:
        topwindow3.nametowidget("frame_remove_ship.destroyer_remove").config(state=NORMAL)
    else:
        topwindow3.nametowidget("frame_remove_ship.destroyer_remove").config(state=DISABLED)

    center_window(topwindow3)

    topwindow3.deiconify()

    topwindow3.lift()
    topwindow3.grab_set()


def remove(window, topwindow3, player, length, sea_image, ship_image):
    """
    Aφαιρεση πλοίου.

    window = Το κύριο παράθυρο του παιχνιδιού.
    topwindow3 = Το παράθυρο το οποίο περιέχει όλα τα διαθέσιμα προς διαγραφή πλοια
    player = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον παίχτη
    length = Το μήκος του πλοίου που χρειαζόμαστε το οποίο δίνεται σε self.AIRCRAFT_CARRIER = 5
                                                                      self.BATTLESHIP = 4
                                                                      self.CRUISER = 3
                                                                      self.DESTROYER = 2
    sea_image = Η εικόνα που αναπαριστά τη θάλασσα πάνω στο ταμπλό με σκοπό την ανακατασκευή του.
    ship_color = είναι η εικόνα που θα έχει το κάθε πλοίο που θα τοποθετειται στο ταμπλό.    
    
    Μία συνάρτηση η οποία αφαιρει πλοία από το ταμπλό και ταυτόχρονα επαναφέρει το ταμπλό
    στην κατάσταση που χρειάζεται.
    """

    player.remove(length)

    # Eνεργοποίηση κουμπιών μετά την αφαίρεση.
    for x in range(10):
        for y in range(11):
            window.nametowidget(f"frame_enemy.enemy{x}{y}").config(state=NORMAL, image=sea_image)

    for some_ship in [player.aircraft_carrier,
                      player.battleship,
                      player.cruiser,
                      player.destroyer]: 
        for x, y in some_ship["position"]:
            window.nametowidget(f"frame_enemy.enemy{x}{y}").config(state=DISABLED, image=ship_image)
        for x, y in some_ship["adjacent"]:
            window.nametowidget(f"frame_enemy.enemy{x}{y}").config(state=DISABLED)

    check_buttons(window, player)

    topwindow3.withdraw()
    topwindow3.grab_release()
    
    

def check_buttons(window, player):
    """
    Έλεγχος λειτουργικότητας κουμπιών.

    window = Το παράθυρο που υπάρχουν τα widgets.
    player = Το αντικειμενο το οποίο εξετάζουμε.
    
    Ελέγχει αν τα κουμπιά τοποθέτησης πλοίων και έναρξης παιχνιδιού
    πρέπει να ειναι ενεργά ή όχι.
    """
    if player.aircraft_carrier["position"] and player.battleship["position"] and player.cruiser["position"] and player.destroyer["position"]:
        window.nametowidget("frame_ship_input.ship_add").config(state=DISABLED)
        window.nametowidget("frame_ship_input.ship_remove").config(state=NORMAL)
        window.nametowidget("frame_ship_input.start").config(state=NORMAL)
    else:
        for some_ship in [player.aircraft_carrier["position"],
                          player.battleship["position"],
                          player.cruiser["position"],
                          player.destroyer["position"]]:
            if some_ship:
                window.nametowidget("frame_ship_input.ship_add").config(state=NORMAL)
                window.nametowidget("frame_ship_input.ship_remove").config(state=NORMAL)
                window.nametowidget("frame_ship_input.start").config(state=DISABLED)
                break
            else:
                window.nametowidget("frame_ship_input.ship_add").config(state=NORMAL)
                window.nametowidget("frame_ship_input.ship_remove").config(state=DISABLED)
                window.nametowidget("frame_ship_input.start").config(state=DISABLED)


def new_game(window, topwindow, end_window, friend, enemy, default_image_button, default_image_label):
    """
    Συνάρτηση επανέναρξης του παιχνιδιού.

    window = Το κύριο παράθυρο του παιχνιδιού.
    topwindow = Το παράθυρο το οποίο χρησιμοποιειται για την ονομασία του παιχτη.
    end_window = Το παράθυρο το οποίο εμφανίζεται με τη λήξη του παιχνιδιού.
    friend = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον παίχτη.
    enemy = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον εχθρό.
    default_image_button = Η εικόνα που αναπαριστά τη θάλασσα πάνω στο ταμπλό με σκοπό την ανακατασκευή του
                           αφορά τα κουμπιά.
    default_image_label = Η εικόνα που αναπαριστά τη θάλασσα πάνω στο ταμπλό με σκοπό την ανακατασκευή του
                          αφορά τις ταμπέλες.
    
    Αρχίζει καινούριο παιχνίδι.
    """

    friend.reset()
    enemy.reset()

    for x in range(10):
        for y in range(11):
            window.nametowidget(f"frame_enemy.enemy{x}{y}").config(state=NORMAL, command="", image=default_image_button)
    for x in range(10):
        for y in range(11):
            window.nametowidget(f"frame_player.player{x}{y}").config(image=default_image_label)

    window.nametowidget("frame_ship_input.ship_add").config(state=NORMAL)

    center_window(topwindow)

    end_window.withdraw()
    end_window.grab_release()

    topwindow.deiconify()

    topwindow.lift()
    topwindow.grab_set()
    

def start_game(window, enemy, friend, end_window, enemy_red, enemy_white, friend_gray, friend_red, friend_white, deafult_image, print_ships):

    """
    Συνάρτηση η οποία ξεκινάει το παιχνίδι.

    window = Το κύριο παράθυρο του παιχνιδιού.
    enemy = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον εχθρό.
    friend = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον παίχτη.
    end_window = Το παράθυρο το οποίο εμφανίζεται με τη λήξη του παιχνιδιού.
    enemy_red = Το χρώμα που παίρνουν τα κουμπιά σε περίπτωση ύπαρξης εχθρικού πλοίου
    enemy_white = Το χρώμα που παίρνουν τα κουμπιά σε περίπτωση μη ύπαρξης εχθρικού πλοίου
    friend_gray = Το χρώμα που παίρνουν οι ταμπέλες για τις αρχικές θέσεις των πλοίων
    friend_red = Το χρώμα που παίρνουν οι ταμπέλες σε περίπτωση ύπαρξης φίλιου πλοίου
    friend_white = Το χρώμα που παίρνουν οι ταμπέλες σε περίπτωση μη ύπαρξης φίλιου πλοίου  
    default_image = Η εικόνα που αναπαριστά τη θάλασσα πάνω στο ταμπλό με σκοπό την ανακατασκευή του
                    αφορά τα κουμπιά.
    print_ships = Ειναι μία μεταβλητή η οποία όταν έχει την τιμή True κατασκευάζει στο idle μία αναπαράσταση
                  με όλες τις πληροφορίες του ταμπλό οι οποίες περιλαμβάνουν: Το εχθρικό ταμπλό
                                                                              Την εχθρική διάταξη πλοίων
                                                                              Το φίλιο ταμπλό
                                                                              Την φίλια διάταξη πλοίων
                  Η μεταβλητή αυτή έχει βοηθητικό σκοπό για την κατασκευή και την επιβεβαιωση πως η
                  εφαρμογή δουευει σωστά.

    Αυτή η συνάρτηση τοποθετει τα πλοία του εχθρού και κάνει τις
    απαραιτητες ενέργειες για να ξεκινήσουμε τα πυρά.
    """

    window.nametowidget("frame_ship_input.ship_add").config(state=DISABLED)
    window.nametowidget("frame_ship_input.ship_remove").config(state=DISABLED)
    window.nametowidget("frame_ship_input.start").config(state=DISABLED)

    # Εδώ γίνεται η τυχαια εισαγωγή πλοίων στο ταμπλό του εχθρού.
    list_of_ships = [enemy.AIRCRAFT_CARRIER,
                     enemy.BATTLESHIP,
                     enemy.CRUISER,
                     enemy.DESTROYER]

    while list_of_ships:

        list_of_directions = ["left", "right", "up", "down"]
        
        length = random.choice(list_of_ships)
        position = random.choice(enemy.choice)

        while list_of_directions:
            direction = random.choice(list_of_directions)
            if enemy.check_in_direction(position, direction, length):
                enemy.place(position, direction, length)
                enemy.fill_adjacent_space(direction, length)
                list_of_ships.remove(length)
                enemy.choice_update(length)
                break
            list_of_directions.remove(direction)

    # Εκτύπωση πληροφοριών αν ειναι True η μεταβλητή print_ships
    if print_ships:
        ##!!##
        print("-------Εχθρική διάταξη πλοίων-------\n")
        enemy.prnt()
        print("--------Φίλια διάταξη πλοίων--------\n")
        friend.prnt()


    def enemy_buttons(x, y, window, enemy, friend, end_window, enemy_red, enemy_white, friend_red, friend_white):

        """
        Η συνάρτηση enemy_buttons επιστρέφει μία συνάρτηση

        Τα x και y θα αλλάζουν ανάλογα με τα ορίσματα που θα τις δίνονται.
        Τα υπόλοιπα ορίσματα παραμένουν σταθερά και τα παιρνει
        απο τη συνάρτηση start_game.

        Τελικά η συνάρτηση αυτή επιστρέφει μία άλλη συνάρτηση η οποία θα δέχεται
        όλα τα ορίσματα τις head και θα έχει σταθερά αλλα διαφορετικά για κάθε κλήση
        της head x και y.
        """
        
        def player_choice():
            """
            Συνάρτηση διαφορετική για κάθε κουμπί.

            Η συνάρτηση αυτή ελέγχει αν ο χρήστης έχει πετύχει κάποιο πλοίο του εχθρού καθώς και το ίδιο
            για τον εχθρό.
            Ανάλογα με τις βολές του κάθε ένα διαμορφώνει και το παράθυρο του παιχνιδιού.
            """

            if enemy.is_ocupied[x][y] == "*":
                window.nametowidget(f"frame_enemy.enemy{x}{y}").config(state=DISABLED, image=friend_red)
                friend.score += 1
                window.nametowidget("score").config(text=f"{Ship.ACTIVE_PLAYER_NAME}: {friend.score}\tCPU: {enemy.score}")
            else:
                window.nametowidget(f"frame_enemy.enemy{x}{y}").config(state=DISABLED, image=friend_white)

            # Συνάρτηση η οποία εκτελέι τις απαραιτητες ενέργειες για να κάνει τον εχθρό έξυπνο
            # δηλαδή να επιλέγει την επόμενη κίνησή του ορθά
            enemy_choice(window, friend, enemy, end_window, enemy_red, enemy_white)

            if friend.score == 14:
                end_window.nametowidget("end_game_frame.end_game_label").config(text=f"O Παίχτης με το Όνομα: {Ship.ACTIVE_PLAYER_NAME}, νίκησε!!!")
                end_game(end_window)
            if enemy.score == 14:
                end_window.nametowidget("end_game_frame.end_game_label").config(text="O Υπολογιστής νίκησε!!!")
                end_game(end_window)
                
            
        return player_choice

    
    for x in range(10):
        for y in range(11):
            player_choice = enemy_buttons(x, y, window, enemy, friend, end_window, enemy_red, enemy_white, friend_red, friend_white)
            window.nametowidget(f"frame_enemy.enemy{x}{y}").config(state=NORMAL,
                                                                   image=deafult_image,
                                                                   command=player_choice)
            if friend.is_ocupied[x][y] == "*":
                window.nametowidget(f"frame_player.player{x}{y}").config(image=friend_gray)
                                                                           

def enemy_choice(window, friend, enemy, end_window, enemy_red, enemy_white):

    """
    Συνάρτηση επιλογής επόμενης κίνησης απο τον εχθρό.

    window = Το κύριο παράθυρο του παιχνιδιού.
    friend = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον παίχτη.
    enemy = Το αντικειμενο που περιέχει όλες τις πληροφορίες για τον εχθρό.
    end_window = Το παράθυρο το οποίο εμφανίζεται με τη λήξη του παιχνιδιού.
    enemy_red = Το χρώμα που παίρνουν τα κουμπιά σε περίπτωση ύπαρξης εχθρικού πλοίου
    enemy_white = Το χρώμα που παίρνουν τα κουμπιά σε περίπτωση μη ύπαρξης εχθρικού πλοίου

    Συνάρτηση η οποία εκτελέι τις απαραιτητες ενέργειες για να κάνει τον εχθρό έξυπνο
    δηλαδή να επιλέγει την επόμενη κίνησή του ορθά. Χρησιμοποιει της συναρτήσεις απο το
    module Enemy_Algorythm για την επίτευξη του σκοπού του.
    """

    # Καθυστέρηση της εκτέλεσης κατα 1 δευτερόλεπτο.
    time.sleep(1)
                
    
    # Μεταβλητή για την επιστρογή του χρώματος απο τη συνάρτηση check_if_tile_is_ship
    color = ""

    some_ship = [friend.destroyer,
                 friend.cruiser,                 
                 friend.battleship,
                 friend.aircraft_carrier]

    # Εδώ γίνεται έλεγχος άν οι συντεταγμένες που επιλέγει ο εχθρός ανήκουν σε κάποιο
    # από τα πλοία του παίχτη.
    if not friend.hit:
        # Αν δεν έχει χτυπηθεί κάποιο πλοίο, ο υπολογιστής παίρνει γενικά τυχαίες συντεταγμένες
        # από το ταμπλό
        friend.position = random.choice(friend.choice)
    else:
        # Αν χτυπηθεί κάποιο πλοίο τότε ο υπολογιστής βλέπει αν η θέση έχει χτυπηθεί ξανά
        # αλλιώς αλλάζει την κατεύθυνση της επόμενης επίθεσής του
        friend.direction, friend.passes = check_hit_validity(friend.position,
                                                             friend.direction,
                                                             friend.choice,
                                                             friend.passes,
                                                             friend.ROWS,
                                                             friend.COLUMNS,
                                                             friend.is_ocupied)
        if friend.passes > 1:
            ######
            # Ο αλγόριθμος αυτός αφαιρεί τις περιμετρικές συντεταγμένες ενός πλοίου αφού
            # καταστραφεί, αφού ξέρουμε πως δεν γίνεται να εφάπτονται τα πλοία.
            for coords in some_ship[friend.counter-2]["adjacent"]:
                if coords in friend.choice:
                    friend.choice.remove(coords)
            ######
            friend.hit = False
            friend.counter = 0
            friend.position = random.choice(friend.choice)
            friend.passes = 0

    # Αν δεν έχει χτυπηθεί στην προηγούμενη βολή κάποιο πλοίο, τότε γίνεται έλεγχος αν η επιλεγμένες
    # συντεταγμένες αντιστοιχούν σε κάποιο απο τα πλοία.
    # Αν ανήκει, δημιουργείται μία προσωρινή λίστα συντεταγμένων κοντά στο χτυπημένο πλοίο απο τις
    # οποίες θα επιλέγει ο υπολογιστής μέχρι να εξαντληθούν.
    if not friend.hit:     
        if friend.is_ocupied[friend.position[0]][friend.position[1]] == "*":
            friend.hit = True
            enemy.score += 1
            friend.counter += 1
            window.nametowidget("score").config(text=f"{Ship.ACTIVE_PLAYER_NAME}: {friend.score}\tCPU: {enemy.score}")
            friend.direction = "up"
            friend.choice.remove(friend.position)
            window.nametowidget(f"frame_player.player{friend.position[0]}{friend.position[1]}").config(image=enemy_red)
        # Αν δέν βρεθεί συντεταγμένη πλοίου
        else:
            friend.choice.remove(friend.position)
            window.nametowidget(f"frame_player.player{friend.position[0]}{friend.position[1]}").config(image=enemy_white)
    # Αν έχει χτυπηθεί στην προηγούμενη βολή κάποιο πλοίο, τότε γίνεται έλεγχος αν η επιλεγμένες
    # συντεταγμένες απο την προσωρινή μνήμη αντιστοιχούν σε κάποιο κομμάτι του πλοίου.
    else:
        friend.position, friend.direction, friend.choice, color = check_if_tile_is_ship(friend.position,
                                                                                        friend.direction,
                                                                                        friend.choice,
                                                                                        friend.is_ocupied)
        if color[0] == "red":
            window.nametowidget(f"frame_player.player{color[1][0]}{color[1][1]}").config(image=enemy_red)
            enemy.score += 1
            friend.counter +=1
            window.nametowidget("score").config(text=f"{Ship.ACTIVE_PLAYER_NAME}: {friend.score}\tCPU: {enemy.score}")
        else:
            window.nametowidget(f"frame_player.player{color[1][0]}{color[1][1]}").config(image=enemy_white)


def end_game(end_window):
    """
    Μία συνάρτηση η οποία εμφανίζει το παράθυρο του τερματισμού.

    end_window = Το παράθυρο το οποίο εμφανίζεται με τη λήξη του παιχνιδιού.
    """

    center_window(end_window)

    end_window.deiconify()

    end_window.lift()
    end_window.grab_set()
        
        
        
