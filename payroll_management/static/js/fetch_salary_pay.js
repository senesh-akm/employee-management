document.addEventListener("DOMContentLoaded", function () {
    const salaryProcessingDropdown = document.getElementById("salary_processing");

    salaryProcessingDropdown.addEventListener("change", function () {
        const salaryProcessingId = this.value;

        if (salaryProcessingId) {
            fetch(`/payroll/sp/${salaryProcessingId}/`)
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        document.getElementById("salary").value = data.salary_processing.salary;
                        document.getElementById("taxes").value = data.salary_processing.taxes;
                        document.getElementById("no_pay").value = data.salary_processing.no_pay;
                        document.getElementById("days").value = data.salary_processing.days;
                        document.getElementById("payment").value = data.salary_processing.payment;
                    } else {
                        alert(data.error || "Error fetching salary processing information.");
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                    alert("An error occurred while fetching salary processing information.");
                });
        }
    });
});