<?php
// Connect to MySQL database
$servername = "localhost";
$username = "root";
$password = "Atul@12345";
$dbname = "email_data";
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Get form data
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// Insert data into MySQL database
$sql = "INSERT INTO contact_form (name, email, message) VALUES ('$name', '$email', '$message')";
mysqli_query($conn, $sql);

// Send email to sender
$to = $_POST['email'];
$subject = "contact_form";
$message = "Thank you for submitting the form. Your data has been recorded in the database.";
$headers = "From: atulkumar1130@gmail.com";
mail($to, $subject, $message, $headers);
?>
