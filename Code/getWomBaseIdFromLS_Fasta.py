#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:51:01 2021

@author: lu
"""
import os
import csv
targetDir="/home/lu/AcrossTissue/Fastas"

outputDir=targetDir
for file in os.listdir(targetDir):
    if ".fasta" in file and ".csv" not in file:
        path=os.path.join(targetDir,file)
        f=open(path,"r")
        wormbaseIdList=[]
        lines=f.readlines()
        for line in lines:
            if ('>' in line):
                wormbaseId=line[1:].rstrip()
                wormbaseIdList.append(wormbaseId)
        outputFileName=os.path.join(outputDir,file+".wormbaseId.csv")
        print(wormbaseIdList[:5])
        with open(outputFileName,'w') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            for item in wormbaseIdList:
                wr.writerow([item,])



        