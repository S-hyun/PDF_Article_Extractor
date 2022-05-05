import tabula # Read pdf into list of DataFrame 
import sys
import pandas as pd

def table(args):
  try:
    f_ = open(args.file, 'rb')
    print('23')
    f_.close()
  except:
    print(f'can\'t open file \'{args.file}\'.')
    return
  df = tabula.read_pdf(args.file, pages='all') #Read remote pdf into list of DataFrame
  writer=pd.ExcelWriter(args.file.replace('pdf', 'xlsx'), engine='openpyxl') # Generate xlsx file

  table_num = 0
  for i in range(len(df)):
    if len(df[i]) > 2 and len(df[i].columns) > 3:
      table_num = table_num + 1
      #After specifying the sheet name in the generated file, put the saved result value in the dataframe
      df[i].to_excel(writer, sheet_name='table'+str(table_num))

  # save the xlsx file
  writer.save()
