const gamepads = {};

const gamepadInfo = document.getElementById("gamepad-info");

let loopStarted = false;

window.addEventListener("gamepadconnected", (e) => {
    addGamepad(e.gamepad);
});

window.addEventListener("gamepaddisconnected", (e) => {
    removeGamepad(e.gamepad);
});

function gameLoop() {
    updateStatus();
}

function addGamepad(gamepad) {
    const d = document.createElement("div");
    d.setAttribute("id", `controller${gamepad.index}`);

    const t = document.createElement("h1");
    t.textContent = `gamepad: ${gamepad.id}`;
    d.append(t);

    const b = document.createElement("ul");
    b.className = "buttons";

    gamepad.buttons.forEach((button, i) => {
        const e = document.createElement("li");
        e.className = "button";
        e.textContent = `Button ${i}`;
        b.append(e);
    });

    d.append(b);

    const a = document.createElement("div");
    a.className = "axes";

    gamepad.axes.forEach((axis, i) => {
        const p = document.createElement("progress");
        p.className = "axis";
        p.setAttribute("max", "2");
        p.setAttribute("value", "1");
        p.textContent = i;
        a.append(p);
    });
    d.appendChild(a);

    const start = document.querySelector("#start");

    if (start) {
        start.style.display = "none";
    }

    document.body.append(d);
    if (!loopStarted) {
        requestAnimationFrame(updateStatus);
        loopStarted = true;
    }
}

function removeGamepad(gamepad) {
    document.querySelector(`#controller${gamepad.index}`).remove();
}


function updateStatus() {
  for (const gamepad of navigator.getGamepads()) {
    if (!gamepad) continue;

    const d = document.getElementById(`controller${gamepad.index}`);
    const buttonElements = d.getElementsByClassName("button");

    for (const [i, button] of gamepad.buttons.entries()) {
      const el = buttonElements[i];

      const pct = `${Math.round(button.value * 100)}%`;
      el.style.backgroundSize = `${pct} ${pct}`;
      if (button.pressed) {
        el.textContent = `Button ${i} [PRESSED]`;
        el.style.color = "#42f593";
        el.className = "button pressed";
      } else {
        el.textContent = `Button ${i}`;
        el.style.color = "#2e2d33";
        el.className = "button";
      }
    }

      gamepad.buttons.forEach((button, index) => {
          if (button.pressed) {
              console.log('Button '+index+' is pressed');
              
          }
      });

    const axisElements = d.getElementsByClassName("axis");
    for (const [i, axis] of gamepad.axes.entries()) {
      const el = axisElements[i];
      el.textContent = `${i}: ${axis.toFixed(4)}`;
      el.setAttribute("value", axis + 1);
    }
  }

  requestAnimationFrame(updateStatus);
}


