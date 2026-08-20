print("🌦️ Weather Outfit Advisor")
print("--------------------------")

temperature = float(input("Enter temperature (°C): "))
rain = input("Is it raining? (yes/no): ").lower()

print("\n👕 Your Recommendation")
print("----------------------")

# Temperature recommendation
if temperature >= 30:
    print("🥵 Wear light and breathable clothes.")
elif temperature >= 20:
    print("👕 Wear a T-shirt and comfortable pants.")
elif temperature >= 10:
    print("🧥 Wear a jacket or sweater.")
else:
    print("🧣 Wear warm clothes, a jacket, and consider a scarf.")

# Rain recommendation
if rain == "yes":
    print("☔ Take an umbrella.")
    print("🥾 Waterproof shoes are recommended.")
elif rain == "no":
    print("😎 No umbrella needed.")
else:
    print("⚠️ Please enter 'yes' or 'no' for rain.")

print("\n✅ Outfit advice complete!")