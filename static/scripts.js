// JAVASCRIPT KODAS DINAMIŠKAI GENERUOTI LENTELĘ SU DUOMENIMIS
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/allcars')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('projektai-body');
            tbody.innerHTML = '';

            data.forEach(projektas => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${projektas.id}</td>
                    <td>${projektas.brand}</td>
                    <td>${projektas.model}</td>
                    <td>${projektas.year}</td>
                    <td>${projektas.price}</td>
                    <td>${projektas.date}</td>
                    <td>${projektas.image}</td>
                `;

                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

