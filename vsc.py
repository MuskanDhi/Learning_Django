import csv

highest_total = 0
highest_student = ""

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("results.csv", "w", newline="") as output_file:

        fieldnames = [
            "Name",
            "Python",
            "SQL",
            "Java",
            "Total",
            "Percentage",
            "Result"
        ]

        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            name = row["Name"]

            python_marks = int(row["Python"])
            sql_marks = int(row["SQL"])
            java_marks = int(row["Java"])

            total = python_marks + sql_marks + java_marks

            percentage = (total / 300) * 100

            if percentage >= 40:
                result = "Pass"
            else:
                result = "Fail"

            if total > highest_total:
                highest_total = total
                highest_student = name

            writer.writerow({
                "Name": name,
                "Python": python_marks,
                "SQL": sql_marks,
                "Java": java_marks,
                "Total": total,
                "Percentage": f"{percentage:.2f}",
                "Result": result
            })

print("Highest Scorer:", highest_student)
print("Highest Total:", highest_total)
print("Results saved to results.csv")