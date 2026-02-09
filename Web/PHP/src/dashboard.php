<?php
session_start();

if (!($_SESSION['admin'] ?? false)) {
    die("Access denied");
}

$flag = trim(file_get_contents("/flag.txt"));

echo "<h2>Welcome admin</h2>";
echo "<pre>$flag</pre>";
