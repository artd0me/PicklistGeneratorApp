---
output:
  html_document: default
  pdf_document: default
---

# PicklistGeneratorApp

This app was designed to create picklists compatible with the Echo Liquid handling systems.\
The current purpose is to shoot fluorescent antibody panels to stain cells for flow cytometry.\
Using this app reduces the time for preparing the picklist while including controls such as FMOs, isotype controls and single stains for compensation.

## Getting started

## Download the app

To download the app, click on the green "<> Code" button and choose "Download ZIP".
Save the whole folder in a directory of your choice.

IF YOU ARE WORKING ON MAC:

Open the "RunAppMac.sh" file in an editor (e.g. TextEdit) and replace the pathname with the new path in which you saved the "gui.py" file, e.g:

```{bash}
python /your/path/to/gui.py
```


### Installation of Python on Windows

To use this app, install Python on your computer: download it and execute the downloaded file.\
Under Advanced options during the installation setup, tick the field "Add Python to environment variables".\
To verify that Python is working, use the Windows Command Prompt:\
1. Press Windows key + R.\
2. Type "cmd" and press enter.

Once you are in the Command Prompt, type

```{bash}
python --version
```

If the output does not show the current Python version and you're encountering the "python is not recognized as an internal or external command" error in the Windows Command Prompt, it usually means that the Python executable is not properly added to your system's PATH environment variable during the installation. Here's how you can fix this issue:

1.  Check Python Installation Path: Verify the path where Python is installed on your system.\
2.  Add Python to PATH: You need to add the Python installation directory to your system's PATH variable. Follow these steps:\
3.  Right-click on the "This PC" or "My Computer" icon on your desktop or in the File Explorer and select "Properties." Click on "Advanced system settings" (you might need administrator privileges).\
4.  In the System Properties window, click the "Environment Variables" button. In the Environment Variables window, under the "System variables" section, find and select the "Path" variable, then click the "Edit" button.\
5.  Click the "New" button and add the path to your Python installation directory.\
6.  Click "OK" to close all the windows.\
7.  Restart Command Prompt: After modifying the PATH environment variable, close any open Command Prompt windows and reopen a new one. Try running

```{bash}
python --version
```

again to see if the issue is resolved.\

8.  Restart Your Computer: If the issue persists, try restarting your computer after modifying the PATH variable to ensure the changes take effect.

After completing these steps, the "python is not recognized" error should be resolved, and you should be able to run Python commands from the Command Prompt without any issues. If you continue to experience problems, double-check that you followed the steps correctly and consider reinstalling Python, making sure to select the option to add Python to the PATH during installation.

### Installation of pandas

In the Command Prompt, run

```{bash}
pip install pandas
```

to install the pandas package needed for the execution of the App.

After the installation is complete, you can verify that Pandas is installed by opening a Python interactive shell. Type

```{bash}
python
```

in the Command Prompt and press Enter to open the Python shell, then type the following:

```{python}
import pandas as pd
print(pd.__version__)
```

This should display the version number of the Pandas library that was installed.

### Preparation of the input files

#### The Panel library / Reference file
The panel library file serves as a reference that contains the layout of the source plate and defines the design of each panel and it's modifications.
In the example file "ExamplePanelLibrary.csv", we have 9 different columns defining the panel:  

+ Panel: the name of the panel, e.g. TCellpanel, Panel1 etc.  
+ Marker: Which molecule does this antibody bind to?  
+ Color: What fluorophor is the antibody conjugated to?  
+ Modification: is the panel complete with all antibodies, or is it an FMO panel (FMOCD3 doesn't include CD3), only a single stain or IgG control?  
+ Panel_Modification: merge between Panel and Modification, works as the "key" word to connect to the destination plate layout (AnnotationFile). DO NOT CHANGE THE NAME OF THIS COLUMN!   
+ Source Well: In which well of the source plate is the antibody?  DO NOT CHANGE THE NAME OF THIS COLUMN!   
+ nl_per_20: how much nl of the antibody do you need to transfer per 20 µl cell suspension. DO NOT CHANGE THE NAME OF THIS COLUMN!    
+ Source Plate Barcode: the name of your source plate! Use the same name, if you use only one source plate! If you have the antibodies distributed to several source plates, give them different names! DO NOT CHANGE THE NAME OF THIS COLUMN!   

!! Make sure that the .csv-file uses commas to separate columns " , " !!  

This file serves as a masterfile, that you can continuously update with new panels or if your source plate layout changes!


#### The Destination plate / Annotation file
The annotation file serves as the layout of your destination plate, where you define which panels go into which well.  
In the example file "ExampleDestinationPlateAnnotation.csv", we have 5 different columns:

+ Destination Plate Barcode: the name of your destination plate! Use the same name, if you only have one destination plate. If you have several destination plates to dispense to, give them different names (only if different layouts are needed. If you do replicas, you can reuse the same annotation file) DO NOT CHANGE THE NAME OF THIS COLUMN!   
+ Destination Well: Well, to which the antibodies are transferred to. DO NOT CHANGE THE NAME OF THIS COLUMN!   
+ Panel_Modification: Describes with which panel and modicifation you want to stain this well. Needs to be the exact value as in the panel library, as it works as the "key" word to connect to the source plate layput (panel library). DO NOT CHANGE THE NAME OF THIS COLUMN!  
+ cell_volume: How big is your suspension volume (in µl)? Needed for calculating the final transfer volume! DO NOT CHANGE THE NAME OF THIS COLUMN!   
+ sampledescription: your description to identify/annotate the samples!  

!! Make sure that the .csv-file uses commas to separate columns " , " !!  


### Running the app
#### Starting it up on Windows
Double click the file "RunAppWindows.py"

#### Generate picklists

Once the window opens, you can browse your annotation and library file, select a folder to save your picklist, and paste the name of the experiment!

Click "Generate Picklist".

The picklist should be saved in the folder you selected and you can close the window again!

### The picklist

The picklist name has the following structure:

DATE_Picklist_ExperimentName

+ DATE: the date when you generated the picklist in a YYYYMMDD format   
+ ExperimentName: The name you have given it in the last step while running the app!

The picklist contains the following columns:

+ Source Plate Barcode: see previously   
+ Source Well: See previously   
+ Destination Plate Barcode: see previously   
+ Destination Well: see previously    
+ Transfer Volume: the final volume the Echo will be shooting from source to destination well!    

The picklist can be loaded into the Echo system, without any further unticking or ticking of any boxes!




