
#orbital information
solar_sytem = {
    "mercury": {"Perihelion (AU)": 0.3075, "Aphelion (AU)":0.4667},
    "Venus": {"Perihelion (AU)":0.7184, "Aphelion (AU)":0.7282},
    "Earth": {"Perihelion (AU)": 0.9833, "Aphelion (AU)":1.0167},
    "Mars": {"Perihelion (AU)":1.3814, "Aphelion (AU)":1.6660},
    "Jupiter": {"Perihelion (AU)":4.9501, "Aphelion (AU)":5.4588},
    "Saturn": {"Perihelion (AU)":9.0480, "Aphelion (AU)":10.1238},
    "Uranus": {"Perihelion (AU)":18.3755, "Aphelion (AU)":20.0833},
    "Neptune": {"Perihelion (AU)":29.7667, "Aphelion (AU)":30.4413}
}

#menu function
def menu(number):
    if number ==  '1':
        planet_name = input("Enter name of planet: ").capitalize()
        print(planet_info(planet_name))

    elif number == '2':
        planet_1 = input("enter first planet: ").capitalize()
        planet_2 = input("enter second planet: ").capitalize()
        print(peri_calc(planet_1, planet_2))
    else:
        print("Invalid option")

#function to view planetary info
def planet_info(planet_name):
    if planet_name.capitalize() in solar_sytem:
        perihelion = solar_sytem[planet_name]["Perihelion (AU)"]
        aphelion = solar_sytem[planet_name]["Aphelion (AU)"]
        return (f"perihelion (closest orbit) of {planet_name} is: {perihelion} AU \naphelion (furthest orbit) is: {aphelion} AU")
    else:
        return f"Planet does not exist"


#DISTANCE CALC FUNC
def peri_calc(planet_1, planet_2):

    if planet_1.capitalize() and planet_2.capitalize() in solar_sytem:
        perihelion = solar_sytem[planet_1]["Perihelion (AU)"]
        perihelion = solar_sytem[planet_2]["Perihelion (AU)"]


        planet_1 = solar_sytem[planet_1]["Perihelion (AU)"]
        planet_2 = solar_sytem[planet_2]["Perihelion (AU)"]

        diffirence_au = round(float(planet_1) - float(planet_2), 5)
        difference_km = round(diffirence_au * 150_000_000, 1)
        return f"difference in Perihelion is: {abs(diffirence_au)} AU\ndifference in kilometer is km {abs(difference_km)}"
    else:
        return f"Planets not in solar system"

number = input("Enter number: ")
menu(number)