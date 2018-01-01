def getFormattedCurrency(value, type="nc"):
	"""
		getFormattedCurrency is used to get formatted string currency value based on country
		:param value
		:return formatted str 
	"""
	if type=="nc": return f"Rs. {value}"
	elif type=="usd": return f"$ {value}"

if __name__ == '__main__':
	help(getFormattedCurrency)