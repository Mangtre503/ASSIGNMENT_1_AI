class GameScreen {
  constructor(mapData, level, onBack) {
    this.map = mapData;
    this.level = level;
    this.onBack = onBack;
    this.solution = "";
    this.moveIndex = -1;
    this.originalMap = JSON.parse(JSON.stringify(mapData));
    this.map = JSON.parse(JSON.stringify(mapData));
    this.history = [];
  }
  draw() {
    if (!this.ctx) return;

    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    for (let r = 0; r < this.map.length; r++) {
      for (let c = 0; c < this.map[r].length; c++) {
        const tile = this.map[r][c];
        let color = "#ddd"; // default floor

        if (tile === "#") color = "black"; // wall
        if (tile === ".") color = "yellow"; // goal
        if (tile === "$") color = "brown"; // box
        if (tile === "*") color = "orange"; // box on goal
        if (tile === "@") color = "blue"; // player
        if (tile === "+") color = "lightblue"; // player on goal

        this.ctx.fillStyle = color;
        this.ctx.fillRect(
          c * this.tileSize,
          r * this.tileSize,
          this.tileSize,
          this.tileSize
        );

        this.ctx.strokeStyle = "gray";
        this.ctx.strokeRect(
          c * this.tileSize,
          r * this.tileSize,
          this.tileSize,
          this.tileSize
        );
      }
    }
  }

  render(container) {
    this.ontainer = container;
    container.innerHTML = `
      <button id="btnBack">BACK</button>

      <div class="control-panel">
        <select id="algorithmSelect">
          <option value="BlindSearch">Blind Search</option>
          <option value="Heuristic">Heuristic</option>
        </select>
        <button id="btnLoadSolution">Load Solutions</button>
        <button id="btnPrev" disabled>&lt;</button>
        <button id="btnNext" disabled>&gt;</button>
      </div>

      <canvas id="gameCanvas"></canvas>
    `;

    document
      .getElementById("btnBack")
      .addEventListener("click", () => this.onBack());

    document
      .getElementById("btnLoadSolution")
      .addEventListener("click", () => this.loadSolution());

    document
      .getElementById("btnNext")
      .addEventListener("click", () => this.nextMove());

    document
      .getElementById("btnPrev")
      .addEventListener("click", () => this.prevMove());

    this.canvas = document.getElementById("gameCanvas");
    this.ctx = this.canvas.getContext("2d");
    this.tileSize = 50;
    this.tileSize = 50;

    this.canvas.width = this.map[0].length * this.tileSize; // số cột
    this.canvas.height = this.map.length * this.tileSize; // số hàng

    this.draw();
    this.findPlayer();
  }
  async loadSolution() {
    const algo = document.getElementById("algorithmSelect").value;
    const path = `${window.location.origin}/ASSIGNMENT_1_AI/Backend/${algo}/solutions/testcase_${this.level}.txt`;
    try {
      const res = await fetch(path);
      const text = await res.text();

      this.solution = text.trim().replace(";", "");
      this.moveIndex = -1;

      console.log("Loaded solution:", this.solution);

      document.getElementById("btnNext").disabled = false;
      document.getElementById("btnPrev").disabled = false;

      alert("Loaded solution successfully!");

      this.map = JSON.parse(JSON.stringify(this.originalMap));
      this.history = [];
      this.findPlayer();
      this.draw();
    } catch (err) {
      console.error(err);
      alert("Không tải được solution!");
    }
  }
  nextMove() {
    if (this.moveIndex < this.solution.length - 1) {
      this.history.push({
        map: JSON.parse(JSON.stringify(this.map)),
        player: { ...this.player },
      });

      this.moveIndex++;
      this.makeMove(this.solution[this.moveIndex]);
    }
  }

  prevMove() {
    if (this.moveIndex >= 0 && this.history.length > 0) {
      const previous = this.history.pop();

      this.map = JSON.parse(JSON.stringify(previous.map));
      this.player = { ...previous.player };
      this.draw();
      this.moveIndex--;
    }
  }

  findPlayer() {
    for (let r = 0; r < this.map.length; r++) {
      for (let c = 0; c < this.map[r].length; c++) {
        if (this.map[r][c] === "@" || this.map[r][c] === "+") {
          this.player = { r, c };
          return;
        }
      }
    }
  }

  makeMove(d) {
    const dir = { U: [-1, 0], D: [1, 0], L: [0, -1], R: [0, 1] }[d];
    const nr = this.player.r + dir[0];
    const nc = this.player.c + dir[1];

    const target = this.map[nr][nc];

    if (target === "#") return;

    const behindR = nr + dir[0];
    const behindC = nc + dir[1];

    if (target === "$" || target === "*") {
      const nextTarget = this.map[behindR][behindC];
      if (nextTarget === "#" || nextTarget === "$" || nextTarget === "*") {
        return;
      }

      const boxOnGoalOld = target === "*";
      const isGoalNext = this.originalMap[behindR][behindC] === ".";

      this.map[behindR][behindC] = isGoalNext ? "*" : "$";
    }

    const wasGoal = this.originalMap[this.player.r][this.player.c] === ".";
    this.map[this.player.r][this.player.c] = wasGoal ? "." : " ";

    const isGoalStep = this.originalMap[nr][nc] === ".";
    this.map[nr][nc] = isGoalStep ? "+" : "@";

    this.player = { r: nr, c: nc };
    this.draw();
  }
}
