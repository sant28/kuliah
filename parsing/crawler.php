<?php
include_once('simple_html_dom.php');
phpinfo();
$target = "localhost/";
$html = new_simple_html_dom();
$html->load_file($target);
foreach ($html->href as $link) {
	# code...
	echo $link;
}
?>