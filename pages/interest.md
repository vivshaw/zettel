tags:: finance, economics
alias:: interest rate

- **simple interest:** $P * i * N$
	- where:
		- $P$ = the initial principal
		- $i$ = the interest rate
		- $N$ = the number of time periods
- **compound interest:**: $P * (1 + i)^N$
  id:: 65485818-8169-4e96-976d-90d9e543c97b
	- $(1+i)^N$ is also known as the **Compound Amount Factor**
		- its inverse, $\dfrac{1}{(1+i)^N}$, is known as the **Present Value Factor**
	- how to calculate...
		- the principal? $P = \dfrac{FV}{(1 + i)^N}$
		- the interest rate? $i = (\frac{FV}{PV})^{\frac{1}{N}} - 1$
		- the periods? $N = \dfrac{log(\frac{FV}{PV})}{log(1 + i)}$
- **nominal interest rate:** the interest rate expressed on an annual basis. also, APR (annual percentage rate)
- **compounding:** dividing the APR into sub-periods. for example, 12% interest compounded monthly would be calculated as 1% interest paid per month. this nominal rate of 12% actually ends up paying 12.68% worth of interest!
- **effective interest rate:** the actual interest on an annual basis
	- $i_{ear} = (1 + (\frac{i}{M})) ^ M - 1$
		- where:
			- $i$ is the nominal interest rate (expressed annually)
			- $M$ is the number of compounding periods per year
			- $i_{ear}$ is the effective interest rate