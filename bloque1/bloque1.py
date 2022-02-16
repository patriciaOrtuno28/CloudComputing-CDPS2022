#!/usr/bin/python3
from subprocess import call
import os 

call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
call(['sudo', 'apt-get', 'update'])
call(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])
os.chdir('practica_creativa2/bookinfo/src/productpage')
call(['pip3', 'install', '-r', 'requirements.txt'])

os.environ['GROUP_NUMBER'] = '28'
call(['mv', 'productpage_monolith.py', 'productpage_monolith_onlyRead.py'])
fin = open('productpage_monolith_onlyRead.py', 'r')
fout = open('productpage_monolith.py', 'w')

for line in fin:
	# Creamos una variable local que referencie la variable de entorno
	if 'flood_factor = 0 if (os.environ.get("FLOOD_FACTOR") is None) else int(os.environ.get("FLOOD_FACTOR"))' in line :
		fout.write(line)
		fout.write(os.linesep + 'groupNumber = 0 if (os.environ.get("GROUP_NUMBER") is None) else int(os.environ.get("GROUP_NUMBER"))' + os.linesep)
	# La enviamos en el renderizado del html
	elif 'def front():' in line :
		fout.write(line)
		fout.write('    group = groupNumber' + os.linesep)
	elif '\'productpage.html\',' in line :
		fout.write(line)
		fout.write('\tgroup=group,' + os.linesep)
	else :
		fout.write(line)

fin.close()
fout.close()
call(['rm', '-f', 'productpage_monolith_onlyRead.py'])

os.chdir('templates')
call(['mv', 'productpage.html', 'productpage_onlyRead.html'])
fin = open('productpage_onlyRead.html', 'r')
fout = open('productpage.html', 'w')

for line in fin:
	# Cambiamos el titlte del html con la variable recibida del python
	if '{% block title %}Simple Bookstore App{% endblock %}' in line :
		fout.write(line.replace('{% block title %}Simple Bookstore App{% endblock %}', '{% block title %}GRUPO: {{ group }}{% endblock %}'))
	else :
		fout.write(line)

fin.close()
fout.close()
call(['rm', '-f', 'productpage_onlyRead.html'])

os.chdir('..')
call(['python3', 'productpage_monolith.py', '9080'])
