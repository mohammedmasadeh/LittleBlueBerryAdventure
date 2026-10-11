from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = """<!DOCTYPE html>
<html>
<body style="margin:0; background:#111; color:white; font-family:sans-serif">
<p style="padding:10px">Click the game, then use W A S D to move the blue square.</p>
<canvas id="game" width="600" height="400" style="background:#222"></canvas>
<script>
const c = document.getElementById("game");
const ctx = c.getContext("2d");
let x = 275, y = 175;
const size = 50, speed = 4;
const keys = {};

addEventListener("keydown", e => keys[e.key.toLowerCase()] = true);
addEventListener("keyup", e => keys[e.key.toLowerCase()] = false);

function loop() {
  if (keys.w) y -= speed;
  if (keys.s) y += speed;
  if (keys.a) x -= speed;
  if (keys.d) x += speed;

  x = Math.max(0, Math.min(c.width - size, x));
  y = Math.max(0, Math.min(c.height - size, y));

  ctx.clearRect(0, 0, c.width, c.height);
  ctx.fillStyle = "blue";
  ctx.fillRect(x, y, size, size);
  requestAnimationFrame(loop);
}
loop();
</script>
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(PAGE.encode())

    def log_message(self, *args):
        pass


print("Game running! Click 'Open in Browser' in the popup,")
print("or open the PORTS tab at the bottom and click the link for port 8000.")
print("Press Ctrl+C here to stop.")
HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()