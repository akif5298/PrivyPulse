"use client";

import React, { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState<any>(null);

  const submitQuery = async () => {
    const res = await fetch("http://localhost:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <main style={{ padding: 40 }}>
      <h1>PrivyPulse</h1>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a market research question..."
      />

      <button onClick={submitQuery}>Submit</button>

      {result && (
        <div>
          <h3>Result</h3>
          <p>{result.result}</p>
          <small>Agents used: {result.agents_used.join(", ")}</small>
        </div>
      )}
    </main>
  );
}
