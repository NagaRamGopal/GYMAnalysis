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
    def run_all():
        Up.ProfileReport()

o1=Up()
o1.run_all()