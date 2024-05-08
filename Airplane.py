class Airplane:
    def __init__(self, id_num, company, airport):
        self.id_num = id_num
        self.company = company
        self.flying = False
        self.airport = airport
        self.destination = None

    #apogeiwsi me proorismo to airport
    def take_off(self, airport):
        self.flying = True
        self.destination = airport

    #prosgeiwsi(an vrisketai se ptisi)
    def landing(self):
        if not self.flying:
            return False
        else:
            self.flying = False
            self.airport = self.destination
            return True

    #airplane info
    def info(self):
        return f"Το αεροπλάνο {self.id_num}, τύπου: {self.air_type}, εταιρία {self.company}"

    #print tin katastasi tou aeroplanou(an einai se ptisi i exei prosgeiwthei)
    def __str__(self):
        if self.flying:
            return f"Κατάσταση: Σε πτήση προς το αεροδρόμιο {self.destination}"
        else:
            return f"Κατάσταση: Έχει προσγειωθεί στο αεροδρόμιο {self.airport}"
# Passenger Airplane Class
class Passenger_Plane(Airplane):
    '''Η κλάση Passenger_Plane κληρονομεί την κλάση Airplane, αφορά την κατηγορία επιβατηγών αεροπλάνων. '''
    def __init__(self, id_num,company,type,flying,airport,passengers):
        self.id_num=id_num
        self.company=company
        self.type=type
        self.flying=flying 
        self.airport=airport
        self.passengers=passengers

    def __str__(self):
        return (f'Πτήση επιβατηγού αεροπλάνου\nΤο αεροπλάνο {self.id_num}, τύπου:{self.type},εταιρία: {self.company}\nΚατάσταση:' )