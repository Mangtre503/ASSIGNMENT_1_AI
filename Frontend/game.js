const app = document.getElementById("app");

function showMenu() {
  const menu = new MenuScreen((level) => loadLevel(level));
  menu.render(app);
}
async function loadLevel(level) {
  const res = await fetch(
    `${window.location.origin}/ASSIGNMENT_1_AI/SokobanMap/mini_cosmos_${level}.txt`
  );
  // Linux
  // const res = await fetch(
  //   `${window.location.origin}/SokobanMap/mini_cosmos_${level}.txt`
  // );
  const mapData = JSON.parse(await res.text());

  const game = new GameScreen(mapData, level, () => showMenu());
  game.render(app);
}

showMenu();
