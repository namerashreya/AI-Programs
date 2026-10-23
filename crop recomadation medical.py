# ---------------------------------------------------------
# EXPERT SYSTEM FOR CROP RECOMMENDATION
# ---------------------------------------------------------

def get_answer(question):
    while True:
        answer = input(question + " (yes/no): ").lower().strip()

        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")


def crop_recommendation():
    print("=" * 55)
    print("       CROP RECOMMENDATION EXPERT SYSTEM")
    print("=" * 55)
    print("Answer the following questions with yes or no.\n")

    # Collect information
    high_rainfall = get_answer("Does your area have high rainfall?")
    low_rainfall = get_answer("Does your area have low rainfall?")
    fertile_soil = get_answer("Is the soil fertile?")
    black_soil = get_answer("Is the soil black?")
    sandy_soil = get_answer("Is the soil sandy?")
    clay_soil = get_answer("Is the soil clayey?")
    warm_climate = get_answer("Is the climate warm?")
    cool_climate = get_answer("Is the climate cool?")
    enough_water = get_answer("Is enough water available for irrigation?")
    summer = get_answer("Is it summer season?")
    winter = get_answer("Is it winter season?")

    print("\n" + "=" * 55)
    print("              CROP RECOMMENDATION")
    print("=" * 55)

    # -----------------------------------------------------
    # RULES
    # -----------------------------------------------------

    # Rule 1: Rice
    if high_rainfall and clay_soil and enough_water:
        crop = "Rice"
        explanation = (
            "Rice generally requires sufficient water and "
            "grows well in clayey soil and high-rainfall conditions."
        )

    # Rule 2: Wheat
    elif winter and fertile_soil and cool_climate:
        crop = "Wheat"
        explanation = (
            "Wheat is commonly grown during cooler conditions "
            "in fertile soil."
        )

    # Rule 3: Cotton
    elif black_soil and warm_climate and low_rainfall:
        crop = "Cotton"
        explanation = (
            "Cotton can grow well in black soil and warm "
            "conditions with relatively lower rainfall."
        )

    # Rule 4: Groundnut
    elif sandy_soil and warm_climate:
        crop = "Groundnut"
        explanation = (
            "Groundnut grows well in warm conditions and "
            "well-drained sandy soil."
        )

    # Rule 5: Maize
    elif fertile_soil and warm_climate and enough_water:
        crop = "Maize"
        explanation = (
            "Maize can grow well in fertile soil with warm "
            "conditions and adequate water."
        )

    # Rule 6: Bajra
    elif low_rainfall and sandy_soil and warm_climate:
        crop = "Bajra"
        explanation = (
            "Bajra is suitable for warm and relatively "
            "dry conditions."
        )

    # Rule 7: Mustard
    elif winter and cool_climate and low_rainfall:
        crop = "Mustard"
        explanation = (
            "Mustard is commonly grown in cooler and "
            "relatively dry conditions."
        )

    # Rule 8: Sugarcane
    elif warm_climate and high_rainfall and enough_water:
        crop = "Sugarcane"
        explanation = (
            "Sugarcane generally needs warm conditions "
            "and substantial water availability."
        )

    # No matching rule
    else:
        crop = "No Clear Recommendation"
        explanation = (
            "The available information does not match "
            "the crop rules in this expert system."
        )

    print("\nRecommended Crop:", crop)
    print("Reason:", explanation)

    print("\nNote: This system is for educational purposes only.")
    print("Actual crop selection should consider local soil testing,")
    print("weather, irrigation, market conditions and expert advice.")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

crop_recommendation()
