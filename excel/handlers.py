# -*- coding: utf-8 -*-
"""
Class allowing to interact with an Excel file
"""

from pyExcelerator import *
from os.path import abspath

from excel.headers import main_header_type

class BSExcelFileData:

# NOTES FOR DEVELOPPEMENT
# sheetname : self.xls[sheet][0] 
# sheetdata : self.xls[sheet][1]
# nb_sheets : len(self.data)

    def __init__(self,filename):
	try :
	    self.xls = ImportXLS.parse_xls(filename)
	except :
	    print "No excel file found at %s" %(abspath(filename))
	    exit(1)
	    
        # Init
	self.data = [] # liste de dictionnaires. 1 dico --> 1 feuille XL
	self.nsheet = len(self.xls)
	self.sheetname = []
	self.cols = []
	self.rows = []

        # Parsing
	for sheet in range(self.nsheet):
	    if len(self.xls[sheet][1]) != 0: # If worksheet not empty
		self.sheetname.append(self.xls[sheet][0])
		self.data.append(self.xls[sheet][1])

	self.nsheet = len(self.data)
        
    def get_corners(self,sheet):
        """
        Returns dimensions of sheet as tuple of 4 values:
        * column_max
        * row_max
        * column_min
        * row_min
        """
	if sheet>=self.nsheet:
	    return
	rowmax,colmax = max(self.data[sheet].keys()) ## lower right corner
	rowmin,colmin = min(self.data[sheet].keys()) ## higher left corner
	return colmin, rowmin, colmax, rowmax
            

    def get_data_by_dict(self,token_data):
        """
        Get sheet column names.
	The format of token_data is 'key':[column,type]
	the result is a list of dict 'key':value  
	"""
	result = []
	for sheet in range(self.nsheet):
	    d = self.data[sheet]
            colmin, rowmin, colmax, rowmax = self.get_corners(sheet)
	    for row in range(rowmin,rowmax+1):
		td = {}
		for key in token_data.keys():
		    col = token_data[key][0]
		    typ = token_data[key][1]
		    if d.has_key((row,col)):
			if type(typ) != type(unicode("yop")):
			    try:
				val = int(d[(row,col)])
				if type(val)==type(typ):
				    td[key] = d[(row,col)] 
			    except ValueError :
				try :
				    val = float(d[(row,col)])
				    if type(val)==type(typ):
					td[key] = val
					print val
				except ValueError:
				    pass			    
			else:
			    td[key] = d[(row,col)]
		    
		if len(td.keys())==len(token_data.keys()):
		    result.append(td)
	return result

    def find_token(self,token):
        """ 
        'FIND' tool with returns a list of [sheet_number, (row, colum)] 
        of found occurences of input token 
        """
	self.spot = []
	for sheet in range(self.nsheet):
	    d = self.data[sheet]
	    for l in d.keys():
		if (type(d[l]) is str) or ( type(d[l]) is unicode) :
		    if d[l].upper() == token.upper():
			self.spot.append([sheet,l])
        return self.spot

    def get_row(self, sheet, nrow):
        """Select the data stored in a row given the sheet name and the row index"""

        colmin, rowmin, colmax, rowmax = self.get_corners(sheet) 
        
        data = self.xls[sheet][1]
        if nrow > 0 :
            row = {}
            for ncol in range(colmax+1):
                if (nrow, ncol) in data:
                    row.update( {data[0, ncol]: data[nrow, ncol]} )
                else:
                    # Problem : null value for unicode = '' and null value for others = None
                    if isinstance(main_header_type[ncol], unicode):
                        row.update( {data[0, ncol]: ''} ) 
                    else:
                        row.update( {data[0, ncol]: None} )
            return row

    def get_header(self, sheet):
        """Select the header titles of a sheet"""
        return select_row(sheet,0)
                       


if __name__=='__main__':
    
    xl = BSExcelFileData('../../Data/Test_Data_BIM.xls')
    print xl.get_corners(0)
    d = {'nom':[1,unicode("yop")],'prenom':[2,unicode("yop")]}
    print xl.get_data_by_dict(d)
    print xl.find_token('prenom(s)')
    
