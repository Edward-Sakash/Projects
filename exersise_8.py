data = """id,first_name,last_name,email,ip_address
1,Jennine,Kohnert,jkohnert0@disqus.com,45.55.73.106
2,Katalin,Nolda,knolda1@123-reg.co.uk,223.30.112.215
3,Atalanta,Kaming,akaming2@gmpg.org,254.219.7.208
4,Kassie,Covell,kcovell3@cafepress.com,150.145.187.71
5,Vonni,Dignam,vdignam4@cafepress.co.uk,138.219.98.53
6,Billie,Neubigging,bneubigging5@addthis.org,180.79.192.175
7,Etan,Peers,epeers6@cafepress.com,199.1.3.70
8,Pail,Walcher,pwalcher7@cafepress.com,199.170.155.126
9,Edlin,Kosel,ekosel8@columbia.edu,217.59.107.252
10,Jennifer,Tibalt,jtibalt9@sun.com,73.29.190.227
11,Douglas,Howe,dhowea@cafepress.com,93.94.19.71
12,Galina,Antoniewski,gantoniewskib@freewebs.com,69.177.160.104
13,Emelita,Pauer,epauerc@house.gov,178.243.169.131
14,Edmon,Cleugh,POTATOKING.2000@furl.net,100.219.252.98
15,kyo,zipulimakkarakeitto,kz@guardian.com,78.226.120.240
16,Harlin,Goodrich,hgoodrichf@guardian.com,232.242.92.122
17,Paddie,Brittain,pbrittaing@jigsy.com,230.116.80.29
18,Blisse,Barbrook,bbarbrookh@nytimes.com,153.237.126.205
19,Latia,Roughey,lrougheyi@guardian.co.uk,184.128.166.8
20,Gregoire,Castelow,gcastelowj@51.la,87.181.120.134
21,lorenza,kurn,ljurnk@nsw.gov.au,192.238.146.135
22,Dulciana,Wilce,dwilcel@noaa.gov,234.245.232.7
23,Boyd,Sponton,bspontonm@guardian.com,106.75.217.74
24,Lenora,Issard,lissardn@guardian.com,167.91.15.190
25,Lissi,Davidovitz,ldavidovitzo@guardian.com,48.7.220.5"""

lines = data.split("\n")
print(lines)
print(lines[1])
print(len(lines))

count = 0

for user in lines: 
 count = count + 1

 if count == 5: 
  count = 0
  print(user)

  #Task 2

count = 0  

for user in lines:
 if count == 0:
  count = 5
  #print("first")
 else:
  user_data = user.split(",") 
 # print(user_data) 
  print(user_data[3])

print("-------------")

#Task 3
count = 0  
emails_with_co = 0

for user in lines:
 if count == 0:
  count = 5
  #print("first")
 else:
  user_data = user.split(",") 
 # print(user_data) 
  #print(user_data[3])

  if ".co.uk" in user_data[3]:
   emails_with_co = emails_with_co + 1

 first_name = user_data[1].upper()
 #print(first_name[0])
 if first_name[0] == "K":
  print("K")


print(emails_with_co)


