SHARES_PURCHASED = 2000
INITIAL_PPS = 40.00
COMMISSION_RATE = 0.03
SHARES_SOLD = 2000
SELLING_PPS = 42.75

initial_cost = SHARES_PURCHASED * INITIAL_PPS
print("Initial cost: $" + format(initial_cost, ",.2f"))

initial_commission = initial_cost * COMMISSION_RATE
print("Initial commission: $" + format(initial_commission, ",.2f"))

sold_amt = SHARES_SOLD * SELLING_PPS
print("Amount sold: $" + format(sold_amt, ",.2f"))

selling_commission = sold_amt * COMMISSION_RATE
print("Selling commission: $" + format(selling_commission, ",.2f"))

profit_loss = sold_amt - initial_cost - selling_commission - initial_commission
print("Profit/Loss with commissions: $" + format(profit_loss, ",.2f"))
