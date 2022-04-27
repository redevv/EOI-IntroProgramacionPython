from datetime import datetime
from pytz import timezone
import pytz

# print(pytz.all_timezones) -> Aparecen todas las zonas horarias del planeta
print(datetime.now(pytz.timezone('Asia/Tokyo')))
print(datetime.now(pytz.timezone('Europe/Madrid')))
