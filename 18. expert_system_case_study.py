def diagnose():
    print("Expert System: Flu Diagnosis")
    
    fever = input("Do you have a fever? (yes/no): ").lower()
    cough = input("Do you have a cough? (yes/no): ").lower()
    sore_throat = input("Do you have a sore throat? (yes/no): ").lower()
    body_aches = input("Do you have body aches? (yes/no): ").lower()

    if fever == 'yes' and cough == 'yes' and sore_throat == 'yes' and body_aches == 'yes':
        print("\nDiagnosis: You may have the flu.")
    elif fever == 'yes' and cough == 'yes':
        print("\nDiagnosis: You may have a common cold.")
    else:
        print("\nDiagnosis: Symptoms unclear. Please consult a doctor.")

diagnose()
