#verificar o site
import urllib3
import telepot
sempre = 0
while (sempre == 0):
	try:
		http = urllib3.PoolManager()
		r = http.request("GET", "http://138.68.228.15:3000")
		r.status
		t= int(r.status)
	except:
		t= 404


	arquivo = open("Status.txt", "r")
	conteudo = arquivo.read()
	arquivo.close()

	bot = telepot.Bot("1020447898:AAHWY_MfhRGiqa4PdcVxbXNMssCUIYnOXwE")

	if (t == 200):
		if (conteudo != "Online"):
			bot.sendMessage(-343579963, "O sistema esta online!")
			bot.sendMessage(-343579963, t)
			arquivo = open("Status.txt", "w")
			arquivo.write("Online")
			arquivo.close()
			print "ok", t
	elif (t != 200):
		if(conteudo != "Offline"):
			bot.sendMessage(-343579963,"O sistema esta offline!")
			bot.sendMessage(-343579963, t)
			arquivo = open("Status.txt", "w")
			arquivo.write("Offline")
			arquivo.close()
			print "of", t

