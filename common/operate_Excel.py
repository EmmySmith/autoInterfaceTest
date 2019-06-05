#coding=utf-8
import xlrd

class readExcel(object):
     def __init__(self, path,index):
         self.path = path
         self.index = index

     def getSheet(self):
         # 获取索引
         xl = xlrd.open_workbook(self.path)
         sheet = xl.sheet_by_index(self.index)
         # counts = len(xl.sheets())
         # print(counts)
         return sheet

     def getRows(self):
         # 获取行数
         row = self.getSheet().nrows
         return row

     def getCol(self):
         # 获取列数
         col = self.getSheet().ncols
         return col

     # 以下是分别获取每一列的数值
     def getName(self):
         TestName = []
         for i in range(1, self.getRows()):
             TestName.append(self.getSheet().cell_value(i, 0))
         return TestName

     def getData(self):
         TestData = []
         for i in range(1, self.getRows()):
             TestData.append(self.getSheet().cell_value(i, 1))
         return TestData

     def getUrl(self):
         TestUrl = []
         for i in range(1, self.getRows()):
             TestUrl.append(self.getSheet().cell_value(i, 2))
         return TestUrl

     def getMethod(self):
         TestMethod = []
         for i in range(1, self.getRows()):
             TestMethod.append(self.getSheet().cell_value(i, 3))
         return TestMethod

     # def getUid(self):
     #     TestUid = []
     #     for i in range(1, self.getRows()):
     #         TestUid.append(self.getSheet().cell_value(i, 4))
     #     return TestUid

     def getCode(self):
         TestCode = []
         for i in range(1, self.getRows()):
             TestCode.append(self.getSheet().cell_value(i, 4))
         return TestCode


# readExcel(r'D:\automation_testcase\case_test.xlsx',2).getSheet()