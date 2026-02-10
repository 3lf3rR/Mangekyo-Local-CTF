<?php
// web/documents.php
$page_title = "Documents";
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
  <h2>Documents</h2>
  <p class="text-muted">Repository of company documents and reports.</p>

  <div class="card shadow-sm">
    <div class="card-body">
      <table class="table table-hover mb-0">
        <thead class="table-light">
          <tr><th>Title</th><th>Type</th><th>Date</th></tr>
        </thead>
        <tbody>
          <tr><td>Project Plan</td><td>PDF</td><td>2025-01-15</td></tr>
          <tr><td>Financial Report</td><td>XLSX</td><td>2025-03-22</td></tr>
          <tr><td>Security Guidelines</td><td>DOCX</td><td>2025-06-10</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</main>

<script src="/assets/js/script.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
