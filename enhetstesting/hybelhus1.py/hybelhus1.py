# Global ordbok for å lagre studentinformasjon
leiligheter = {}


def flytt_inn(student_id, navn, epost, telefon):
    """Registrerer en ny student som flytter inn."""
    if student_id in leiligheter:
        return "Studenten er allerede registrert."
    leiligheter[student_id] = {
        'navn': navn,
        'epost': epost,
        'telefon': telefon,
        'status': 'in'
    }
    return f"{navn} har flyttet inn."


def flytt_ut(student_id):
    """Registrerer at en student flytter ut."""
    if student_id not in leiligheter:
        return "Studenten finnes ikke."
    if leiligheter[student_id]['status'] == 'out':
        return "Studenten har allerede flyttet ut."
    leiligheter[student_id]['status'] = 'out'
    return f"{leiligheter[student_id]['navn']} har flyttet ut."


def sjekk_status(student_id):
    """Sjekker status for en student (inn eller ut)."""
    if student_id not in leiligheter:
        return "Studenten finnes ikke."
    return f"{leiligheter[student_id]['navn']} er {'inn' if leiligheter[student_id]['status'] == 'in' else 'ut'}."


def vis_studentinfo(student_id):
    """Viser informasjon om en student."""
    if student_id not in leiligheter:
        return "Studenten finnes ikke."
    student = leiligheter[student_id]
    return f"Navn: {student['navn']}, E-post: {student['epost']}, Telefon: {student['telefon']}, Status: {student['status']}"
