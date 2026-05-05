
if (!query || !product) {
  document.getElementById("output").innerHTML = "<p style='color:red'>Please fill in both fields.</p>";
  return;
}

async function analyze() {
  document.getElementById("output").innerHTML = "<p>Analyzing... ⏳</p>";
  const query = document.getElementById("query").value;
  const product = document.getElementById("product").value;

  let html = "<h2>AI Visibility Report</h2>";

  try {
  const res = await fetch(window.location.origin + "/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ query, product_name: product })
  });
  const data = await res.json();
  // your existing code...
} catch (err) {
  document.getElementById("output").innerHTML = "<p style='color:red'>Something went wrong. Please try again.</p>";
}

  const data = await res.json();

  // SCORE
  html += "<h3>Visibility</h3>";
  for (let model in data.score) {
    const s = data.score[model];
    html += `<p><b>${model.toUpperCase()}</b>: ${s.found ? "✅ Rank " + s.rank : "❌ Not Found"}</p>`;
  }

  // COMPETITORS
  html += "<h3>Competitors</h3>";

  let hasResults = false;

  for (let model in data.results) {
    if (data.results[model].length > 0) {
      hasResults = true;

      data.results[model].forEach(item => {
        html += `
          <div style="margin:10px;padding:10px;background:#111;border-radius:8px;">
            <b>${item.name}</b><br>${item.reason}
          </div>
        `;
      });
    }
  }

  if (!hasResults) {
    html += "<p>No AI recommendations found</p>";
  }

  // INSIGHTS
  html += "<h3>Insights</h3>";
  data.insights.forEach(i => {
    html += `<p>⚠️ ${i}</p>`;
  });

  // 🔥 FINAL VERDICT (important)
  html += "<h3>Final Verdict</h3>";

  if (!data.score.gemini.found && !data.score.gpt.found) {
    html += "<p style='color:red'>❌ Your product is invisible in AI recommendations</p>";
  } else {
    html += "<p style='color:green'>✅ Your product appears in AI recommendations</p>";
  }

  document.getElementById("output").innerHTML = html;
}
