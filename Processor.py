"""T
his program is designed to function with 'BatchProcessor.py' and requires both files to function. 

this program will take the input values chosen the user and use them to batch process raster and vector
files without having to run each file individually through the process. Information on how to use the code
can be found in the readme file.
"""

import os
import shutil
import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("3d")

TheArguments= sys.argv

if (len(TheArguments)>1):
    
#All files dumped into this folder for processing
    InputPath=str(TheArguments[1]) #linked to GUI
    
    #Processed files will either be copied if not projected 
    #New files created from projection will be output here
    OutputPath=str(TheArguments[2]) #Linked to gui
    
    FileType =str(TheArguments[3])
    
    OutProj = str(TheArguments[4])
    #All files in the input folder will be moved here after copy and process
    #to keep the input clear so no duplication happens
    OriginalsPath=str(TheArguments[2]+"/Originals/") #linked to gui
    
print(InputPath)
print(OutputPath)
print(FileType)
print(OutProj)
#Reads contents of input folder
TheList=os.listdir(InputPath)

    
    #Main batch processor
for TheFile in TheList:
    TheFileName,TheFileExtension = os.path.splitext(TheFile)
    print(TheFileExtension) #For debugging/testing
    InputFilePath=InputPath+TheFileName+TheFileExtension
    ProjFilePath=InputPath+TheFileName+".prj"
    #Sorts out if the extention file can be projected or not. 
    #Non projectable files will be copied over to the output folder.
    #this takes care of the supporting files associated with the main files
    
    if FileType == "Raster":
        
        #Check to see if file is projectable.
        if (TheFileExtension in (".tif",".dat",".bil",".bip",".bmp",".bsq",".gif",".img",".jpg","jp2",".png",".tif",".mrf",".crf")):
            sr = arcpy.Describe(InputFilePath).spatialReference
        
            print (sr.Name)#debug/test
            if OutProj == "WGS_1984_UTM_10N":
                
                if sr.Name == "WGS_1984_UTM_Zone_10N":  #OutputRaster. this will be linked to the selection in the GUI
                    print ("sweet") #debug/test
                    
                    ProjCoords = arcpy.Describe(InputFilePath).spatialReference
                
                    
                    print(ProjCoords.GCS.Name)            
                    #Copy the files to the output path then move 
                    #the originals to the original folder
                    shutil.copy(InputFilePath,OutputPath)
                    shutil.move(InputFilePath,OriginalsPath)
                else:
                    print("Not Sweet") #debug/test
                    #SendToProjector 
                    
                    ProjCoords = arcpy.Describe(InputFilePath).spatialReference
                
                    
                    print(ProjCoords.GCS.Name)
                    ProjCoordsName = ProjCoords.GCS.Name
                   
                    if ProjCoordsName == "GCS_North_American_1983": 
                        ProjectRaster = arcpy.ProjectRaster_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (32610) ,"#" ,"#" ,"NAD_1983_To_WGS_1984_5","#" , ProjCoords , "#")
                        shutil.move(InputFilePath,OriginalsPath)
                    elif ProjCoordsName == "GCS_North_American_1927":
                        ProjectRaster = arcpy.ProjectRaster_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (32610) ,"#" ,"#" ,"NAD_1927_To_WGS_1984_4","#" , ProjCoords , "#")
                        shutil.move(InputFilePath,OriginalsPath)
                    elif ProjCoordsName == "GCS_WGS_1972":
                        ProjectRaster = arcpy.ProjectRaster_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (32610) ,"#" ,"#" ,"WGS_1972_To_WGS_1984_1","#" , ProjCoords , "#")
                        shutil.move(InputFilePath,OriginalsPath)
                    else:
                        
                        print("Datum not currently supported")
                
            elif OutProj == "NAD_1983_UTM_Zone_10N":
                if sr.Name == "NAD_1983_UTM_Zone_10N":
                    print ("sweet") #debug/test
                    
                    ProjCoords = arcpy.Describe(InputFilePath).spatialReference

                    print(ProjCoords.GCS.Name)            
                    #Copy the files to the output path then move 
                    #the originals to the original folder
                    shutil.copy(InputFilePath,OutputPath)
                    shutil.move(InputFilePath,OriginalsPath)
                else:
                    print("Not Sweet") #debug/test
                     
                    #Checks geographic coordinates 
                    ProjCoords = arcpy.Describe(InputFilePath).spatialReference
                    print(ProjCoords.GCS.Name)
                    ProjCoordsName = ProjCoords.GCS.Name
                    if ProjCoordsName == "GCS_North_American_1927":
                        ProjectRaster = arcpy.ProjectRaster_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (26910) ,"#" ,"#" ,"NAD_1927_To_NAD_1983_NADCON","#" , ProjCoords , "#")
                        shutil.move(InputFilePath,OriginalsPath)
                    #elif ProjCoordsName =="GCS_ITRF_2000":
                        #ProjectRaster = arcpy.ProjectRaster_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (26910) ,"#" ,"#" ,"ITRF_2000_To_NAD_1983_2011","#" , ProjCoords , "#")
                        #shutil.move(InputFilePath,OriginalsPath)
                    else:
                        print("Datum not supported")
        else:
                #Copy over files that accompany the main files
                #Move originals to originals folder
                #shutil.copy(InputFilePath,OutputPath)
                shutil.move(InputFilePath,OriginalsPath)
                print("non raster file")#debug/test
                
    elif FileType == "Vector":
        
        if (TheFileExtension in (".shp",".cpg",".dbf",".prj",".sbn",".sbx",".shx")):
            if (TheFileExtension in (".shp")):

                           
                if OutProj == "WGS_1984_UTM_10N":
                    sr = arcpy.Describe(InputFilePath).spatialReference
                    
                    print (sr.Name)#debug/test                                     
                    if sr.Name == "WGS_1984_UTM_Zone_10N":  #OutputRaster. this will be linked to the selection in the GUI
                        print ("sweet") #debug/test
                        
                        ProjCoords = arcpy.Describe(InputFilePath).spatialReference

                        print(ProjCoords.GCS.Name)            
                        #Copy the files to the output path then move 
                        #the originals to the original folder
                        shutil.copy(InputFilePath,OutputPath)
                        shutil.move(InputFilePath,OriginalsPath)
                    else:
                        print("Not Sweet") #debug/test
                        #SendToProjector 
                        
                        ProjCoords = arcpy.Describe(InputFilePath).spatialReference
                        
                        print(ProjCoords.GCS.Name)
                        ProjCoordsName = ProjCoords.GCS.Name
                    
                        if ProjCoordsName == "GCS_North_American_1983": 
                        
                        #if statement that will decide the projection path  
                            ProjectRaster = arcpy.Project_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (32610) ,"NAD_1983_To_WGS_1984_5" ,"#" ,"#","#" , "#")
                            shutil.move(InputFilePath,OriginalsPath)
                        elif ProjCoordsName == "GCS_North_American_1927":
                            ProjectRaster = arcpy.ProjectRaster_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (32610) ,"NAD_1927_To_WGS_1984_4","#" ,"#" ,"#","#")
                            shutil.move(InputFilePath,OriginalsPath)
                        elif ProjCoordsName == "GCS_WGS_1972":
                            ProjectRaster = arcpy.ProjectRaster_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (32610) ,"WGS_1972_To_WGS_1984_1" ,"#", "#" ,"#" , "#")
                            shutil.move(InputFilePath,OriginalsPath)
                        else:
                            #end path will show error not supporting the transformation
                            print("Datum not currently supported")
                    #if sr.Name == "NAD_1983_UTM_Zone_10N":
                elif OutProj == "NAD_1983_UTM_Zone_10N":
                    sr = arcpy.Describe(InputFilePath).spatialReference
                    if sr.Name == "NAD_1983_UTM_Zone_10N":
                        print ("sweet") #debug/test
                        
                        ProjCoords = arcpy.Describe(InputFilePath).spatialReference
                    
                        print(ProjCoords.GCS.Name)            
                        #Copy the files to the output path then move 
                        #the originals to the original folder
                        shutil.copy(InputFilePath,OutputPath)
                        shutil.move(InputFilePath,OriginalsPath)
                    else:
                        print("Not Sweet") #debug/test
                        #SendToProjector 
                        
                        ProjCoords = arcpy.Describe(InputFilePath).spatialReference
                    
                        print(ProjCoords.GCS.Name)
                        ProjCoordsName = ProjCoords.GCS.Name
                        if ProjCoordsName == "GCS_North_American_1927":
                            ProjectRaster = arcpy.ProjectRaster_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (26910) ,"NAD_1927_To_NAD_1983_NADCON" ,"#" ,"#","#" , "#")
                            shutil.move(InputFilePath,OriginalsPath)
                        elif ProjCoordsName =="GCS_WGS_1984":
                            ProjectRaster = arcpy.ProjectRaster_management(InputFilePath, OutputPath+TheFileName+"_Reprojected"+TheFileExtension, (26910) ,"#" ,"#" ,"NAD_1983_To_WGS_1984_5","#" , ProjCoords , "#")
                            shutil.move(InputFilePath,OriginalsPath)
                        else:
                            print("Datum not supported")
            else:
                #Copy files from input to originals. these will be deleted when the subprocess is complete
                shutil.copy(InputFilePath,OriginalsPath)
        else:
                
                
                print("non Vector file")#debug/test
    else:
        print("no files can be processed")
        