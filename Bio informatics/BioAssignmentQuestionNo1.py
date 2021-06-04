def questionNo1(filename):
    counter =1
    listing = 1;
    Dna = ""
    Rna = ""
    Flag = 0
    first =0
    Second = 3
    Seq = ""
    Condon = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    with open(filename,'r') as f:
        for line in f:
            for word in line.split():
                if (counter == 1):
                    sequence = word
                    
#                     print(sequence)
                    
                if (counter == 2):
                    number = int(word)
                    
                if (counter == 3):
                    number1 = int(word)
                    
                counter = counter +1
            counter = 1
            
#           splicing points

            for i in range(0,len(sequence)):
                if(i >= number and i <= number1):
                    continue
                else:
                    Dna = Dna + sequence[i]
                    
#           Dna into Rna
            
            for i in range(0,len(Dna)):
                if(Dna[i] == "G"):
                    Rna = Rna +"C"
                if(Dna[i] == "C"):
                    Rna = Rna + "G"
                if(Dna[i] == "T"):
                    Rna = Rna + "A"
                if(Dna[i] == "A"):
                    Rna = Rna + "U"
                    
#          Form Codon Table 

            vara1= int(len(Rna)/3)
            for i in range(0,vara1):
                if (Flag == 1 and Rna[first:Second] != ""):
                    if(Rna[first:Second] == "STOP"):
                        Flag = 0
                    else:
                        vara= Rna[first:Second]
                        seq = seq + (Condon[vara])
                if (Rna[first:Second] == "AUG"):
                    seq = Condon["AUG"]
                    Flag = 1
               
                first += 3
                Second +=3
                
            print("The",listing,"Sequence is " ,seq)
            listing = listing + 1
            Rna = ""
            Dna =""
            
questionNo1("Bio_File.txt")