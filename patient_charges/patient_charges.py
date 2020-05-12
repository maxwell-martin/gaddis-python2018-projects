import patient, procedure

def main():
    patient1 = patient.Patient("Joe", "Harold", "Smith", "123 Main St.", \
                              "Beverly Hills", "California", "90210", \
                              "123-456-7890", "Sally Smith", "987-654-3210")
    
    procedure1 = procedure.Procedure("Physical Exam", "03/17/2020", \
                                     "Dr. Irvine", 250.00)
    procedure2 = procedure.Procedure("X-ray", "03/17/2020", \
                                     "Dr. Jamison", 500.00)
    procedure3 = procedure.Procedure("Blood test", "03/17/2020", \
                                     "Dr. Smith", 200.00)
    
    print("---------------Patient Information--------------")
    print(patient1)

    print("--------------------Procedures------------------")
    print(procedure1)
    print(procedure2)
    print(procedure3)

    total_charges = procedure1.get_charges() + procedure2.get_charges() + \
                    procedure3.get_charges()

    print("----------------------Charges-------------------")
    print("Total Charges: $" + format(total_charges, ",.2f"))

main()
