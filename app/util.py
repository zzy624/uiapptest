# -*-coding:utf-8-*-
import xlrd
import os,platform
import json
from xlutils.copy import copy

file_path = os.path.dirname(__file__).split('/app')[0] + '/data/xls/testcase.xls'

FUNC_TEMPLATE = '''@unittest.skipUnless({state},'state值为0,跳过测试')\ndef {func}(self):
        '{casename}'
        Testcase(self.dr,{onecase},'{sheetname}').execute_case()
        '''

def getXlsTestCase(sheet_name):
    """
    :param sheet_name:
    :return: 测试用例集
    """
    # 获取xls sheet页
    conn = xlrd.open_workbook(file_path, formatting_info=False)
    table = conn.sheet_by_name(sheet_name)
    nRows = table.nrows  # 获取行数
    nCols = table.ncols  # 获取列数
    # 定义测试用例集列表
    testCasesList = []
    try:
        for row in range(nRows):
            # 定义单个测试用例字典
            testCaseDict = {}
            if row:  # 首行标题不添加字典中
                for col in range(nCols):
                    testCaseDict[table.cell(0, col).value] = table.cell(row, col).value
                testCasesList.append(testCaseDict)
        print('获取测试用例')
        return testCasesList
    except:
        print('未获取测试用例')
        raise IOError('测试用例获取失败')


def setResults(sheet_name, case_id, col, value):
    # 获取sheet_index
    sheet_index = getXlsSheetIndex(sheet_name)
    # 获取results单元格坐标
    cell = getCell(sheet_name, case_id)
    row = ''
    if col == 'results':
        row = cell['row']
        col = cell['col']
    if col == 'actual':
        row = cell['row']
        col = int(cell['col']) - 1
    if setTestCaseForXls(sheet_index, row, col, value):
        print('{0} 测试结果写入表格成功!'.format(value))
        return True
    print('测试结果写入失败!')
    return False


def getXlsSheetIndex(sheet_name):
    conn = xlrd.open_workbook(file_path, formatting_info=False)
    sheets = conn.sheet_names()
    for index, item in enumerate(sheets):
        if item == sheet_name:
            return index


def getCell(sheet_name, case_id):
    """
    table = self.__xlsConn().sheet_by_name(sheet_name)
    nRows = table.nrows  # 获取行数
    nCols = table.ncols  # 获取列数
    table.row_values(index) # 获取整行（数组）
    table.col_values(index)  # 整列的值（数组）
    :param sheet_name:
    :param case_id:
    :return: 获取excel表格中单元格坐标,返回字典坐标
    """
    cell_dict = {}
    conn = xlrd.open_workbook(file_path, formatting_info=False)
    table = conn.sheet_by_name(sheet_name)
    for index, item in enumerate(table.col_values(0)):
        if item == case_id:
            cell_dict['row'] = index
            break
    for index, item in enumerate(table.row_values(0)):
        if item == 'results':
            cell_dict['col'] = index
            break
    return cell_dict

def setXlsTestCase(sheet_index, row, col, value):
    try:
        rb = xlrd.open_workbook(file_path)
        # 通过sheet_by_index()获取的sheet没有write()方法
        # rs = rb.sheet_by_name(sheet_index)
        wb = copy(rb)
        # 通过get_sheet()获取的sheet有write()方法
        ws = wb.get_sheet(sheet_index)
        ws.write(row, col, value)
        wb.save(file_path)
        return True
    except Exception as e:
        print (e)
        return False

# 不更改原有样式
def setTestCaseForXls(sheet_index, row, col, value):
    # if "Windows" in platform.platform():
    #     file_path = file_path.replace('/', '\\')
    open_xls = xlrd.open_workbook(file_path, formatting_info=True)  # 打开xls文件
    outwb = copy(open_xls)
    outSheet = outwb.get_sheet(sheet_index)
    try:
        """ Change cell value without changing formatting. """

        def _getOutCell(outSheet, colIndex, rowIndex):
            """ HACK: Extract the internal xlwt cell representation. """
            row = outSheet._Worksheet__rows.get(rowIndex)
            if not row:
                return None
            cell = row._Row__cells.get(colIndex)
            return cell

        # HACK to retain cell style.
        previousCell = _getOutCell(outSheet, col, row)
        # END HACK, PART I
        outSheet.write(row, col, value)
        # HACK, PART II
        if previousCell:
            newCell = _getOutCell(outSheet, col, row)
            if newCell:
                newCell.xf_idx = previousCell.xf_idx
        # END HACK
        outwb.save(file_path)
        return True
    except Exception as e:
        print (e)
        return False




if __name__ == '__main__':
    data = getXlsTestCase('login_test')
    # print(data)
    for i in data:
        # print i['actual']
        print(json.dumps(i, encoding='UTF-8', ensure_ascii=False))

    setResults('login_test','test1_Login_01','results','Nss')