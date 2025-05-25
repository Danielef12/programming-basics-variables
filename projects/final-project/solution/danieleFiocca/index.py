'''Personal diet calculator: a simple tool to calculate your meal plan starting from your daily calorie needs
 '''

print("=" * 60)
print("                PERSONAL DIET CALCULATOR")
print("=" * 60)
print("Welcome in this tool for calculate balance meal plan.")
print("For calculate the plan, please provide the next questions. \n")


# Ask the generality of the user

gender = input("Select your Gender (Male/Female): ").lower()

age = int(input("Insert your age: "))

height = float(input("Insert your height in centimeters: "))

weight = float(input("Insert your weight in kilograms: "))

print("-" * 60)
print("Explane physical-activity")
print("-" * 60)
print("1. SEDENTARY: no sports or physical activity")
print("2. LIGHT: 1 OR 2 days training session in a week")
print("3. MODERATE: 3 days of training sessions in a week")
print("4. HEAVY: 5 or more days of training session in a week\n")

activity = input("Insert your level of physical-activity (sedentary/light/moderate/heavy): ").lower()

if activity == "sedentary":
    activity_val = 1.2
elif activity == "light":
    activity_val = 1.375
elif activity == "moderate":
    activity_val = 1.55
elif activity == "heavy":
    activity_val = 1.9

#Ask the user for any food preferences or restrictions and store them in a text variable.


food_preference = input("Do you have any food preference? Write here separate by comma: ").split(", ")

# for calculate the daily calories we need the basal metabolism

if gender == "male":
    basal = 10 * weight + 6.25 * height - 5 * age + 5
elif gender == "female":
    basal = 10 * weight + 6.25 * height - 5 * age - 161

calories = basal * activity_val

# I divide the calories for all the meals of the day

breakfast_percentage = calories * 0.25
lunch_percentage = calories * 0.35
dinner_percentage = calories * 0.30
snack_percentage = calories * 0.10

# I create a dictionary with foods and their macros
# food are organized in [calories, protein, carbs, fat] in 100g

foods = {
    "oatmeal": [389, 16.9, 66.3, 6.9],
    "milk": [42, 3.4, 5.0, 1.0],
    "banana": [89, 1.1, 22.8, 0.3],
    "almonds": [579, 21.2, 21.6, 49.9],
    "apple": [52, 0.3, 13.8, 0.2],
    "walnuts": [654, 15.2, 13.7, 65.2],
    "rice": [130, 2.7, 28.0, 0.3],
    "chicken breast": [165, 31.0, 0.0, 3.6],
    "broccoli": [34, 2.8, 6.6, 0.4],
    "olive oil": [884, 0.0, 0.0, 100.0],
    "salmon": [208, 20.0, 0.0, 13.0],
    "quinoa": [120, 4.4, 21.3, 1.9],
    "spinach": [23, 2.9, 3.6, 0.4],
    "egg": [155, 13.0, 1.1, 11.0],
    "greek yogurt": [59, 10.0, 3.6, 0.4]
}

# I use a standard balanced menu for all meals

# Breakfast: Oatmeal(40%) + milk(30%) + banana(20%) + almonds(10%)
oatmeal_ratio = 0.4  # percentuale assegnata a quel pasto
oatmeal_calorie_need = breakfast_percentage * oatmeal_ratio
qty_oatmeal = (oatmeal_calorie_need / foods["oatmeal"][0]) * 100 # grams needed 

milk_ratio = 0.3
milk_calorie_need = breakfast_percentage * milk_ratio
qty_milk = (milk_calorie_need / foods["milk"][0]) * 100 

banana_ratio = 0.2
banana_calorie_need = breakfast_percentage * banana_ratio
qty_banana = (banana_calorie_need / foods["banana"][0]) * 100

almonds_ratio = 0.1
almonds_calorie_need = breakfast_percentage * almonds_ratio
qty_almonds = (almonds_calorie_need / foods["almonds"][0]) * 100

# break: Apple(50%) + Walnuts(50%)
apple_ratio = 0.5
apple_calorie_need = snack_percentage * apple_ratio
qty_apple = (apple_calorie_need / foods["apple"][0]) * 100

walnuts_ratio = 0.5
walnuts_calorie_need = snack_percentage * walnuts_ratio
qty_walnuts = (walnuts_calorie_need / foods["walnuts"][0])* 100

# Lunch: Rice(40%) + chicken(35%) + Broccoli(15%) + Olive oil(10%)
rice_ratio = 0.4
rice_calorie_need = lunch_percentage * rice_ratio
qty_rice = (rice_calorie_need / foods["rice"][0]) * 100

chicken_ratio = 0.35
chicken_calorie_need = lunch_percentage * chicken_ratio
qty_chicken = (chicken_calorie_need / foods["chicken breast"][0]) * 100

broccoli_ratio = 0.15
broccoli_calorie_need = lunch_percentage * broccoli_ratio
qty_broccoli = (broccoli_calorie_need / foods["broccoli"][0]) * 100

oil_ratio = 0.1
oil_calorie_need = lunch_percentage * oil_ratio
qty_oil = (oil_calorie_need / foods["olive oil"][0]) * 100

# Dinner: Salmon(35%) + Quinoa(35%) + Spinach(20%) + Olive Oil(10%)
salmon_ratio = 0.35
salmon_calorie_need = dinner_percentage * salmon_ratio
qty_salmon = (salmon_calorie_need / foods["salmon"][0]) * 100

quinoa_ratio = 0.35
quinoa_calorie_nees = dinner_percentage * quinoa_ratio
qty_quinoa = (quinoa_calorie_nees / foods["quinoa"][0]) * 100

spinach_ratio = 0.2
spinach_calorie_need = dinner_percentage * spinach_ratio
qty_spinach = (spinach_calorie_need / foods["spinach"][0]) * 100

oil_ratio = 0.1
oil_calorie_need = dinner_percentage * oil_ratio
qty_oil = (oil_calorie_need / foods["olive oil"][0]) * 100

print("=" * 60)
print("This is your plan of the day based on your data:")
print("=" * 60 )

print("\n--- PERSONAL DATA ---")
print(f"- Gender: {gender}")
print(f"- Age: {age}")
print(f"- Height: {height}cm")
print(f"- Weight: {weight}Kg")
print(f"- Physical-Activities: {activity}\n")

print("--- ANALYSES ---")
print(f"Your daily calorie requirement is: {calories:.0f}Kcal.\n")






print("*" * 60)
print(f"Breakfast {breakfast_percentage:.0f} cal")
print("*" * 60)

print(f"\nOatmeal: {qty_oatmeal:.0f} g")
print(f"Milk: {qty_milk:.0f} g")
print(f"Banana: {qty_banana:.0f} g")
print(f"Almonds: {qty_almonds:.0f} g\n")

breakfast_protein = (foods["oatmeal"][1] * qty_oatmeal / 100) + (foods["milk"][1] * qty_milk / 100) + (foods["banana"][1] * qty_banana /100) + (foods["almonds"][1] * qty_almonds / 100)
breakfast_carbs = (foods["oatmeal"][2] * qty_oatmeal / 100) + (foods["milk"][2] * qty_milk / 100) + (foods["banana"][2] * qty_banana /100) + (foods["almonds"][2] * qty_almonds / 100)
breakfast_fat = (foods["oatmeal"][3] * qty_oatmeal / 100) + (foods["milk"][3] * qty_milk / 100) + (foods["banana"][3] * qty_banana /100) + (foods["almonds"][3] * qty_almonds / 100)
print(f"Total breakfast macros: protein {breakfast_protein:.0f}g | carbs {breakfast_carbs:.0f}g | fat {breakfast_fat:.0f}g\n")

print("*" * 60)
print(f"Snak {snack_percentage:.0f} cal")
print("*" * 60)

print(f"\nApple: {qty_apple:.0f} g")
print(f"Walnuts: {qty_walnuts:.0f} g\n")
snak_protein = (foods["apple"][1] * qty_apple / 100) + (foods["walnuts"][1] * qty_walnuts / 100)
snak_carbs = (foods["apple"][2] * qty_apple / 100) + (foods["walnuts"][2] * qty_walnuts / 100)
snak_fat = (foods["apple"][3] * qty_apple / 100) + (foods["walnuts"][3] * qty_walnuts / 100)
print(f"Total Snak macros: protein {snak_protein:.0f}g | carbs {snak_carbs:.0f}g | fat {snak_fat:.0f}g\n")

print("*" * 60)
print(f"Lunch {lunch_percentage:.0f} cal")
print("*" * 60)

print(f"\nRice {qty_rice:.0f}g")
print(f"Chicken Breast {qty_chicken:.0f}g")
print(f"Broccoli {qty_broccoli:.0f}g")
print(f"Olive oil {qty_oil:.0f}g")
lunch_protein = (foods["rice"][1] * qty_rice / 100) + (foods["chicken breast"][1] * qty_chicken / 100) + (foods["broccoli"][1] * qty_broccoli / 100) + (foods["olive oil"][1] * qty_oil / 100)
lunch_carbs = (foods["rice"][2] * qty_rice / 100) + (foods["chicken breast"][2] * qty_chicken / 100) + (foods["broccoli"][2] * qty_broccoli / 100) + (foods["olive oil"][2] * qty_oil / 100)
lunch_fat = (foods["rice"][3] * qty_rice / 100) + (foods["chicken breast"][3] * qty_chicken / 100) + (foods["broccoli"][3] * qty_broccoli / 100) + (foods["olive oil"][3] * qty_oil / 100)
print(f"Total Lunch macros: protein {lunch_protein:.0f}g | carbs {lunch_carbs:.0f}g | fat {lunch_fat:.0f}g\n")

print("*" * 60)
print(f"Dinner for {dinner_percentage:.0f} cal")
print("*" * 60)

print(f"\nSalmon {qty_salmon:.0f}g")
print(f"Quinoa {qty_quinoa:.0f}g")
print(f"Spinach {qty_spinach:.0f}g")
print(f"Oliva oil {qty_oil:.0f}g\n")

dinner_protein = (foods["salmon"][1] * qty_salmon / 100) + (foods["quinoa"][1] * qty_quinoa / 100) + (foods["spinach"][1] * qty_spinach / 100) + (foods["olive oil"][1] * qty_oil / 100)
dinner_carbs = (foods["salmon"][2] * qty_salmon / 100) + (foods["quinoa"][2] * qty_quinoa / 100) + (foods["spinach"][2] * qty_spinach / 100) + (foods["olive oil"][2] * qty_oil / 100)
dinner_fat = (foods["salmon"][3] * qty_salmon / 100) + (foods["quinoa"][3] * qty_quinoa / 100) + (foods["spinach"][3] * qty_spinach / 100) + (foods["olive oil"][3] * qty_oil / 100)
print(f"Total Dinner macros: protein {dinner_protein:.0f}g | carbs {dinner_carbs:.0f}g | fat {dinner_fat:.0f}g\n")

total_protein_day = breakfast_protein + snak_protein + lunch_protein + dinner_protein
total_carbs_day = breakfast_carbs +snak_carbs + lunch_carbs + dinner_carbs
total_fat_day = breakfast_fat + snak_fat + lunch_fat + dinner_fat

print("-" * 60)
print(f"The amount of macronutrients for the day is: ")
print("-" * 60)
print(f"\n- Protein: {total_protein_day:.0f}g")
print(f"- Carbs: {total_carbs_day:.0f}g")
print(f"- Fat: {total_fat_day:.0f}g\n\n")


print("*" * 60)
print("DISCLAMER")
print("The information contained in this tool is not to be \nconsidered a substitute for a real specialist, \nif you should not feel well or encounter problems during the process, \nimmediately suspend the treatment and contact your doctor")
print("*" * 60)

print("\nThank you for using our Personal Diet Calculator.")





