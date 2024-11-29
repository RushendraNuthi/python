# Student Feedback Application

This is a Python-based desktop application for collecting student feedback. It uses the **Tkinter** library for creating the graphical user interface (GUI) and **csv** for storing the feedback data.

## Features

- **Feedback Form**: Collects user name, roll number, and feedback.
- **Submit Feedback**: Saves the feedback to a CSV file named `Response.csv`.
- **Clear Form**: Resets all input fields for new feedback.

---

## Code Overview

### Libraries Used

- **Tkinter**: For creating the GUI.
- **csv.writer**: For appending feedback to a CSV file.
- **tkinter.messagebox**: For showing pop-up messages to confirm actions.

---

### Functions

#### `clear()`
- Clears all the input fields.
- Asks for confirmation before clearing.
- Deletes the text in the name, roll number, and feedback fields.

#### `submit()`
- Saves the data entered in the form to `Response.csv`.
- Data saved includes:
  - Name
  - Roll Number
  - Feedback text
- Shows a confirmation message upon successful submission.
- Resets the input fields after submission.

---

## How to Use

1. **Run the Application**:
   Run the Python script (`main.py`) in an environment with Tkinter installed.

2. **Fill the Form**:
   - Enter your Name.
   - Enter your Roll Number.
   - Provide your feedback in the text area.

3. **Submit Feedback**:
   - Click the "Submit" button to save your feedback.
   - A confirmation pop-up will appear.

4. **Clear Form**:
   - Click the "Clear" button to reset all fields for new feedback.

---

## File Structure

- **`main.py`**: The main script containing the application logic.
- **`Response.csv`**: The file where feedback entries are saved.

---

## Dependencies

- Python 3.x
- Tkinter (comes bundled with Python)
- CSV (comes bundled with Python)
