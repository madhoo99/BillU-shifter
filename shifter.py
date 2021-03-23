import shutil, os, xlrd

# Give the location of the excel sheet 
loc = ("/Users/madho/Downloads/BillU Dataset.xlsx")

# Enter location of dataset folder path (DO NOT FORGET the '/' after dataset)
path = '/Users/madho/Downloads/dataset/'

def create_folder(name):
	dirc = path + name
	try:
		os.mkdir(dirc)
	except OSError:
		print ("Creation of the directory %s failed" % dirc)
	else:
		print ("Successfully created the directory %s" % dirc)


def shifter():
	# To open Workbook 
	wb = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(1) 
	for count in range(1,9505):

		# For row 0 and column 0 
		user = sheet.cell_value(count, 0)
		file = sheet.cell_value(count, 3)
		# user_path = "/Users/madho/Downloads/dataset/%s"%user
		# file_path = "/Users/madho/Downloads/dataset/%s"%file

		if not os.path.isfile(file):
			print('File %s not in dataset!'%file)
			continue
		if os.path.isdir(user):
			shutil.move(file, user)
		else:
			create_folder(user)
			shutil.move(file, user)

shifter()




# files = ['415.jpg']
# for f in files:
#     shutil.copy(f, 'dest_folder')

# print(os.path.isdir('dest_folder2'))