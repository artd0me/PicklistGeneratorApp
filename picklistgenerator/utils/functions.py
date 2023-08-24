"""
A module for generating and exporting Echo compatible picklists.
"""

# import packages
import pandas as pd
import platform
from datetime import datetime

class Picklist:
    def __init__(self, annotationpath, panelpath):
        self.annotation = pd.read_csv(annotationpath)
        self.panel = pd.read_csv(panelpath)

    def generate_picklist(self):
        """Merges annotation and panel file and returns a data frame containing only the columns relevant for the Echo dispenser.
    
        Args: 
        annotation(pd.DataFrame): dataframe containing the annotation of the destination plate
        panel(pd.DataFrame): dataframe containing the panel library and source plate layout
    
        Returns: 
        pd.DataFrame containing only relevant columns for an Echo picklist
        """
        dfMerged = pd.merge(self.annotation, self.panel, on = 'Panel_Modification')
        dfMerged['Transfer Volume'] = dfMerged.nl_per_20 * dfMerged.cell_volume / 20
        dfPicklist = dfMerged[['Source Plate Barcode','Source Well', 'Destination Plate Barcode','Destination Well', 'Transfer Volume']]
        self.picklist = dfPicklist

    def export_picklist(self, path, name):
        """Exports the picklist as a .csv file to the chosen path and gives chosen name.
    
        Args: 
        picklist(pd.DataFrame): dataframe containing the picklist, return value of generate_picklist
        path(str): string containing the path where the picklist will be saved as a csv 
        name(str): string containing the name used in the export name of the csv.file
        """

        fileName = str(datetime.today().date()).replace('-','') + "_Picklist_" + name + ".csv"

        if platform.system() == "Darwin":  # macOS
            separator = "/"
        elif platform.system() == "Windows":
            separator = "\\"
        else:
            separator = "/"  # Default to "/" for other operating systems

        self.exportName = path + separator + fileName
        self.picklist.to_csv(self.exportName, sep = ",", index = False)

        



def import_file(filepath):
    """
    Imports the selected .csv files and returns as pd.DataFrame.

    Args:
        filepath(str): path to .csv file
    """

    file = pd.read_csv(filepath)
    return file

def generate_picklist(annotation, panel):
    """Merges annotation and panel file and returns a data frame containing only the columns relevant for the Echo dispenser.
    
    Args: 
        annotation(pd.DataFrame): dataframe containing the annotation of the destination plate
        panel(pd.DataFrame): dataframe containing the panel library and source plate layout
    
    Returns: 
        pd.DataFrame containing only relevant columns for an Echo picklist
    """
    dfMerged = pd.merge(annotation, panel, on = 'Panel_Modification')
    dfMerged['Transfer Volume'] = dfMerged.nl_per_20 * dfMerged.cell_volume / 20
    dfPicklist = dfMerged[['Source Plate Barcode','Source Well', 'Destination Plate Barcode','Destination Well', 'Transfer Volume']]
    return dfPicklist

def export_picklist(picklist, path, name):
    """Exports the picklist as a .csv file to the chosen path and gives chosen name.
    
    Args: 
        picklist(pd.DataFrame): dataframe containing the picklist, return value of generate_picklist
        path(str): string containing the path where the picklist will be saved as a csv 
        name(str): string containing the name used in the export name of the csv.file
    """

    fileName = str(datetime.today().date()).replace('-','') + "_Picklist_" + name + ".csv"

    if platform.system() == "Darwin":  # macOS
        separator = "/"
    elif platform.system() == "Windows":
        separator = "\\"
    else:
        separator = "/"  # Default to "/" for other operating systems

    exportName = path + separator + fileName

    picklist.to_csv(exportName, sep = ",", index = False)