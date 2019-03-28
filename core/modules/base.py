#from sty import fg, rs

from core.utils import *

# ----------------------------------------------- ABSTRACT CLASSES

class Option(object): # ABSTRACT
	NAME = str()
	DESCRIPTION = str() 
	REQUIRED = bool()

	"""def __init__(self, required, name, description):
		self.REQUIRED = bool(required)
		self.NAME = name
		self.DESCRIPTION = description"""

	def __init__(self):
		pass

	def createOption(self, required, name, description):
		self.REQUIRED = bool(required)
		self.NAME = name
		self.DESCRIPTION = description

	def showOption(self):
		pass
	
class ParameterOption(Option): # ABSTRACT
	_VALUE = None # Encapsulated variables
	_TYPE = None
	DEFAULT = None

	"""def __init__(self, required, name, description, default=None):
		Option.__init__(self, required, name, description)
		if default:
			self.DEFAULT = default
			self._VALUE = default"""

	def __init__(self): # Usefull for pre-created options
		if self.DEFAULT:
			self._VALUE = self.DEFAULT

	def createOption(self, required, name, description, default=None): # VERY IMPORTANT: Function to create personalized options
		Option.createOption(self, required, name, description)
		if default:
			self.DEFAULT = default
			self._VALUE = default

		return self

	def getOption(self): # Will return a dict with the option values
		pass

	def setValue(self):
		pass

	def getValue(self):
		return self._VALUE

	def getType(self):
		return self._TYPE

# ---------------------------------------------------------------

class SingleParameterOption(ParameterOption):
	_VALUE = str()
	_TYPE = "SINGLE"

	def setValue(self, value):
		self._VALUE = str(value)

	def getOption(self):
		return self.REQUIRED, self.NAME, self._VALUE, self.DESCRIPTION


class MultipleParameterOption(ParameterOption):
	_VALUE = list()
	_TYPE = "MULTIPLE"

	def setValue(self, *values):
		for value in values:
			_VALUE.append(value)

	def getOption(self):
		return self.REQUIRED, self.NAME, [x for x in self._VALUE], self.DESCRIPTION

class OptionsMenu(object):
	OPTIONS = dict()

	def createOptions(self, *args): # Function that must be used in each module to generate the functions.
		# This function will return a clean dict to be used in the the updateOptions function of the BaseModule
		finalOptions = dict()
		for arg in args:
			if isinstance(arg, Option):
				finalOptions.update({arg.NAME : arg})
			else:
				raiseError(f"Option {arg} is not a valid option object instance!")
		self.OPTIONS = finalOptions

	def setOption(self, option, value):
		if not option in self.OPTIONS:
			raiseError(f"Option {option} not found!")
			return
		self.OPTIONS[option].setValue(value)

	def getOptions(self): # Function that return all functions of the menu
		return self.OPTIONS

	def showOptions(self): # Executed with the show options command
		if not self.OPTIONS:
			raiseError("No options to show")
		print("+----------------------------------------+")
		print("| NAME | REQUIRED | VALUES | DESCRIPTION |")
		print("+----------------------------------------+")
		for option in self.OPTIONS:
			optionObject = self.OPTIONS[option]
			# IMPORTANT: THIS WILL BE CHANGED TO GET THE DATA WITH THE OWN OPTION OBJECT VARIABLES
			data = optionObject.getOption() # Getting a dict with the option values
			if optionObject.getType() == "MULTIPLE": # Print values with ',' splitting them
				values_text = ",".join(x for x in data[2])
				print(f"{data[1]} | REQUIRED = {data[0]} | {values_text} | {data[3]}")
			else:
				print(f"{data[1]} | REQUIRED = {data[0]} | {data[2]} | {data[3]}")

# ----------------------------------------------- ABSTRACT CLASSES

class BaseModule(object):
	NAME = "Example"
	DESCRIPTION = "Example description"

	OPTIONS_MENU = None # IMPORTANT: Here are the options stored in the shown by the show options for example
	"""
	IMPORTANT: These are the options that'll be used in the module in the run function. They only are setted when the module runs

	Also, these dict options will have directly the values, no the option
	"""
	OPTIONS = dict()

	def __init__(self):
		self.OPTIONS_MENU = OptionsMenu()	

	def getOptions(self): # Return option menu options
		return self.OPTIONS_MENU.OPTIONS

	def updateOptions(self): # Load the options to be accesible to the module
		try:
			for option in self.OPTIONS_MENU.OPTIONS:
				self.OPTIONS.update({option : self.OPTIONS_MENU.OPTIONS[option].getValue()})
		except AttributeError:
			pass

	def raiseMessage(self, message):
		print(f"({self.NAME}) {fg.green}[+]{rs.all} {message}")

	def raiseWarning(self, message):
		print(f"({self.NAME}) {fg.yellow}[*]{rs.all} {message}")

	def raiseError(self, message):
		print(f"({self.NAME}) {fg.red}[-]{rs.all} {message}")

	def run(self): # IMPORTANT: This function must be modified with the module actions. You can take the options via self.OPTIONS["option"]
		pass

	def executeModule(self): # IMPORTANT: This function should not be modified
		self.updateOptions()
		self.run()
# ---------------------------------------------------------------