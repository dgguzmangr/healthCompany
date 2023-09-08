<template>
    <div>
        <h2>Crear Nuevo Paciente</h2>
        <form @submit.prevent="createPatient">
            <label>Doctor ID:</label>
            <input v-model="doctorId" type="number" required>
            <br>
            <label>Nurse ID:</label>
            <input v-model="nurseId" type="number" required>
            <br>
            <label>Assistant ID:</label>
            <input v-model="assistantId" type="number" required>
            <br>
            <label>Email:</label>
            <input v-model="email" type="email" required>
            <br>
            <label>Password:</label>
            <input v-model="password" type="password" required>
            <br>
            <button type="submit">Crear Paciente</button>
        </form>
    </div>
</template>

<script>
export default {
  data() {
    return {
        doctorId: null,
        doctorName: '',
        nurseId: null,
        assistantId: null,
        email: '',
        password: ''
        };
    },
    methods: {
        createPatient() {
            const formData = {
                doctorId: this.doctorId,
                nurseId: this.nurseId,
                assistantId: this.assistantId,
                email: this.email,
                password: this.password
            };
            fetch("http://127.0.0.1:8000/create_patient/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            })
            .then(respose => {
                if (respose.ok) {
                    console.log("El paciente se ha creado con éxito.");
                } else {
                    console.log("Error al crear el paciente.");
                }
            })
            .catch(error => {
                console.error("Error de red:", error);
            });
        },
    },
};
</script>