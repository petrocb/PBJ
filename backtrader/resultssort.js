document.addEventListener("DOMContentLoaded", function() {
    const selectOption = document.getElementById("sort-option");
    const resultContainers = document.querySelectorAll(".result-container");

    selectOption.addEventListener("change", function() {
        const selectedValue = selectOption.value;
        if (selectedValue === "profit") {
             //Convert the result containers to an array and sort them by profit
            const sortedContainers = Array.from(resultContainers).sort(function(a, b) {
                const profitA = parseFloat(a.querySelector("p").textContent.match(/'pnl': ([^,]+)/)[1]);
                const profitB = parseFloat(b.querySelector("p").textContent.match(/'pnl': ([^,]+)/)[1]);
                return profitB - profitA; // Descending order
            });

             //Append the sorted containers back to the parent
            const parent = resultContainers[0].parentNode;
            sortedContainers.forEach(container => parent.appendChild(container));

        }
        if (selectedValue === "run order") {
            // Convert the result containers to an array and sort them by run order
            const sortedContainers = Array.from(resultContainers).sort(function(a, b) {
                const runOrderA = parseInt(a.querySelector(".result").textContent.match(/^\d+/)[0]);
                const runOrderB = parseInt(b.querySelector(".result").textContent.match(/^\d+/)[0]);
                return runOrderA - runOrderB; // Ascending order
            });

            // Append the sorted containers back to the parent
            const parent = resultContainers[0].parentNode;
            sortedContainers.forEach(container => parent.appendChild(container));
        }
    });
});