<?php

if(isset($_POST['save'])) {
  // retrieve data from the form
  $first_name = $_POST['first_name'];
  $last_name = $_POST['last_name'];
  $gender = $_POST['gender'];
  $email = $_POST['email'];
  $phone = $_POST['phone'];
  
  // validate data here if needed
  
  // process data, such as inserting it into a database
  $servername = "localhost";
  $username = "root";
  $password = "";
  $dbname = "database 1";
  
  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);
  
  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  
  // Prepare and bind the data
  $stmt = $conn->prepare("INSERT INTO my_table (first_name, last_name, gender, email, phone) VALUES (?, ?, ?, ?, ?)");
  $stmt->bind_param("sssss", $first_name, $last_name, $gender, $email, $phone);
  
  // Execute the statement
  $stmt->execute();
  
  // Close the statement and connection
  $stmt->close();
  $conn->close();
  
  // redirect to a success page or show a success message
  echo "Data submitted successfully!";
}

?>