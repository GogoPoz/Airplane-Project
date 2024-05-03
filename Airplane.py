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
            return True
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
