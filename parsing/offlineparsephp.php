<?php
$xml= simplexml_load_file("alamatbalai.xml");
foreach ($xml->Row as $DataBaris){
	echo "Balai : ".$DataBaris->Balai."\n";
	echo "Alamat : ".$DataBaris->Alamat."\n";
	echo "Telp : ".$DataBaris->telp."\n\n";
}
?>