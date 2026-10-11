from datetime import datetime

simdi = datetime.now()

print(simdi)
print(simdi.year)
#------------------------------------------------------------------------------------------
simdi.month   # ay
simdi.day     # gün
simdi.hour    # saat
simdi.minute  # dakika
#------------------------------------------------------------------------------------------

from datetime import datetime

simdi = datetime.now()

print(f" Tarih: {simdi.day}/{simdi.month}/{simdi.year}")
print(f" Saat: {simdi.hour}:{simdi.minute}")


from datetime import datetime

simdi = datetime.now()

print(f"Saat: {simdi.hour}:{simdi.minute:02d}")

#------------------------------------------------------------------------------------------
 #02d 
# 2 = minimum 2 basamaklı olacak
# d = decimal (tam sayı) olacak
# 0 = eksik basamaklar için 0 ile doldurulacak
#------------------------------------------------------------------------------------------
#%d → gün
#%m → ay
#%Y → 4 haneli yıl
#%y → 2 haneli yıl
#------------------------------------------------------------------------------------------

from datetime import datetime

simdi = datetime.now()

print(simdi.strftime("%d/%m/%Y %H:%M"))


from datetime import datetime   

simdi = datetime.now()

print(simdi.strftime("%d.%m.%y"))
