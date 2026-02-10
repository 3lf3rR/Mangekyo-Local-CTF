<?php
// web/about.php
$page_title = "About";
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title><?= htmlspecialchars($page_title) ?> - Acme Corp</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body class="bg-light">
<?php include('navbar.php'); ?>

<main class="container py-5">
  <h2>About Acme Corp</h2>
  <p>We deliver enterprise-grade solutions with a focus on reliability and user experience. This site is a demo application used for testing and demonstration purposes.</p>
</main>

<script src="/assets/js/script.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
