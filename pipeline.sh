#start with the input file, raw reads from E-MTAB-2812-atlasExperimentSummary.Rdata

Rscript  ./RExperiment/ProcessReads.R

#Output collasedReplicate.csv and worm_collasedReplicate.csv to the "RExperiement "dir
#These are Deg-Seq2 Processed Reads mapped with gene id or wormbase id respectively.
#From there we extract the 5LS that we are insterested in (this part hasnt been scripted yet) and put it in the "csvs" folder
#For the current scope, the life stage reads we are interested in are in the "5LS_L2L3Combined.csv"

#From this file, we run LifeStageSpecific.py from the "Code" directory on it to find the genes we consider life stage specifif, see notes for details.


# home/lu/AcrossTissue/csvs/LifeStageGenes_collapse.csv




