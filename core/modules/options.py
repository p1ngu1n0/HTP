from core.modules import *
from core.utils import *

"""
This file contains options that can be used in any module just creating a object with them
"""

class TARGET(SingleParameterOption):
	DEFAULT = "TARGETDEFAULT"
	NAME = "TARGET"
	DESCRIPTION = "Target for the module"
	REQUIRED = True

	def setValue(self, value): # This function must be replaced
		self._VALUE = value

class TARGETS(MultipleParameterOption):
	DEFAULT = "TARGETDEFAULT"
	NAME = "TARGET"
	DESCRIPTION = "Target for the module"
	REQUIRED = True

	def setValue(self, targets):
		self._VALUE = targets
