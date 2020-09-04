from pybars import Compiler

def applySwap(KeyPairs, File):
	Template_File = open(File, 'r')
	with Template_File:
		source = Template_File.read()
	compiler = Compiler()
	template = compiler.compile(source)
	Swapped = template(KeyPairs)
	Template_File.close
	return Swapped


#file = open("SwappedFile.txt", "r")

def main(): 
	Output_File = open('asbQuadcopterWorld.wrl', 'w')
	SwapKeys = {	'person': 'Eoin', 
			'trait': 'in the ufc'}
	Output_File.write(applySwap(SwapKeys, 'template.txt') + '\n')
	Output_File.write(applySwap(SwapKeys, 'template.txt'))
main()