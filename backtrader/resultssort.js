// Get references to the necessary elements
const sortOption = document.getElementById('sort-option');
const resultContainer = document.querySelectorAll('.result-container');

// Function to sort the divs by profit
function sortByProfit() {
    const divArray = Array.from(resultContainer);

    divArray.sort((a, b) => {
        const aProfit = parseFloat(a.querySelector('p').textContent.match(/pnl: ([0-9.-]+)/)[1]);
        const bProfit = parseFloat(b.querySelector('p').textContent.match(/pnl: ([0-9.-]+)/)[1]);

        return bProfit - aProfit; // Descending order
    });

    // Append sorted divs back to the container
    divArray.forEach(div => resultContainer.appendChild(div));
}

// Attach a change event listener to the select element
sortOption.addEventListener('change', function() {
    if (sortOption.value === 'profit') {
        sortByProfit();
    }
});