from BusinessClass import Business
import pprint

# User inputs
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
    expansion = input('Are you undergoing any sort of expansion, i.e. products, personnel, locations, etc (Y or N)? ')
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
    owner_satisfaction = int(input('Owner satisfaction level (1 being very low to 11 being very high): '))
    employee_satisfaction = int(input('Employee satisfaction level (1 being very low to 11 being very high): '))

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

    debt_service_coverage = npl / sample_business.current_liabilities
    td = debt_service_coverage
    td_str = "{:.{}f}".format(td, 2)
    print("Debt service coverage: ", td_str)

    dar = sample_business.debt_asset_ratio()
    dar_str = "{:.{}f}".format(dar, 1)
    print("Debit-to-asset ratio: ", dar_str)

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
    business_data['gross profit margin'] = round(gpm, 2)
    business_data['net profit/loss'] = round(npl, 2)
    business_data['liquidity'] = round(liq, 2)
    business_data['debt service coverage'] = round(td, 2)
    business_data['debt-to-asset ratio'] = round(dar, 2)
    # business_data['be'] = be
    business_data['customer retention rate'] = round(crr, 2)
    business_data['employee/owner satisfaction'] = round(sat, 2)
    business_data['dead inventory'] = round(i_health, 2)
    business_data['month-over-month growth'] = round(growth, 2)

    # Creating dictionary of (possible) multiple businesses
    business_dict[name] = business_data

    # Small business health checkup using key metrics
    def health_checkup(business_data):

        # Metric 1: Gross profit margin
        def gpm_health(business_data):
            if business_data['gross profit margin'] >= 60:
                return 11
            elif 50 <= business_data['gross profit margin'] < 60:
                return 9
            elif 30 <= business_data['gross profit margin'] < 50:
                return 7
            elif 20 <= business_data['gross profit margin'] < 30:
                return 5
            elif 10 <= business_data['gross profit margin'] < 20:
                return 3
            elif 5 <= business_data['gross profit margin'] < 10:
                return 1

        # Metric 2: Net profit/loss
        def npl_health(business_data, expansion):
            if expansion.lower() == 'y':
                if business_data['net profit/loss'] > 0:
                    return 11
                return 9
            elif expansion.lower() == 'n':
                if business_data['net profit/loss'] >= 5000:
                    return 11
                elif 5000 > business_data['net profit/loss'] >= 2000:
                    return 10
                elif 2000 > business_data['net profit/loss'] >= 1000:
                    return 9
                elif 1000 > business_data['net profit/loss'] >= 0:
                    return 8
                elif -1000 < business_data['net profit/loss'] < 0:
                    return 7
                elif -2000 < business_data['net profit/loss'] <= -1000:
                    return 6
                elif -5000 < business_data['net profit/loss'] <= -2000:
                    return 5
                return 4

        # Metric 3: Liquidity
        # > 1.0 is considered good
        def liq_health(business_data):
            if business_data['liquidity'] > 1.8:
                return 11
            elif 1.2 < business_data['liquidity'] <= 1.8:
                return 10
            elif 0.8 < business_data['liquidity'] <= 1.2:
                return 9
            elif 0.4 < business_data['liquidity'] <= 0.8:
                return 8
            return 7

        # Metric 4: Debt service coverage ratio (banks use this figure to determine loan qualifications)
        # > 1.25 is okay
        def td_health(business_data):
            if business_data['debt service coverage'] > 2:
                return 11
            elif 1.5 < business_data['debt service coverage'] <= 2:
                return 10
            elif 1.25 < business_data['debt service coverage'] <= 1.5:
                return 9
            elif 1.0 < business_data['debt service coverage'] <= 1.25:
                return 8
            elif 0.8 < business_data['debt service coverage'] <= 1.0:
                return 7
            return 6

        # Metric 5: Debt-to-asset ratio
        # The higher the ratio, the greater the risk
        def dar_health(business_data):
            if business_data['debt-to-asset ratio'] < 0.4:
                return 11
            elif 0.5 > business_data['debt-to-asset ratio'] >= 0.4:
                return 10
            elif 0.6 > business_data['debt-to-asset ratio'] >= 0.5:
                return 9
            elif 0.7 > business_data['debt-to-asset ratio'] >= 0.6:
                return 8
            elif 0.8 > business_data['debt-to-asset ratio'] >= 0.7:
                return 7
            return 6

        # Metric 6: Customer retention rate
        # 90% and above is great
        def crr_health(business_data):
            points = 1
            if sample_business.rewards_program.lower() == 'y':
                if business_data['customer retention rate'] >= 90:
                    return 11 + points
                elif 80 <= business_data['customer retention rate'] < 90:
                    return 10 + points
                elif 70 <= business_data['customer retention rate'] < 80:
                    return 9 + points
                elif 60 <= business_data['customer retention rate'] < 70:
                    return 8 + points
                return 6 + points
            elif sample_business.rewards_program.lower() == 'n':
                if business_data['customer retention rate'] >= 90:
                    return 10
                elif 80 <= business_data['customer retention rate'] < 90:
                    return 9
                elif 70 <= business_data['customer retention rate'] < 80:
                    return 8
                elif 60 <= business_data['customer retention rate'] < 70:
                    return 7
                return 5

        # Metric 7: Owner & Employee satisfaction
        def empl_health(business_data):
            return business_data['employee/owner satisfaction']

        # Metric 8: Inventory health
        # The lower the dead inventory percentage, the better
        def inventory_health(business_data):
            if business_data['dead inventory'] <= 5:
                return 11
            elif 5 < business_data['dead inventory'] <= 10:
                return 10
            elif 10 < business_data['dead inventory'] <= 15:
                return 9
            elif 15 < business_data['dead inventory'] <= 20:
                return 8
            elif 20 < business_data['dead inventory'] <= 25:
                return 7
            elif 25 < business_data['dead inventory'] <= 30:
                return 6
            return 5

        # Metric 9:  Growth
        # You're either growing or your dying
        def growth_health(business_data):
            if sample_business.prior_revenue < sample_business.total_revenue:
                return 11
            else:
                return 6

        # Health computation (in aggregate)
        def health_compilation():
            metric_1 = gpm_health(business_data)
            metric_2 = npl_health(business_data, expansion)
            metric_3 = liq_health(business_data)
            metric_4 = td_health(business_data)
            metric_5 = dar_health(business_data)
            metric_6 = crr_health(business_data)
            metric_7 = empl_health(business_data)
            metric_8 = inventory_health(business_data)
            metric_9 = growth_health(business_data)

            # Adding metrics to dictionary
            business_metrics['gross profit margin'] = metric_1
            business_metrics['net profit/loss'] = metric_2
            business_metrics['liquidity'] = metric_3
            business_metrics['debt service coverage'] = metric_4
            business_metrics['debt-to-asset ratio'] = metric_5
            business_metrics['customer retention rate'] = metric_6
            business_metrics['employee/owner satisfaction'] = metric_7
            business_metrics['dead inventory'] = metric_8
            business_metrics['month-over-month growth'] = metric_9

            business_dict[name + '_metrics'] = business_metrics

            return metric_1 + metric_2 + metric_3 + metric_4 + metric_5 + metric_6 + metric_7 + metric_8 + metric_9

        final_score = health_compilation()
        business_final_grade[name] = final_score

    health_checkup(business_data)

    def review():
        if business_final_grade[name] >= 90:
            print('Grade A :: Excellent! You are on the fast-track for growth and sustainability.')
        elif 90 > business_final_grade[name] >= 80:
            print('Grade B :: Good Job! Your data points look good. As you expand, try to keep'
                  ' costs the same as you expand and scale your business.')
        elif 80 > business_final_grade[name] >= 70:
            print('Grade C :: There is more work to accomplish. Keep an eye on debt and dead inventory. '
                  'Ensure the company is taking care of the employees and customers.')
        elif 70 > business_final_grade[name] >= 60:
            print('Grade D :: Whoa, buddy! Debt overload. Profit margins are too low and your customers need to'
                  'know they are loved.')
        else:
            print('Grade F :: No bueno! Give extra attention to your suppliers and bring your costs down. Watch out '
                  'for payroll expenses, over-aggressive expansion, and large'
                  ' short-term debt obligations. Most '
                  'importantly, take extra special care of your employees and customers. They are the life blood of '
                  'your business.')

    review()
    print()


# Running the program
# if __name__ == '__main__':
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
