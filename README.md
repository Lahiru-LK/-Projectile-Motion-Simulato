# 🚀 Projectile Motion Simulator 💻


This repository contains the **Projectile Simulator** 🖥️, a Python application built using the Pygame library. The simulator demonstrates the physics of projectile motion by allowing users to input various parameters like velocity, angle, mass, gravity, air resistance, and more. The motion is then visualized along with calculated values like maximum height and horizontal distance.

---
https://github.com/user-attachments/assets/c6e4727f-2bfb-435f-9263-7787ca7ad57e

## Features ✨

1. **Interactive UI**:
   - Input parameters like velocity, angle, mass, air resistance, gravity, radius, and air density. 🎛️
   - Buttons to Start, Pause, and Reset the simulation. ▶️⏸️🔄

2. **Visualization**:
   - Displays the projectile's motion trajectory in real-time. 📈
   - Plots the path of the projectile based on user inputs. 🖌️

3. **Physics Integration**:
   - Simulates realistic physics, including drag, air resistance, and gravity. 🌍
   - Calculates and displays important metrics like maximum vertical height and horizontal distance. 📊

4. **Dynamic Control**:
   - Pause and reset the simulation at any time. ⏯️

---

## How It Works 🛠️

1. The user inputs the parameters (e.g., velocity, angle, mass, etc.) into the UI. 📝
2. When the "Start" button is clicked, the simulation begins based on the provided inputs. ▶️
3. The motion of the projectile is calculated using physics equations, and the results are visualized on the screen. 🔍
4. Key results like max height and horizontal distance are displayed on the right. 📐

---

## Libraries Required 📚

To run this application, you need the following libraries installed:

1. **pygame** - For rendering graphics and handling input. 🎮

You can install Pygame by running:

```bash
pip install pygame
```

---

## How to Run 🚦

1. Clone this repository or download the project files. 📂

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project folder. 📁

   ```bash
   cd <project_folder>
   ```

3. Ensure you have Python and Pygame installed. ✅

4. Run the `main.py` file:

   ```bash
   python main.py
   ```

5. The simulator window will open. Input your parameters, then click "Start" to begin the simulation. 🏁

---

## Why This Project? 🤔

The **Projectile Simulator** is designed as an educational tool to demonstrate the principles of projectile motion in physics. 🧪 It helps visualize how different parameters like velocity, angle, and air resistance affect the motion of a projectile.

---

## Code Structure 🗂️

1. **`main.py`**:
   - The entry point of the application. 🚪
   - Initializes the main loop and handles user interaction. 💻

2. **Classes**:
   - `UI`: Handles the graphical user interface and input fields. 🎨
   - `INPUTS`: Manages user input for parameters like velocity and angle. 📝
   - `RENDERER`: Responsible for drawing the projectile and displaying equations. 🖌️
   - `PHYSICSENGINE`: Implements the physics calculations for the projectile motion. ⚙️

3. **Constants**:
   - Predefined values like window size, colors, and frame rate. 📏

---

## Example Simulation 🧮

### Input Parameters
- Velocity: 35 m/s 🏃
- Angle: 45 degrees 📐
- Mass: 5 kg ⚖️
- Air Resistance: 0.3 🌫️
- Gravity: 9.8 m/s² 🌍
- Radius: 1 m 🔵
- Air Density: 1.22 kg/m³ 💨

### Results 🏆
- Max Vertical Height: ~60.81 m 📏
- Horizontal Distance: ~135.74 m 🛤️

---

## Use Cases 💡

- **Education**: Visualizing projectile motion in physics classes. 🧑‍🏫
- **Experimentation**: Testing how various factors (e.g., air resistance, angle) affect motion. 🔬
- **Game Development**: Inspiration for implementing projectile motion in games. 🎮

---

## Future Improvements 🚀

- Add 3D simulation capabilities. 🖼️
- Include wind direction and speed effects. 🌬️
- Enhance the UI for better user experience. 🎨

---

## Contributions 🤝

Feel free to fork this project, make improvements, and submit a pull request. Contributions are welcome! 🌟

---

## License 📜

This project is licensed under the MIT License. See the LICENSE file for more details. 📄
