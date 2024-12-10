document.addEventListener("DOMContentLoaded", function () {
    const employeeDropdown = document.getElementById("employee");

    employeeDropdown.addEventListener("change", function () {
        const employeeId = this.value;

        if (employeeId) {
            fetch(`/payroll/professional/${employeeId}/`)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        document.getElementById("title").value = data.employee.title;
                        document.getElementById("full_name").value = data.employee.full_name;
                        document.getElementById("job_number").value = data.employee.job_number;
                        document.getElementById("department").value = data.employee.department;
                        document.getElementById("designation").value = data.employee.designation;
                    } else {
                        alert(data.error || "Error fetching professional information.");
                    }
                })
                .catch(error => {
                    console.error("Error:", error);
                    alert("An error occurred while fetching professional information.");
                });
        }
    });
});