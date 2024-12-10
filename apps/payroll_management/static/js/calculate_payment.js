document.addEventListener("DOMContentLoaded", function () {
    const salaryInput = document.getElementById("salary");
    const noPayInput = document.getElementById("no_pay");
    const daysInput = document.getElementById("days");
    const paymentInput = document.getElementById("payment");
    const taxInput = document.getElementById("taxes");

    function calculateNoPay() {
        const salary = parseFloat(salaryInput.value) || 0;
        const noPay = salary / 30;
        noPayInput.value = noPay.toFixed(2);
        calculatePayment();
    }

    function calculatePayment() {
        const salary = parseFloat(salaryInput.value) || 0;
        const noPay = parseFloat(noPayInput.value) || 0;
        const days = parseInt(daysInput.value) || 0;
        const tax = parseFloat(taxInput.value) || 0;

        const taxableSalary = salary - (salary * tax) / 100;

        const payment = taxableSalary - noPay * days;

        paymentInput.value = payment.toFixed(2);
    }

    salaryInput.addEventListener("input", calculateNoPay);
    daysInput.addEventListener("input", calculatePayment);
    taxInput.addEventListener("input", calculatePayment);

    calculateNoPay();
    calculatePayment();
});