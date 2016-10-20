<?php
$xml = simplexml_load_file("http://feeds.bbc.co.uk/indonesian/index.xml");
foreach ($xml->item as $baris) {
	echo "Judul : ".$baris->title."\n";
	echo "Deskripsi : ".$baris->description."\n";
	# code...
}
?>