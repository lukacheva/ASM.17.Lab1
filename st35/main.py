from .Container import *
import codecs, sys, os

class App(UIFunc):	
	''' Workhorse for the project.  '''
	def __init__(self):
		super().__init__()
		self.project_title = u'Lab project 01'	
		# Container instance
		self.container = Container()

		# Description for quit method
		setattr(App.interface_quit,self.p_desc_field,"Exit application");	

		''' Collect invokable methods from all inheritors of UIFunc '''
		''' Structure of data in functionsList : [ 0 = Class reference, 1 = method reference, 2 = Method description ] '''
		self.functions = list()
		for classRef in self.inheritors(UIFunc):
			self.functions += classRef.get_functions(classRef)		
		pass
	
	''' This method collects all direct and indirect inheritors of a given class'''		
	''' Using klass, as "class" is a reserved keyword '''	
	def inheritors(self,klass):		
	    subclasses = set()
	    work = [klass]
	    while work:
	        parent = work.pop()
	        for child in parent.__subclasses__():
	            if child not in subclasses:
	                subclasses.add(child)
	                work.append(child)
	    return subclasses		

	def interface_quit(self):
		''' Function for leaving application '''
		print("Leaveing application. BYE !")
		#exit()
		raise RuntimeError('Exit command issued')
		pass

	def printFunctions(self, functionsList):		
		''' Provides graphics menu retreived from all available UIFunc inheritors '''			
		for idx, function in enumerate(functionsList): print('{0}. {1}'.format(idx+1,function[2]))
		pass		

	
	def cls(self):
		''' Wait for user action and clear screen. Should be OS independent :) '''
		input("Press enter to continue...")
		os.system('cls' if os.name=='nt' else 'clear')			
	

	def mainLoop(self):
		''' Provides list of available user actions, validates input and trigger 
		    requested functions '''
		command = None
		while True:			
			print(self.project_title)
			self.printFunctions(self.functions)						
			try:
				command = int(input(u'Command: '))	
				# Validate user input
				# if command > 0 and command <= len(self.functions):
				# Range doesn't include last element
				if command in range(1, len(self.functions) + 1):					
					# Call selected function
					self.functions[command-1][1](self.container)
					# Clear screen from previous functions					
				else:					
					print("Incorrect command selected")	
					pass							
				self.cls()	
			except ValueError as e:
				print('Please enter a number')
				pass
			except RuntimeError as e:
				print(str(e))
				break
		pass

				
			

def main() :
	''' Creates instance of App and initiates input loop '''
	App().mainLoop()

if __name__ == "__main__":
    main()