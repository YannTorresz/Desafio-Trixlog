#verificar o site
import urllib3
import telepot
sempre = 0
while (sempre == 0):
	try:
		http = urllib3.PoolManager()
		r = http.request("GET", "http://localhost/Telegram/")
		r.status
		t= int(r.status)
	except:
		t= 404

	arquivo = open("Status.txt", "r")
	conteudo = arquivo.read()
	arquivo.close()

	bot = telepot.Bot("1020447898:AAHWY_MfhRGiqa4PdcVxbXNMssCUIYnOXwE")

	if ((t == 200) and (conteudo != "Online")):
		bot.sendMessage(-343579963, "O sistema esta online!")
		arquivo = open("Status.txt", "w")
		arquivo.write("Online")
		arquivo.close()
	elif ((t != 200) and (conteudo != "Offline")):
		bot.sendMessage(-343579963,"O sistema esta offline!")
		arquivo = open("Status.txt", "w")
		arquivo.write("Offline")
