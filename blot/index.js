function drawScaledPattern() {
  const numPoints = bt.randIntInRange(1, 200);

  for (let i = 0; i < numPoints; i++) {
    const angle = (i * 2 * Math.PI) / numPoints;
    const x = 55 + 30 * Math.cos(angle);
    const y = 80 + 30 * Math.sin(angle);

    const star = [];
    for (let j = 0; j < 10; j++) {
      const angle2 = (j * 2 * Math.PI) / 10;
      star.push([x + 12 * Math.cos(angle2), y + 12 * Math.sin(angle2)]);
    }

    drawLines(bt.rotate([star], 2, [60, 60]));
  }
}

drawScaledPattern();
