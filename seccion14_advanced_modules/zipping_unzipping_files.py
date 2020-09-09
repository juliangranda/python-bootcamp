f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()

f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()


#zipping files
import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

#extracting zipp files

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")







