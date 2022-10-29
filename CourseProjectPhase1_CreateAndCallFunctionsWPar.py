#Rebecca Stricklan
#Course Project Phase 1
#CIS261
def GetEmpName():
    empname = input("Enter employee name: ")
    return enpname
def GetHoursWorked():
    hoursworked = float(input("Enter hours worked: "))
    return hoursworked
def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))

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
    print(f"Total Hours Worked: {TotHours:,.2f}")
    print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    print(f"Total Income Tax: {TotTax:,.2f}")
    print(f"Total Net Pay: {TotNetPay:,.2f}")

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
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        grosspay, incomtax, netpay = CalTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
        
           



