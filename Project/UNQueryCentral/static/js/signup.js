document.addEventListener('DOMContentLoaded', function() {
    const radioButtons = document.querySelectorAll('input[name="category"]');
    const studentFields = document.getElementById('student-fields');
    const teacherFields = document.getElementById('teacher-fields');
    const staffFields = document.getElementById('staff-fields');

    // Afficher les champs correspondants en fonction de la catégorie sélectionnée
    function showFields(category) {
        studentFields.style.display = 'none';
        teacherFields.style.display = 'none';
        staffFields.style.display = 'none';

        if (category === 'student') {
            studentFields.style.display = 'block';
        } else if (category === 'teacher') {
            teacherFields.style.display = 'block';
        } else if (category === 'staff') {
            staffFields.style.display = 'block';
        }
    }

    // Gestionnaire d'événement pour les boutons radio
    radioButtons.forEach(button => {
        button.addEventListener('change', function() {
            showFields(this.value);
        });
    });

    // Initialisation : vérifiez quel bouton radio est sélectionné au chargement
    const selectedRadioButton = document.querySelector('input[name="category"]:checked');
    if (selectedRadioButton) {
        showFields(selectedRadioButton.value);
    }

    // Filtrer les options du champ "département" en fonction de la faculté sélectionnée
    const facultyStudentSelect = document.getElementById('faculty-student');
    const departmentStudentSelect = document.getElementById('department-student');
    facultyStudentSelect.addEventListener('change', function() {
        const selectedFaculty = this.value;
        const departmentOptions = departmentStudentSelect.querySelectorAll('.department-option');
        departmentOptions.forEach(option => {
            if (option.classList.contains(selectedFaculty)) {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
        });
        departmentStudentSelect.selectedIndex = 0; // Réinitialiser la sélection du département
    });

    const facultyTeacherSelect = document.getElementById('faculty-teacher');
    const departmentTeacherSelect = document.getElementById('department-teacher');
    facultyTeacherSelect.addEventListener('change', function() {
        const selectedFaculty = this.value;
        const departmentOptions = departmentTeacherSelect.querySelectorAll('.department-option');
        departmentOptions.forEach(option => {
            if (option.classList.contains(selectedFaculty)) {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
        });
        departmentTeacherSelect.selectedIndex = 0; // Réinitialiser la sélection du département
    });

    // Filtrer les options du champ "filière" en fonction du département sélectionné
    const majorStudentSelect = document.getElementById('major-student');
    departmentStudentSelect.addEventListener('change', function() {
        const selectedDepartment = this.value;
        const majorOptions = majorStudentSelect.querySelectorAll('.major-option');
        majorOptions.forEach(option => {
            if (option.classList.contains(selectedDepartment)) {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
        });
        majorStudentSelect.selectedIndex = 0; // Réinitialiser la sélection de la filière
    });
});
