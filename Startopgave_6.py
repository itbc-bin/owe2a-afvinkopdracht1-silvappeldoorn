
# Naam:
# Datum:
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    try:

        bestand = "alpaca.fa" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
        if ".fasta" not in bestand and not ".fa" in bestand:
            raise ValueError
    except ValueError:
        print("Dit bestand is geen fasta bestand, plaats een geldig bestand in de map.")

    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
    try:
        header, seqs = lees_inhoud(bestand) 
    
        zoekwoord = input("Geef een zoekwoord op: ")

        
        lijstZoekwoord = [i for i, s in enumerate(header) if zoekwoord in s]
        
        index = 0
        i = 0
        
        for items in lijstZoekwoord:

            print(80 * '-')

            index = int(lijstZoekwoord[i])

            isDNA = is_dna(seqs,index)
            print("dit is de header die bij de sequentie hoort: ")
            print(header[index])

            knipt(seqs,index,zoekwoord)

            if type(isDNA) != bool:
                raise TypeError
            if isDNA == True:
                print("De sequentie is DNA")
            else:
                raise TypeError

   
            i+=1
    except UnboundLocalError:
        print("Fout met variabelen en of bestand is niet aanwezig.") 
    except KeyboardInterrupt:
        print("Onderbreking door gebruiker.")
    except TypeError:
        print("Dit bestand is geen DNA of bevat andere tekens dan ATGC.")
    
        # schrijf hier de rest van de code nodig om de aanroepen te doen
    
    
def lees_inhoud(bestands_naam):
    try:
        bestand = open(bestands_naam)       
        seqs = []
        header = []
        seq = ''
        for line in bestand:  
            #print(line)
            if line.startswith('>'):
                line = line.replace('\n', '')
                header.append(line)
                if seqs != '':
                    seqs.append(seq)
                    seq = ''
            else:
                line = line.replace('\n', '')
                seq += line
                
        seqs.append(seq)
        seqs.remove('')



    except IOError:
        print("Dit bestand bestaat niet in deze map.")    
    except FileNotFoundError:
        print("Dit bestand bestaat niet in deze map.")
    
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
     
    return header, seqs

    
def is_dna(seqs,index):

    aantala = int(seqs[index].count("A"))
    aantalg = int(seqs[index].count("G"))
    aantalt = int(seqs[index].count("T"))
    aantalc = int(seqs[index].count("C"))
    totaal = aantala + aantalg + aantalt + aantalc

    isDNA = False

    if totaal == len(seqs[index]):
       isDNA = True
    
    return isDNA

    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    

def knipt(seqs,index,zoekwoord):
    enzymen = open("enzymen.txt")
    enzym_list = []
    i=0
    for regel in enzymen:
        enzym, seq = regel.split()
        seq = seq.replace('^', '')                          
        for seq_index in range(0,len(seqs[index])):
            if seqs[index][seq_index:len(seq) + seq_index] == seq:
                if enzym not in enzym_list:
                    enzym_list.append(enzym)
    print("deze restrictie enzymen knippen in de sequentie die bij", zoekwoord, "hoort: ")
    while i < len(enzym_list):
        print(enzym_list[i])
        i += 1 
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
       
    
main()
