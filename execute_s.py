from org.apache.nifi.processors.script import ExecuteScript #processor importu
from org.apache.nifi.processor.io import StreamCallback # ne zman çagıracağim belli olmayan fonk
from java.nio.charset import StandardCharsets #Dönüşüm Formatı
from org.apache.commons.io import IOUtils #yönlendirme
import re #regex

class inputSC(StreamCallback): #fonksiyonlarımı buranın içinde kullanacağim

  def __init__(self):
    def flow(self, input, output):

      logs=IOUtils.toString(input, StandardCharsets.UTF_8): #loglarımı alıyorum. değişik karakterliler sorun cıkarmasın diey utf ekliyorum
      #firewall
      logid_forti=re.search("(?<=logid=\W+)\w+",logs)
      if logid_forti:
        logid=("LogID="+str(logid_forti))
        time_forti=re.search("(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",logs)
        date_forti=re.search("\d{4}-\d+-\d+",logs)
        srcip_forti=re.search("(?<=srcip=)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)
        type_forti=re.search("(?<=type=\W+)\w+",logs)
        type_sophos=re.search("(?<=log_type=\W+)\w+",logs)
        subtype_forti=re.search("(?<=subtype=\W+)\w+",logs)
        level_forti=re.search("(?<=level=\W+)\w+",logs)
        srcport_forti=re.search("(?<=srcport=)\w+",logs)
        src_interface_forti=re.search("(?<=srcintfrole=\W+)\w+",logs)
        dstip_forti=re.search("(?<=dstip\W+)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)
        dstport_forti=re.search("(?<=dstport=)\w+",logs)
        fpolicy_forti=re.search("(?<=action=\W+)\w+",logs)
        NatSrcIp_forti=re.search("(?<=transip=)(?:[0-9]{1,3}\.){3}[0-9]{1,3}"logs)  
        sentbyte_forti=re.search("(?<=sentbyte=)\w+",logs)
        pcktrcivd_forti=re.search("(?<=rcvdpkt=)\w+",logs)
        os_forti=re.search("(?<=osname\W+)\w+",logs)
        app_forti=re.search("(?<=app\W+)\S+(\w+)",logs)
        sentpkt_forti=re.search("(?<=sentpkt\W+)\w+",logs)
        duration_forti=re.search("(?<=duration\W+)\w+",logs)
        proto_forti=re.search("(?<=proto\W+)\w+",logs)
        break
        
      logid_sophos=re.search("(?<=log_id=)\w+",logs)
      if logid_sophos:
        time_sophos=re.search("(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",logs)
        date_sophos=re.search("\d{4}-\d+-\d+",logs)
        srcip_sophos=re.search("(?<=src_ip=)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)
        type_sophos=re.search("(?<=log_type=\W+)\w+",logs)
        subtype_sophos=re.search("(?<=log_subtype=\W+)\w+",logs)
        level_sophos=re.search("")
        srcport_sophos=re.search("(?<=src_port=)\w+",logs)
        src_interface_sophos=re.search("(?<=in_interface\W+)\w+\W+\w+")
        dstip_sophos=re.search("(?<=dst_ip\W+)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)
        dstport_sophos=re.search("(?<=dst_port=)\w+",logs)
        fpolicy_sophos=re.search("")
        NatSrcIp_sophos=re.search("")
        sentbyte_sophos=re.search("(?<=sent_bytes=)\w+",logs)
        pcktrcivd_sophos=re.search("")
        os_sophos=re.search("")
        app_sophos=re.search("")
        sentpkt_sophos=re.search("(?<=sent_pkts\W+)\w+",logs)
        duration_sophos=re.search("(?<=duration\W+)\w+")
        proto_sophos=re.search("(?<=protocol\W+)\w+",logs)
        break

      logid_palo=re.search("(?<=SerialNumber=)\w+",logs)
      if logid_palo:
        time_sophos=re.search("(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",logs)
        date_palo=re.search("\d{4}/\d{2}/\d{2}",logs)
        srcip_palo=re.search("(?<=src=)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)  
        type_palo=re.search("")   
        subtype_palo=re.search("(?<=Subtype=)\w+",logs)
        level_palo=re.search("")
        srcport_palo=re.search("(?<=srcPort=)\w+",logs)
        src_interface_palo=re.search("")
        dstip_palo=re.search("(?<=dst\W+)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)
        dstport_palo=re.search("(?<=dstPort=)\w+",logs)
        fpolicy_palo=re.search("(?<=action=)\w+",logs)
        NatSrcIp_palo=re.search("(?<=srcPostNATPort=)\w+",logs)
        sentbyte_palo=re.search("")
        pcktrcivd_palo=re.search("")
        os_palo=re.search("")
        app_palo=re.search("")
        sentpkt_palo=re.search("")
        duration_palo=re.search("")
        proto_palo=re.search("(?<=proto\W+)\w+",logs)
        break

      _forti=re.search
      _sophos=re.search
      _palo=re.search

      _forti=re.search
      _sophos=re.search
      _palo=re.search

       """*********************************************************************************************************************************"""

      channel_win=re.search("(?<=Channel>)\w+",logs)
      time_win=re.search("(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",logs)
      date_win=re.search("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))",logs)
      guid_win=re.search("(?<=Guid\W+)\w+.\w+.\w+.\w+.\w+",logs)
      eventRecordID_win=re.search("(?<=EventRecordID\W)\w+",logs)
      level_win=re.search("(?<=Level\W)\w+",logs)
      task_win=re.search("(?<=task\W)\w+",logs)
      opcode_win=re.search("(?<=Opcode\W)\w+",logs)
      Keywords_win=re.search("(?<=Keywords\W)\w+",logs)
      ProcessID_win=re.search("(?<=ProcessID\W)\w+",logs)
      Computer ???
      


       """*********************************************************************************************************************************"""
      type_centos=re.search("(?<=type\W)\w+",logs)
      arch_centos=re.search("(?<=arch\W)\w+",logs)
      syscall_centos=re.search("(?<=syscall\W)\w+",logs)
      succsess_centos=re.search("(?<=success\W)\w+",logs)
      exit_centos=re.search("(?<=exit\W)\w+",logs)
      a0_centos=re.search("(?<=a0\W+)\w+",logs)
      a1_centos=re.search("(?<=a1\W+)\w+",logs)
      a2_centos=re.search("(?<=a2\W+)\w+",logs)
      a3_centos=re.search("(?<=a3\W+)\w+",logs)
      items_centos=re.search("(?<=items\W+)\w+",logs)
      ppid_centos=re.search("(?<=ppid\W+)\w+",logs) 
      pid_centos=re.search("(?<=pid\W+)\w+",logs)
      auid_centos=re.search("(?<=auid\W+)\w+",logs)
      uid_centos=re.search("(?<=uid\W+)\w+",logs)
      gid_centos=re.search("(?<=gid\W+)\w+",logs)
      euid_centos=re.search("(?<=euid\W+)\w+",logs)
      suid_centos=re.search("(?<=suid\W+)\w+",logs)
      fsuid_centos=re.search("(?<=fsuid\W+)\w+",logs)
      egid_centos=re.search("(?<=egid\W+)\w+",logs)
      sgid_centos=re.search("(?<=sgid\W+)\w+",logs)
      fsgid_centos=re.search("(?<=fsgid\W+)\w+",logs)
      tty_centos=re.search("(?<=tty\W+)\w+",logs)
      ses_centos=re.search("(?<=ses\W+)\w+",logs)
      comm_centos=re.search("(?<=comm\W+)\w+",logs)
      exe_centos=re.search("(?<=exe\W+)\S+")
      _centos=re.search("(?<=subj\W+)\S+")
      _centos=re.search("(?<=key\W+)\w+")


 """*********************************************************************************************************************************"""

      time_mssql=re.search("(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",logs)
      date_mssql=re.search("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))",logs)
      client_ip_mssql=re.search("(?<=client_ip\W+)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)
      _mssql=re.search
      _mssql=re.search
      _mssql=re.search
      _mssql=re.search
      _mssql=re.search

      time_mysql=re.search("(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",logs)
      date_mysql=re.search("(?<=TIMESTAMP\W+)([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))",logs)
      client_ip_mysql=re.search("(?<=IP\W+)(?:[0-9]{1,3}\.){3}[0-9]{1,3}",logs)
      _mysql=re.search
      _mysql=re.search
      _mysql=re.search
      _mysql=re.search

      time_postgresql=re.search
      date_postgresql=re.search
      client_ip_postgresql=re.search
      _postgresql=re.search
      _postgresql=re.search
      _postgresql=re.search
      _postgresql=re.search

      time_elastıcsql=re.search
      date_elastıcsql=re.search
      client_ip_elastıcsql=re.search
      _elastıcsql=re.search
      _elastıcsql=re.search
      _elastıcsql=re.search
      _elastıcsql=re.search
      _elastıcsql=re.search


