from random import randint
import datetime
from lxml import html
import requests
from bs4 import BeautifulSoup
import time

#BIN="442347xxxxxxxxxx"
bin_list = []



def read_the_last_bin():
    # file_bin=open('last_bin' ,'w')
    with open("last_bin") as file_bin:
        lines=file_bin.readlines()
    v_last_bin=lines[0].replace("\n","")
    return v_last_bin


def add_to_last_bin():
    l_bin=read_the_last_bin()
    print(l_bin)
    new_bin=int(l_bin)+1
    binani=str(new_bin)
    #################
    with open("last_bin","w") as file_bin:
        file_bin.write(binani)

def save_successed_bin(card_numer):
    # l_bin=read_the_last_bin()
    print(card_numer)
    # new_bin=int(l_bin)+1
    # binani=str(new_bin)
    #################
    with open("succed_bin","a") as file_bin:
        file_bin.write(card_numer+"\n")







def cc_gen(BIN) :
    #bin_list =[]
    cctype=cc_check (BIN)
    print(cctype)
    if cctype != 'UNKNOWN':
        BIN_V = bin_len_check (BIN)
        BIN_V = BIN_V.upper()
        ADD_X =16-len(BIN_V)
        BIN_V = BIN_V+("X")*ADD_X
        

        #print (BIN_V)
    else:
        print ("invalid")
        return
    #print(BIN_V)
    return BIN_V

def cc_check (bin_format):
    global cc_type
    print("CARD TYPE        :  ", end='',flush=True)
    if bin_format.startswith(('4', '5','6','R')) !=True:
        cc_type="UNKNOWN"
    else:
        cc_type = cc_type_check(bin_format)
    return cc_type




def bin_len_check (BIN):
    print("VALIDATE THE BIN :  ",end='',flush=True)
    if len(BIN) != 16:
        bin_len_valid = 0
    else:
        bin_len_valid = 1
        BIN0 = bin_mod (BIN)
        print(BIN0)
    #return #bin_len_valid , BIN
    return BIN0




def cc_check (bin_format):
    global cc_type

    print("CARD TYPE        :  ", end='',flush=True)
    if bin_format.startswith(('4', '5')) !=True:
        cc_type="UNKNOWN"
    else:
        cc_type = cc_type_check(bin_format)
    return cc_type




def cc_type_check (bin_format):
    
    if bin_format.startswith(('4')) ==True:
        cc_type="VISA"
    else:
        cc_type="MASTER"
    if bin_format.startswith(('R')) ==True:
        cc_type="VISA"
    if bin_format.startswith(('6')) ==True:
        cc_type="DISCOVERY"
    return cc_type


def bin_mod (BIN):
    count=0
    #global BIN
    for v in BIN [::-1]:
        try:
            if v.isdigit() != True:
                count-= 1
            else:
                break
        except:
            continue
    BIN0 =BIN[0:count]
    return BIN0

def cc_genrator(BIN_V):
    out_card=""
    for i in range(15):
        if BIN_V[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            #out_card = out_card + str(randint(0,9))
            out_card = out_card + BIN_V[i]
            continue
        elif  BIN_V[i] in ("x"):
            out_card = out_card + str(randint(0,9))
    #return out_card
    #chk 
    for i in range(10):
        checksum_check = out_card
        checksum_check = checksum_check + str(i)
        if cardLuhnChecksumIsValid(checksum_check):
            out_card = checksum_check
            break
        else :
            checksum_check = out_card
    return out_card


def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

#GENERA UNA BASE DE BIN XXXXXXXXXXXXXXXX
#GENERA UNA BASE DE BIN XXXXXXXXXXXXXXXX

def ccvgen():
    ccv = ""
    num = randint(10,999)

    if num < 100:
        ccv = "0" + str(num)
    else:
        ccv = str(num)
    #print(ccv)

    return(ccv)

        
def dategen():
    #print("shit")
    now = datetime.datetime.now()
    date = ""
    month = str(randint(1, 12))
    if int(month) < 10 :
        month = "0"+month
    current_year = str(now.year)
    year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 4))
    date = month + "|" + year
    #print(date)
    return date

def bin_remove_x (BIN):
    count=0
    #global BIN
    for v in BIN [::-1]:
        try:
            if v.isdigit() != True:
                count-= 1
            else:
                break
        except:
            continue
    BIN0 =BIN[0:count]
    return BIN0





def rigle_bin(bin_fazed):
    #print(bin_fazed)
    BIN_V = "invalid"
    if len(bin_fazed) < 6 and len(bin_fazed)> 16 :
        BIN_V = "invalid"
        #print("lenght < 6")

    if len(bin_fazed) <=16 and len(bin_fazed) >=6 :
        #print("gooo")
        addx=16 - len(bin_fazed)
        #print(bin_remove_x (bin_fazed))
        BIN_V = bin_fazed+("x")*addx
        #print(BIN_V)
    return BIN_V



def generator_bin_old(bin_numbre,quantity):
    #print(bin_numbre,quantity)
    bin_all_card=[]
    for i in range(int(quantity)):
        if "RND" in bin_numbre :
            print("RANDOM")
        else :
            bin0_0=rigle_bin(bin_numbre)
            #print(bin0_0)
            bin_all_card.append(cc_genrator(bin0_0)+"|"+dategen()+"|"+ccvgen()+"| [ "+bin_numbre+" ] ")
    #print(bin_all_card)
    return bin_all_card

def generator_bin(bin_numbre,quantity):
    #print(bin_numbre,quantity)
    bin_all_card=[]
    for i in range(int(quantity)):
        if "RND" in bin_numbre :
            print("RANDOM")
        else :
            bin0_0=rigle_bin(bin_numbre)
            #print(bin0_0)
            bin_all_card.append(cc_genrator(bin0_0)+"#"+dategen()+"#"+ccvgen())
    #print(bin_all_card)
    return bin_all_card
# bin_all_card=generator_bin("5543505076", 1)
# print(bin_all_card)
def generate_card_from_bin(bin_number):
    arry_card_bin_info=[]
    # print("GENERATE CARD  OF BIN [ "+bin_number+" ]            ",end='',flush=True)
    print(" _GENERATE CARD  OF BIN       : ",end='',flush=True)
    # time.sleep(1)
    bin_all_card=generator_bin(bin_number,1)
    # print(bin_all_card)
    arry_bin=bin_all_card[0].split("#")
    card_num=arry_bin[0]
    card_date=arry_bin[1]
    card_date=card_date.replace('|','')
    card_ccv=arry_bin[2]
    arry_card_bin_info.extend((card_num,card_date,card_ccv))
    print(arry_card_bin_info)
    return arry_card_bin_info