#!/usr/bin/python
from xml.dom.minidom import parse
import xml.dom.minidom

cari = xml.dom.minidom.parse("alamatbalai.xml")
dokumen = cari.documentElement

for baris in dokumen.getElementsByTagName("Row") :
	balai = baris.getElementsByTagName("Balai")[0]
	alamat = baris.getElementsByTagName("Alamat")[0]
	telp = baris.getElementsByTagName("telp")[0]
	print "Balai : %s" % balai.childNodes[0].data
	print "Alamat balai : %s" % alamat.childNodes[0].data
	print "Telp : %s \n" % telp.childNodes[0].data