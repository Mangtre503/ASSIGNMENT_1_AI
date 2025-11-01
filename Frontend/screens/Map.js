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

    this.tileSize = 70;
    this.loadImages().then(() => this.draw());
  }

  async loadImages() {
    window;
    const imagePaths = {
      "#": `${window.location.origin}/ASSIGNMENT_1_AI/Frontend/Images/assets/WallRound_Black.png`, // tường
      ".": `${window.location.origin}/ASSIGNMENT_1_AI/Frontend/Images/assets/EndPoint_Yellow.png`, // đích
      $: `${window.location.origin}/ASSIGNMENT_1_AI/Frontend/Images/assets/CrateDark_Red.png`, // thùng
      "*": `${window.location.origin}/ASSIGNMENT_1_AI/Frontend/Images/assets/Crate_Yellow.png`, // thùng ở đích
      " ": `${window.location.origin}/ASSIGNMENT_1_AI/Frontend/Images/assets/GroundGravel_Concrete.png`, // sàn
      "@": `${window.location.origin}/ASSIGNMENT_1_AI/Frontend/Images/assets/Character4.png`, // player
      "+": `${window.location.origin}/ASSIGNMENT_1_AI/Frontend/Images/assets/Character4.png`, // play on goal
    };

    // Linux
    // const imagePaths = {
    //   "#": `${window.location.origin}/Frontend/Images/assets/WallRound_Black.png`, // tường
    //   ".": `${window.location.origin}/Frontend/Images/assets/EndPoint_Yellow.png`, // đích
    //   $: `${window.location.origin}/Frontend/Images/assets/CrateDark_Red.png`, // thùng
    //   "*": `${window.location.origin}/Frontend/Images/assets/Crate_Yellow.png`, // thùng ở đích
    //   " ": `${window.location.origin}/Frontend/Images/assets/GroundGravel_Concrete.png`, // sàn
    //   "@": `${window.location.origin}/Frontend/Images/assets/Character4.png`, // player
    //   "+": `${window.location.origin}/Frontend/Images/assets/Character4.png`, // play on goal
    // };
    const loadImage = (src) =>
      new Promise((resolve) => {
        const img = new Image();
        img.src = src;
        img.onload = () => resolve(img);
      });

    this.images = {};
    for (const [key, path] of Object.entries(imagePaths)) {
      this.images[key] = await loadImage(path);
    }
  }

  draw() {
    if (!this.ctx || !this.images[" "]) return;

    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    for (let r = 0; r < this.map.length; r++) {
      for (let c = 0; c < this.map[r].length; c++) {
        const tile = this.map[r][c];
        const floor = this.images[" "]; // nền mặc định
        const img = this.images[tile] || floor;

        // Vẽ nền trước
        this.ctx.drawImage(
          floor,
          c * this.tileSize,
          r * this.tileSize,
          this.tileSize,
          this.tileSize
        );

        // Vẽ vật thể (nếu không phải nền trống)
        if (tile !== " ") {
          this.ctx.drawImage(
            img,
            c * this.tileSize,
            r * this.tileSize,
            this.tileSize,
            this.tileSize
          );
        }
      }
    }
  }

  render(container) {
    this.container = container;
    container.innerHTML = `
      <div class="control-panel">
        <button id="btnBack">BACK</button>
        <select id="algorithmSelect">
          <option value="BlindSearch">Blind Search</option>
          <option value="Heuristic">Heuristic</option>
        </select>
        <button id="btnLoadSolution">Load Solutions Before Start</button>
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
    this.tileSize = 70;

    this.canvas.width = this.map[0].length * this.tileSize;
    this.canvas.height = this.map.length * this.tileSize;

    this.draw();
    this.findPlayer();
  }
  async loadSolution() {
    const algo = document.getElementById("algorithmSelect").value;
    // window
    const path = `${window.location.origin}/ASSIGNMENT_1_AI/Backend/${algo}/solutions/${value}_testcase_${this.level}.txt`;
    //linux
    // const path = `${window.location.origin}/Backend/solutions/${algo}_testcase_${this.level}.txt`;

    try {
      const res = await fetch(path);
      if (!res.ok) {
        throw new Error(
          `Không tìm thấy file solution, vui lòng chạy Backend/index để lưu kết quả trước khi thử nghiệm`
        );
      }

      const text = await res.text();

      this.solution = text.trim().replace(";", "");
      this.moveIndex = -1;

      console.log("Loaded solution:", this.solution);

      document.getElementById("btnNext").disabled = false;
      document.getElementById("btnPrev").disabled = false;

      alert("Tải solution thành công!");
      this.map = JSON.parse(JSON.stringify(this.originalMap));
      this.history = [];
      this.findPlayer();
      this.draw();
    } catch (err) {
      console.error(err);
      alert(
        "Không tìm thấy file solution, vui lòng chạy Backend/index để lưu kết quả trước khi thử nghiệm"
      );
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
    } else {
      alert("Giải hết! Quay lại menu để chọn level mới!");
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

      const isGoalNext =
        (this.originalMap[behindR][behindC] === ".") |
        (this.originalMap[behindR][behindC] === "*");
      const boxOnGoalOld = target === "*";

      this.map[nr][nc] = this.originalMap[nr][nc];

      this.map[behindR][behindC] = isGoalNext ? "*" : "$";
    }

    const wasGoal =
      (this.originalMap[this.player.r][this.player.c] === ".") |
      (this.originalMap[this.player.r][this.player.c] === "*");
    this.map[this.player.r][this.player.c] = wasGoal ? "." : " ";

    const isGoalStep =
      this.originalMap[nr][nc] === "." || this.originalMap[nr][nc] === "*";
    this.map[nr][nc] = isGoalStep ? "+" : "@";

    this.player = { r: nr, c: nc };
    this.draw();
  }
}
