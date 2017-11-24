#coding:utf-8
__version__ = '0.3'
import subprocess, re, os

class BarCodeReader():
  location = ""
  command = "java"
  libs = ["javase.jar", "core.jar","jcommander-1.48.jar"]
  args = ["-cp", "LIBS", "com.google.zxing.client.j2se.CommandLineRunner"]

  def __init__(self, loc=""):
    if not len(loc):
      if (os.environ.has_key("ZXING_LIBRARY")):
        loc = os.environ["ZXING_LIBRARY"]
      else:
        loc = ".."
        # loc="file:///H:/flask-list/flask-QRcode-master/zxing/"
        # loc = "http://127.0.0.1:8000/"

    self.location = loc

  def decode(self, files, try_harder = False, qr_only = False):
    cmd = [self.command]
    cmd += self.args[:] #copy arg values
    if try_harder:
      cmd.append("--try_harder")
    if qr_only:
      cmd.append("--possibleFormats=QR_CODE")

    libraries = [l for l in self.libs]
    print(libraries)
    cmd = [ c if c != "LIBS" else os.pathsep.join(libraries) for c in cmd ]

    # send one file, or multiple files in a list
    SINGLE_FILE = False
    if type(files) != type(list()):
      cmd.append(files)
      SINGLE_FILE = True
    else:
      cmd += files

    (stdout, stderr) = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True).communicate()
    codes = []
    file_results = stdout.split("\nfile:")


    for result in file_results:

      print(result)
      lines = stdout.split("\n")
      if re.search("No barcode found", lines[0]):
        codes.append(None)
        continue

      codes.append(BarCode(result))

    if SINGLE_FILE:

      return codes[0]
    else:

      return codes

#this is the barcode class which has
class BarCode:
  format = ""
  points = []
  data = ""
  raw = ""

  def __init__(self, zxing_output):
    lines = zxing_output.split("\n")
    raw_block = False
    parsed_block = False
    point_block = False

    self.points = []
    for l in lines:
      m = re.search("format:\s([^,]+)", l)
      if not raw_block and not parsed_block and not point_block and m:
        self.format = m.group(1)
        continue

      if not raw_block and not parsed_block and not point_block and l == "Raw result:":
        raw_block = True
        continue

      if raw_block and l != "Parsed result:":
        self.raw += l + "\n"
        continue

      if raw_block and l == "Parsed result:":
        raw_block = False
        parsed_block = True
        continue

      if parsed_block and not re.match("Found\s\d\sresult\spoints", l):
        self.data += l + "\n"
        continue

      if parsed_block and re.match("Found\s\d\sresult\spoints", l):
        parsed_block = False
        point_block = True
        continue

      if point_block:
        m = re.search("Point\s(\d+):\s\(([\d\.]+),([\d\.]+)\)", l)
        if (m):
          self.points.append((float(m.group(2)), float(m.group(3))))

    return


