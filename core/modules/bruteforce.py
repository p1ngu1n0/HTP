from core.modules import *

class BruteforceModule(BaseModule):
	# BY DEFAULT, THE RUN FUNCTION WILL EXECUTE WITH THREADS THE FUNCTION 'STEP'

	def __init__(self):
		BaseModule.__init__(self)

	THREADS = 10 # Default value for threading

	def run(self): 
		"""
		BY DEFAULT THIS FUNCTION DON'T NEED TO BE OVERWRITED, IT CONTAINS DE FUNCTION OF RUNNING THE STEP IN DIFFERENT THREADS
		"""
		print("test")

	def step(self):
		"""
		Here, you have to write the things that the bruteforce will do with each check
		"""
		pass