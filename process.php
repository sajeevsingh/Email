<?php

		$name = $_POST['name'];
		$email = $_POST['email'];
		$message = $_POST['message'];



		// Database connection
		$conn = new mysqli('localhost','root','Atul@12345','email_data');
		if($conn->connect_error){
			echo "$conn->connect_error";
			die("Connection Failed : ". $conn->connect_error);
		} else {
			$stmt = $conn->prepare("insert into contact_form(name, email, message) values(?, ?, ?)");
			$stmt->bind_param("sssssi", $name, $email, $messaage);
			$execval = $stmt->execute();
			echo $execval;
			echo "Registration successfully...";
			$stmt->close();
			$conn->close();
		}
?>
