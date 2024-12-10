document.getElementById("employee").addEventListener("change", function () {
    const employeeId = this.value;

    if (employeeId) {
        fetch(`/tax-management/salary/${employeeId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById("salary").value = data.salary.salary;
                } else {
                    alert(data.error || "Error fetching employee salary.");
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("An error occurred while fetching employee salary.");
            });
    }
});