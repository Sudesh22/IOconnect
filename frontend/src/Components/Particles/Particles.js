import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";

const Particle = function () {
  const particlesInit = async (main) => {
    await loadFull(main);
  };
  const particlesLoaded = (container) => {};
  const ParticleOptions = {
    background: {
      //   color: {
      //     value: "0d47a1",
      //   },
    },
    fullScreen: {
      enable: true,
      zIndex: -1,
    },
    fpsLimit: 300,
    interactivity: {
      events: {
        onClick: {
          enable: false,
          mode: "push",
        },
        onHover: {
          enable: false,
          mode: "repulse",
        },
        resize: true,
      },
      modes: {
        push: {
          quantity: 4,
        },
        repulse: {
          distance: 200,
          duration: 0.4,
        },
      },
    },
    particles: {
      color: {
        value: "#212121",
      },
      links: {
        color: "#212121",
        distance: 150,
        enable: true,
        opacity: 0.5,
        width: 1,
      },
      collisions: {
        enable: true,
      },
      move: {
        direction: "none",
        enable: true,
        outModes: {
          default: "bounce",
        },
        random: false,
        speed: 1,
        straight: false,
      },
      number: {
        density: {
          enable: true,
          area: 600,
        },
        value: 80,
      },
      opacity: {
        value: 0.2,
      },
      shape: {
        type: "circle",
      },
      size: {
        value: { min: 1, max: 5 },
      },
    },
    detectRetina: true,
  };
  return (
    <Particles
      id="tsparticles"
      init={particlesInit}
      loaded={particlesLoaded}
      options={ParticleOptions}
    />
  );
};
export default Particle;
