# encoding: utf-8
import win32ui
import re
from pyExcelerator import Workbook


# 打开文件对话框
# 读取txt数据 (数组操作/正则表达式)
# 输出xls 表格

def opendlgtxt():
    dlg = win32ui.CreateFileDialog(1)
    dlg.SetOFNInitialDir("D:\\demo")
    dlg.DoModal()
    filename = dlg.GetPathName()
    return filename


def txt2els(sourcename, destname):
    w = Workbook()
    ws = w.add_sheet("Cpp glossary")
    row = 0
    ep = re.compile(r'\s\s+')  # 用两个及以上空格分解开
    EnRow, TwRow, CnRow = [], [], []
    with open(sourcename) as txtline:
        for r in txtline:
            result = re.split(ep, r)
            EnRow.append(result[0])
            if len(result) >= 3:  # 检查是否分割正确
                TwRow.append(result[1])
                CnRow.append(result[2])
                ws.write(row, 1, TwRow[row].decode('GBK'))
                ws.write(row, 2, CnRow[row].decode('GBK'))
            else:
                TwRow.append("丢失")
                CnRow.append("丢失")
            ws.write(row, 0, EnRow[row].decode('GBK'))
            row += 1
    w.save(destname)


if __name__ == '__main__':
    txtname = opendlgtxt()
    txt2els(txtname, "D://demo//glossary.xls")
