<?php

if (isset($_POST['auth'])) {
$Surname = $_POST['Surname'];
$Name = $_POST['Name'];
$Patronymic = $_POST['Patronymic'];
$c = $Surname.' '. $Name.' '. $Patronymic;
$file=fopen('mes.txt','w');
fputs($file, $c);
fclose($file);
echo 'Успешно';
}
?>



