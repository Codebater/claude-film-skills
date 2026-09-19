import Scene from "./scene/Scene";

// Fixed full-viewport stage. Dark by default — remove `dark` for light scenes.
// Keep overflow hidden: nothing may scroll unless the scene is about scrolling.
export default function App() {
  return (
    <div
      id="stage"
      className="dark relative h-screen w-screen overflow-hidden bg-background text-foreground antialiased"
    >
      <Scene />
    </div>
  );
}
