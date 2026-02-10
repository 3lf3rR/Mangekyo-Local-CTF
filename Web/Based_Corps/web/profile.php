<?php
$page_title = "Profile";
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title><?= htmlspecialchars($page_title) ?> - MyApp</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body class="bg-light">
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">MyApp</a>
  </div>
</nav>

<main class="container py-4">
  <h1>Your Profile</h1>
  <p>Name: John Doe</p>
  <p>Email: john.doe@example.com</p>
  <p>Role: User</p>
  <p>Member since: Jan 2025</p>

  <h3>Recent Activity</h3>
  <ul>
    <li>Logged in from IP 192.168.1.100</li>
    <li>Updated profile picture</li>
    <li>Viewed dashboard report #23</li>
  </ul>
</main>
</body>
</html>
