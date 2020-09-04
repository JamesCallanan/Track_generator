from pybars import Compiler

def applySwap(KeyPairs, File):
	Template_File = open(File, 'r')
	with Template_File:
		source = Template_File.read()
	compiler = Compiler()
	template = compiler.compile(source)
	Swapped = template(KeyPairs)
	return Swapped


#file = open("SwappedFile.txt", "r")

def main(): 
	Output_File = open('asbQuadcopterWorld.wrl', 'w')
	
	segment_no 		= 1
	rotation_angle 	= 0
	x_line_translation 	= 58
	y_line_translation 	= 94
	segment_length 	= 0.6

	x_circ_translation 	= 55
	y_circ_translation 	= 90
	
	LineKeyValPairs = {	'segment_no': segment_no,
			'rotation_angle': rotation_angle,
			'x_translation': x_line_translation,
			'y_translation': y_line_translation,
			'segment_length': segment_length}

	CircleKeyValPairs = {	'x_translation': x_circ_translation,
				'y_translation': y_circ_translation}

	#Writing fixed base content to output file
	Output_File.write(open('base.wrl','r').read()+'\n')
	#Writing line segment objects to file
	Output_File.write(applySwap(LineKeyValPairs, 'TrackSegTemplate.wrl'))
	#Writing circle object to file
	Output_File.write(applySwap(CircleKeyValPairs, 'CircleTemplate.wrl'))
main()