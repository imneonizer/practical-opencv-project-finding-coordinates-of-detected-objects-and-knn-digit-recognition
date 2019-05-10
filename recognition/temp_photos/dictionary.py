import os

class my_dict():
	def start(my_dir): 
		mdir = os.listdir(my_dir)

		my_dict = {}

		for i in mdir:
			ustr = str(i)
			ustr = ustr.replace(".png","")
			ustr = list(ustr)
			#print(ustr)

			axtart = int(ustr[0])
			axend = str(ustr[2:])
			axend = axend.replace("[","")
			axend = axend.replace("'","")
			axend = axend.replace("]","")
			axend = axend.replace(", ","")
			axend = int(axend)
			#print(str(axend))
			my_dict.update({axtart : axend})
		return my_dict
		#print(my_dict)
		#os.system('pause')
