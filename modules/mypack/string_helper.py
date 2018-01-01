import os

def getFormattedCurrency(value, type="nc"):
	if type=="nc": return f"Rs. {value}"
	elif type=="usd": return f"$ {value}"

def getJavaHome():
	return os.environ.get('JAVA_HOME')
