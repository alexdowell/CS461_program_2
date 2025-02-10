# CS461_program_2
# Class Scheduling Genetic Algorithm

## Overview
This script implements a **Genetic Algorithm (GA)** to optimize a university course schedule. It assigns:

- **Time slots**  
- **Rooms** (with capacities)  
- **Instructors**  

…all in a way that aims to maximize constraints such as:
- Avoiding double-booking rooms or instructors
- Matching preferred vs. acceptable instructors
- Balancing enrollment with room capacity
- Spacing course sections logically

## Features
1. **Chromosome Representation**  
   Each chromosome is a list of course assignments (genes). Each gene holds:  
   - `name`, `time`, `room`, `room_capacity`, `instructor`, `expected_enrollment`  
   - `preferred_instructors`, `other_instructors`, `remaining_instructors`

2. **Fitness Function**  
   Assigns a **fitness score** based on whether constraints are met (room capacity, instructor load, time conflicts, spacing between sections, etc.).

3. **Selection, Crossover, and Mutation**  
   - **Tournament selection** picks parent chromosomes based on fitness-proportional probabilities.  
   - **Single-point crossover** swaps a segment of genes between parents.  
   - **Mutation** randomly changes time slots, rooms, or instructors with a small probability.

4. **Tracking Best Solutions**  
   - Prints the **best chromosome’s** (schedule’s) fitness score each generation.  
   - Displays the final best schedule in a table, showing course, time, room, and instructor.

## Requirements
- **Python 3**
- **NumPy**
- **tabulate** (for formatted table output)
- **datetime**, **random**, **math**, **statistics** (standard Python libraries)

If needed, install missing packages:
pip install numpy tabulate

## Usage
1. **Clone or download** this script to your local system.
2. **Install dependencies** (see above).
3. **Run** the script:
   python your_script_name.py
4. **Check** the console for:
   - **Generation-by-generation** updates (best and average fitness).
   - The **final best schedule** (table) and overall **fitness score**.

## How It Works
1. **Population Initialization**  
   - Creates a population of random schedules (chromosomes).

2. **Fitness Evaluation**  
   - Each schedule is scored based on constraints in `fitness_function`.

3. **Selection**  
   - Uses **softmax** probabilities and **tournament selection** to choose parents.

4. **Crossover & Mutation**  
   - **Single-point crossover** to produce child schedules.  
   - Random **mutation** of a gene’s time slot, room, or instructor.

5. **Iterations**  
   - Repeats the process for a defined number of **generations**.  
   - Monitors **best** and **average** fitness in each generation.

6. **Final Output**  
   - At the end, it prints the **best schedule** (highest fitness).  
   - Shows each course’s **time**, **room**, and **instructor** in a **tabulated** format.

## Example Output
During execution, you might see lines like:
gen:  1   best:  -2.0   average:  -4.1234   percent gain in averages:  10.0 %
gen:  2   best:  -1.5   average:  -3.9475   percent gain in averages:  4.5 %
...

Then, once finished:
schedule fitness score:  3.4
+----------+--------+-----------------+-----------------+
| course   | time   | building/room   | instructor      |
+----------+--------+-----------------+-----------------+
| CS101A   | 10 AM  | Haag 201        | Gharibi         |
| CS101B   | 11 AM  | Royall 206      | Shah            |
...

## License
This project is open-source, intended for educational and research purposes.
