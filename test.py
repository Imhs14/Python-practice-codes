def cars(company, **models):
    print("The car brand is", company)
    for key, value in models.items():
        print(" ",key+" : ",value)
cars("mclaren",model = "720s", horsepower = 720, color = "orange", price = "$650,000")