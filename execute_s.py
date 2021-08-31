from org.apache.nifi.processors.script import ExecuteScript #processor importu
from org.apache.nifi.processor.io import StreamCallback # ne zman çagıracağim belli olmayan fonk
from java.nio.charset import StandardCharsets #Dönüşüm Formatı
from org.apache.commons.io import IOUtils #yönlendirme
import re #regex

class inputSC(StreamCallback): #fonksiyonlarımı buranın içinde kullanacağim

  def __init__(self):
  def flow(self, input, output):

      logs=IOUtils.toString(input, StandardCharsets.UTF_8) #loglarımı alıyorum. değişik karakterliler sorun cıkarmasın diey utf ekliyorum
      """time, date , srcip, srcport, dstcountry, log type , transip , transport  """
      # üstünde çalıştıgım kısım

      date_regex=re.search("\d{4}-\d+-\d+",logs) #forti ve sophos
      date_check=re.search("((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\W+(0[1-9]|[12]\d|3[01]))",logs)
      date_palo=re.search("\d{4}/\d{2}/\d{2}",logs)
      logid_forti=re.search("(?<=logid=\W+)\w+",logs)
      logid_check=re.search("")
      logid_sophos=re.search("(?<=log_id=)\w+",logs)
      logid_palo=re.search("(?<=SerialNumber=)\w+",logs)

      time_regex=re.search("(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",logs) #hepsine uyuyor

      srcip_forti=re.search("(?<=srcip=)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",logs) 
      srcip_check=re.search("(?<=src=\W+)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",logs) 
      srcip_sophos=re.search("(?<=src_ip=)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",logs) 
      srcip_palo=re.search("(?<=src=)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",logs)

      type_forti=re.search("(?<=type=\W+)\w+",logs)
      type_check=re.search("")
      type_sophos=re.search("(?<=log_type=\W+)\w+",logs)
      type_palo=re.search("")

      subtype_forti=re.search("(?<=subtype=\W+)\w+",logs)
      subtype_check=re.search("")
      subtype_sophos=re.search("(?<=log_subtype=\W+)\w+",logs)
      subtype_palo=re.search("(?<=Subtype=)\w+",logs)

      level_forti=re.search("(?<=level=\W+)\w+",logs)
      level_check=re.search("")
      level_sophos=re.search("")
      level_palo=re.search("")
  
      srcport_forti=re.search("(?<=srcport=)\w+",logs)
      srcport_check=re.search("")
      srcport_sophos=re.search("(?<=src_port=)\w+",logs)
      srcport_palo=re.search("(?<=srcPort=)\w+",logs)
      
      src_interface_forti=re.search("(?<=srcintfrole=\W+)\w+",logs)
      src_interface _check=re.search("")
      src_interface_sophos=re.search("(?<=in_interface\W+)\w+\W+\w+")
      src_interface_palo=re.search("")

      dstip_forti=re.search("(?<=dstip\W+)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",logs)
      dstip_check=re.search
      dstip_sophos=re.search("(?<=dst_ip\W+)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",logs)
      dstip_palo=re.search("(?<=dst\W+)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",logs)

      _forti=re.search
      _check=re.search
      _sophos=re.search
      _palo=re.search

      _forti=re.search
      _check=re.search
      _sophos=re.search
      _palo=re.search




      
      
