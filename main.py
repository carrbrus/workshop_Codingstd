"""Sistema de Gestión de Calificaciones de Estudiantes.

Este módulo implementa el registro, validación y cálculo de notas
cumpliendo estrictamente con las convenciones de código PEP 8.
"""

from typing import List, Optional, Union


class Student:
    """Representa a un estudiante y su historial de calificaciones."""

    def __init__(self, student_id: str, name: str) -> None:
        """Inicializa una instancia de Student con validación de entradas."""
        clean_id = student_id.strip() if isinstance(student_id, str) else ""
        clean_name = name.strip() if isinstance(name, str) else ""

        if not clean_id:
            raise ValueError(
                "El identificador del estudiante no puede estar vacío."
            )
        if not clean_name:
            raise ValueError(
                "El nombre del estudiante no puede estar vacío."
            )

        self.student_id: str = clean_id
        self.name: str = clean_name
        self.grades: List[float] = []

    def add_grade(self, grade: Union[int, float]) -> bool:
        """Agrega una calificación válida en el rango [0.0, 100.0]."""
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            print(f"[Error] La calificación '{grade}' debe ser numérica.")
            return False

        if 0.0 <= float(grade) <= 100.0:
            self.grades.append(float(grade))
            return True

        print(
            f"[Error] Calificación {grade} fuera de rango. Debe ser 0 a 100."
        )
        return False

    def calculate_average(self) -> Optional[float]:
        """Calcula el promedio aritmético de las calificaciones."""
        if not self.grades:
            return None
        return round(sum(self.grades) / len(self.grades), 2)

    def determine_letter_grade(self) -> str:
        """Determina la calificación en letra a partir del promedio."""
        avg = self.calculate_average()
        if avg is None:
            return "N/A"
        if avg >= 90.0:
            return "A"
        if avg >= 80.0:
            return "B"
        if avg >= 70.0:
            return "C"
        if avg >= 60.0:
            return "D"
        return "F"

    def is_passed(self) -> str:
        """Indica si el estudiante aprobó o reprobó."""
        avg = self.calculate_average()
        if avg is None:
            return "N/A"
        return "Passed" if avg >= 60.0 else "Failed"

    def is_honor_roll(self) -> bool:
        """Determina si clasifica al Cuadro de Honor (promedio >= 90)."""
        avg = self.calculate_average()
        return avg is not None and avg >= 90.0

    def remove_grade_by_index(self, index: int) -> bool:
        """Elimina una nota según su posición en la lista (índice 0)."""
        if not isinstance(index, int) or isinstance(index, bool):
            print(f"[Error] El índice '{index}' debe ser un número entero.")
            return False

        if 0 <= index < len(self.grades):
            removed = self.grades.pop(index)
            print(
                f"[Éxito] Calificación {removed} removida del índice {index}."
            )
            return True

        print(
            f"[Error] Índice {index} fuera de rango. "
            f"Disponibles: {len(self.grades)}."
        )
        return False

    def remove_grade_by_value(self, value: Union[int, float]) -> bool:
        """Elimina la primera coincidencia del valor numérico provisto."""
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            print(f"[Error] El valor a remover '{value}' debe ser numérico.")
            return False

        target = float(value)
        if target in self.grades:
            self.grades.remove(target)
            print(f"[Éxito] Calificación {target} eliminada.")
            return True

        print(f"[Error] La calificación {target} no existe en el registro.")
        return False

    def generate_summary_report(self) -> str:
        """Genera un reporte tabular formateado del desempeño del alumno."""
        avg = self.calculate_average()
        avg_display = f"{avg:.2f}" if avg is not None else "N/A"

        separator = "=" * 45
        return (
            f"\n{separator}\n"
            f"          REPORTE DE CALIFICACIONES\n"
            f"{separator}\n"
            f"  ID Estudiante     : {self.student_id}\n"
            f"  Nombre            : {self.name}\n"
            f"  Total Notas       : {len(self.grades)}\n"
            f"  Promedio          : {avg_display}\n"
            f"  Letra Final       : {self.determine_letter_grade()}\n"
            f"  Estado Aprobación : {self.is_passed()}\n"
            f"  Cuadro de Honor   : {self.is_honor_roll()}\n"
            f"{separator}\n"
        )


def main() -> None:
    """Punto de entrada de prueba con casos de éxito y excepciones."""
    try:
        Student("", "Estudiante Fantasma")
    except ValueError as err:
        print(f"[Control] {err}")

    student = Student("ST-2026-001", "María Delgado")

    student.add_grade(95.5)
    student.add_grade(88.0)
    student.add_grade(100.0)
    student.add_grade("Cien")
    student.add_grade(150.0)
    student.add_grade(-10.0)

    student.remove_grade_by_value(88.0)
    student.remove_grade_by_value(40.0)
    student.remove_grade_by_index(10)
    student.remove_grade_by_index(0)

    student.add_grade(92.0)
    student.add_grade(94.0)

    print(student.generate_summary_report())


if __name__ == "__main__":
    main()
