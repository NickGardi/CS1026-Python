# Nicholas Gardi                   Assignment #4
#                                     Part #1
#setting up the Country class and variables
class Country:
    def __init__(self, name, pop, area, continent):
        self.name = name
        self.pop = pop
        self.area = area
        self.continent = continent

    #defining the string that is to be returned when the object is called
    def __repr__(self) :
        return ('{} in {}'.format(self.name, self.continent))

    #changes a country's population to whatever the user would like
    def setPopulation(self, newPop):
        self.pop = newPop

    #returns the name of the country
    def getName(self):
        return self.name

    #returns the country's area
    def getArea(self):
        return self.area

    #returns the country's population
    def getPopulation(self):
        return self.pop

    #returns the country's continent
    def getContinent(self):
        return self.continent

    #returns the country's population density
    def getPopDensity(self):
        return (self.pop / self.area)

#                                     Part #2
catalogue = []
cDictionary = {}
#defining the CountryCatalogue class
class CountryCatalogue:
    #setting up the list and dictionary needed, opening the specified files, and appending values to the data structures
    def __init__(self,filename):
        continentFile = open("continent.txt", "r", encoding="utf-8")
        for line in continentFile:
            line = line.split(",")
            country = line[0]
            continent = line[-1].strip()
            continent = line[-1].strip()
            cDictionary[country] = continent

        dataFile = open(filename, "r", encoding="utf-8")
        for line in dataFile:
            line = line.split("|")
            name = line[0]
            pop = line[1]
            area = line[2]
            continent = cDictionary[name]
            countryObj = Country(name, pop, area, continent)
            catalogue.append(countryObj)

    #defining the method to add a new country object to the catalogue
    def addCountry(self):
        x = 1
        while x == 1:
            userInput = input("Enter a country that you want to add to the dictionary, along with the population, area, and continent (name, population, area, continent): ")
            userInput = userInput.split(",")
            countryName = userInput[0]
            if countryName in cDictionary:
                x = 0
                print("That country is already included, please try again.")
            else:
                x = 0
                name = userInput[0]
                pop = userInput[1]
                area = userInput[2]
                continent = userInput[3]
                countryObj = Country(name, pop, area, continent)
                catalogue.append(countryObj)
                cDictionary[name] = continent
                print("Country has been successfully added.")

    #defining the method to delete a specified country from the catalogue
    def deleteCountry(self):
        x = 1
        country = input("Enter a country that you want deleted: ")
        for obj in catalogue:
            if obj.name == country:
                catalogue.remove(obj)
                print("The country was successfully deleted.")
                x = 0
        if x == 1:
            print("That country is not in the dictionary")

    #defining the method to return a country's information
    def findCountry(self):
        x=1
        country = input("Enter a country name to see it's information")
        for obj in catalogue:
            if obj.name == country:
                print("Name: ", obj.name)
                print("Continent: ", obj.continent)
                print("Population: ", obj.pop)
                print("Area: ", obj.area)
                x=0
        if x != 0:
            print("That country's information is not available.")


    #defining the method to return all countris in a specified continent
    def filterCountriesByContinent(self):
        continent1 = input("Enter a continent to see all the countries within: ")
        for country in catalogue:
            if country.continent == continent1:
                print(country)

    #defining the method to print the country catalogue
    def printCountryCatalogue(self):
        print(catalogue)

    #defining the method to change the population of a specific country
    def setPopulationOfASelectedCountry(self):
        countryInput = input("Enter the name of the country you would like to edit: ")
        newPop = input("Enter the new population of this country: ")
        for country in catalogue:
            if country.name == countryInput:
                country.pop = newPop
                if country.pop == newPop:
                    area = float((country.area).replace(",", "").strip())
                    print("New population density is:" , (int(newPop))/area)

    #defining the method to find the country with the largest population
    def findCountryWithLargestPop(self):
        popList = []
        for country in catalogue:
            pop = country.pop
            pop = pop.replace(",", "")
            if pop.isdigit():
                pop = int(pop)
                popList.append(pop)

        maxPop = max(popList)

        for country in catalogue:
            pop = country.pop
            pop = pop.replace(",", "")
            if pop.isdigit():
                pop = int(pop)
                if pop == maxPop:
                    print("The country with the largest population is: ", country.name)

    #defining the method to print the country with the smallest area
    def findCountryWithSmallestArea(self):
        areaList = []
        for country in catalogue:
            area = country.area
            area = area.replace(",", "")
            try:
                area = float(area)
                areaList.append(area)
            except ValueError:
                pass

        minArea = min(areaList)

        for country in catalogue:
            area = country.area
            name = country.name
            area = area.replace(",", "")
            try:
                area = float(area)
                if area == minArea:
                    print("The country with the smallest area is: ", name)
            except ValueError:
                pass
    #defining the method to print the countries within a certain population density range
    def filterCountriesByPopDensity(self):
        upBound = float(input("Enter the upper bound for pop density: "))
        lowBound = float(input("Enter the lower bound for pop density: "))
        for country in catalogue:
            pop = (country.pop).replace(",","")
            if pop.isdigit():
                pop = float(pop)
                area = float((country.area).replace(",",""))
                popDensity = (pop/area)
                if popDensity >= lowBound and popDensity <= upBound:
                    print(country.name , "has a population density of", popDensity, "and is with the specified range")

    #defining the method to print the country with the highest population
    def findMostPopulousContinent(self):
        countryObjList = []

        northAmericaList = []
        asiaList = []
        africaList = []
        europeList = []
        southAmericaList = []

        for country in catalogue:
            pop = (country.pop).replace(",","")
            if pop.isdigit():
                countryObjList.append(country)

        for country in countryObjList:
            if country.continent == "North America":
               northAmericaList.append(country)
            if country.continent == "Asia":
               asiaList.append(country)
            if country.continent == "Africa":
               africaList.append(country)
            if country.continent == "Europe":
               europeList.append(country)
            if country.continent == "South America":
               southAmericaList.append(country)

        northAmericaPop = 0
        asiaPop = 0
        africaPop = 0
        europePop = 0
        southAmericaPop = 0

        for country in northAmericaList:
            pop = float((country.pop).replace(",",""))
            northAmericaPop += pop
        for country in asiaList:
            pop = float((country.pop).replace(",",""))
            asiaPop += pop
        for country in africaList:
            pop = float((country.pop).replace(",",""))
            africaPop += pop
        for country in europeList:
            pop = float((country.pop).replace(",",""))
            europePop += pop
        for country in southAmericaList:
            pop = float((country.pop).replace(",",""))
            southAmericaPop += pop
        allContinentPopList = []
        allContinentPopList.append(northAmericaPop)
        allContinentPopList.append(asiaPop)
        allContinentPopList.append(africaPop)
        allContinentPopList.append(europePop)
        allContinentPopList.append(southAmericaPop)
        maxPop = max(allContinentPopList)
        if maxPop == northAmericaPop:
            print("The continent with the most number of people living in it is North America, with this many people:", maxPop)
        if maxPop == asiaPop:
            print("The continent with the most number of people living in it is Asia, with this many people:", maxPop)
        if maxPop == africaPop:
            print("The continent with the most number of people living in it is Africa, with this many people:", maxPop)
        if maxPop == europePop:
            print("The continent with the most number of people living in it is europe, with this many people:", maxPop)
        if maxPop == southAmericaPop:
            print("The continent with the most number of people living in it is South America, with this many people:", maxPop)

    #defining the method to save the required output to any file specified
    def saveCountryCatalogue(self, filename):
        outputList = []
        for country in catalogue:
            pop = (country.pop).replace(",","")
            if pop.isdigit():
                pop = int(pop)
                try:
                    area = float((country.area).replace(",",""))
                    area = float(area)
                    popDens = "{0:.2f}".format(pop/area)
                    final = str(country.name+"|"+country.continent+"|"+str(pop)+"|"+str(popDens))
                    outputList.append(final)
                except ValueError:
                    pass
        outputList.sort()
        file = open(filename, "w", encoding="utf-8")
        for line in outputList:
            file.write(line + "\n")
        print("The country information has been saved to the specified file.")
