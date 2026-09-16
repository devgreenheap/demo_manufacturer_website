// GIO Electronics — lightweight vanilla JS (no external libraries)
document.addEventListener("DOMContentLoaded", function () {
  initNavbar();
  initMobileMenu();
  initScrollReveal();
  initHeroCanvas();
  initFileDrop();
});

/* Navbar solidifies on scroll */
function initNavbar() {
  const nav = document.querySelector(".navbar");
  if (!nav) return;
  const onScroll = () => nav.classList.toggle("is-scrolled", window.scrollY > 20);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

/* Mobile hamburger menu */
function initMobileMenu() {
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  const scrim = document.querySelector(".nav-scrim");
  if (!toggle || !links) return;

  const openIcon = toggle.querySelector(".icon-menu");
  const closeIcon = toggle.querySelector(".icon-close");

  function setOpen(isOpen) {
    links.classList.toggle("is-open", isOpen);
    if (scrim) scrim.classList.toggle("is-open", isOpen);
    toggle.setAttribute("aria-expanded", String(isOpen));
    document.body.style.overflow = isOpen ? "hidden" : "";
    if (openIcon && closeIcon) {
      openIcon.style.display = isOpen ? "none" : "";
      closeIcon.style.display = isOpen ? "" : "none";
    }
  }

  toggle.addEventListener("click", () => setOpen(!links.classList.contains("is-open")));
  if (scrim) scrim.addEventListener("click", () => setOpen(false));
  links.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => setOpen(false)));
}

/* Fade/slide-up reveal on scroll using IntersectionObserver */
function initScrollReveal() {
  const targets = document.querySelectorAll(".reveal, .reveal-scale, .timeline-step");
  if (!targets.length) return;

  if (!("IntersectionObserver" in window)) {
    targets.forEach((el) => el.classList.add("in-view"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -60px 0px" }
  );

  targets.forEach((el) => observer.observe(el));
}

/* Hero: lightweight glowing-node circuit animation on canvas */
function initHeroCanvas() {
  const canvas = document.querySelector(".hero-canvas");
  if (!canvas || !canvas.getContext) return;
  const ctx = canvas.getContext("2d");
  let width, height, nodes;
  const NODE_COUNT = 28;
  const LINK_DIST = 150;

  function resize() {
    width = canvas.width = canvas.offsetWidth;
    height = canvas.height = canvas.offsetHeight;
  }

  function makeNodes() {
    nodes = Array.from({ length: NODE_COUNT }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.25,
      vy: (Math.random() - 0.5) * 0.25,
      r: Math.random() * 1.6 + 1,
    }));
  }

  function step() {
    ctx.clearRect(0, 0, width, height);
    nodes.forEach((n) => {
      n.x += n.vx;
      n.y += n.vy;
      if (n.x < 0 || n.x > width) n.vx *= -1;
      if (n.y < 0 || n.y > height) n.vy *= -1;
    });

    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i], b = nodes[j];
        const dist = Math.hypot(a.x - b.x, a.y - b.y);
        if (dist < LINK_DIST) {
          ctx.strokeStyle = `rgba(20, 121, 255, ${0.16 * (1 - dist / LINK_DIST)})`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }
    }

    nodes.forEach((n) => {
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(255, 106, 0, 0.7)";
      ctx.shadowColor = "rgba(255, 106, 0, 0.8)";
      ctx.shadowBlur = 6;
      ctx.fill();
      ctx.shadowBlur = 0;
    });

    requestAnimationFrame(step);
  }

  resize();
  makeNodes();
  window.addEventListener("resize", () => {
    resize();
    makeNodes();
  });

  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    requestAnimationFrame(step);
  }
}

/* Quote form: custom file-drop UI */
function initFileDrop() {
  const drop = document.querySelector(".file-drop");
  const input = document.querySelector("#attachment");
  if (!drop || !input) return;
  const label = drop.querySelector(".file-name");

  drop.addEventListener("click", () => input.click());
  drop.addEventListener("dragover", (e) => {
    e.preventDefault();
    drop.classList.add("is-dragover");
  });
  drop.addEventListener("dragleave", () => drop.classList.remove("is-dragover"));
  drop.addEventListener("drop", (e) => {
    e.preventDefault();
    drop.classList.remove("is-dragover");
    if (e.dataTransfer.files.length) {
      input.files = e.dataTransfer.files;
      updateLabel();
    }
  });
  input.addEventListener("change", updateLabel);

  function updateLabel() {
    if (input.files.length && label) {
      label.textContent = input.files[0].name;
    }
  }
}
