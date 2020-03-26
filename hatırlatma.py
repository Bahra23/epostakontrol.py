import time
import datetime 
import locale 
import sqlite3

locale.setlocale(locale.LC_ALL, '') #Türkçe dilinde ayarladık.

bugün = datetime.datetime.now()
bugün_month = datetime.datetime.strftime(bugün,'%B')
bugün_days = datetime.datetime.strftime(bugün,'%A')
print("Bilginiz olsun",bugün.year,"yılındayız.",bugün_month,"ayındayız.",bugün_days,"günündeyiz.")

hatırlatıcı_adı = str(input("Neyi hatırlatmamı istersin:")) 
time.sleep(0.3)
müddet_sonra = str(input("""Hangi zamandan sonra hatırlatmamı istersiniz? 

>> Gün
>> Dakika
>> Saniye
"""))
süre = int(input("Ne kadar süre sonra: "))

if müddet_sonra == "Gün":
    hatırlatma_günü = datetime.timedelta(days=süre)
    time.sleep(süre)
    print(hatırlatıcı_adı)

"""elif müddet_sonra == "Saniye":
	hatırlatma_günü = datetime.timedelta(minute= süre)
    time.sleep(süre)
    print(hatırlatıcı_adı)"""

"""import time
print("What shall I remind you about?")
text = str(input())
print("In how many minutes?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)
print("Bu internette bulduğum örnek.")
"""