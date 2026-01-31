const BASE_URL = "http://localhost:8000";

export async function createStory(prompt) {
  const res = await fetch(`${BASE_URL}/api/story/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  return res.json();
}

export async function getJobStatus(taskId) {
  const res = await fetch(`${BASE_URL}/api/jobs/${taskId}`);
  return res.json();
}
