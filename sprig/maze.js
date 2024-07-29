const player = "p";
const wall = "w";
const goal = "g";

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
  [goal, bitmap`
................
................
................
................
................
................
.....444444.....
....44444444....
....44444444....
.....444444.....
................
................
................
................
................
................`]
);

// Set the level map
const level = map`
wwwwwwwwww
w........w
w..wwwww.w
w..w...w.w
w..w.w.w.w
w..w.w.w.w
w..w.w.w.w
w..w.w.w.w
w..w.w.w.w
w..w.w.w.w
w..w.w.w.w
w..w.w.w.w
w..w.w...w
w..w.wwwww
w........w
wwwwwwwwgw`;

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

// Check for win condition
afterInput(() => {
  const playerSprite = getFirst(player);
  const goalTile = getTile(playerSprite.x, playerSprite.y).find(sprite => sprite.type === goal);
  if (goalTile) {
    addText("You Win!", { x: 5, y: 5, color: color`3` });
  }
});

// Place the player at the start
addSprite(1, 1, player);
