import bdsf
input_images = ['3C286-selfcalimg4.fits','2206-185-selfcalimg3.fits']
for input_image in input_images:
#	img = bdsf.process_image(input_image)
	img = bdsf.process_image(input_image, adaptive_rms_box=True, thresh='hard')
#	tput 'MYIMGTGSS.sav'
# Write the source list catalog. File is named automatically.
	img.write_catalog(format='ascii', catalog_type='srl')
# Write the residual image. File is named automatically.
	img.export_image(img_type='gaus_resid')
# Write the model image. Filename is specified explicitly.
	img.export_image(img_type='gaus_model', outfile=input_image+'.model')


