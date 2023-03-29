<?php
require 'PHPMailer/PHPMailer.php';
require 'PHPMailer/SMTP.php';

// Create a new PHPMailer object
$mail = new PHPMailer\PHPMailer\PHPMailer();

// Set the SMTP server details
$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->Username = 'atulkumar1130@gmail.com';
$mail->Password = '';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;

// Set the email details
$mail->setFrom('your-email@gmail.com', 'Your Name');
$mail->addAddress('recipient-email@example.com', 'Recipient Name');
$mail->Subject = 'Email Subject';

// Read the HTML file and set it as the email body
$html = file_get_contents('path/to/your/html/file');
$mail->isHTML(true);
$mail->Body = $html;

// Send the email
if ($mail->send()) {
  echo 'Email sent successfully';
} else {
  echo 'Error sending email: ' . $mail->ErrorInfo;
}
?>
