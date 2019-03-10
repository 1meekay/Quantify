import pandas as pd, mysql.connector as msc, pprint, pickle

db_ = msc.connect(
    host='localhost',
    user='test_proj',
    passwd='projtest',
    database='test_companies'
)

cursor = db_.cursor()
'''
cursor.execute("SHOW columns FROM companies_table")
cols = []
for col in cursor.fetchall():
    cols.append(col[0])

cursor.execute("SELECT id FROM companies_table")
ids = []
for id in cursor.fetchall():
    ids.append(id[0])

cursor.execute("SELECT * FROM companies_table")
data = cursor.fetchall()
dataframe = pd.DataFrame(data=data, index=ids, columns=cols)

with open('data.pickle', 'wb') as pickle_out:
    pickle.dump(dataframe, pickle_out)
'''

dataframe = pickle.load(open('data.pickle', 'rb'))

# ======================================================================================================================

"""
Business Class :: Team NoName
Quantifying the health of a small business


class Business:

    def __init__(self, name='', location='', industry='', total_revenue=0.0, cogs=0.0,
                 op_expenses=0.0, cash_balance=0.0, current_assets=0.0, current_liabilities=0.0,
                 long_term_liabilities=0.0, dso=0.0, break_even=0.0,
                 owner_satisfaction=0.0, employee_satisfaction=0.0, new_customers=0, start_customers=0,
                 end_customers=0, total_inventory=0.0, dead_inventory=0.0, rewards_program='', avg_ticket_size=0.0,
                 no_transactions=0, exp_transactions=0, expansion='', prior_revenue=0.0):

        # General business information
        self.name = name
        self.location = location
        self.industry = industry

        # Gross revenue (e.g. total income before expenses)
        self.total_revenue = total_revenue
        self.prior_revenue = prior_revenue

        # Cost of goods sold (e.g. inventory, merchant fees, shipping)
        self.cogs = cogs

        # Operating expenses (e.g. rent, payroll, taxes, utilities, etc.)
        self.op_expenses = op_expenses

        # Cash in the bank
        self.cash_balance = cash_balance

        # Cash on-hand + liquid assets
        self.current_assets = current_assets

        # Short-term liabilities and interest due (within 12 months)
        self.current_liabilities = current_liabilities

        # Long-term debt obligations
        self.long_term_liabilities = long_term_liabilities

        # Days sales outstanding (i.e. average age of accounts receivable)
        # > 30 is a negative sign unless a NET60 or NET90 is utilized
        self.dso = dso

        # Keep the lights on amount
        self.break_even = break_even

        # Owner & employee satisfaction
        self.owner_satisfaction = owner_satisfaction
        self.employee_satisfaction = employee_satisfaction

        # Number of monthly transactions, expected monthly transactions, avg ticket size
        self.no_transactions = no_transactions
        self.exp_transactions = exp_transactions
        self.avg_ticket_size = avg_ticket_size

        # Info for customer loyalty and retention
        self.new_customers = new_customers
        self.start_customers = start_customers
        self.end_customers = end_customers
        self.rewards_program = rewards_program

        # Current & dead inventory
        self.total_inventory = total_inventory
        self.dead_inventory = dead_inventory

        # Expansion info; justifies a net loss
        self.expansion = expansion

    # ================ Computational methods ================ #

    # Overall profit margin; industry differences
    def gross_profit_margin(self):
        gpm = ((self.total_revenue - self.cogs) / self.total_revenue) * 100.0
        return gpm

    # Profitability factor
    def net_profit_loss(self):
        npl = (self.total_revenue - self.cogs - self.op_expenses)
        return npl

    # Gross profit
    def gross_profit(self):
        ni = self.total_revenue - self.cogs
        return ni

    # Quick ratio (i.e. excludes inventory from assets & excludes current debt)
    # < 1.0 signals danger as current liabilities exceeds current assets
    def liquidity(self):
        liquid = (self.cash_balance + self.current_assets) / self.current_liabilities
        return liquid

    # Debt information
    def total_debt(self):
        td = (self.current_liabilities + self.long_term_liabilities)
        return td

    # Debt ratios 0.4 and lower signal healthy debt
    def debt_ratio(self):
        dr = (self.current_liabilities + self.long_term_liabilities) / (self.current_assets + self.cash_balance)
        return dr

    # Break-even expenses should be less than total revenue
    # Aggressive expansion may cause losses, but doesn't signal bad health
    def break_even(self):
        be = self.op_expenses + self.cogs
        return be

    # Closer to 80-100% is a good retention rate
    def customer_retention_rate(self):
        crr = (((self.end_customers - self.new_customers) / self.start_customers) * 100.0)
        return crr

    # Inventory health; < 15% is healthy
    def inventory(self):
        ih = (self.dead_inventory / self.total_inventory) * 100.0
        return ih

    # def outlook(self):
    #     proj_rev = self.avg_ticket_size * self.exp_transactions
    #     return "{:.{}f}%".format(proj_rev, 2)
"""
# ======================================================================================================================

cursor.execute("SELECT * FROM companies_table")

for x in cursor.fetchall():
    print(x)

'''
try:
    name = input('Business name: ')
    location = input('Business location: ')
    industry = input('Industry: ')
    total_revenue = float(input('Total monthly revenue: $'))
    prior_revenue = float(input('Previous monthly revenue: $'))
    cogs = float(input('Monthly cost of goods sold: $'))
    op_expenses = float(input('Monthly operating expenses (includes payroll): $'))
    cash_balance = float(input('Enter cash-on-hand: $'))
    current_assets = float(input('Enter value of current assets: $'))
    current_liabilities = float(input('Enter value of monthly, short-term liabilities: $'))
    long_term_liabilities = float(input('Enter value of long-term liabilities: $'))
    expansion = input('Are you undergoing any sort of expansion (i.e. products, personnel, locations, etc)? ')
    total_inventory = float(input('Enter current value of total inventory: $'))
    dead_inventory = float(input('Enter value of dead inventory (i.e. inventory > 30 days old): $'))
    start_customers = int(input('Enter beginning of month customer count: '))
    end_customers = int(input('Enter end of month customer count: '))
    new_customers = int(input('Number of new customers: '))
    rewards_program = input('Do you utilize a customer rewards program? (Y or N) ')
    # avg_ticket_size = float(input('Average ticket size: $'))
    # no_transactions = int(input('Number of monthly transactions: '))
    # exp_transactions = int(input("Next month's projected transactions:  "))
    # dso = float(input('Days sales outstanding (i.e. average age of accounts receivable): '))
    owner_satisfaction = int(input('Owner satisfaction level (1 being very low to 12 being very high): '))
    employee_satisfaction = int(input('Employee satisfaction level (1 being very low to 12 being very high): '))

except ValueError:
    print('An exception occurred')

business_data = {}
business_dict = {}
business_final_grade = {}
business_metrics = {}


def add_business():
    sample_business = Business(name=name, location=location, industry=industry,
                               total_revenue=total_revenue, cogs=cogs, op_expenses=op_expenses,
                               cash_balance=cash_balance, current_assets=current_assets,
                               current_liabilities=current_liabilities, long_term_liabilities=long_term_liabilities,
                               owner_satisfaction=owner_satisfaction,
                               employee_satisfaction=employee_satisfaction, new_customers=new_customers,
                               start_customers=start_customers, end_customers=end_customers,
                               total_inventory=total_inventory, dead_inventory=dead_inventory,
                               rewards_program=rewards_program, expansion=expansion, prior_revenue=prior_revenue)
    # avg_ticket_size=avg_ticket_size, no_transactions=no_transactions, exp_transactions=exp_transactions
    # dso=dso

    print()
    print('=============== Company Results ===============')
    print()

    gp = sample_business.gross_profit()
    gp_str = "${:.{}f}".format(gp, 2)
    print("Gross profit: ", gp_str)

    gpm = sample_business.gross_profit_margin()
    gpm_str = "{:.{}f}%".format(gpm, 1)
    print("Gross profit margin: ", gpm_str)

    npl = sample_business.net_profit_loss()
    npl_str = "${:.{}f}".format(npl, 2)
    print("Net profit/loss:  ", npl_str)

    liq = sample_business.liquidity()
    liq_str = "{:.{}f}".format(liq, 1)
    print("Liquidity: ", liq_str)

    debt_service_coverage = npl / total_revenue
    td = debt_service_coverage
    td_str = "${:.{}f}".format(td, 2)
    print("Total debt: ", td_str)

    dr = sample_business.debt_ratio()
    dr_str = "{:.{}f}%".format(dr, 1)
    print("Debit-to-asset ratio: ", dr_str)

    # be = sample_business.break_even()
    # print('Monthly break-even amount: ', be)

    crr = sample_business.customer_retention_rate()
    crr_str = "{:.{}f}%".format(crr, 1)
    print("Customer retention rate: ", crr_str)

    sat = (sample_business.employee_satisfaction + sample_business.owner_satisfaction) / 2
    print('Owner & employee satisfaction rate: ', sat)

    i_health = sample_business.inventory()
    i_health_str = "{:.{}f}%".format(i_health, 1)
    print("Inventory health (dead inventory): ", i_health_str)

    growth = sample_business.prior_revenue
    print()

    # Adding business data to dictionary
    business_data['gpm'] = round(gpm, 2)
    business_data['npl'] = round(npl, 2)
    business_data['liq'] = round(liq, 2)
    business_data['td'] = round(td, 2)
    business_data['dr'] = round(dr, 2)
    # business_data['be'] = be
    business_data['crr'] = round(crr, 2)
    business_data['sat'] = round(sat, 2)
    business_data['i_health'] = round(i_health, 2)
    business_data['growth'] = round(growth, 2)

    # Creating dictionary of (possible) multiple businesses
    business_dict[name] = business_data

    # Small business health checkup using key metrics
    def health_checkup(business_data):

        # Metric 1: Gross profit margin
        def gpm_health(business_data):
            if business_data['gpm'] >= 60:
                return 11
            elif 50 <= business_data['gpm'] < 60:
                return 9
            elif 30 <= business_data['gpm'] < 50:
                return 7
            elif 20 <= business_data['gpm'] < 30:
                return 5
            elif 10 <= business_data['gpm'] < 20:
                return 3
            elif 5 <= business_data['gpm'] < 10:
                return 1

        # Metric 2: Net profit/loss
        def npl_health(business_data, expansion):
            if expansion.lower() == 'y':
                if business_data['npl'] > 0:
                    return 11
                return 8
            elif expansion.lower() == 'n':
                if business_data['npl'] >= 5000:
                    return 11
                elif 5000 > business_data['npl'] >= 2000:
                    return 9
                elif 2000 > business_data['npl'] >= 1000:
                    return 7
                elif 1000 > business_data['npl'] >= 0:
                    return 5
                elif -1000 < business_data['npl'] < 0:
                    return 3
                elif -2000 < business_data['npl'] <= -1000:
                    return 2
                elif -5000 < business_data['npl'] <= -2000:
                    return 1
                return 0

        # Metric 3: Liquidity
        def liq_health(business_data):
            if business_data['liq'] > 1.8:
                return 11
            elif 1.2 < business_data['liq'] <= 1.8:
                return 9
            elif 0.8 < business_data['liq'] <= 1.2:
                return 7
            elif 0.4 < business_data['liq'] <= 0.8:
                return 5
            return 3

        # Metric 4: Debt service coverage ratio (banks use this figure to determine loan qualifications)
        # > 1.25 is okay
        def td_health(business_data):
            if business_data['td'] > 2:
                return 11
            elif 1.5 < business_data['td'] <= 2:
                return 9
            elif 1.25 < business_data['td'] <= 1.5:
                return 7
            elif 1.0 < business_data['td'] <= 1.25:
                return 5
            elif 0.8 < business_data['td'] <= 1.0:
                return 3
            return 0

        # Metric 5: Debt-to-asset ratio
        def dr_health(business_data):
            if business_data['dr'] < 0.4:
                return 11
            elif 0.6 > business_data['dr'] >= 0.4:
                return 7
            elif 0.8 > business_data['dr'] >= 0.6:
                return 3
            return 0

        # Metric 6: Customer retention rate
        def crr_health(business_data):
            if business_data['crr'] >= 90:
                return 11
            elif 80 <= business_data['crr'] < 90:
                return 9
            elif 70 <= business_data['crr'] < 80:
                return 7
            elif 60 <= business_data['crr'] < 70:
                return 4
            return 0

        # Metric 7: Owner & Employee satisfaction
        def empl_health(business_data):
            return business_data['sat']

        # Metric 8: Inventory health
        def inventory_health(business_data):
            points = 1
            if sample_business.rewards_program.lower() == 'y':
                if business_data['i_health'] <= 0.05:
                    return 11 + points
                elif 0.05 < business_data['i_health'] <= 0.10:
                    return 9 + points
                elif 0.10 < business_data['i_health'] <= 0.15:
                    return 7 + points
                elif 0.15 < business_data['i_health'] <= 0.2:
                    return 5 + points
                elif 0.2 < business_data['i_health'] <= 0.25:
                    return 3 + points
                elif 0.25 < business_data['i_health'] <= 0.3:
                    return 1 + points
                return 0
            else:
                if business_data['i_health'] <= 0.05:
                    return 10
                elif 0.05 < business_data['i_health'] <= 0.10:
                    return 8
                elif 0.10 < business_data['i_health'] <= 0.15:
                    return 6
                elif 0.15 < business_data['i_health'] <= 0.2:
                    return 4
                elif 0.2 < business_data['i_health'] <= 0.25:
                    return 2
                elif 0.25 < business_data['i_health'] <= 0.3:
                    return 1
                return 0

        # Metric 9:  Growth
        def growth_health(business_data):
            if sample_business.prior_revenue > sample_business.total_revenue:
                return 11
            else:
                return 5

        # Health computation (aggregate)
        def health_compilation():
            metric_1 = gpm_health(business_data)
            metric_2 = npl_health(business_data, expansion)
            metric_3 = liq_health(business_data)
            metric_4 = td_health(business_data)
            metric_5 = dr_health(business_data)
            metric_6 = crr_health(business_data)
            metric_7 = empl_health(business_data)
            metric_8 = inventory_health(business_data)
            metric_9 = growth_health(business_data)

            # Adding metrics to dictionary
            business_metrics['gpm'] = metric_1
            business_metrics['npl'] = metric_2
            business_metrics['liq'] = metric_3
            business_metrics['td'] = metric_4
            business_metrics['dr'] = metric_5
            business_metrics['crr'] = metric_6
            business_metrics['sat'] = metric_7
            business_metrics['i_health'] = metric_8
            business_metrics['growth'] = metric_9

            business_dict[name + '_metrics'] = business_metrics

            return metric_1 + metric_2 + metric_3 + metric_4 + metric_5 + metric_6 + metric_7 + metric_8 + metric_9

        final_score = health_compilation()
        business_final_grade[name] = final_score

    health_checkup(business_data)


add_business()

print('==============================================')
print("Business_dict: ")
pprint.pprint(business_dict)
print('==============================================')
print("Business_data: ")
pprint.pprint(business_data)
print('==============================================')
print("Business_metrics: ")
pprint.pprint(business_metrics)
print('==============================================')
print("Business_final_grade: ")
pprint.pprint(business_final_grade)
'''