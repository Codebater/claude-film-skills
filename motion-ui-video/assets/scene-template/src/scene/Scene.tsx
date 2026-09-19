import { motion } from "motion/react";

// Every beat lives here, in seconds. Derive all delays from T — never inline
// magic numbers, so re-timing a request ("make it come in later") is one edit.
const T = {
  headline: 0.3,
  sub: 0.9,
};

const enter = (at: number) => ({
  initial: { opacity: 0, y: 24, filter: "blur(8px)" },
  animate: { opacity: 1, y: 0, filter: "blur(0px)" },
  transition: { delay: at, duration: 0.6, ease: [0.22, 1, 0.36, 1] as const },
});

// Placeholder scene — replace entirely per brief.
export default function Scene() {
  return (
    <div className="flex h-full w-full flex-col items-center justify-center gap-4">
      {/* soft stage glow so the scene doesn't float on flat black */}
      <div
        aria-hidden
        className="pointer-events-none absolute left-1/2 top-1/2 h-[60vh] w-[60vw] -translate-x-1/2 -translate-y-1/2 rounded-full opacity-40 blur-3xl"
        style={{ background: "radial-gradient(closest-side, oklch(0.45 0.12 285 / .5), transparent)" }}
      />
      <motion.h1 {...enter(T.headline)} className="relative text-6xl font-semibold tracking-tight">
        Motion scene
      </motion.h1>
      <motion.p {...enter(T.sub)} className="relative text-lg text-muted-foreground">
        Replace me with the real choreography.
      </motion.p>
    </div>
  );
}
