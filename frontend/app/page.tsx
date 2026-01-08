"use client";

import React, { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const submitQuery = async () => {
    if (!query.trim()) return;
    
    setLoading(true);
    setResult(null);
    
    try {
      const res = await fetch("http://localhost:8000/query/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      setResult(data);
    } catch (error) {
      setResult({
        error: true,
        response: "Failed to connect to backend. Make sure the server is running on http://localhost:8000",
        error_agent: "Network"
      });
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      submitQuery();
    }
  };

  return (
    <main style={{ 
      padding: 40, 
      maxWidth: 1200, 
      margin: "0 auto",
      fontFamily: "system-ui, -apple-system, sans-serif"
    }}>
      <h1 style={{ marginBottom: 10 }}>PrivyPulse</h1>
      <p style={{ color: "#666", marginBottom: 30 }}>
        Privacy-Preserving Market Research Assistant
      </p>

      <div style={{ marginBottom: 20 }}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Ask a market research question... (e.g., 'What are the trends in AI market?')"
          disabled={loading}
          style={{
            width: "100%",
            padding: "12px",
            fontSize: "16px",
            border: "1px solid #ddd",
            borderRadius: "8px",
            marginBottom: "10px"
          }}
        />
        <button 
          onClick={submitQuery}
          disabled={loading || !query.trim()}
          style={{
            padding: "12px 24px",
            fontSize: "16px",
            backgroundColor: loading ? "#ccc" : "#0070f3",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: loading || !query.trim() ? "not-allowed" : "pointer"
          }}
        >
          {loading ? "Processing..." : "Submit Query"}
        </button>
      </div>

      {result && (
        <div style={{ 
          marginTop: 20, 
          padding: 24, 
          border: "1px solid #e0e0e0", 
          borderRadius: 12,
          backgroundColor: "#fafafa"
        }}>
          <h3 style={{ marginTop: 0, marginBottom: 20 }}>Response</h3>
          {result.error ? (
            <div style={{ 
              color: "#d32f2f", 
              padding: 16, 
              backgroundColor: "#ffebee", 
              borderRadius: 8,
              border: "1px solid #ffcdd2"
            }}>
              <p style={{ margin: "0 0 8px 0" }}><strong>Error:</strong> {result.response}</p>
              {result.error_agent && (
                <p style={{ margin: 0, fontSize: "14px" }}>Failed at: <code>{result.error_agent}</code></p>
              )}
            </div>
          ) : (
            <>
              <div style={{ 
                whiteSpace: "pre-wrap", 
                fontFamily: "monospace", 
                fontSize: "14px",
                lineHeight: "1.6",
                padding: 16,
                backgroundColor: "white",
                borderRadius: 8,
                border: "1px solid #e0e0e0",
                maxHeight: "600px",
                overflowY: "auto"
              }}>
                {result.response}
              </div>
              <div style={{ 
                marginTop: 20, 
                padding: 16,
                backgroundColor: "white",
                borderRadius: 8,
                border: "1px solid #e0e0e0",
                fontSize: "13px", 
                color: "#666" 
              }}>
                <h4 style={{ marginTop: 0, marginBottom: 12, color: "#333" }}>Execution Details</h4>
                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: 12 }}>
                  <div>
                    <strong>Agents used:</strong>
                    <div style={{ marginTop: 4 }}>
                      {result.agents_used?.map((agent: string, idx: number) => (
                        <span key={idx} style={{
                          display: "inline-block",
                          margin: "2px 4px 2px 0",
                          padding: "4px 8px",
                          backgroundColor: "#e3f2fd",
                          borderRadius: 4,
                          fontSize: "12px"
                        }}>
                          {agent}
                        </span>
                      ))}
                    </div>
                  </div>
                  {result.task_plan && (
                    <div>
                      <strong>Task focus:</strong>
                      <div style={{ 
                        marginTop: 4,
                        padding: "4px 8px",
                        backgroundColor: "#f3e5f5",
                        borderRadius: 4,
                        display: "inline-block",
                        fontSize: "12px"
                      }}>
                        {result.task_plan.focus?.replace("_", " ")}
                      </div>
                    </div>
                  )}
                  {result.metadata && (
                    <>
                      {result.metadata.validation_passed !== undefined && (
                        <div>
                          <strong>Validation:</strong>
                          <div style={{ 
                            marginTop: 4,
                            color: result.metadata.validation_passed ? "#2e7d32" : "#f57c00",
                            fontWeight: "bold"
                          }}>
                            {result.metadata.validation_passed ? "✓ Passed" : "⚠ Needs improvement"}
                          </div>
                        </div>
                      )}
                      {result.metadata.data_sources && result.metadata.data_sources.length > 0 && (
                        <div>
                          <strong>Data sources:</strong>
                          <div style={{ marginTop: 4 }}>
                            {result.metadata.data_sources.map((source: string, idx: number) => (
                              <span key={idx} style={{
                                display: "inline-block",
                                margin: "2px 4px 2px 0",
                                padding: "4px 8px",
                                backgroundColor: "#e8f5e9",
                                borderRadius: 4,
                                fontSize: "12px"
                              }}>
                                {source}
                              </span>
                            ))}
                          </div>
                        </div>
                      )}
                    </>
                  )}
                </div>
              </div>
            </>
          )}
        </div>
      )}
    </main>
  );
}
