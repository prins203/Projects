<?php
$name = $_POST['name'];
$dob = $_POST['dob'];
$email = $_POST['email'];
$psw = $_POST['psw'];
$phn = $_POST['phn'];

if (!empty($name) || !empty($dob) || !empty($email) || !empty($psw) || !empty($phn)) {
$host = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbname = "hotelregister";
$conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
 if (mysqli_connect_error()) {
     die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
    } else {
$SELECT = "SELECT email From users Where email = ? Limit 1";
$INSERT = "INSERT Into users(name,dob,email,psw,phn) values(?,?,?,?,?)";
     $stmt = $conn->prepare($SELECT);
     $stmt->bind_param("s", $email);
     $stmt->execute();
     $stmt->bind_result($email);
     $stmt->store_result();
     $rnum = $stmt->num_rows;
     if ($rnum==0) {
      $stmt->close();
      $stmt = $conn->prepare($INSERT);
      $stmt->bind_param("ssssi", $name, $dob, $email, $psw, $phn);
      $stmt->execute();
      echo "New record inserted sucessfully";
     } else {
      echo "Someone already register using this email";
     }
     $stmt->close();
     $conn->close();
    }}else {
 echo "All field are required";
	die();}

?>