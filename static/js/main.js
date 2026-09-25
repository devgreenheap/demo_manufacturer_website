// GIO Electronics — lightweight vanilla JS (no external libraries)

/* Top loading bar: fills while the page loads, completes on window "load",
   and restarts on internal link clicks so the next page feels instant. */
(function initPageLoader() {
  const bar = document.getElementById("page-loader");
  if (!bar) return;

  requestAnimationFrame(() => bar.classList.add("is-loading"));

  window.addEventListener("load", () => {
    bar.classList.remove("is-loading");
    bar.classList.add("is-done");
  });

  document.addEventListener("click", (e) => {
    const link = e.target.closest("a[href]");
    if (!link) return;
    const isInternal = link.origin === window.location.origin;
    const isNewTab = link.target === "_blank" || e.metaKey || e.ctrlKey;
    const isAnchor = link.getAttribute("href").startsWith("#");
    if (isInternal && !isNewTab && !isAnchor) {
      bar.classList.remove("is-done");
      bar.classList.add("is-loading");
    }
  });
})();

document.addEventListener("DOMContentLoaded", function () {
  initNavbar();
  initMobileMenu();
  initScrollReveal();
  initHeroCanvas();
  initFileDrop();
  initSubnavSpy();
  initTiltCards();
  initNavDropdown();
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

  function setOpen(isOpen) {
    links.classList.toggle("is-open", isOpen);
    if (scrim) scrim.classList.toggle("is-open", isOpen);
    toggle.classList.toggle("is-open", isOpen);
    toggle.setAttribute("aria-expanded", String(isOpen));
    document.body.style.overflow = isOpen ? "hidden" : "";
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
          ctx.strokeStyle = `rgba(30, 64, 175, ${0.2 * (1 - dist / LINK_DIST)})`;
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
      ctx.fillStyle = "rgba(30, 64, 175, 0.75)";
      ctx.shadowColor = "rgba(30, 64, 175, 0.8)";
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

/* Highlight the active sub-nav tab as the user scrolls past each section */
function initSubnavSpy() {
  const links = document.querySelectorAll("[data-subnav]");
  if (!links.length) return;

  const sections = Array.from(links)
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);
  if (!sections.length) return;

  function setActive(id) {
    links.forEach((link) => {
      link.classList.toggle("is-active", link.getAttribute("href") === `#${id}`);
    });
  }

  if (!("IntersectionObserver" in window)) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    },
    { rootMargin: "-40% 0px -55% 0px", threshold: 0 }
  );

  sections.forEach((section) => observer.observe(section));

  links.forEach((link) => {
    link.addEventListener("click", (e) => {
      const target = document.querySelector(link.getAttribute("href"));
      if (!target) return;
      e.preventDefault();
      const subnav = document.querySelector(".page-subnav");
      const offset = (subnav ? subnav.offsetHeight : 0) + 80;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - offset, behavior: "smooth" });
    });
  });
}

/* 3D tilt-on-hover for cards: follows the cursor position within the card
   and tilts it in 3D space. Skipped on touch devices, which have no
   meaningful pointer position to track. */
function initTiltCards() {
  const cards = document.querySelectorAll(".tilt-card");
  if (!cards.length) return;
  if (window.matchMedia("(hover: none)").matches) return;

  const MAX_TILT = 9;

  cards.forEach((card) => {
    card.style.transformStyle = "preserve-3d";

    card.addEventListener("mousemove", (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const rotateY = ((x - rect.width / 2) / (rect.width / 2)) * MAX_TILT;
      const rotateX = -((y - rect.height / 2) / (rect.height / 2)) * MAX_TILT;
      card.style.transition = "transform 0.1s ease-out";
      card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px) scale(1.02)`;
    });

    card.addEventListener("mouseleave", () => {
      card.style.transition = "transform 0.5s var(--ease-pop)";
      card.style.transform = "";
    });
  });
}

/* Products nav dropdown: hover-reveal on desktop, tap-to-expand on mobile
   (the caret toggles the panel without following the link; the link text
   itself still navigates to the Products page). */
function initNavDropdown() {
  const dropdown = document.querySelector(".nav-dropdown");
  const caret = document.querySelector(".nav-caret-btn");
  if (!dropdown || !caret) return;

  caret.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    dropdown.classList.toggle("is-open");
  });

  document.addEventListener("click", (e) => {
    if (!dropdown.contains(e.target)) dropdown.classList.remove("is-open");
  });
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
