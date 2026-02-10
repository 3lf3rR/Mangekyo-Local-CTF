#!/bin/sh
# entrypoint.sh - ensure runtime tmpfs dirs exist and file perms, then exec apache

# Ensure runtime dirs exist (tmpfs may be mounted by docker run/compose)
mkdir -p /var/run /var/lock/apache2 /var/log/apache2 /tmp 2>/dev/null || true

# Reapply safe perms for the flag
if [ -f /flag.txt ]; then
  chmod 444 /flag.txt 2>/dev/null || true
fi

# Ensure symlink exists in webroot (in case webroot is tmpfs)
ln -sf /flag.txt /var/www/html/flag.txt 2>/dev/null || true

# Ensure ownership of webroot static files (no-op if already correct)
chown -R www-data:www-data /var/www/html 2>/dev/null || true

# Exec the main CMD (apache2-foreground)
exec "$@"
