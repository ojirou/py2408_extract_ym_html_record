import pandas as pd
import subprocess
import win32com.client
import os
years=[]
months=[]
BaseFolder=r'C:\\'
OutExl=BaseFolder+r'23年まとめ_記録表.xlsx'
years = [str(23)] * 12  # '23' を12回繰り返す
months = [f'{m:02}' for m in range(1, 13)]  # 1月から12月までを2桁の文字列に変換
yms = [y + '年' + m + '月' for y, m in zip(years, months)]
for year, month in zip(years, months):
    df = pd.DataFrame(index=range(0), columns=[])
    year=str(year)
    month=f'{month:02}'
    YearMonth=year+'年'+month+'月'    
    FileName=str(year)+str(month)+r"記録表.html"
    FilePath=BaseFolder+r'記録表\\'+FileName
    dfs = pd.read_html(FilePath)
    df=dfs[0]
    df['年月']=YearMonth
    df.columns=['日付','ラン','スイム','バイク','ウォーキング','エキササイズ','累積標高','計測量','日記','年月']
    df=df[['年月','日付','ラン','スイム','バイク','ウォーキング','エキササイズ']]
    ExcelName=BaseFolder+r'記録表\\'+YearMonth+'記録表.xlsx'
    df.to_excel(ExcelName)
df2=pd.DataFrame(columns=['インデックス','年月','日付','ラン','スイム','バイク','ウォーキング','エキササイズ'])
for ym in yms:
    ExcelFile = BaseFolder + r'記録表\\' + ym + '記録表.xlsx'  # 拡張子をxlsxに変更
    df = pd.read_excel(ExcelFile, engine='openpyxl')  # pd.read_csvの代わりにpd.read_excelを使用
    df['年月'] = ym
    df2 = pd.concat([df2, df], ignore_index=True)
df2 = df2.sort_values('日付', ascending=True)
df2 = df2[['年月', '日付','ラン','スイム','バイク','ウォーキング','エキササイズ']]
df2.to_excel(OutExl, index=False)  # index=Falseでインデックスを出力しないようにする
subprocess.Popen(["start", "", OutExl], shell=True)