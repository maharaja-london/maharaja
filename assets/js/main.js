/* Maharaja London — shared interactions */
(function () {
  // Sticky header
  var hdr = document.getElementById('hdr');
  if (hdr) {
    var onScroll = function () { hdr.classList.toggle('solid', window.scrollY > 60); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Mobile menu
  var burger = document.getElementById('burger');
  var mm = document.getElementById('mobileMenu');
  if (burger && mm) {
    burger.addEventListener('click', function () { mm.classList.toggle('open'); });
    mm.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { mm.classList.remove('open'); });
    });
  }

  // Scroll reveal
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
