# Copilot Instructions for AI Agents

## Project Overview
This repository contains code projects for coursework and experimentation, organized by semester and topic. The structure is primarily educational, with each folder representing a different subject or assignment.

## Key Directories & Files
- `AI Intro/`, `programering/`, `ur/`: Main folders for different subjects or themes.
- `K6 - DAKI/`, `test/`: Subfolders for specific lessons or exercises.
- Example files: `lektion 6.py`, `opgaver 3. lektion.py`, `housing.py`, `ur- start.py`.

## Patterns & Conventions
- File and folder names may include spaces and special characters (e.g., `#`, `-`). Handle paths carefully in scripts and automation.
- Python scripts are used for exercises and assignments; naming often reflects the lesson or task.
- Data files (e.g., `.csv`) are colocated with scripts for easy access.
- Notebooks (`.ipynb`) are used for interactive lessons and experiments.

## Workflows
- There is no unified build or test system; run scripts directly (e.g., `python "programering/lektion 5 tegne.py"`).
- For Jupyter notebooks, open and run in VS Code or Jupyter Lab.
- No external dependencies are enforced, but some scripts may require standard Python libraries (e.g., `pandas`, `matplotlib`).

## Recommendations for AI Agents
- When generating new files, match the naming and placement conventions seen in each subject folder.
- Avoid introducing frameworks or tools not already present.
- When referencing files, use relative paths and preserve special characters.
- If adding new lessons or exercises, follow the existing folder structure and naming style.
- Document any new workflow or dependency in the relevant folder's README (if present).

## Example: Adding a New Exercise
- Place new Python scripts in the appropriate subject folder.
- Name the file to reflect the lesson or topic (e.g., `lektion 7.py`).
- If using data, place `.csv` files alongside the script.

---
For questions or unclear conventions, review existing files in the relevant folder for examples.
