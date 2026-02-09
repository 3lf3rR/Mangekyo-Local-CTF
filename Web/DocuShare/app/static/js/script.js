document.addEventListener("DOMContentLoaded", function () {
  // mark nav link active if URL contains segment
  const links = document.querySelectorAll('nav a.nav-link');
  links.forEach(a => {
    try {
      const href = a.getAttribute('href');
      if (href && location.pathname.toLowerCase().startsWith(href.toLowerCase())) {
        a.classList.add('active');
      }
    } catch (e) {}
  });
});
