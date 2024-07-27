function drawScaledPattern() {
 const numPoints = bt.randIntInRange(1, 200);
 const radius = 30;
 const rotationSpeed = 2;

 let polylines = [];

 for (let i = 0; i < numPoints; i++) {
  const angle = (i * 2 * Math.PI) / numPoints;
  const x = 55 + radius * Math.cos(angle);
  const y = 80 + radius * Math.sin(angle);

  let star = [];
  for (let j = 0; j < 10; j++) {
   const angle2 = (j * 2 * Math.PI) / 10;
   const x2 = x + 12 * Math.cos(angle2);
   const y2 = y + 12 * Math.sin(angle2);
   star.push([x2, y2]);
  }
  polylines.push(star);
 }

 polylines = bt.rotate(polylines, rotationSpeed, [60, 60]);
 drawLines(polylines);
}

drawScaledPattern();
