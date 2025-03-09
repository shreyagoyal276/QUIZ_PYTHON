# **Quiz Game (Python CLI) 🎯**

A command-line quiz application that allows users to test their knowledge across different categories, including Science, Technology, General Knowledge, Sports, and Mathematics. The quiz randomly selects questions from a CSV file and provides a scoring system with feedback.

## **Features 🚀**
- 📂 **Loads quiz questions from a CSV file** (`quiz_data.csv`)
- 🎯 **Categories:** Science, Technology, GK, Sports, and Maths
- 🔀 **Randomized question selection**
- ✅ **Scoring system with performance evaluation**
- ➕ **Option to add new questions to the CSV file**
- 🏆 **Final score display with performance remarks**
- 🎮 **Interactive CLI menu for smooth navigation**

---

## **Setup & Installation 🛠️**
1. **Clone the repository**  
   ```sh
   git clone https://github.com/your-username/quiz-game.git
   cd quiz-game
   ```
2. **Ensure Python is installed (>=3.x)**  
   Check your Python version:  
   ```sh
   python --version
   ```
3. **Prepare the quiz data file**  
   - Ensure `quiz_data.csv` exists in the project directory.  
   - Format:  
     ```
     Category,Question,Option1,Option2,Option3,Option4,CorrectOption
     ```
   - Example:
     ```
     Sci,What is the chemical symbol for water?,H2O,CO2,O2,NH3,1
     ```
4. **Run the script**  
   ```sh
   python QUIZ_CODE.py
   ```

---

## **How to Play? 🎮**
1. Run the script and choose an option from the main menu:  
   - `1` **Start Quiz** – Choose a category and answer questions.  
   - `2` **Add Questions** – Add new questions to `quiz_data.csv`.  
   - `3` **Exit** – Quit the game.
2. Answer the multiple-choice questions by selecting the correct option (1/2/3/4).
3. Receive your score and feedback based on performance.

---

## **Code Breakdown 📜**
### **Main Functions**
- `load_ques()`: Loads quiz questions from `quiz_data.csv` and organizes them into categories.
- `display_menu()`: Shows the main menu with options.
- `starting_quiz()`: Displays category choices.
- `quiz(choice, n)`: Runs the quiz, displaying questions and checking answers.
- `score_result(score, n)`: Evaluates and prints performance based on the score.
- `add_ques()`: Allows users to append new questions to `quiz_data.csv`.

---

## **Contributing 🤝**
Contributions are welcome! Feel free to:
- Open issues for bug reports or feature requests.
- Submit pull requests with improvements.

