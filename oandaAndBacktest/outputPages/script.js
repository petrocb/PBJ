function readCSV() {
    const fileInput = document.getElementById('csvInput');
    const outputDiv = document.getElementById('output');

    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            const csvContent = e.target.result;
            const lines = csvContent.split('\n');

            // Process the CSV data (you can customize this part)
            let htmlOutput = '<ul>';
            lines.forEach(line => {
                const columns = line.split(',');
                htmlOutput += '<li>' + columns.join('</li><li>') + '</li>';
            });
            htmlOutput += '</ul>';

            outputDiv.innerHTML = htmlOutput;
        };

        reader.readAsText(file);
    } else {
        alert('Please select a CSV file.');
    }
}