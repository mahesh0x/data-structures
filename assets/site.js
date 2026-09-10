/* ============================================================
   NeetCode 150 Study Notes — shared behaviour
   nav injection · TOC · python highlighting · copy · theme
   ============================================================ */
(function () {
  "use strict";

  var PAGES = [
    { id: "arrays",    n: "01", title: "Arrays & Hashing",   href: "ArraysHashing/arrays_hashing.html" },
    { id: "twop",      n: "02", title: "Two Pointers",       href: "TwoPointers/two_pointers.html" },
    { id: "window",    n: "03", title: "Sliding Window",     href: "SlidingWindow/sliding_window.html" },
    { id: "stack",     n: "04", title: "Stack",              href: "Stack/stack.html" },
    { id: "bsearch",   n: "05", title: "Binary Search",      href: "BinarySearch/binary_search.html" },
    { id: "linked",    n: "06", title: "Linked Lists",       href: "LinkedList/linked_list.html" },
    { id: "tree",      n: "07", title: "Binary Trees",       href: "Tree/tree.html" },
    { id: "heap",      n: "08", title: "Heap / Priority Q",  href: "Heap/heap.html" },
    { id: "backtrack", n: "09", title: "Backtracking",       href: "Backtracking/backtracking.html" },
    { id: "graphs",    n: "10", title: "Graphs",             href: "Graphs/graphs.html" },
    { id: "advgraphs", n: "11", title: "Advanced Graphs",    href: "AdvancedGraphs/advanced_graphs.html" }
  ];
  var EXTRAS = [
    { id: "sets", n: "★", title: "Mixed Revision Sets", href: "practice_sets.html" }
  ];

  var body = document.body;
  var ROOT = body.getAttribute("data-root") || "";
  if (ROOT && ROOT.slice(-1) !== "/") ROOT += "/";
  var CURRENT = body.getAttribute("data-page") || "";

  /* ---------- theme ---------- */
  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function load(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }

  var saved = load("nc150-theme");
  if (saved === "dark" || saved === "light") {
    document.documentElement.setAttribute("data-theme", saved);
  } else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
    document.documentElement.setAttribute("data-theme", "dark");
  }
  function toggleTheme() {
    var now = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", now);
    store("nc150-theme", now);
    paintThemeBtn();
  }
  function paintThemeBtn() {
    var b = document.getElementById("theme-btn");
    if (b) b.textContent = document.documentElement.getAttribute("data-theme") === "dark" ? "☀ Light" : "☾ Dark";
  }

  /* ---------- sidebar ---------- */
  function buildSidebar() {
    var nav = document.createElement("nav");
    nav.className = "sidebar";
    nav.id = "sidebar";

    var html = '<a class="sidebar-brand" href="' + ROOT + 'index.html">' +
               '<b>NeetCode 150 Notes</b><span>Patterns &amp; templates</span></a>' +
               '<div class="nav-group-label">Topics</div>';
    PAGES.forEach(function (p) {
      html += '<a class="nav-link' + (p.id === CURRENT ? " active" : "") + '" href="' + ROOT + p.href + '">' +
              '<span class="nav-num">' + p.n + '</span><span>' + p.title + '</span></a>';
    });
    html += '<div class="nav-group-label">Revision</div>';
    EXTRAS.forEach(function (p) {
      html += '<a class="nav-link' + (p.id === CURRENT ? " active" : "") + '" href="' + ROOT + p.href + '">' +
              '<span class="nav-num">' + p.n + '</span><span>' + p.title + '</span></a>';
    });
    nav.innerHTML = html;

    var layout = document.querySelector(".layout");
    if (layout) layout.insertBefore(nav, layout.firstChild);
  }

  /* ---------- topbar ---------- */
  function buildTopbar() {
    var bar = document.querySelector(".topbar");
    if (!bar) return;
    var me = PAGES.concat(EXTRAS).filter(function (p) { return p.id === CURRENT; })[0];
    bar.innerHTML =
      '<div class="crumbs">' +
        (CURRENT ? '<a href="' + ROOT + 'index.html">Home</a> &nbsp;/&nbsp; ' + (me ? me.title : "") : "NeetCode 150 — study notes") +
      '</div>' +
      '<div class="topbar-actions">' +
        '<button class="ghost menu-btn" id="menu-btn">☰ Menu</button>' +
        '<button class="ghost" id="theme-btn">☾ Dark</button>' +
      '</div>';
    paintThemeBtn();
    document.getElementById("theme-btn").addEventListener("click", toggleTheme);
    var mb = document.getElementById("menu-btn");
    if (mb) mb.addEventListener("click", function () {
      document.getElementById("sidebar").classList.toggle("open");
    });
    document.addEventListener("click", function (e) {
      var sb = document.getElementById("sidebar");
      if (!sb || !sb.classList.contains("open")) return;
      if (sb.contains(e.target) || e.target.id === "menu-btn") return;
      sb.classList.remove("open");
    });
  }

  /* ---------- table of contents ---------- */
  function slug(s) {
    return s.toLowerCase().replace(/[^\w\s-]/g, "").trim().replace(/\s+/g, "-").slice(0, 60);
  }
  function buildTOC() {
    var holder = document.querySelector(".toc");
    if (!holder) return;
    var heads = document.querySelectorAll(".article h2");
    if (!heads.length) { holder.style.display = "none"; return; }
    var html = '<div class="toc-title">On this page</div><ol>';
    Array.prototype.forEach.call(heads, function (h, i) {
      if (!h.id) h.id = slug(h.textContent) || "section-" + i;
      html += '<li><a href="#' + h.id + '">' + h.textContent + "</a></li>";
    });
    holder.innerHTML = html + "</ol>";
  }

  /* ---------- prev / next ---------- */
  function buildPager() {
    var el = document.querySelector(".pager");
    if (!el) return;
    var all = PAGES.concat(EXTRAS);
    var i = -1;
    all.forEach(function (p, k) { if (p.id === CURRENT) i = k; });
    if (i < 0) return;
    var html = "";
    if (i > 0) {
      html += '<a class="prev" href="' + ROOT + all[i - 1].href + '"><div class="dir">← Previous</div>' +
              '<div class="ttl">' + all[i - 1].title + "</div></a>";
    }
    if (i < all.length - 1) {
      html += '<a class="next" href="' + ROOT + all[i + 1].href + '"><div class="dir">Next →</div>' +
              '<div class="ttl">' + all[i + 1].title + "</div></a>";
    }
    el.innerHTML = html;
  }

  /* ---------- python syntax highlighting ---------- */
  var KW = ("False None True and as assert async await break class continue def del elif else except " +
            "finally for from global if import in is lambda nonlocal not or pass raise return try while with yield")
            .split(" ");
  var BI = ("len range enumerate sorted sort set dict list tuple int str float min max sum abs map filter zip " +
            "print reversed any all divmod ceil deque defaultdict Counter heappush heappop heapify float inf")
            .split(" ");
  var KWSET = {}, BISET = {};
  KW.forEach(function (k) { KWSET[k] = 1; });
  BI.forEach(function (k) { BISET[k] = 1; });

  function esc(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function highlightPython(src) {
    var out = "", i = 0, n = src.length;
    while (i < n) {
      var c = src[i];
      // comment
      if (c === "#") {
        var j = src.indexOf("\n", i); if (j < 0) j = n;
        out += '<span class="tok-com">' + esc(src.slice(i, j)) + "</span>";
        i = j; continue;
      }
      // string
      if (c === '"' || c === "'") {
        var q = c, k = i + 1;
        while (k < n && src[k] !== q) { if (src[k] === "\\") k++; k++; }
        k = Math.min(k + 1, n);
        out += '<span class="tok-str">' + esc(src.slice(i, k)) + "</span>";
        i = k; continue;
      }
      // number
      if (/[0-9]/.test(c) && !/[\w.]/.test(src[i - 1] || " ")) {
        var m = /^[0-9][0-9_.eE+-]*/.exec(src.slice(i))[0];
        out += '<span class="tok-num">' + esc(m) + "</span>";
        i += m.length; continue;
      }
      // identifier
      if (/[A-Za-z_]/.test(c)) {
        var w = /^[A-Za-z_][A-Za-z0-9_]*/.exec(src.slice(i))[0];
        var after = src.slice(i + w.length);
        var prev2 = src.slice(Math.max(0, i - 4), i);
        if (KWSET[w]) out += '<span class="tok-kw">' + w + "</span>";
        else if (/^\s*\(/.test(after) && BISET[w]) out += '<span class="tok-bi">' + w + "</span>";
        else if (/def\s+$/.test(prev2) || /class\s$/.test(src.slice(Math.max(0, i - 6), i))) out += '<span class="tok-fn">' + w + "</span>";
        else if (/^\s*\(/.test(after)) out += '<span class="tok-fn">' + w + "</span>";
        else out += w;
        i += w.length; continue;
      }
      out += esc(c);
      i++;
    }
    return out;
  }

  function decorateCode() {
    Array.prototype.forEach.call(document.querySelectorAll("pre > code"), function (code) {
      var pre = code.parentNode;
      var raw = code.textContent;
      if (!pre.classList.contains("no-hl")) code.innerHTML = highlightPython(raw);

      var wrap = pre.parentNode;
      if (!wrap.classList.contains("code-wrap")) {
        wrap = document.createElement("div");
        wrap.className = "code-wrap";
        pre.parentNode.insertBefore(wrap, pre);
        wrap.appendChild(pre);
      }
      var btn = document.createElement("button");
      btn.className = "copy-btn";
      btn.textContent = "Copy";
      btn.addEventListener("click", function () {
        var done = function () { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = "Copy"; }, 1200); };
        if (navigator.clipboard) { navigator.clipboard.writeText(raw).then(done, function(){}); }
        else {
          var ta = document.createElement("textarea");
          ta.value = raw; document.body.appendChild(ta); ta.select();
          try { document.execCommand("copy"); done(); } catch (e) {}
          document.body.removeChild(ta);
        }
      });
      wrap.appendChild(btn);
    });
  }

  /* ---------- labelled code blocks ---------- */
  function moveLabels() {
    Array.prototype.forEach.call(document.querySelectorAll(".code-label"), function (lbl) {
      var wrap = lbl.nextElementSibling;
      if (wrap && wrap.classList.contains("code-wrap")) {
        wrap.parentNode.insertBefore(lbl, wrap);
      }
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    buildSidebar();
    buildTopbar();
    buildTOC();
    buildPager();
    decorateCode();
    moveLabels();
  });
})();
