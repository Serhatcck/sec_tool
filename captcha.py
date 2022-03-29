from email.policy import default
import os
import subprocess
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file",help="captcha file")
parser.add_argument("-r", "--result",help="captcha result")
parser.add_argument('-m','--mogrify',help='use mogrify ? For tesseract dpi error',type=bool,default=False)
args = parser.parse_args()




captcha_file = args.file
file_inf = captcha_file.split(".")
file_extension = file_inf[len(file_inf) -1]
true_result = args.result
mogrify = args.mogrify

for i in range (1,100):
	os.system('convert '+captcha_file+' -threshold '+str(i)+'% -paint 1 -blur 0 out.'+file_extension)
	if(mogrify):
		os.system('mogrify -set units PixelsPerInch -density 300 out.'+file_extension)
	result = subprocess.check_output('tesseract out.'+file_extension+' -',shell=True)
	result = result.decode('utf-8').strip()
	if result == true_result:
		print('Success!')
		print('convert '+captcha_file+' -threshold '+str(i)+'% -paint 1 -blur 0 out.'+file_extension)
		if (mogrify):
			print('mogrify -set units PixelsPerInch -density 300 out.'+file_extension)
		
		print('tesseract out.'+file_extension+' -')
		break
	os.system('rm out.'+file_extension)


