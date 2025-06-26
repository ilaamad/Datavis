import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dotDataFrame = pd.read_excel("IpFiles/DotInput.xlsx")
lineDataFrame = pd.read_excel("IpFiles/LineInput.xlsx")
dotLineDataFrame = pd.read_excel("IpFiles/DotLineInput.xlsx")
barDataFrame = pd.read_excel("IpFiles/BarInput.xlsx")
def showDotData(dotDataFrame):
    print("before duplicates - Dot Data: ", dotDataFrame)
    df = dotDataFrame.drop_duplicates()
    print("After duplicates  - Dot Data: ", df)
    sns.scatterplot(x='Name', y='Age', data=df)
    plt.show()

def showLineData(lineDataFrame):
    print("before duplicates - Line Data: ", lineDataFrame)
    df = lineDataFrame.drop_duplicates()
    print("After duplicates  - Line Data: ", df)
    sns.lineplot(x='Name', y='Age', data=df)
    plt.show()

def showDotLineData(dotLineDataFrame):
    print("before duplicates - DotLine Data: ", dotLineDataFrame)
    df = dotLineDataFrame.drop_duplicates()
    print("After duplicates  - DotLine Data: ", df)
    sns.pointplot(x='Name', y='Age', data=df)
    plt.show()
def showBarData(barDataFrame):
    print("before duplicates - Bar Data: ", barDataFrame)
    df = barDataFrame.drop_duplicates()
    print("After duplicates  - Bar Data: ", df)
    sns.barplot(x='Name', y='Age', data=df)
    plt.show()

showDotData(dotDataFrame)
showLineData(lineDataFrame)
showDotLineData(dotLineDataFrame)
showBarData(barDataFrame)










































































