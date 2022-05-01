import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from fnmatch import fnmatch
import numpy as np
import csv
from utils.type import Investor, Rate, Index

class GetData:
    # Construct
    def __init__(self, fname):
        # Const member variables
        self.result_ = []
        self.data_ = []
        self.date_index_ = 0
        self.header_ = 0
        self.start_ = 1
        self.size_ = 0
        with open(fname, 'r', encoding = 'UTF-8') as f:
            rows_ = csv.reader(f)
            for row in rows_:
                self.size_ += 1
                self.data_.append(row)
        print(self.size_)
    
    # Member Functions
    def FindObjectIndex(self, header, object):
        for i in range(len(header)):
            if header[i] == object:
                return i
        
        return -1

    def GetInvestor(self, institute):
        try:
            object_index_ = self.FindObjectIndex(self.data_[self.header_], institute)
        except:
            print("data_error!")

        for i in range(self.start_, self.size_):
            res = Investor(institute, self.data_[i][self.date_index_], self.data_[i][object_index_])
            self.result_.append(res)
        
        return self.result_

    def GetInvestorByTime(self, institute, time_from, time_to):
       
        try:
            object_index_ = self.FindObjectIndex(self.data_[self.header_], institute)
        except:
            print("data_error!")

        for i in range(self.start_, self.size_):
            if time_from <= self.data_[i][self.date_index_] <= time_to:
                res = Investor(institute, self.data_[i][self.date_index_], self.data_[i][object_index_])
                self.result_.append(res)
        
        return self.result_


    def GetRate(self, name):
        try:
            object_index_ = self.FindObjectIndex(self.data_[self.header_], name)
        except:
            print("data_error!")

        for i in range(self.start_, self.size_):
            res = Rate(name, self.data_[i][self.date_index_], self.data_[i][object_index_])
            self.result_.append(res)
        
        return self.result_

    def GetRateByTime(self, name, time_from, time_to):
        try:
            object_index_ = self.FindObjectIndex(self.data_[self.header_], name)
        except:
            print("data_error!")

        for i in range(self.start_, self.size_):
            if time_from <= self.data_[i][self.date_index_] <= time_to:
                res = Rate(name, self.data_[i][self.date_index_], self.data_[i][object_index_])
                self.result_.append(res)
        
        return self.result_

    def GetIndex(self, name):
        try:
            object_index_ = self.FindObjectIndex(self.data_[self.header_], name)
        except:
            print("data_error!")

        for i in range(self.start_, self.size_):
            res = Index(name, self.data_[i][self.date_index_], self.data_[i][object_index_])
            self.result_.append(res)
        
        return self.result_
    
    def GetIndexByTime(self, name, time_from, time_to):
        try:
            object_index_ = self.FindObjectIndex(self.data_[self.header_], name)
        except:
            print("data_error!")

        for i in range(self.start_, self.size_):
            if time_from <= self.data_[i][self.date_index_] <= time_to:
                res = Index(name, self.data_[i][self.date_index_], self.data_[i][object_index_])
                self.result_.append(res)
        
        return self.result_
