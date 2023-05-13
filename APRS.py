import re
import math

class APRS:
  debug = False

  def __init__(self, debug=False):
     self.debug=debug
  
  def makeTimestamp(self, format, day, hour, minute, sec='00'):
    if (format == 'z'): 
       return '{}{}{}z'.format(day, hour, minute)
    else:
       return '{}{}{}h'.format(hour, minute, sec)
    
  def makePosition(self, lat, lon, speed, course, altitude, symbol):
     # FIXME: course/speed/altitude are not supported yet,

     # check lat/lon
     if (lat < -89.99999 or lat > 89.99999 or
        lon < -179.99999 or lon > 179.99999):
        return None
     
     symboltable = ""
     symbolcode = ""
     if len(symbol) == 0:
          symboltable = "/"
          symbolcode = "/"
     elif re.match(r"^([\/\\A-Z0-9])([\x21-\x7b\x7d])$", symbol):
          symboltable = symbol[0]
          symbolcode = symbol[1]
     else:
          return None
      

     latval = 380926 * (90 - lat)
     lonval = 190463 * (180 + lon)
     latstring = ""
     lonstring = ""
     for i in range(3, -1, -1):
       value = int(latval / (91 ** i))
       latval = latval % (91 ** i)
       latstring += chr(value + 33)
       value = int(lonval / (91 ** i))
       lonval = lonval % (91 ** i)
       lonstring += chr(value + 33)

     symboltable = re.sub(r"[0-9]", lambda m: chr(ord(m.group()) - ord("0") + ord("a")), symboltable)
     retstring = symboltable + latstring + lonstring + symbolcode
      
     if speed >= 0 and course > 0 and course <= 360:
          cval = int((course + 2) / 4)
          if cval > 89:
              cval = 0
          retstring += chr(cval + 33)
          
          speednum = int((math.log((speed / 1.852) + 1) / math.log(1.08)) + 0.5)
          if speednum > 89:
              speednum = 89
          retstring += chr(speednum + 33) + "A"
     else:
          retstring += "  A"
      
     return retstring