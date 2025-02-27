[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Uzapeobl)

# README

## Students/Team: 
- Luis Alfonso Agudelo Ramirez
- Julián Lara Aristizabal
## Class: 
- "Lenguajes Formales" SI2002-1 (7308)
## Teacher: 
- Adolfo Andrés Castro Sánchez

## Version 1
- OS: Windows 10
- Programming Lenguage Used: Python 3.12
- Tools used: Visual Studio Code
## Implementation Instructions:
### Previous Requirements:
    - Have Python 3.12 installed in your OS.
    - Have the editor "Visual Studio Code" installed and configured with the Python Extension.
- To run the code, you must first download the textfile "casosDePrueba.txt" found in the Github Repository, this file contains examples of the DFA in the format previously specified in the file containing the assignments instructions. 
- The text file must be downloaded and stored in the same folder where the Python Script is saved, so that Visual Studio nCode can run it with no issues. 

## Algorithm Explanation:
This implementation identifies equivalent states in a Deterministic Finite Automaton (DFA) using a partitioning and refinement approach to simplify its structure.

### 1. Initial State Partitioning
- The set of states is initially divided into two groups:
Accepting states: Those that lead to an acceptance condition.
Non-final states: Those that do not lead to acceptance.
### 2. Group Refinement
- Each state is analyzed based on its transitions, checking which group each transition leads to.
- If states within a group transition to different partitions, the group is subdivided into new sets.
- This process is repeated until no further changes occur in the partitions.
### 3. Identifying Equivalent States
Once the refinement is complete, states that remain in the same partition are considered equivalent.
Equivalent state pairs can then be merged to reduce the number of states in the DFA.
