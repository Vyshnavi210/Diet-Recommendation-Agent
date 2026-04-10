import os
from langchain_groq import ChatGroq

# -----------------------------
# Add your Groq API Key
# -----------------------------
os.environ["GROQ_API_KEY"] = "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"

# -----------------------------
# Take User Input
# -----------------------------
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))

# -----------------------------
# BMI Calculation (Tool Logic)
# -----------------------------
height_m = height / 100
bmi = weight / (height_m ** 2)

# -----------------------------
# BMR Calorie Calculation
# -----------------------------
calories = 10 * weight + 6.25 * height - 5 * age + 5

print("\n----- HEALTH ANALYSIS -----")
print(f"BMI: {round(bmi,2)}")
print(f"Estimated Daily Calories: {round(calories,2)}")

# -----------------------------
# Initialize Groq LLM
# -----------------------------
llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

# -----------------------------
# Prompt for Diet Plan
# -----------------------------
prompt = f"""
You are a professional nutritionist.

User details:
Age: {age}
Weight: {weight} kg
Height: {height} cm
BMI: {round(bmi,2)}
Daily calories needed: {round(calories,2)}

Create a healthy vegetarian diet plan for weight loss.

Provide:

Breakfast
Lunch
Dinner
Snacks
"""

response = llm.invoke(prompt)

print("\n==============================")
print(" FINAL DIET RECOMMENDATION")
print("==============================\n")

print(response.content)