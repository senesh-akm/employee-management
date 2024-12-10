document.getElementById("employee").addEventListener("change", function () {
    const employeeId = this.value;

    if (employeeId) {
        fetch(`/salary-processing/bank-details/${employeeId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById("bank").value = data.bank_details.bank;
                    document.getElementById("account_number").value = data.bank_details.account_number;
                    document.getElementById("account_holder").value = data.bank_details.account_holder;
                    document.getElementById("bank_code").value = data.bank_details.bank_code;
                    document.getElementById("branch_code").value = data.bank_details.branch_code;
                    document.getElementById("swift_code").value = data.bank_details.swift_code;
                    document.getElementById("salary").value = data.bank_details.salary;
                } else {
                    alert(data.error || "Error fetching bank details.");
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("An error occurred while fetching bank details.");
            });
    }
});