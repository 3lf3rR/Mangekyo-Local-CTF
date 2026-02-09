FROM php:7.4-apache

RUN a2enmod rewrite

COPY src/ /var/www/html/
COPY flag.txt /flag.txt

RUN chmod 444 /flag.txt
RUN chown -R www-data:www-data /var/www/html

EXPOSE 80
