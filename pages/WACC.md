tags:: finance, management

- the **weighted average cost of capital** is used to calculate a company's [[discount rate]]
- for projects funded with loans or bonds, the cost of capital is a weighted average of the interest rates on those assets
- for projects funded from retained profits, the cost of capital is tied to *the investor's expected rate of return*:
	- `i_expected = r_rf + β(r_m - r_rf`
		- where
			- `i_expected` is the investors' expected rate of return
			- `r_rf` is the risk-free rate of return (i.e., a short term gov't bond)
			- `r_m` is the average return of the stock market
			- `β` is [[beta (β) (finance)]], a measure of the risk associated with the company relative to the whole stock market
	- ...and whaddaya know, that's just [[CAPM]]!
- **what about taxes?** interest payments are tax-deductible, so we need to adjust interest payments for the corporate tax rate:
	- `i_after_tax = i_before_tax (1 - tax_rate)`
- e.g., a company with a capital structure like so, and corporate tax of 21%:
	- | Financing Type | Amount | Cost of capital | After-tax Cost of Capital |
	  | --- | --- | --- | ---|
	  | Equity | $60M | 12% | 12%|
	  | Bonds | $40M | 6% | 4.79% |
	  | Loans | $20M | 8% | 6.32% |
	  | Total | $120M | | |
	- would have a WACC of **8.6%**.
-