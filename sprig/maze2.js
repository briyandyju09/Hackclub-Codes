const player = "p";
const wall = "w";
const treasure = "t";
const trap = "x";

// Define the sprites
setLegend(
  [player, bitmap`
................
................
................
.....333333.....
....33333333....
...3333333333...
..333333333333..
..333333333333..
..333333333333..
..333333333333..
..333333333333..
...3333333333...
....33333333....
.....333333.....
................
................`],
  [wall, bitmap`
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111`],
  [treasure, bitmap`
................
................
................
......6666......
....66666666....
...6666666666...
..666666666666..
..666666666666..
..666666666666..
..666666666666..
..666666666666..
...6666666666...
....66666666....
......6666......
................
................`],
  [trap, bitmap`
................
................
......4444......
.....444444.....
....44444444....
...4444444444...
..444444444444..
..444444444444..
..444444444444..
..444444444444..
...4444444444...
....44444444....
.....444444.....
......4444......
................
................`]
);

// Set the level map
const level = map`
wwwwwwwwwwwwwwwwww
w......t.........w
w..wwwww...w.....w
w..w...w...w..x..w
w..w.w.w...w.....w
w..w.w.w..t......w
w..w.w.w...wwww..w
w..w.w.w....t....w
w..w.w.w....w....w
w..w.w.wwwww...x.w
w..w.w.w........tw
w..w.w.w........tw
w..w.w.w........tw
w..w.w.wwwwwwwwwww
w..w.w.........t.w
w..w.wwwwwwwww...w
w..........w.....w
w..........w.....w
w....x.....w.....w
wwwwwwwwwwwwwwwwww`;

// Initialize the map and set solids
setMap(level);
setSolids([player, wall]);

// Player movement
onInput("w", () => {
  getFirst(player).y -= 1;
});

onInput("a", () => {
  getFirst(player).x -= 1;
});

onInput("s", () => {
  getFirst(player).y += 1;
});

onInput("d", () => {
  getFirst(player).x += 1;
});

// Check for treasure collection and trap detection
afterInput(() => {
  const playerSprite = getFirst(player);

  // Check for treasures
  const treasures = getTile(playerSprite.x, playerSprite.y).filter(sprite => sprite.type === treasure);
  treasures.forEach(t => t.remove());

  // Check for traps
  const traps = getTile(playerSprite.x, playerSprite.y).filter(sprite => sprite.type === trap);
  if (traps.length > 0) {
    addText("Game Over!", { x: 5, y: 5, color: color`3` });
  }

  // Check if all treasures are collected
  if (getAll(treasure).length === 0) {
    addText("You Win!", { x: 5, y: 5, color: color`3` });
  }
});

// Place the player at the start
addSprite(1, 1, player);
