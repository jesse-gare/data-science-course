from win32com import client

excel = client.Dispatch("Excel.Application")
workbook = excel.Workbooks.Add()
worksheet = excel.Worksheets.Add()
worksheet.Cells(1,1).Value = "Hello from Python!"
excel.visible = True
