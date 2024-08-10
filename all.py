# Question 1 Task 1:Setting Up a Python Virtual Environment and Installing Packages
cd path/to/your/project-directory
python -m venv myenv
# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS and Linux:
source myenv/bin/activate
# Install the requests package
 pip install requests
# verify installation
pip list

# Question 1 Task 2:Fetching Data from the Pokémon API
import requests
url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    name = data['name']
abilities = [ability['ability']['name'] for ability in data['abilities']]

print(f"Name: {name.capitalize()}")
print("Abilities:")
for ability in abilities:
    print(f"- {ability}")
else:
    print (f"failed to retrieve data: {response.status_code}")

# Question 1 Task 3:Analyzing and Displaying Data
import requests 
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def calculate_average_weight(pokemon_list):
    total_weight = 0
    count = 0
    for pokemon in pokemon_list:
        if pokemon:
            total_weight += pokemon['weight']
            count += 1
    return total_weight/count if count > 0 else 0
pokemon_names = ["pikachu", "bulbasuar", "charmander"]
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon in pokemon_data:
    if pokemon:
        name = pokemon['name']
        abilities = [ability['ability']['name']for ability in pokemon['abilities']]
        print(f"Name: {name}")
        print(f"abilities: {','.join(abilities)}")

average_weight = calculate_average_weight(pokemon_data)
print(f"Average Weight: {average_weight}")

# Question 2 Task 1: Set up a Python Virtual Environment and Install Required Packages
cd path/to/your/project-directory
python -m venv myenv
# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS and Linux:
source myenv/bin/activate
# Install the requests package
 pip install requests
# verify installation
pip list

# Question 2 Task 2:Fetch Data from a Space API 
import requests
def fetch_planet_data():
    url = "https://api.le-system-solaire.net/rest/bodies/"
    response = requests.get(url)
    if response.status_code == 200:
        plantes = response.json()['bodies']
        for planet in plantes:
            if planet['isPlanet']:
                name = planet.get('englishName', 'N/A')
                mass = planet.get('mass', {}).get('massValue', 'N/A')
                mass_exponent = planet.get('mass', {}).get('massExponent',0)
                orbit_period = planet.get('sideralOrbit', 'N/A')

                if mass != 'N/A':
                    mass = f"{mass}e{mass_exponent} kg"
                print(f"planet: {name}, Mass: {mass}, Orbit Period:{orbit_period} days")
    else:
        print(f"failed to retrieve data: {response.status_code}")
fetch_planet_data()

# Question 2 Task 3:Data Presentation and Analysis
import requests
def fetch_planet_data():
    response = requests.get("http://api.le-system-solaire.net/rest/bodies/")
    data = response.json()
    planets = [body for body in data['bodies'] if body['isPlanet']]

    formatted_planets = []
    for planet in planets:
           formatted_planets.append({
            'name': planet['englishName'],
            'mass': planet['mass'][massValue] * (10** planet['mass']['massexponent']) if planet['mass'] else None, 
            'orbit_period': planet['sideralOrbit']
        })
    return formatted_planets
def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda p: p['mass'] if p['mass'] else 0)

    retrun heaviest_planet['name'], heaviest_planet['mass']
                                  
planets = fetch_planet_data
name, mass, = find_heaviest_planet(planets)
print(f"The heaviest palnet is {name} with a mass of {mass} kg ")


