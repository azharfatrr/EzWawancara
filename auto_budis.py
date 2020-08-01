from fpdf import FPDF
import random

print("==========================")
print("Auto Budies Maker by Azhar")
print("==========================\n")
nim_kamu = int(input("Masukkan NIM Kamu : "))
# Data Pool First Impression
fi = open("fi.txt","r")
list_fi = fi.readlines()

print("...\nProgram is Running")

def split_list(list,separator,end):
    new_list = []
    sub_list = []
    for e in list:
        if e != separator:
            sub_list.append(e)
        elif e == end:
            new_list.append(sub_list)
        else:     
            new_list.append(sub_list)   
            sub_list = [] 
    return new_list

def buat_pdf(nim_kamu,nama,nim,jurusan,unik,fi):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font("times",'B',18)
    pdf.cell(200,20,txt = "Wawancara Budies", align='C', ln=1)
    pdf.set_font("times",size=12)
    pdf.cell(0,0,txt = "", align='C',ln=2)
    pdf.cell(20,10,txt = "Nama       : %s" %nama,ln=2)
    pdf.cell(20,10,txt = "NIM        : %s" %nim,ln=2)
    pdf.cell(20,10,txt = "Jurusan    : %s" %jurusan,ln=2)
    pdf.cell(20,10,txt = "Keunikan : %s" %unik,ln=2)
    pdf.cell(20,10,txt = "First Impression : %s" %fi,ln=2)
    # Prosesnya
    out = str(nim_kamu)+"_"+(str(nim).replace(" ",""))+".pdf"
    pdf.output(out)

# Membuka data buddies
data = open("data_budis.txt","r")
array_data = data.readlines()
list_orang = split_list(array_data,"\n","Finish")

# Memulai mengisi pdf
sum = 0
i = 0
error = False
for orang in list_orang:
    fi_orang = random.sample(list_fi, k=2)
    fi = str(fi_orang[0].replace("\n","")) +", "+ str(fi_orang[1].replace("\n",""))
    for id in orang:
        i += 1
        b = id.split(":",2)
        if "nama" in b[0].lower():
            nama = b[1].replace("\n","").lstrip(' ').title()
        elif "nim" in b[0].lower():
            nim = b[1].replace("\n","").lstrip(' ')
        elif "jurusan" in b[0].lower():
            jurusan = b[1].replace("\n","").lstrip(' ')
        elif ("keunikan" or "unik") in b[0].lower():
            unik = b[1].replace("\n","").lstrip(' ').capitalize()
        else:
            print("Error: format data di file data_budis.txt tidak terbaca di line "+str(i))
            error = True
            break
    if error:
        break
    else:
        buat_pdf(nim_kamu,nama,nim,jurusan,unik,fi)
        sum += 1

if not(error):
    print("...\nProgram Finish, "+str(sum)+" people has been made.")
else:
    print("...\nProgram Finish, "+str(sum)+" people has been made.\nThere is an error occure!")
input()



