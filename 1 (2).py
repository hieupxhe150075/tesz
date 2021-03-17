import random
import os



os.system("clear")

aas = """

╭━━━┳╮╱╭┳━━━┳━━━┳━━━╮
┃╭━╮┃┃╱┃┃╭━╮┃╭━╮┃╭━╮┃
┃┃╱╰┫┃╱┃┃╰━╯┃┃╱╰┫┃╱┃┃
┃┃╭━┫┃╱┃┃╭╮╭┫┃╭━┫╰━╯┃
┃╰┻━┃╰━╯┃┃┃╰┫╰┻━┃╭━╮┃
╰━━━┻━━━┻╯╰━┻━━━┻╯╱╰╯
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       
Am Toola taybata badrws Comboy raqam krdni raqa 4mlonraqam ba tekaly
random asyawkorak drwsaka
 =============================
"""

def start():
	print(aas)
	a = ("+962770","+962750","+962771","+962751","+962772","+962773")
	hh = ("1122334455","1234512345")
	op=open(".txt","w")
	for x in range(4000000):
		f = "1234567890"
		x1 = random.choice(a)
		x2 = random.choice(f)
		x3 = random.choice(f)
		x4 = random.choice(f)
		x5 = random.choice(f)
		x6 = random.choice(f)
		x7 = random.choice(f)
		x8 = random.choice(f)
		x9 = random.choice(f)
		x10 = random.choice(f)
		x11 = random.choice(f)
		x22 = random.choice(hh)
		
		dd = x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+":"+x22
		print(dd)
		op.write(dd+"/n")
		

		
def ss():
	print(aas)
	print("Tkaya bo das pekrdn [1]Lebda")
	
	f = int(input("[×] option : "))
	if f==1:
		os.system("clear")
		start()
	else :
		print("Tkaya Zhmara[1]Bnwsa")
		
ss()
		
		
	
	
