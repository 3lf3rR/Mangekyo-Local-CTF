<?php
// web/projects.php
$page_title = "Projects";
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
  <h2>Projects</h2>
  <p class="text-muted">Current and recent projects across our departments.</p>

  <div class="row mt-4">
    <div class="col-md-6">
      <div class="card mb-3 shadow-sm">
        <div class="card-body">
          <h5 class="card-title">Project Orion</h5>
          <p class="card-text">Platform migration and performance improvements. Status: <strong>Active</strong></p>
        </div>
      </div>
    </div>

    <div class="col-md-6">
      <div class="card mb-3 shadow-sm">
        <div class="card-body">
          <h5 class="card-title">Project Atlas</h5>
          <p class="card-text">Data analytics and dashboarding. Status: <strong>Completed</strong></p>
        </div>
      </div>
    </div>
  </div>
</main>

<script src="/assets/js/script.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
