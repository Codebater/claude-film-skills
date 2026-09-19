import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);

// The recorder waits for this before starting the virtual clock, so
// entrance animations begin exactly at frame 0 with fonts loaded.
document.fonts.ready.then(() => {
  (window as unknown as { __SCENE_READY: boolean }).__SCENE_READY = true;
});
