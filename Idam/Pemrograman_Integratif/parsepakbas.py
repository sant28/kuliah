#Ahmad Idham T Lubis
#18214027

#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser

DOMTree = xml.dom.minidom.parse("propinsi_04_2.xml")  # Dokumen XML
collection = DOMTree.documentElement

#Data waktu pengambilan data cuaca
tanggal = collection.getElementsByTagName("Tanggal")
for waktu in tanggal:
    mulai = waktu.getElementsByTagName('Mulai')[0]
    print "Tanggal: %s" % mulai.childNodes[0].data

print "\n"

# Ambil semua "Kota".
# Kota diambil dari "Row" yang merupakan loop representasi kota
rows = collection.getElementsByTagName("Row")

# Print detail of each "Kota".
for row in rows:
    kota = row.getElementsByTagName('Kota')[0]
    print "Kota: %s" % kota.childNodes[0].data
    balai = row.getElementsByTagName('Balai')[0]
    print "Balai: %s" % balai.childNodes[0].data
    propinsi = row.getElementsByTagName('Propinsi')[0]
    print "Propinsi: %s" % propinsi.childNodes[0].data
    print "\n"