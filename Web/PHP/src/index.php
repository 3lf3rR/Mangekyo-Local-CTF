<?php

error_reporting(0);
ini_set('display_errors', 0);

session_start();

function is_admin($user) {
    if ($user === "admin") {
        die("nope");
    }

    if (strcmp($user, "admin") == 0) {
        return true;
    }

    return false;
}

// Accept GET or POST
$user = $_REQUEST['user'] ?? null;

if ($user !== null) {
    if (is_admin($user)) {
        $_SESSION['admin'] = true;
        header("Location: /dashboard.php");
        exit;
    } else {
        $error = "Invalid user";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Lesgoooo</title>
    <style>
        body {
            font-family: monospace;
            background: #0f172a;
            color: #e5e7eb;
            padding: 20px;
        }
        h1, h2 {
            color: #38bdf8;
        }
        .box {
            background: #020617;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        a {
            color: #22d3ee;
        }
        pre {
            overflow-x: auto;
        }
    </style>
</head>
<body>

<h1>Lesgoooo</h1>

<div class="box">
    <h2>Login</h2>
    <?php if (isset($error)) echo "<p>$error</p>"; ?>
    <form>
        <input name="user" placeholder="username">
        <button>Login</button>
    </form>
</div>

<div class="box">
    <h2>Source Code</h2>
    <?php highlight_file(__FILE__); ?>
</div>

</body>
</html>
