<!DOCTYPE html>
<html>
<head>
	<title></title>
	<style type="text/css">
		table{
			border-color: black;
			border : solid 0.5px;
		}
		th{
			border: solid 0.5px;
			border-color: black;
			font-weight: normal;
			text-align: left;
			padding: 3px;
		}
	</style>
</head>
<body>
<?php
$con = mysqli_connect("localhost", "phpmyadmin", "Santowijaya", "mahasiswa");

if ($con){
	echo "Berhasil";
} else {
	echo "Gagal";
}

$sql = "SELECT * FROM bio";
$hasil = mysqli_query($con, $sql);

if(mysqli_num_rows($hasil) >0){
	//Cetak ke layar
	echo "
	<table cellspacing='0' cellpadding = '0'>
	<tr bgcolor='#FF0000'>
		<th> nim </th>
		<th> firstname </th>
		<th> lastname </th>
		<th> email </th>

	</tr>";
	while($baris = mysqli_fetch_assoc($hasil)){
		echo "<tr>
			<th>".$baris["nim"]."</th>
			<th>".$baris["firstname"]."</th>
			<th>".$baris["lastname"]."</th>
			<th>".$baris["email"]."</th>
		</tr>";
	}
	echo"</table>";
} else {
	echo "Tanpa hasil";
}

mysqli_close($con);
?>
</body>
</html>

