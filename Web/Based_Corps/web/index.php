<?php
// web/index.php
$page_title = "Home";
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
  <div class="text-center mb-4">
    <h1 class="display-5">Acme Corp</h1>
    <p class="lead">Business solutions with real results.</p>
  </div>

  <div class="row g-4">
    <div class="col-md-4">
      <div class="card shadow-sm h-100">
        <div class="card-body">
          <h5 class="card-title">Projects</h5>
          <p>Overview of ongoing and completed projects across teams.</p>
          <a href="/projects.php" class="btn btn-outline-primary btn-sm">View</a>
        </div>
      </div>
    </div>

    <div class="col-md-4">
      <div class="card shadow-sm h-100">
        <div class="card-body">
          <h5 class="card-title">Reports</h5>
          <p>Access reports, downloads and KPIs.</p>
          <a href="/documents.php" class="btn btn-outline-primary btn-sm">Documents</a>
        </div>
      </div>
    </div>

    <div class="col-md-4">
      <div class="card shadow-sm h-100">
        <div class="card-body">
          <h5 class="card-title">Support</h5>
          <p>Contact our support team for help or general inquiries.</p>
          <a href="/contact.php" class="btn btn-outline-primary btn-sm">Contact</a>
        </div>
      </div>
    </div>
  </div>
</main>

<script src="/assets/js/script.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
