# Dockerfile
FROM php:8.2-apache

# Copy web root
COPY web/ /var/www/html/

# Copy entrypoint (runtime helper)
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Minimal Apache hardening
RUN a2enmod headers \
 && echo "ServerTokens Prod" >> /etc/apache2/conf-available/security.conf \
 && echo "ServerName localhost" >> /etc/apache2/conf-available/security.conf \
 && a2enconf security || true

# Create canonical flag (readable by all, non-writable)
RUN printf "SecurinetsISTIC{c0mm4nd_inj3t1oN_fr_t00_risky}\n" > /flag.txt \
 && chmod 444 /flag.txt

# Create symlink in webroot so both `cat flag.txt` and `cat /flag.txt` work
RUN ln -sf /flag.txt /var/www/html/flag.txt || true

# Ensure web root files owned by www-data for static content
RUN chown -R www-data:www-data /var/www/html || true

# Entrypoint ensures runtime dirs and perms then starts apache
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["apache2-foreground"]
