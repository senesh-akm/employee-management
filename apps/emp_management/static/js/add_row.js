document.querySelectorAll('.add-row').forEach(button => {
    button.addEventListener('click', () => {
        const table = button.closest('.card-body').querySelector('tbody');
        const newRow = table.querySelector('tr').cloneNode(true);
        newRow.querySelectorAll('input').forEach(input => input.value = '');
        table.appendChild(newRow);
    });
});