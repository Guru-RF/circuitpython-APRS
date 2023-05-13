from APRS import APRS

aprs = APRS()

latitude = 50.94750
longitude = 4.242367
callsign = "ON3URE-11"
type = '/j'
comment = "LoRa APRS RF.Guru"
ts = aprs.makeTimestamp('z','10','08','01')
pos = aprs.makePosition(latitude,longitude,-1,-1,-1,type)

#DJ0ABR-7>APLT00,WIDE1-1:!4849.27N/01307.72E[/A=001421LoRa Tracker
message = "{}>APLORA,WIDE1-1:!{}{}".format(callsign, ts, pos, comment)
print(message)