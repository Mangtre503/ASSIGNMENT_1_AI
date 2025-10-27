class MenuScreen {
  constructor(onLevelSelect) {
    this.onLevelSelect = onLevelSelect;
  }

  render(container) {
    container.innerHTML = `
      <div class="levelSelect">
        <h1>SELECT LEVEL</h1>
        <div class="levels-grid"></div>
      </div>
    `;

    const grid = container.querySelector(".levels-grid");

    for (let i = 1; i <= 20; i++) {
      const btn = document.createElement("button");
      btn.classList.add("level-button");
      btn.textContent = i;

      btn.addEventListener("click", () => this.onLevelSelect(i));
      grid.appendChild(btn);
    }
  }
}
