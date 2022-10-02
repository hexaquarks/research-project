import random
import numpy as np
from enum import Enum

class SimulationType(Enum):
     BROWNIAN = 1
     NANODOMAIN = 2
     HOPDIFFUSION = 3     

PATH = tuple[list[float]]
DPI = 100
RADIUS_PADDING = 10
RADIUS = 250
CORRECTED_CANVAS_RADIUS = RADIUS - RADIUS_PADDING

TIME_PER_FRAME: float = 0.02 # 20 ms
DIFFUSION_SPEED_CORRECTION: int = 35 # arbitrary
MEMBRANE_DIFFUSION_COEFFICIENT: float = 0.1 # micrometer^2 / s
MEMBRANE_DIFFUSION_FACTOR: float = 2 * np.sqrt(MEMBRANE_DIFFUSION_COEFFICIENT * TIME_PER_FRAME)
MEMBRANE_DIFFUSION_FACTOR_CORRECTED: float = MEMBRANE_DIFFUSION_FACTOR * DIFFUSION_SPEED_CORRECTION

class Simulation:
    
    def __init__(self, n: int = 5):
        self.number_of_particles: int = n
        self.particles_location: list[tuple[int, int]] = [] 
        self.paths: list[list[tuple[int, int]]] = []
        
        self.init_particles()
        self.init_paths()
        
    def init_paths(self):
        self.paths.extend([[coordinate] for coordinate in self.particles_location])
            
    def init_particles(self) -> None:
        mem: list[tuple] = []
        
        def get_random_canvas_value(self) -> int:
            return int(random.randint(-(CORRECTED_CANVAS_RADIUS), CORRECTED_CANVAS_RADIUS))
        
        def rec(self, x: int = 0, y: int = 0) -> tuple[int, int]:
            x, y = [get_random_canvas_value(self) for _ in range(2)]
            while (x, y) in mem:
                return rec(self, x, y)
            mem.append((x, y))
            return x,y
        
        self.particles_location.extend([rec(self) for _ in range(5)])
        