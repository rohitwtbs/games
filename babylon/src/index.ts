import * as BABYLON from 'babylonjs';

class FlappyBirdGame {
  private canvas: HTMLCanvasElement;
  private engine: BABYLON.Engine;
  private scene: BABYLON.Scene;
  private camera: BABYLON.FreeCamera;
  private bird: BABYLON.Mesh;
  private ground: BABYLON.Mesh;

  constructor(canvas: HTMLCanvasElement) {
    this.canvas = canvas;
    this.engine = new BABYLON.Engine(this.canvas, true);
    this.createScene();
    this.engine.runRenderLoop(() => this.scene.render());
    window.addEventListener('resize', () => this.engine.resize());
  }

  private createScene(): void {
    this.scene = new BABYLON.Scene(this.engine);

    // Create camera
    this.camera = new BABYLON.FreeCamera('camera', new BABYLON.Vector3(0, 5, -10), this.scene);
    this.camera.setTarget(BABYLON.Vector3.Zero());

    // Create bird
    this.bird = BABYLON.MeshBuilder.CreateBox('bird', { size: 1 }, this.scene);
    this.bird.position.y = 2;

    // Create ground
    this.ground = BABYLON.MeshBuilder.CreateGround('ground', { width: 50, height: 50 }, this.scene);
  }
}

const canvas = document.getElementById('renderCanvas') as HTMLCanvasElement;
const game = new FlappyBirdGame(canvas);
