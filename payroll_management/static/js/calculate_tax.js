document.addEventListener("DOMContentLoaded", function () {
    const incomeTaxInput = document.getElementById("income_tax");
    const otherTaxInput = document.getElementById("other_taxes");
    const allTaxInput = document.getElementById("all_taxes");

    function calculatePayment() {
        const income = parseFloat(incomeTaxInput.value) || 0;
        const other = parseFloat(otherTaxInput.value) || 0;

        const allTax = income + other;

        allTaxInput.value = allTax.toFixed(2);
    }

    incomeTaxInput.addEventListener("input", calculatePayment);
    otherTaxInput.addEventListener("input", calculatePayment);

    calculatePayment();
});