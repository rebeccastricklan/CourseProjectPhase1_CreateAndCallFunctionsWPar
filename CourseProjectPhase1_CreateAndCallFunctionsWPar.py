#Rebecca Stricklan
#Course Project Phase 1
#CIS261
def GetEmpName():
    empname = input("Enter employee name: ")
    return enpname
def GetHoursWorked():
    hoursworked = input("Enter hours worked: ")
    return hoursworked
def GetHourlyRate():
    hourlyrate = input("Enter hourly rate: ")
    return hourlyrate
def GetTaxRate():
    taxrate = input("Enter tax rate: ")

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incomtax = grosspay * taxrate
    netpay = grosspay - incomtax
    return grosspay, incomtax, netpay

def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2F}", f"{netpay:,.2f}")
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
def printinfo(TotHours, TotGrossPay, TotTax, TotNetPay):
    print(TotHours, f"{TotHours:,.2f}", f"{TotGrossPay:,.2f}", f"{TotTax:,.2f}", f"{TotNetPay:,.2f}")

if __name__ == "__main__":
    TotEmploees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        hours = GetHoursWorked()
        if (hours.upper() == "END"):
            break
        hourlyrate = GetHourlyRate()
        if (hourlyrate.upper() == "END"):
            break
        taxrate = GetTaxRate()
        if (taxrate.upper() == "END"):
            break



