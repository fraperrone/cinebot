import pytest
from cinebot_FrancoPerroneRey_MaximilianoEzequielFunes import reservar_entradas, consultar_cartelera, dejar_reseña

def test_reservar_entradas(monkeypatch, capsys):
    # Simulamos las entradas del usuario en orden
    inputs = iter([
        "1",            # opción de película
        "1",            # tipo de entrada
        "2",            # cantidad de entradas
        "Juan",         # nombre asistente 1
        "María",        # nombre asistente 2
        "Perez"         # nombre de la reserva
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    reservar_entradas()
    captured = capsys.readouterr()
    assert "Resumen de su compra:" in captured.out
    assert "PEREZ" in captured.out
    assert "Su reserva fue realizada con éxito" in captured.out

def test_consultar_cartelera(capsys):
    consultar_cartelera()
    captured = capsys.readouterr()
    assert "Cartelera disponible hoy:" in captured.out
    # verificamos que se imprimió al menos una película
    assert any(line.strip() for line in captured.out.splitlines() if "-" in line)

def test_dejar_reseña(monkeypatch, capsys):
    inputs = iter([
        "1",                # opción de película
        "Muy buena peli",   # reseña
        "5"                 # puntuación
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    dejar_reseña()
    captured = capsys.readouterr()
    assert "¡Nos alegra que haya disfrutado la película!" in captured.out
    assert "Gracias por dejar su reseña en MovieTime" in captured.out

