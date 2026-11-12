import fs from "node:fs";

const html = fs.readFileSync("football_academy_analytics_demo.html", "utf8");
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];

if (scripts.length !== 1) {
  throw new Error(`Expected one inline script, found ${scripts.length}`);
}

new Function(scripts[0][1]);
console.log("Inline JavaScript syntax is valid.");
