"""
Business Class :: Team NoName
Quantifying the health of a small business
"""


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
    def debt_asset_ratio(self):
        dar = (self.current_liabilities + self.long_term_liabilities) / (self.current_assets + self.cash_balance)
        return dar

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

