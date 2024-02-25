<template>
    <div>
      <canvas ref="bjsCanvas" width="500" height="500" />
    </div>
  </template>
  
  <script>
  import { createScene } from "../components/MyFirstScene";
  
  export default {
    name: "BabylonScene",
  
    mounted() {
      const bjsCanvas = this.$refs.bjsCanvas;
      if (bjsCanvas) {
        const fpsCallback = (fps) => {
          this.$emit("fps", fps);
        };
        createScene(bjsCanvas, fpsCallback);
      }
    },
  };
  </script>
  