try:
    start_value = float(input("Startkapital: "))
    percentage = float(input("Anslått gjennomsnittlig årlig avkastning (i prosent): "))
    yearly_cost_percentage = float(input("Gebyr (i prosent) : "))
    years = float(input("Antall år: "))
    coefficient = float(percentage)/100 + 1
    yearly_cost = float(yearly_cost_percentage) / 100
    final_coefficient = float(coefficient) - float(yearly_cost)
    multiply_factor = pow(float(final_coefficient), float(years))
    result = float(start_value) * float(multiply_factor)
    earnings = float(result) - float(start_value)
    print("Total verdi: ")
    print(round(result))
    print("Penger tjent:" )
    print(round(earnings))
    if float(start_value) >= 10000000 and float(final_coefficient) >= 1.30:
         print("Rige du, reina Warren Buffett jo")
except ValueError:
    print("Feil, prøv igjen")

