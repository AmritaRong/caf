def format_company_name(company_name):
    if company_name is None or company_name.strip()=="":
        return "Invalid company_name"
    name_lower=company_name.lower()
    if "caf" in name_lower:
        return "CAF SoftSol India Pvt Ltd."
    return "Unknown Company"
print(format_company_name("CAF softsol"))
print(format_company_name("CAF solution"))
print(format_company_name("CAF softSolution India Pvt Limited"))
print(format_company_name(""))
print(format_company_name(None))
print(format_company_name("Google"))