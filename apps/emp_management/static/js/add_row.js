document.querySelectorAll(".add-row").forEach((button) => {
    button.addEventListener("click", () => {
        const tableBody = button.closest(".card-body").querySelector("tbody");
        const totalForms = tableBody.querySelector("[name$='-TOTAL_FORMS']");
        const formCount = parseInt(totalForms.value, 10);

        const emptyRow = tableBody.querySelector("tr.empty-form");
        const newRow = emptyRow.cloneNode(true);
        newRow.classList.remove("empty-form");
        newRow.innerHTML = newRow.innerHTML.replace(/__prefix__/g, formCount);

        tableBody.appendChild(newRow);
        totalForms.value = formCount + 1;
    });
});