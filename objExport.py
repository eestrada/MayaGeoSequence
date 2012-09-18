# Authored by Zack Glynn 2010


#def obj_ex():       # uncomment this line if this script is to be used as a function
if True:             # comment out or delete this line if this is used as a function instead of a standalone script
	import maya.cmds as mc

	if len(mc.ls(sl = True)) != 0:	# Checks to see if anything is selected. Otherwise, the script cancels out.

		startFr = mc.playbackOptions(query = True, min = True)
		endFr = mc.playbackOptions(query = True, max = True)
		print('Start frame is: ' + str(startFr))
		print('End frame is: ' + str(endFr))
		window1 = mc.fileDialog2(caption = "Choose the directory to save your .obj sequence", fileMode = 3, dialogStyle=2)

		if str(window1) != 'None':
			#origName = mc.file(q=True, sceneName=True)
			pathname = window1[0]
			objName = 'defaultName' # Default name used if no name is specified
			u = '_'

			window2 = mc.promptDialog(title = 'Sequence Name', message = 'Type the name you would like to give your .obj sequence.', button = ['OK','Cancel'], defaultButton = 'OK', cancelButton = 'Cancel')
			if window2 == 'OK': # Names the sequence if user hits "OK" button. Otherwise the default name is used
				objName = mc.promptDialog(query = True, text = True)
				objName = str(objName)

			while startFr <= endFr:
				mc.currentTime (startFr)
				fileName = objName + u + '%04d' % (startFr)
				mc.file(rename = pathname + '/' + fileName)
				mc.file(es = True, typ = 'OBJexport', pr = True)
				print('Successfully exported: ' + fileName)
				startFr = startFr + 1

			mc.confirmDialog(title = 'Success', message = '.obj sequence successfully exported and saved.')

		else:
			mc.confirmDialog(title = 'Canceled', message = 'Operation canceled')

	else:
		mc.confirmDialog(title = 'Nothing selected', message = 'No objects were selected to export! Please try again.')
