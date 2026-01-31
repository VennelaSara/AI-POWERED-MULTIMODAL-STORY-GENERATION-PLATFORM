import { useState } from "react";
import SceneCard from "./SceneCard";
import ProgressBar from "./ProgressBar";

export default function StoryEditor() {
  const [prompt, setPrompt] = useState("");
  const [status, setStatus] = useState("");

  const generate = async () => {
    setStatus("Starting...");
    const res = await fetch("http://localhost:8000/stories/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    const data = await res.json();
    setStatus(`Job started: ${data.job_id}`);
  };

  return (
    <div>
      <h2>Story Editor</h2>
      <textarea onChange={(e) => setPrompt(e.target.value)} />
      <button onClick={generate}>Generate</button>
      <ProgressBar status={status} />
      <SceneCard title="Scene 1" text="Generated scene content..." />
    </div>
  );
}
