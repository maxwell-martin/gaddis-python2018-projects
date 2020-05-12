def main():
    year_prices_dict = {}
    month_prices_dict = {}
    hi_lo_ppy_dict = {}
    full_date_prices_dict = {}
    
    with open("GasPrices.txt", "r") as infile:
        for line in infile:
            date_price = line.split(":")

            year = date_price[0][6:]
            month = date_price[0][0:2]
            full_date = date_price[0]
            price = float(date_price[1])

            # Build dictionary of { year: [prices] }
            if year not in year_prices_dict.keys():
                year_prices_dict[year] = [price]
            else:
                year_prices_dict[year].append(price)

            # Build dictionary of { month: [prices] }
            if month not in month_prices_dict.keys():
                month_prices_dict[month] = [price]
            else:
                month_prices_dict[month].append(price)

            # Build dictionary of
            # { year, { "high": [date, price], "low": [date, price] } }
            if year not in hi_lo_ppy_dict.keys():
                hi_lo_ppy_dict[year] = { "high": [], "low": [] }
            hi_lo_ppy_dict = get_hi_low_ppy(hi_lo_ppy_dict, year, full_date, price)

            # Build dictionary of { full_date: price }
            full_date_prices_dict[full_date] = price            
            
    print("Average Price Per Year\n",
          "Format ('Year', 'Price ($)':\n",
          avg_ppy_or_ppm(year_prices_dict), sep = "")
    print()

    print("Average Price Per Month\n",
          "Format ('Month', 'Price ($)':\n",
          avg_ppy_or_ppm(month_prices_dict), sep = "")
    print()

    print("Highest and Lowest Prices Per Year\n",
          hi_lo_ppy_dict, sep = "")

    # Create file of "date:price" of prices from low to high
    with open("GasPricesLowToHigh.txt", "w") as outfile:
        dates_prices = get_sorted_dates_and_prices(full_date_prices_dict, False)
        for dp in dates_prices:
            outfile.write(dp + "\n")

    # Create file of "date:price" of prices from high to low
    with open("GasPricesHighToLow.txt", "w") as outfile:
        dates_prices = get_sorted_dates_and_prices(full_date_prices_dict, True)
        for dp in dates_prices:
            outfile.write(dp + "\n")

# Calculate average price per year or price per month
# Returns dictionary of either { 'year': 'avg ppy' } or { 'month': 'avg ppm' }
def avg_ppy_or_ppm(d):
    avgs = {}
    for k in d.keys():
        avgs[k] = "$" + format(sum(d[k])/len(d[k]), ",.2f")
    return avgs

# Find highest and lowest prices per year
# Returns dictionary of
# {'year': {'high': ['date', price], 'low': ['date', price]}
def get_hi_low_ppy(d, year, full_date, price):
    if len(d[year]["high"]) == 0:
        d[year]["high"].append(full_date)
        d[year]["high"].append(price)
    elif price > d[year]["high"][1]:
        d[year]["high"][0] = full_date
        d[year]["high"][1] = price
        
    if len(d[year]["low"]) == 0:
        d[year]["low"].append(full_date)
        d[year]["low"].append(price)
    elif price < d[year]["low"][1]:
        d[year]["low"][0] = full_date
        d[year]["low"][1] = price

    return d

# Sort prices by either highest to lowest or lowest to highest
# Returns list of strings as "date:price"
def get_sorted_dates_and_prices(d, reverse):
    values = list(d.values())
    values.sort(reverse = reverse)
    dates_prices = []
    for value in values:
        for k in d.keys():
            if d[k] == value:
                dates_prices.append(k + ":" + str(value))
    return dates_prices

main()
