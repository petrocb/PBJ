from matplotlib import pyplot as plt
from random import randint
import csv
import html

def createHTMLfile(file_path, text, pic):
        with open(file_path, 'r') as html_file:
            existing_content = html_file.read()

        html_content = f"""
            <div class="result-container">
                <p>{text}</p>
                <a href={pic}>chart</a>
                
            </div>
        """
        insertion_index = existing_content.find('<script')

        if insertion_index != -1:
            # Insert the new content within the body tag
            updated_content = (
                    existing_content[:insertion_index] +
                    html_content +
                    existing_content[insertion_index:]
            )

            # Write the updated content to the file
            with open(file_path, 'w') as html_file:
                html_file.write(updated_content)
        else:
            print("No </body> tag found in the existing content.")

def plotChart():
    with open("EURUSD2.csv", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        plotData = [row for row in csv_reader]
    test = []
    for c in plotData:
        test.append([float(c[2]), float(c[3]), float(c[4]), float(c[5])])
    plt.plot(test)
    pic = 'charts/' + str(randint(0, 9999999)) + '.png'
    plt.savefig(pic)
    return pic