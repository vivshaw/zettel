---
alias: beta
tags: finance, economics
---

- beta ($\beta$) is a term from the [[CAPM]]. The beta of a given security is the [[covariance]] of that individual security’s [[volatility]] with the volatility of the market as a whole.
- effectively, it’s a measure of co-movement with the market, or [[systematic risk]]:
	- **A beta of 1** represents a tendency to move **equally** with the market
	- **A beta > 1** represents a security that moves **more extremely** than the market
	- **A beta < 1** represents a security that moves **less extremely** than the market
- beta can be calculated through doing a regression on the price history of all securities in the market, and comparing the slope on the market regression, with the slope of a regression against the specific asset.
	- That is to say,
	  $βi = \dfrac{\operatorname{Cov}(V_i, V_{market})}{\operatorname{Var}(V_{market})}$
- the variance of the return on a stock is equal to it's beta squared times the variance of the market return ([[systematic risk]]) plus the variance of the residual ([[idiosyncratic risk]]).