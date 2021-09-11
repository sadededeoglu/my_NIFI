from org.apache.nifi.processors.script import ExecuteScript
from org.apache.nifi.processor.io import StreamCallback
from java.nio.charset import StandardCharsets
from org.apache.commons.io import IOUtils
import re

class PyInputStreamCallback(StreamCallback):

  def __init__(self):
    pass

  def process(self, inputStream, outputStream):

    logs=IOUtils.toString(inputStream, StandardCharsets.UTF_8)

    try:
      logid_forti=re.search("(?<=logid=\W+)\w+",logs)
      if logid_forti:
        logid=("LogID="+srt(logid_forti))
        outputStream.write(IOUtils.toBytes(logid))    
    except:
      pass

flowFile = session.get()
if (flowFile != None):
  flowFile = session.write(flowFile, PyInputStreamCallback())
  session.transfer(flowFile, REL_SUCCESS)
