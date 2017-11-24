#coding:utf-8
from main import *

zxing_location = ".."
# testimage = "sample.png"



class Action():
  def __init__(self,path):
    self.path = path
  def test_barcode_parser(self):
    text = """
  file:/home/oostendo/Pictures/datamatrix/4-contrastcrop.bmp (format: DATA_MATRIX, type: TEXT):
  Raw result:
  36MVENBAEEAS04403EB0284ZB
  Parsed result:
  36MVENBAEEAS04403EB0284ZB
  Also, there were 4 result points.
    Point 0: (24.0,18.0)
    Point 1: (21.0,196.0)
    Point 2: (201.0,198.0)
    Point 3: (205.23952,21.0)
  """

    barcode = BarCode(text)
    if (barcode.format != "DATA_MATRIX"):
      return 0

    if (barcode.raw != "36MVENBAEEAS04403EB0284ZB"):
      return 0

    if (barcode.data != "36MVENBAEEAS04403EB0284ZB"):
      return 0

    if (len(barcode.points) != 4 and barcode.points[0][0] != 24.0):
      return 0

    return 1


  def test_codereader(self):
    #~ zx = BarCodeReader(zxing_location)
    print("方法调用成功")
    zx = BarCodeReader()
    print("__init__zx实例化成功")

    barcode = zx.decode(self.path)
    print("解析返回成功")
    if hasattr(barcode,"data"):

      return str(barcode.data).replace("\n","")
    print("图片不能识别")
    return "error"



