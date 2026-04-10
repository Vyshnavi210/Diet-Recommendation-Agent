# Diet Recommendation Agent (Groq + LangChain)

## Project Overview
The Diet Recommendation Agent is an AI-based health assistant that generates a personalized vegetarian diet plan based on the user's health details. The system calculates BMI and daily calorie requirements and then uses a Large Language Model (LLM) from Groq with LangChain to generate a diet plan.

This project demonstrates the use of Agentic AI with external calculations and LLM reasoning.

---

## Features
- Accepts user health inputs (Age, Weight, Height)
- Calculates Body Mass Index (BMI)
- Calculates Estimated Daily Calorie Requirements
- Uses Groq LLM (LLaMA 3.1) to generate a personalized diet plan
- Provides a vegetarian weight-loss diet recommendation

---

## Technologies Used
- Python
- LangChain
- Groq LLM (LLaMA 3.1)
- Basic Health Calculations (BMI & BMR)

---

## Project Structure

```
diet-agent/
│
├── diet_agent.py      # Main Python program
├── README.md          # Project documentation
```

---

## Prerequisites

Make sure the following are installed:

- Python 3.8 or above
- pip package manager
- Groq API Key

You can get the Groq API key from:
https://console.groq.com/

---

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/diet-agent.git
cd diet-agent
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate the environment:

Windows:
```bash
venv\Scripts\activate
```

Linux / Mac:
```bash
source venv/bin/activate
```

### Step 3: Install Required Libraries

```bash
pip install langchain-groq
```

or install from requirements file:

```bash
pip install -r requirements.txt
```

---

## Add Your Groq API Key

Inside the Python file add your API key:

```python
os.environ["GROQ_API_KEY"] = "your_api_key_here"
```

---

## How to Run the Project

Run the Python file:

```bash
python diet_agent.py
```

The program will ask for:

- Age
- Weight
- Height

Example:

```
Enter your age: 21
Enter your weight (kg): 65
Enter your height (cm): 170
```

---

## Output Example

The system will display:

- BMI value
- Daily calorie requirement
- AI-generated vegetarian diet plan

Example Output:

```
----- HEALTH ANALYSIS -----
BMI: 22.49
Estimated Daily Calories: 1625

FINAL DIET RECOMMENDATION

Breakfast:
Oatmeal with fruits and nuts

Lunch:
Brown rice with vegetable curry and salad

Dinner:
Whole wheat roti with dal and vegetables

Snacks:
Fruits, yogurt, nuts
```

---

## BMI Formula Used

```
BMI = Weight (kg) / Height² (m²)
```

---

## Calorie Estimation Formula

The project uses a simplified BMR calculation:

```
Calories = 10 × Weight + 6.25 × Height − 5 × Age + 5
```

---

## Future Improvements

- Add non-vegetarian diet options
- Include exercise recommendations
- Add graphical UI
- Integrate database for user history
- Deploy as a web application

---

## Author

Name: Vishnavi  
Course: B.Tech CSE  
University: GITAM University Bangalore  

Project: Agentic AI Mini Project (Groq + LangChain)

---
