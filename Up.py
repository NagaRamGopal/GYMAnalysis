import pandas as pd
import numpy as np
import pandas_profiling 
from pandas_profiling import ProfileReport

class Up:

    df=pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\GYMAnalysis\gym_members_exercise_tracking.csv')

    @staticmethod
    def ProfileReport():
        rpt=ProfileReport(Up.df,title="Data Report before EDA/changes")
        rpt.to_file("BriefView.html")

    @staticmethod
    def ColumnsCheck():
        print(Up.df.dtypes)
        print(Up.df.describe())
    
    
    @staticmethod
    def Grouping():
        labels = ['Young', 'Adult', 'Senior', 'Old']
        bins = [18, 26, 45, 55, 100] #18-25 young, 26-45 adult, 46-55 senior, 56-100 old
        Up.df['Category'] = pd.cut(Up.df['Age'], bins=bins, labels=labels, right=True) 
        print(Up.df.head())
    
    @staticmethod
    def run_all():
        Up.ProfileReport()
        Up.ColumnsCheck()
        Up.Grouping()

o1=Up()
o1.run_all()