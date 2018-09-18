import os,os.path
class fil:
	def listing(self):
		list=[]
		for x in os.listdir('C:\\Users\\training_c2d.02.11\\Desktop'):
			list.append(x)
		print list
	def count_files(self):
		print len([name for name in os.listdir('.') if os.path.isfile(name)])
		for root, dirs, files in os.walk("C:\\Users\\training_c2d.02.11\\Desktop", topdown=False):
		   for name in files:
			  print(os.path.join(root, name))
		   for name in dirs:
			  print(os.path.join(root, name))
	#def text_count(self):
		#if*0
obj=fil()
obj.listing()
obj.count_files()