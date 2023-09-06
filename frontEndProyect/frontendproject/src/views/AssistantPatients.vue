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
        async createPatient() {
            const formData = {
                doctor_id: this.doctorId,
                nurse_id: this.nurseId,
                assistant_id: this.assistantId,
                email: this.email,
                password: this.password
                };
            try {
                const response = await fetch('/api/create_patient/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        // You might need to include authentication headers if required
                        },
                    body: JSON.stringify(formData)
                    });

                if (response.ok) {
                    // Patient created successfully
                    // You can redirect or show a success message here
                } else {
                    const errorData = await response.json();
                    console.error('Error creating patient:', errorData);
                    }
            } catch (error) {
                console.error('Error creating patient:', error);
            }
        }
    }
};
</script>