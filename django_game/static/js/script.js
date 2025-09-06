// Small helper JS used site-wide (keep minimal)
document.addEventListener("DOMContentLoaded", function () {
  // Example: add a click handler to .game-card for mobile
  document.querySelectorAll(".game-card").forEach(card => {
    card.addEventListener("click", function(e){
      const link = this.querySelector("a");
      if (link) {
        // if click target isn't an anchor, navigate (makes card clickable)
        if (!e.target.closest("a")) {
          window.location = link.href;
        }
      }
    })
  });
});
