
#define procedure Ciphertext()
def CipherText():
    global Temp
    global Cipher
    global Asal
    
    Temp=[ ]
    Cipher=[ ]
    
    Asal=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    K= int( input ("Masukkan Kunci: "))
    for a in range (K) :
        Temp.append (Asal[a])
        
    for b in range ( K , 26 ):
        Cipher.append(Asal[b])
        
    for c in range (K):
        Cipher.append(Temp[c])
        
#define Function CipherText
def Encrypt(Mesej): #Parameter
    Secret=" "
    for a in range (len(Mesej)):
        for b in range(0,26):
            if Mesej[a].isalpha()==True:
                if Mesej[a].islower()==True:
                    if Mesej[a].upper()==Asal[b]:
                       Secret=Secret+Cipher[b].lower()
                else:
                  if Mesej[a]==Asal[b]:
                      Secret=Secret+Cipher[b]
            else:
                Secret=Secret+Mesej[a]
                break
            
    return Secret

def Decrypt(SiferT):
    Secret=""
    for a in range (len(SiferT)):
        for b in range( 0,26 ):
            if SiferT[a].isalpha()==True:
               if SiferT[a].islower()==True:
                  if SiferT[a].upper()==Cipher[b]:
                      Secret=Secret+Asal[b].lower()
               else:
                  if SiferT[a]==Cipher[b]:
                     Secret=Secret+Asal[b]
            else:
                Secret=Secret+SiferT[a]
                break
            
    return Secret



def displaystart():
    print('''

         ====== ===  ===  =======   ===   ===  ========  ======
      ========= ===  ===  ========  ===   ===  ========  =======
      ==        ===  ===  ===   ==  ===   ===  ===       ===   ==
      ==        ===  ===  ========  =========  ======    =======
      ==        ===  ===  =======   ===   ===  ===       ======
      ========= ===  ===  ===       ===   ===  ========  ===  ===
         ====== ===  ===  ===       ===   ===  ========  ===   ===
         
    ''')
    
    
    #Main Program
    print("Selamat Datang")
    displaystart()
    
    while (True):
        print ('''

        =============================================================
                                   PILIHAN
        =============================================================
        ==                      E-Encryption                       ==
        ==                      C-Decryption                       ==
        ==                      X-Exit                             ==           
        =============================================================
        ''')
        pilihan = input("Masukkan pilihan E atau C sahaja: ")
        
        if pilihan.upper()=='E':
            CipherText()
            Mesej=input("Masukkan Mesej Anda : ")
            MesejSulit = Encrypt(Mesej)  #Argument
            print("Mesej sulit anda ialah : ", MesejSulit )
            
        elif pilihan.upper()=='C':
            CipherText()
            SiferT=input("Masukkan Mesej Sulit Anda :")
            MesejPlain = Decrypt(SiferT)
            print("Mesej yang dinyahsulit ialah : ", MesejPlain)
            
        elif pilihan.upper()=='X':
            break
        else:
            pilihan = input("Masukkan pilihan E atau C sahaja :")
            
    #End Program
    displaystart()
    print('''
       ======   ===   ===   ===  =========
       ===       === ===    ===  =========
       ======      ===      ===     ===
       ======    === ===    ===     ===
       ===      ===   ===   ===     ===
       ======  ===     ===  ===     ===
    ''')
            
    