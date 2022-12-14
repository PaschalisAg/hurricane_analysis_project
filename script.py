import operator

# names of hurricanes
names = [
    "Cuba I",
    "San Felipe II Okeechobee",
    "Bahamas",
    "Cuba II",
    "CubaBrownsville",
    "Tampico",
    "Labor Day",
    "New England",
    "Carol",
    "Janet",
    "Carla",
    "Hattie",
    "Beulah",
    "Camille",
    "Edith",
    "Anita",
    "David",
    "Allen",
    "Gilbert",
    "Hugo",
    "Andrew",
    "Mitch",
    "Isabel",
    "Ivan",
    "Emily",
    "Katrina",
    "Rita",
    "Wilma",
    "Dean",
    "Felix",
    "Matthew",
    "Irma",
    "Maria",
    "Michael",
]

# months of hurricanes
months = [
    "October",
    "September",
    "September",
    "November",
    "August",
    "September",
    "September",
    "September",
    "September",
    "September",
    "September",
    "October",
    "September",
    "August",
    "September",
    "September",
    "August",
    "August",
    "September",
    "September",
    "August",
    "October",
    "September",
    "September",
    "July",
    "August",
    "September",
    "October",
    "August",
    "September",
    "October",
    "September",
    "September",
    "October",
]

# years of hurricanes
years = [
    1924,
    1928,
    1932,
    1932,
    1933,
    1933,
    1935,
    1938,
    1953,
    1955,
    1961,
    1961,
    1967,
    1969,
    1971,
    1977,
    1979,
    1980,
    1988,
    1989,
    1992,
    1998,
    2003,
    2004,
    2005,
    2005,
    2005,
    2005,
    2007,
    2007,
    2016,
    2017,
    2017,
    2018,
]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [
    165,
    160,
    160,
    175,
    160,
    160,
    185,
    160,
    160,
    175,
    175,
    160,
    160,
    175,
    160,
    175,
    175,
    190,
    185,
    160,
    175,
    180,
    165,
    165,
    160,
    175,
    180,
    185,
    175,
    175,
    165,
    180,
    175,
    160,
]

# areas affected by each hurricane
areas_affected = [
    ["Central America", "Mexico", "Cuba", "Florida", "The Bahamas"],
    [
        "Lesser Antilles", "The Bahamas", "United States East Coast",
        "Atlantic Canada"
    ],
    ["The Bahamas", "Northeastern United States"],
    [
        "Lesser Antilles", "Jamaica", "Cayman Islands", "Cuba", "The Bahamas",
        "Bermuda"
    ],
    ["The Bahamas", "Cuba", "Florida", "Texas", "Tamaulipas"],
    ["Jamaica", "Yucatn Peninsula"],
    ["The Bahamas", "Florida", "Georgia", "The Carolinas", "Virginia"],
    [
        "Southeastern United States", "Northeastern United States",
        "Southwestern Quebec"
    ],
    ["Bermuda", "New England", "Atlantic Canada"],
    ["Lesser Antilles", "Central America"],
    ["Texas", "Louisiana", "Midwestern United States"],
    ["Central America"],
    ["The Caribbean", "Mexico", "Texas"],
    ["Cuba", "United States Gulf Coast"],
    ["The Caribbean", "Central America", "Mexico", "United States Gulf Coast"],
    ["Mexico"],
    ["The Caribbean", "United States East coast"],
    ["The Caribbean", "Yucatn Peninsula", "Mexico", "South Texas"],
    ["Jamaica", "Venezuela", "Central America", "Hispaniola", "Mexico"],
    ["The Caribbean", "United States East Coast"],
    ["The Bahamas", "Florida", "United States Gulf Coast"],
    ["Central America", "Yucatn Peninsula", "South Florida"],
    ["Greater Antilles", "Bahamas", "Eastern United States", "Ontario"],
    ["The Caribbean", "Venezuela", "United States Gulf Coast"],
    ["Windward Islands", "Jamaica", "Mexico", "Texas"],
    ["Bahamas", "United States Gulf Coast"],
    ["Cuba", "United States Gulf Coast"],
    ["Greater Antilles", "Central America", "Florida"],
    ["The Caribbean", "Central America"],
    ["Nicaragua", "Honduras"],
    [
        "Antilles",
        "Venezuela",
        "Colombia",
        "United States East Coast",
        "Atlantic Canada",
    ],
    [
        "Cape Verde",
        "The Caribbean",
        "British Virgin Islands",
        "U.S. Virgin Islands",
        "Cuba",
        "Florida",
    ],
    [
        "Lesser Antilles",
        "Virgin Islands",
        "Puerto Rico",
        "Dominican Republic",
        "Turks and Caicos Islands",
    ],
    [
        "Central America",
        "United States Gulf Coast (especially Florida Panhandle)"
    ],
]

# damages (USD($)) of hurricanes
damages = [
    "Damages not recorded",
    "100M",
    "Damages not recorded",
    "40M",
    "27.9M",
    "5M",
    "Damages not recorded",
    "306M",
    "2M",
    "65.8M",
    "326M",
    "60.3M",
    "208M",
    "1.42B",
    "25.4M",
    "Damages not recorded",
    "1.54B",
    "1.24B",
    "7.1B",
    "10B",
    "26.5B",
    "6.2B",
    "5.37B",
    "23.3B",
    "1.01B",
    "125B",
    "12B",
    "29.4B",
    "1.76B",
    "720M",
    "15.1B",
    "64.8B",
    "91.6B",
    "25.1B",
]

# deaths for each hurricane
deaths = [
    90,
    4000,
    16,
    3103,
    179,
    184,
    408,
    682,
    5,
    1023,
    43,
    319,
    688,
    259,
    37,
    11,
    2068,
    269,
    318,
    107,
    65,
    19325,
    51,
    124,
    17,
    1836,
    125,
    87,
    45,
    133,
    603,
    138,
    3057,
    74,
]


# write your update damages function here:
def converse_damages(damages_list):
    conversion = {"M": 1000000, "B": 1000000000}
    updated_damages = [
        float(record[:-1]) *
        conversion[record[-1]] if record[-1] in conversion.keys() else
        record if record == "Damages not recorded" else record
        for record in damages_list
    ]

    # since there is no elif statement for list comprehension, it was needed to create
    # else statement that does exactly the same thing as the previous else statement
    # https://stackoverflow.com/a/9987546/16672014

    return updated_damages


updated_damages = converse_damages(damages)
for damage in updated_damages:
    print(type(damage))

print(updated_damages)


# write your construct hurricane dictionary function here:
def create__hurricanes_dict_by_name(names, months, years, max_sustained_winds,
                                    areas_affected, damages, deaths):
    hurricanes = dict()
    length_index = len(names)
    for index in range(length_index):
        hurricanes[names[index]] = {
            "Name": names[index],
            "Month": months[index],
            "Year": years[index],
            "Max Sustained Winds": max_sustained_winds[index],
            "Areas Affected": areas_affected[index],
            "Damages": updated_damages[index],
            "Deaths": deaths[index],
        }
    return hurricanes


hurricanes_by_name = create__hurricanes_dict_by_name(names, months, years,
                                                     max_sustained_winds,
                                                     areas_affected,
                                                     updated_damages, deaths)
print(hurricanes_by_name)


# write your construct hurricane by year dictionary function here:
def hurricanes_dict_by_year(names, months, years, max_sustained_winds,
                            areas_affected, damages, deaths):
    hurricanes = dict()
    length_index = len(names)
    for index in range(length_index):
        hurricanes[years[index]] = {
            "Name": names[index],
            "Month": months[index],
            "Year": years[index],
            "Max Sustained Winds": max_sustained_winds[index],
            "Areas Affected": areas_affected[index],
            "Damages": damages[index],
            "Deaths": deaths[index],
        }
    return hurricanes


hurricanes_by_year = hurricanes_dict_by_year(names, months, years,
                                             max_sustained_winds,
                                             areas_affected, updated_damages,
                                             deaths)
hurricanes_by_year[1924]
hurricanes_by_year[2017]


# write your count affected areas function here:
def count_affected_arreas(dictionary):
    areas_affected = dict()
    counter = 0
    for name in dictionary:
        for area in dictionary[name]["Areas Affected"]:
            if area in areas_affected:
                areas_affected[area] += 1
            else:
                areas_affected[area] = 1
    return areas_affected


count_affected_arreas = count_affected_arreas(hurricanes_by_name)
print(count_affected_arreas)


# write your find most affected area function here:
def find_most_affected_area(dictionary_with_counts):
    result = []
    sort_dictionary = sorted(dictionary_with_counts.items(),
                             key=lambda x: x[1],
                             reverse=True)
    for i in sort_dictionary:
        result += i[0], i[1]
    return sort_dictionary


find_most_affected_area(count_affected_arreas)[:5]


# write your greatest number of deaths function here:
def find_most_lethal_hurricane(dictionary):
    fatality_hurricanes = dict()
    for key, value in dictionary.items():
        fatality_hurricanes[key] = value['Deaths'], value['Year']
    # fatality_hurricanes_sorted = dict(sorted(fatality_hurricanes.items(),
    #                                     key=lambda x: x[1],
    #                                     reverse=True))

    # finding the key with the biggest value and returning both of them (key and value)
    maximum_fatality = max(fatality_hurricanes.items(),
                           key=operator.itemgetter(1))[:2]

    return maximum_fatality


find_most_lethal_hurricane(hurricanes_by_name)
# write your catgeorize by mortality function here:


def categ_hurricanes_mortality_scale(dictionary):

    mortality_scale = {0: list(), 1: list(), 2: list(), 3: list(), 4: list()}

    for name, value in dictionary.items():
        if dictionary[name]["Deaths"] == 0:
            mortality_scale[0].append(value)
        elif dictionary[name]["Deaths"] <= 100:
            mortality_scale[1].append(value)
        elif dictionary[name]["Deaths"] <= 500:
            mortality_scale[2].append(value)
        elif dictionary[name]["Deaths"] <= 1000:
            mortality_scale[3].append(value)
        else:
            mortality_scale[4].append(value)

    return mortality_scale


categ_hurricanes_mortality_scale(hurricanes_by_name)


# write your greatest damage function here:
def greatest_dmg_hurricane(dictionary):
    dmg_hurricanes_dict = dict()

    for name in dictionary:
        if dictionary[name]["Damages"] == "Damages not recorded":
            continue
        else:
            dmg_hurricanes_dict[name] = dictionary[name]["Damages"]
    greatest_dmg_hurricane = sorted(dmg_hurricanes_dict.items(),
                                    key=lambda x: x[1],
                                    reverse=True)[0]

    return greatest_dmg_hurricane


greatest_dmg_hurricane(hurricanes_by_name)


# write your catgeorize by damage function here
def damage_rating_hurricanes(dictionary):

    damage_rating = {0: list(), 1: list(), 2: list(), 3: list(), 4: list()}

    for name, value in dictionary.items():
        if dictionary[name]["Damages"] == "Damages not recorded":
            damage_rating[0].append(value)
        elif dictionary[name]["Damages"] <= 100000000:
            damage_rating[1].append(value)
        elif dictionary[name]["Damages"] <= 1000000000:
            damage_rating[2].append(value)
        elif dictionary[name]["Damages"] <= 10000000000:
            damage_rating[3].append(value)
        else:
            damage_rating[4].append(value)

    return damage_rating


damage_rating_hurricanes = damage_rating_hurricanes(hurricanes_by_name)
damage_rating_hurricanes[0]
