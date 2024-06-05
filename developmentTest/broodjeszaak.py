from typing import Any
import csv
from datetime import date, datetime

# lijst met bestellingen
bestellingen = []
# hoeveelheid bestellingen
count_bestelling = 1
#status bestelling 
status = "Finished" #--> hypothetisch

#bestellingUitgevoerd = False # veranderen naar True met druk op knop
#bestellingCancel = False # veranderen naar True met druk op knop
#status = "To do"
#if bestellingUitgevoerd:
#    status = "Finished"
#elif bestellingCancel:
#    status = "Cancelled"

class Broodje:
    def __init__(self):
        self.brood = ["Geen", "Wit", "Bruin", "Waldkorn", "Multi-granen"]
        self.beleg = ["Kaas", "Ham", "Kip-curry", "American", "Krabsla", "Gebakken kip"]
        self.saus = ["Geen", "Mayonaise", "Ketchup", "Pepersaus", "Andalouse", "Cocktail"]
        self.smos = ["yes", "no"]

    # return lijst brood
    def returnBrood(self):
        #for br in self.brood:
        #    print(br)
        return self.brood
    
    # return lijst beleg
    def returnBeleg(self):
        return self.beleg
    
    # return lijst saus
    def returnSaus(self):
        return self.saus
    
    # return lijst smos
    def returnSmos(self):
        return self.smos
    

broodjes = Broodje()
print(broodjes.returnBrood())
print(broodjes.returnBeleg())
print(broodjes.returnSaus())

class besteldBroodje:
    def __init__ (self, brood, beleg, saus, smos):
        self.brood = brood
        self.beleg = beleg
        self.saus = saus
        self.smos = smos
        #self.status = status
    
    def returnBroodje(self):
        return [self.brood, self.beleg, self.saus, self.smos]
    
#gekozenbroodje = besteldBroodje("Wit", "ham", "mayonaise", "yes") #--> afhankelijk van wat aangeduid wordt in GUI
#print(gekozenbroodje.returnBroodje())
#bestellingen = bestellingen.append(gekozenbroodje.returnBroodje()) #--> na druk op plaats bestelling knop

# maak dictionary van prijzen
with open('Broodjesprijzen.csv', mode='r') as prijzen_file:
    csv_reader = csv.reader(prijzen_file, delimiter=';')
    prijslijst = {}
    count = 0
    for row in csv_reader:
        count +=1 
        # skip header
        if count > 1:
            item = row[0]
            prijs = row[1]
            prijslijst[item] = prijs
    #print(prijslijst)

# hypothetische bestellingen
bestellingen = [["Wit", "ham", "mayonaise", "yes"], ["bruin", "kaas", "ketchup", "no"]]
    
# maak csv met status van bestellingen
with open('geplaatsteBestellingen.csv', mode='w') as bestelde_file:
    bestelde_writer = csv.writer(bestelde_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for bestelling in bestellingen:
        if status == "To do":
            bestelde_writer.writerow([bestelling, "To do"])
        elif status == "Finished":
            bestelde_writer.writerow([bestelling, "Finished"])
        elif status == "Cancelled":
            bestelde_writer.writerow([bestelling, "Cancelled"])
bestelde_file.close()


def returnPrijs(best):
    # brood
    prijsbrood = prijslijst[best[0]]
    prijsbrood = float(prijsbrood.replace(',', '.'))
    # beleg
    prijsbeleg = prijslijst[best[1]]
    prijsbeleg = float(prijsbeleg.replace(',', '.'))
    #saus
    prijssaus = prijslijst[best[2]]
    prijssaus = float(prijssaus.replace(',', '.'))
    # smos
    if best[3] == "yes":
        prijssmos = prijslijst["smos"]
        prijssmos = float(prijssmos.replace(',', '.'))
    elif best[3] == "no":
        prijssmos = 0
    return format(sum([prijsbrood, prijsbeleg, prijssaus, prijssmos]), '.2f')

#print(returnPrijs())

# maak rekening voor elke afgehandelde bestelling
for bestelling in bestellingen:
    if status == "Finished":
        rekening = open("Rekening_broodjeszaak_" + str(datetime.today().strftime('%Y%m%d')) + "_" + str(count_bestelling) +".txt", "w")
        rekening.write("Rekening broodjeszaak\n======================")
        rekening.write("\n{}".format(datetime.today().strftime('%d/%m/%y'))) 
        rekening.write("\nBestelling: \t{} \n\n".format(count_bestelling))
        rekening.write("{}\n{}\n{}".format(bestelling[0], bestelling[1], bestelling[2]))
        if bestelling[3] == "yes":
            rekening.write("\n{}".format("Smos"))
        rekening.write("\n\nTotale prijs: \t{}".format(str(returnPrijs(bestelling)).replace('.', ',')))
        rekening.close()
    count_bestelling += 1


