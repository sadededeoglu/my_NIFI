from org.apache.nifi.processors.script import ExecuteScript
from org.apache.nifi.processor.io import StreamCallback
from java.nio.charset import StandardCharsets
from org.apache.commons.io import IOUtils
import re
class TransformCallback(StreamCallback):
  def __init__(self):
    pass
  def process(self, inputStream, outputStream):
    try:
      logs=IOUtils.toString(inputStream, StandardCharsets.UTF_8)
      logid_forti=re.search("(?<=logid=\W+)\w+",logs)
      if logid_forti:
        logid=("LogID="+srt(logid_forti))
        outputStream.write(logid)    
    except:
      pass

flowFile = session.get()
if flowFile != None:
  flowFile = session.write(flowFile, TransformCallback())
  session.transfer(flowFile, REL_SUCCESS)
