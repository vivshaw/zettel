tags:: finance

	- an **annuity** is series of payments with some uniform value A
		- an **ordinary annuity** is paid at the end of the period
		- conversely, an **annuity due** is paid at the beginning of the period
	- **value of an annuity:** $FV = A * \dfrac{(1+i)^N - 1}{i}$
		- where:
			- $A$ is the annuity payment
			- $i$ is the interest rate
			- $N$ is the number of periods
		- the factor applied to A is called the **uniform series compound amount factor**, and its inverse the **uniform series sinking fund factor**
	- **present value of an annuity:** $PV = A * \dfrac{(1+i)^N - 1}{i * (1 + i)^N}$
	  id:: 65591306-684d-40de-9437-2e97bf8e107c
		- "what's this annuity worth, right now, given that I'll pay this much into it?"
		- the coefficient is known as the **uniform series present value factor**
		- this is basically a combination of the value equation above, and the PV calculation for [[interest]]
	- **annuity for a given PV**: $A = PV * \dfrac{i * (1 + i)^N}{(1+i)^N - 1}$
		- "if I've spent this much capital, how much do I need to make in returns to break even?"
		- the coefficient is known as the **uniform series capital recovery factor**