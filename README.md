# Samsung RISC-V Talent Development Program

## Basic Details 

**Name:**  Muragharajendra S Padasalagi  
**College:** New Horizon college of Engineering  
**Email:** muragharajendra@gmail.com  
**GitHub Profile:** [Muragharajendra](https://github.com/Murghu)  
**LinkedIn Profile:** [Muragharajendra-S-P](https://www.linkedin.com/in/muragharajendra-s-p-230694278/)  

----

## Tasks

### [Task 1: Environment setup and comparing RISC-V compiler with gcc compiler](https://github.com/Murghu/samsung-riscv/tree/main/Task%201)
**Description:** Refer to C-based and RISC-V-based lab videos to:

- Compile C code using `gcc`.
- Compile and count the number of instructions used in `o1` and `ofast` using the RISC-V compiler.

### [Task 2: Analyzing RISC-V Performance with Compiler Optimization Flags (-O1 and -Ofast)](https://github.com/Murghu/samsung-riscv/tree/main/Task%202)
**Description:** In this task, you will explore the compilation process for both standard C and RISC-V architecture:

- Compile a simple C program using the `gcc` compiler.
- Use the RISC-V compiler to compile the same code with optimization flags `-O1` and `-Ofast`.
- Count and compare the number of instructions generated for each optimization level, understanding the impact of compiler optimizations on RISC-V assembly code.

### [Task 3: Decoding and Analyzing RISC-V Instruction Types and 32-Bit Patterns](https://github.com/Murghu/samsung-riscv/tree/main/Task%203)  
**Description:** In this task, you will analyze and decode RISC-V assembly instructions using instruction type formats.

A. **Review RISC-V Instruction Formats:**  
   - Studying the official RISC-V software documentation to understand the following instruction types:  
     - **R-type**  
     - **I-type**  
     - **S-type**  
     - **B-type**  
     - **U-type**  
     - **J-type**  

B. **Analyze Application Code:**  
   - Use the `riscv-objdump` tool to analyze your application code.  
   - Identify 15 unique RISC-V instructions from the disassembled output.

### [Task 4: Functional Simulation of RISC-V Core](https://github.com/Murghu/samsung-riscv/tree/main/Task%204) 

**Description**:  
This task involves performing a functional simulation of a given RISC-V Core Verilog netlist and testbench to verify the core's functional correctness and document the results.

 **Objectives**  
- Simulate the RISC-V Core using the provided Verilog netlist and testbench.  
- Verify the functional correctness by analyzing the output signals.  
- Document the results with waveform snapshots and upload them to GitHub.  

#### Steps  

 **1. Download Files**  
 **2. Set Up Simulation Environment**  
 **3. Run Functional Simulation**  
 **4. Capture Waveforms**  
**5. Documentation to repository**  

###  [Task 5: Smart Elevator Controller Using VSDsquadron Mini](https://github.com/Murghu/samsung-riscv/tree/main/Task%205) 

## Overview
The Smart Elevator Controller is an embedded system using the VSDsquadron Mini board to efficiently manage elevator operations. It integrates a 16x2 LCD with I2C, a 4x4 keypad, and push buttons for user input and real-time status display. This project demonstrates the automation potential of RISC-V-based controllers in embedded applications.

## Key Features
-LCD Display for real-time floor and status updates
-4x4 Keypad for floor selection
-Push Buttons for manual control
-I2C Communication for efficient LCD interfacing
-Embedded C Programming for scalable implementation

## Objectives
-Develop an elevator control system using VSDsquadron Mini
-Interface an I2C LCD for status display
-Implement a keypad-based floor selection system
-Ensure smooth elevator movement between floors
-Demonstrate RISC-V-based real-time automation

## Elevator Working Process

**Initialization:** The elevator is initialized at floor 0, with no target and in an IDLE state.

**Request Handling:** A request is made to move to floor 5.The target floor is set to 5.The direction is set to UP because the current floor (0) is less than the target floor (5).

**Movement:**  The elevator moves floor by floor:The direction is UP, so the elevator increments the current floor by 1 in each iteration.
After each move, the current floor is printed.

**Reaching the Target:** When the elevator reaches floor 5:
The direction is set to IDLE.
The request is cleared.
The final message is printed indicating that the elevator has reached the target floor.
This simple model effectively demonstrates the fundamental logic behind an elevator controller.

