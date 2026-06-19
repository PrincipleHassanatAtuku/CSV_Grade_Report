import csv

def generate_report():
    # Initialize totals for the 4 new courses
    bio_tot, cos_tot, mth_tot, phy_tot, count = 0, 0, 0, 0, 0
    
    with open("hassanat.csv", "r") as f:
        data_reader = csv.reader(f)
        header = next(data_reader) # Skip the headers row
        
        for record in data_reader:
            if not record: 
                continue
            # Read columns by index: Name=0, BIO102=1, COS102=2, MTH102=3, PHY102=4
            bio_tot += int(record[1])
            cos_tot += int(record[2])
            mth_tot += int(record[3])
            phy_tot += int(record[4])
            count += 1

    # Calculate the 4 averages
    b_avg = bio_tot / count
    c_avg = cos_tot / count
    m_avg = mth_tot / count
    p_avg = phy_tot / count

    # Write summaries to the report file
    with open("report.txt", "w") as out:
        out.write("============ STUDENT PERFORMANCE REPORT ============\n")
        out.write(f"Total Students Processed: {count}\n\n")
        out.write(f"Average BIO102 Score: {b_avg:.2f}\n")
        out.write(f"Average COS102 Score: {c_avg:.2f}\n")
        out.write(f"Average MTH102 Score: {m_avg:.2f}\n")
        out.write(f"Average PHY102 Score: {p_avg:.2f}\n")
        out.write("====================================================\n")

generate_report()
print("Report successfully generated as 'report.txt'!")

print("\n--- Displaying Generated Report ---")
print(open("report.txt").read())
