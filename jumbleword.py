import random
# List of country names
countries = [
    'afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua and barbuda', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan',
    'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia and herzegovina', 'botswana',
    'brazil', 'brunei', 'bulgaria', 'burkina faso', 'burundi', 'cambodia', 'cameroon', 'canada', 'cape verde', 'central african republic', 'chad',
    'chile', 'china', 'colombia', 'comoros', 'congo republic', 'congo democratic republic', 'costa rica', "côte d'ivoire", 'croatia', 'cuba', 'cyprus',
    'czech republic', 'denmark', 'djibouti', 'dominica', 'dominican Republic', 'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea',
    'estonia', 'eswatini', 'ethiopia', 'fiji', 'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala',
    'guinea', 'guinea-bissau', 'guyana', 'haiti', 'honduras', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy',
    'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'kosovo', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'lesotho', 'liberia',
    'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall islands', 'mauritania',
    'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar', 'namibia', 'nauru',
    'nepal', 'netherlands', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'north korea', 'north macedonia', 'norway', 'oman', 'pakistan', 'palau',
    'panama', 'papua new guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'rwanda', 'saint kitts and nevis',
    'saint lucia', 'saint vincent and the grenadines', 'samoa', 'san marino', 'são tomé and príncipe', 'saudi arabia', 'senegal', 'serbia',
    'seychelles', 'sierra leone', 'singapore', 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south korea', 'south sudan',
    'spain', 'sri lanka', 'sudan', 'suriname', 'sweden', 'switzerland', 'syria', 'tajikistan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'tonga',
    'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 'uganda', 'ukraine', 'united arab emirates', 'united kingdom',
    'united states', 'uruguay', 'uzbekistan', 'vanuatu', 'vatican city', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe'
    ]
# Game variables
score = 0
total_countries_played = 0
play_again = 'yes'
print("Welcome to Country Jumble Game!")
print("You get 2 chances per word. Guess the country name!")
while play_again.lower() in ['yes', 'y']:
    # Select random country and jumble it
    country = random.choice(countries)
    jumbled = ''.join(random.sample(country, len(country)))
    total_countries_played += 1
    print(f"\nJumbled word: {jumbled}")
    print("You have 2 chances:")
    
    # 2 chances to guess
    correct = False
    for attempt in range(2):
        guess = input(f"Attempt {attempt + 1}/2: ").strip().title()
        if guess == country:
            print("Correct! +1 point")
            score += 1
            correct = True
            break
        else:
            print("Wrong guess!")
    if not correct:
        print(f"Answer revealed: {country}")
    # Ask to continue
    play_again = input("\nWant to continue? (yes/no): ").strip()

# Show final score as total countries played
if play_again == "no" or "n":
    print(f"\nGame Over!")
    print(f"Total countries played: {total_countries_played}")
    print(f"Countries guessed correctly: {score}")
    print(f"Score: {score}/{total_countries_played}")
