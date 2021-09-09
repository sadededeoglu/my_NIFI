from org.apache.nifi.processors.script import ExecuteScript
from org.apache.nifi.processor.io import StreamCallback
from java.nio.charset import StandardCharsets
from org.apache.commons.io import IOUtils
import re
class TransformCallback(StreamCallback):
  def __init__(self):
    pass
  def process(self, input, output):
    try:
      logs=IOUtils.toString(input, StandardCharsets.UTF_8)
      logid_forti=re.search("(?<=logid=\W+)\w+",logs)
      if logid_forti:
        logid=("LogID="+srt(logid_forti))
        time_forti=re.search("(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",logs)
        time=("Time="+str(time_forti))
         
    except:
      pass

flowFile = session.get()
if flowFile != None:
  flowFile = session.write(flowFile, TransformCallback(logid,time))
  session.transfer(flowFile, REL_SUCCESS)
