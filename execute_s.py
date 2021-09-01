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

      srcip_forti=re.search("(?<=srcip=)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs) 
      srcip_check=re.search("(?<=src=\W+)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs) 
      srcip_sophos=re.search("(?<=src_ip=)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs) 
      srcip_palo=re.search("(?<=src=)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)

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

      dstip_forti=re.search("(?<=dstip\W+)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)
      dstip_check=re.search
      dstip_sophos=re.search("(?<=dst_ip\W+)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)
      dstip_palo=re.search("(?<=dst\W+)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)

      dstport_forti=re.search("(?<=dstport=)\w+")
      dstport _check=re.search("")
      dstport_sophos=re.search("(?<=dst_port=)\w+",logs)
      dstport_palo=re.search("(?<=dstPort=)\w+",logs)

      fpolicy_forti=re.search("(?<=action=\W+)\w+",logs)
      fpolicy_check=re.search("(?<=Action=\W+)\w+",logs)
      fpolicy_sophos=re.search("")
      fpolicy_palo=re.search("(?<=action=)\w+",logs)

      NatSrcIp_forti=re.search("(?<=transip=)(?:[0-9]{1,3}\.){3}[0-9]{1,3}"logs)  
      NatSrcIp_check=re.search("")
      NatSrcIp_sophos=re.search("")
      NatSrcIp_palo=re.search("(?<=srcPostNATPort=)\w+",logs)

      sentbyte_forti=re.search("(?<=sentbyte=)\w+",logs)
      sentbyte_check=re.search("")
      sentbyte_sophos=re.search("(?<=sent_bytes=)\w+",logs)
      sentbyte_palo=re.search("")

      pcktrcivd_forti=re.search("(?<=rcvdpkt=)\w+",logs)
      pcktrcivd_check=re.search("")
      pcktrcivd_sophos=re.search("")
      pcktrcivd_palo=re.search("")

      os_forti=re.search("(?<=osname\W+)\w+",logs)
      os_check=re.search("")
      os_sophos=re.search("")
      os_palo=re.search("")

      app_forti=re.search("(?<=app\W+)\S+(\w+)",logs)
      app_check=re.search("(?<=application\W+)\w+.\w+",logs)
      app_sophos=re.search("")
      app_palo=re.search("")

      sentpkt_forti=re.search("(?<=sentpkt\W+)\w+",logs)
      sentpkt_check=re.search("")
      sentpkt_sophos=re.search("(?<=sent_pkts\W+)\w+",logs)
      sentpkt_palo=re.search("")

      duration_forti=re.search("(?<=duration\W+)\w+",logs) 
      duration_check=re.search("")
      duration_sophos=re.search("(?<=duration\W+)\w+")
      duration_palo=re.search("")

      proto_forti=re.search("(?<=proto\W+)\w+",logs)
      proto_check=re.search("")
      proto_sophos=re.search("(?<=protocol\W+)\w+",logs)
      proto_palo=re.search("(?<=proto\W+)\w+",logs)

      _forti=re.search
      _check=re.search
      _sophos=re.search
      _palo=re.search

      _forti=re.search
      _check=re.search
      _sophos=re.search
      _palo=re.search
