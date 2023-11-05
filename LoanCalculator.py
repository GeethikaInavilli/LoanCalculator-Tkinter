# Import tkinter
from tkinter import *


class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        Label(window, text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(window, text="Number of Years").grid(row=2, column=1, sticky=W)
        Label(window, text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(window, text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label(window, text="Total Payment").grid(row=5, column=1, sticky=W)

        self.annualInterestRateVar = StringVar()
        Entry(
            window,
            textvariable=self.annualInterestRateVar,
            justify=LEFT,
            bg="light gray",
        ).grid(row=1, column=3)

        self.numberOfYearsVar = StringVar()
        Entry(
            window, textvariable=self.numberOfYearsVar, justify=LEFT, bg="light gray", 
        ).grid(row=2, column=3)

        self.loanAmountVar = StringVar()
        Entry(
            window, textvariable=self.loanAmountVar, justify=LEFT, bg="light gray"
        ).grid(row=3, column=3)
        self.monthlyPaymentVar = StringVar()
        Label(
            window, textvariable=self.monthlyPaymentVar, width=17
        ).grid(row=4, column=3, sticky=E)

        self.totalPaymentVar = StringVar()
        Label(window, textvariable=self.totalPaymentVar, width=17).grid(
            row=5, column=3, sticky=E
        )

        Button(
            window,
            text="Compute Payment",
            command=self.computePayment,
            bg="light gray",
        ).grid(row=7, column=2, sticky=E)
        window.mainloop()


    # compute the total payment.
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()),
        )

        self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))
        totalPayment = (
            float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        )

        self.totalPaymentVar.set(format(totalPayment, "10.2f"))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute the monthly payment.
        monthlyPayment = (
            loanAmount
            * monthlyInterestRate
            / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        )
        # root = Tk()
        return monthlyPayment


LoanCalculator()
