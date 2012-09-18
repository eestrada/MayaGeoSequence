# Authored by Zack Glynn 2010
# Modified by Ethan Estrada 2011

from __future__ import print_function


#def bgeoExport():       # uncomment this line if this script is to be used as a function
if True:             # comment out or delete this line if this is used as a function instead of a standalone script
	import maya.cmds as mc
	import os
	import subprocess as sp
	

	if len(mc.ls(sl = True)) != 0:	# Checks to see if anything is selected. Otherwise, the script cancels out.

		startFr = mc.playbackOptions(query = True, min = True)
		endFr = mc.playbackOptions(query = True, max = True)
		print('Start frame is: ' + str(startFr))
		print('End frame is: ' + str(endFr))
		window1 = mc.fileDialog2(caption = "Choose the directory to save your .bgeo sequence", fileMode = 3, dialogStyle=2, okCaption='OK')

		if str(window1) != 'None':
			#origName = mc.file(q=True, sceneName=True)
			pathname = window1[0]
			print('Current working directory is ' + os.getcwd())
			os.chdir(pathname)
			print('Changed working directory to ' + os.getcwd() + '\n')
			objName = 'defaultName' # Default name used if no name is specified
			u = '.'

			window2 = mc.promptDialog(title = 'Sequence Name', message = 'Type the name you would like to give your .obj sequence.', button = ['OK','Cancel'], defaultButton = 'OK', cancelButton = 'Cancel')
			if window2 == 'OK': # Names the sequence if user hits "OK" button. Otherwise the default name is used
				objName = mc.promptDialog(query = True, text = True)
				objName = str(objName)
				
			objstr = mc.polyAverageNormal(distance=0.0, prenormalize=True, postnormalize=False, allowZeroNormal=False, replaceNormalXYZ=(1.0, 0.0, 0.0))
			print('Object has had its vertex normals averaged.')
			
			while startFr <= endFr:
			    mc.currentTime (startFr)
			    filename = objName + u + '%04d' % (startFr)
			    mc.file(rename = pathname + '/' + filename + '.obj')
			    mc.file(es = True, ch = False, chn = False, con = False, exp = False, sh = False, typ = 'OBJexport')
			    print('Successfully exported: ' + filename + '.obj')
			    cmdstr = '/opt/hfs.current/bin/gwavefront ' + pathname + '/' + filename + '.obj' + ' ' + pathname + '/' + filename + '.bgeo'
			    print('Converting .obj to .bgeo file...', end='')
			    sp.Popen(cmdstr, shell=True)
			    os.wait()
			    print('done!')
			    os.remove(pathname + '/' + filename + '.obj')
			    print('Deleted .obj file.')
			    os.remove(pathname + '/' + filename + '.mtl')
			    print('Deleted .mtl file.\n')
			    startFr = startFr + 1
			
			mc.confirmDialog(title = 'Success', message = 'Your .bgeo sequence was successfully exported and saved.')

		else:
			mc.confirmDialog(title = 'Canceled', message = 'Operation canceled')

	else:
		mc.confirmDialog(title = 'Nothing selected', message = 'No objects were selected to export! Please try again.')
