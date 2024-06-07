document.addEventListener('DOMContentLoaded', function() {
    const popup = document.getElementById('queryPopup');
    const closePopup = document.getElementById('closePopup');
    const assignButton = document.getElementById('assignButton');
    const studentName = document.getElementById('studentName');
    const studentEmail = document.getElementById('studentEmail');
    const studentDepartment = document.getElementById('studentDepartment');
    const requestType = document.getElementById('requestType');
    const requestSubject = document.getElementById('requestSubject');
    const requestContent = document.getElementById('requestContent');
    const attachedFiles = document.getElementById('attachedFiles');
    const departmentHead = document.getElementById('departmentHead');

    // Ouvrir le pop-up avec les détails de la requête
    function openPopup(details) {
        studentName.textContent = details.studentName;
        studentEmail.textContent = details.studentEmail;
        studentDepartment.textContent = details.studentDepartment;
        requestType.textContent = details.requestType;
        requestSubject.textContent = details.requestSubject;
        requestContent.textContent = details.requestContent;

        // Gérer les fichiers joints
        attachedFiles.innerHTML = '';
        details.attachedFiles.forEach(file => {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = file.url;
            a.textContent = file.name;
            li.appendChild(a);
            attachedFiles.appendChild(li);
        });

        popup.style.display = 'block';
    }

    // Fermer le pop-up
    closePopup.addEventListener('click', function() {
        popup.style.display = 'none';
    });

    // Fermer le pop-up si l'utilisateur clique en dehors
    window.addEventListener('click', function(event) {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });

    // Assigner la requête à un chef de département
    assignButton.addEventListener('click', function() {
        const chefEmail = departmentHead.value;
        // Envoyer une requête au serveur pour assigner le chef de département
        // Vous devez implémenter cette partie en backend
        console.log(`Assigning query to: ${chefEmail}`);
        popup.style.display = 'none';
    });

    // Ajouter des gestionnaires de clics aux lignes du tableau de requêtes
    const queryRows = document.querySelectorAll('.recentOrders tbody tr');
    queryRows.forEach(row => {
        row.addEventListener('click', function() {
            const details = {
                studentName: 'Nom par défaut', // À remplacer par les données réelles
                studentEmail: this.cells[2].textContent,
                studentDepartment: 'Département par défaut', // À remplacer par les données réelles
                requestType: this.cells[0].textContent,
                requestSubject: this.cells[1].textContent,
                requestContent: "Exemple de contenu de la requête pour " + this.cells[2].textContent,
                attachedFiles: [
                    { name: 'document1.pdf', url: '#' },
                    { name: 'document2.pdf', url: '#' }
                ]
            };
            openPopup(details);
        });
    });
});
