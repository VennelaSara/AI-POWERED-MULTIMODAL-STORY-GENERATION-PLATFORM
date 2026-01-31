export default function SceneCard({ title, text }) {
  return (
    <div
      style={{ border: "1px solid #ccc", padding: "10px", marginTop: "10px" }}
    >
      <h4>{title}</h4>
      <p>{text}</p>
    </div>
  );
}
